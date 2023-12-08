import os
import zipfile
from utils.path_converter import PathConverter
class separate_zip:
    def __init__(self, folder_path, split_count=1000, zip_file_name='Backup', target_path='zip_files'):
        self.folder_path = PathConverter.convert_backslash_to_slash(folder_path)
        self.target_path = PathConverter.convert_backslash_to_slash(target_path)
        self.split_count = split_count
        self.zip_file_name = zip_file_name
        self.file_list = []
        self.split_list = []

    def get_file_list(self):
        self.file_list = [f for f in os.listdir(self.folder_path) if f.endswith('.jpg')]

    def split_files(self):
        self.split_list = []
        for i in range(0, len(self.file_list), self.split_count):
            self.split_list.append(self.file_list[i:i+self.split_count])
    def make_zip_files(self):
        if not os.path.exists(self.target_path):
            os.mkdir(self.target_path)

        TOTAL_SPLIT_COUNT = len(self.split_list)
        progress = 0
        prev_progress = -1

        for split_idx, split in enumerate(self.split_list):
            zip_file_full_name = os.path.join(self.target_path, f'{self.zip_file_name}_{split_idx + 1}.zip')
            with zipfile.ZipFile(zip_file_full_name, 'w') as myzip:
                for file_idx, file_name in enumerate(split):
                    file_full_path = os.path.join(self.folder_path, file_name)
                    myzip.write(file_full_path, file_name)

                    current_progress = (split_idx * self.split_count + file_idx + 1) / len(self.file_list) * 100
                    progress = int(current_progress)
                    if progress > prev_progress:
                        progress_bar = int(progress // 5)
                        remaining_progress_bar = 20 - progress_bar
                        print(f'{progress}% [{"=" * progress_bar}>{remaining_progress_bar * " "}] 파일 압축 진행 중...')
                        prev_progress = progress

        if len(self.split_list[-1]) != self.split_count:
            zip_file_full_name = os.path.join(self.target_path, f'{self.zip_file_name}_{TOTAL_SPLIT_COUNT + 1}.zip')
            with zipfile.ZipFile(zip_file_full_name, 'w') as myzip:
                for file_idx, file_name in enumerate(self.split_list[-1]):
                    file_full_path = os.path.join(self.folder_path, file_name)
                    myzip.write(file_full_path, file_name)

                    current_progress = (TOTAL_SPLIT_COUNT * self.split_count + file_idx + 1) / len(self.file_list) * 100
                    progress = int(current_progress)
                    if progress > prev_progress:
                        progress_bar = int(progress // 5)
                        remaining_progress_bar = 20 - progress_bar
                        print(
                            f'{min(100, progress)}% [{"=" * progress_bar}>{remaining_progress_bar * " "}] 파일 압축 진행 중...')
                        prev_progress = progress

        print('압축 완료!')
    def file_to_zip(self):
        self.get_file_list()
        self.split_files()
        self.make_zip_files()
