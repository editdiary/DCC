import os
import shutil
from tqdm import tqdm

def filtering_label(dest_dir, state='train'):
    # 원본 데이터셋 경로
    src_folder = "C:/Users/prohe/OneDrive/Desktop/github_manage/DCC/dataset"

    if state == 'train':
        img_folder = 'training_image'
        lbl_folder = 'training_label'
    elif state == 'validation':
        img_folder = 'validation_image'
        lbl_folder = 'validation_label'

    src_path = os.path.join(src_folder, lbl_folder)
    dest_path = os.path.join(dest_dir, lbl_folder)

    if not os.path.exists(dest_path):
        os.makedirs(dest_path)

    # 오류 발생을 대비하여 처리된 이미지 수 추적
    copy_count = 0
    filtered_count = 0
    processed_count = 0
    error_count = 0

    image_lists = os.listdir(os.path.join(src_folder, img_folder))
    image_lists = [x.split('.')[0] for x in image_lists]

    label_lists = os.listdir(src_path)

    for file in tqdm(label_lists, desc=f"Processing {lbl_folder}", unit='file'):
        lbl_filename = file[:-12]

        src_file_path = os.path.join(src_path, file)
        dest_file_path = os.path.join(dest_path, file)

        try:
            if lbl_filename in image_lists:
                shutil.copy2(src_file_path, dest_file_path)
                processed_count += 1
                copy_count += 1
            else:
                filtered_count += 1
                continue
        except Exception as e:
            error_count += 1
            print(f"Error: {e}")

    print(f"\nFolder: {lbl_folder}")
    print(f"Filtered files: {filtered_count}, Copied files: {copy_count}")
    print(f"Processed files: {processed_count}, Error encountered: {error_count}\n")


if __name__ == "__main__":
    # 필터링된 라벨을 저장할 디렉토리
    dest_dir = "C:/Users/prohe/OneDrive/Desktop/github_manage/DCC/temp"
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    filtering_label(dest_dir, state='train')
    filtering_label(dest_dir, state='validation')