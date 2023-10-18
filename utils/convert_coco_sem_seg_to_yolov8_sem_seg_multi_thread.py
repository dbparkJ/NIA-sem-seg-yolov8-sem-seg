import json
import os
from tqdm import tqdm
from multiprocessing import Pool, Manager


# JSON 파일을 텍스트 파일로 변환하는 함수
def convert_json_to_txt(json_file_path, output_folder, progress_dict):
    with open(json_file_path, 'rb') as json_file:
        json_data = json_file.read().decode('utf-8', 'ignore')

    data = json.loads(json_data)

    image_info = data['images'][0]
    image_width = image_info['width']
    image_height = image_info['height']

    json_filename = os.path.basename(json_file_path)
    txt_filename = os.path.join(output_folder, json_filename.replace('.json', '.txt'))

    with open(txt_filename, 'w') as txt_file:
        annotations = data['annotations']
        for annotation in annotations:
            category_id = annotation['category_id'] - 1
            segmentation = annotation['segmentation'][0]

            # Extract x, y coordinates from the segmentation
            x_coords = segmentation[::2]
            y_coords = segmentation[1::2]

            normalized_coords = [f"{x / image_width:.6f} {y / image_height:.6f}" for x, y in zip(x_coords, y_coords)]
            txt_file.write(f"{category_id} {' '.join(normalized_coords)}\n")

    progress_dict[json_file_path] = 1

# 루트 폴더와 하위 폴더에서 JSON 파일 검색
def find_json_files(folder):
    json_files = []
    for dirpath, dirnames, filenames in os.walk(folder):
        json_files.extend([os.path.join(dirpath, filename) for filename in filenames if filename.endswith('.json')])
    return json_files


def process_json_file(json_file_path, output_folder, progress_dict):
    convert_json_to_txt(json_file_path, output_folder, progress_dict)


if __name__ == '__main__':
    root_folder = r'D:\data\258.지자체 도로부속시설물 파손 데이터\01.데이터\Validation\labels'  # 루트 폴더 경로
    output_folder = r'D:\data\valid\labels'  # 출력 폴더 경로

    json_files = find_json_files(root_folder)

    manager = Manager()
    progress_dict = manager.dict()
    for json_file in json_files:
        progress_dict[json_file] = 0

    with Pool(processes=os.cpu_count()) as pool:
        for _ in tqdm(pool.starmap(process_json_file,
                                   [(json_file, output_folder, progress_dict) for json_file in json_files]),
                      total=len(json_files), desc="JSON을 TXT로 변환 중"):
            pass
