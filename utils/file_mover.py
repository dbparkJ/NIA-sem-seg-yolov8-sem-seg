""""
해당 데이터는 이미지와 라벨의 수가 같아 서로 맞춰줄 필요가 없지만 필요한 경우 사용
"""

import os
import shutil
from tqdm import tqdm

# 이미지 파일이 있는 폴더 경로 입력
jpg_folder = "/home/hdd/workspace/computervision/yolov8_sem_seg/data_source/traffic_damage_data/train/images"

# 라벨 파일이 있는 폴더 경로 입력
txt_folder = "/home/hdd/workspace/computervision/yolov8_sem_seg/data_source/traffic_damage_data/train/labels"

# 이미지 폴더와 라벨 폴더 내의 파일 목록 가져오기
jpg_files = os.listdir(jpg_folder)
txt_files = os.listdir(txt_folder)

# 이미지 파일 이름과 라벨 파일 이름을 비교하고 라벨 파일을 복사
for jpg_file in tqdm(jpg_files, desc="복사 중"):
    jpg_filename, jpg_extension = os.path.splitext(jpg_file)
    txt_file = jpg_filename + '.txt'

    if txt_file in txt_files:
        src_path = os.path.join(txt_folder, txt_file)
        dest_path = os.path.join(
            '/home/hdd/workspace/computervision/yolov8_sem_seg/data_source/traffic_damage_data/train/labels_copy',
            txt_file)  # 복사할 폴더 경로 입력
        shutil.copy(src_path, dest_path)
