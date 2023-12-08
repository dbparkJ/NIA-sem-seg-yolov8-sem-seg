from utils import separate_file_zip

folder_path = r'D:\data\pycharm_project_data\BMWS1000RR'
zip_file_name = 'bike_image'
target_path = r'D:\data\pycharm_project_data'

fm = separate_file_zip.separate_zip(folder_path=folder_path, split_count=2000, zip_file_name=zip_file_name, target_path=target_path)
fm.file_to_zip()
