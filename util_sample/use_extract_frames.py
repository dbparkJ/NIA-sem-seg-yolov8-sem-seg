from utils import extract_frames

# 동영상 파일 경로 및 프레임을 저장할 폴더 지정
input_video_path = r"D:\data\pycharm_project_data\video\face.mkv"
output_folder_path = r"D:\data\pycharm_project_data"

# 동영상을 프레임으로 추출
extract_frames.video_to_frames(input_video_path, output_folder_path)