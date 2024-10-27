import os
from PIL import Image
from tqdm import tqdm

def resize_imgs(origin_path, dest_path):
    total_processed = 0
    total_errors = 0

    for src in ['training_image', 'validation_image']:
        src_folder = os.path.join(origin_path, src)
        dest_folder = os.path.join(dest_path, src)
        if not os.path.exists(dest_folder):
            os.makedirs(dest_folder)

        # 전체 이미지 수 계산
        total_images = sum(1 for filename in os.listdir(src_folder) if filename.endswith('.jpg'))

        print(f"\nProcessing {src} folder:")
        for filename in tqdm(os.listdir(src_folder), total=total_images, desc=f"Resizing {src}"):
            if filename.endswith('.jpg'):
                try:
                    input_path = os.path.join(src_folder, filename)
                    output_path = os.path.join(dest_folder, filename)
                    img = Image.open(input_path)
                    img_resized = img.resize((224, 224), Image.LANCZOS)
                    img_resized.save(output_path)
                    total_processed += 1
                except Exception as e:
                    total_errors += 1
                    print(f"\nError processing {filename}: {str(e)}")

    print(f"\nResizing completed!")
    print(f"Total images processed successfully: {total_processed}")
    print(f"Total images failed: {total_errors}")


if __name__ == "__main__":
    # path 지정
    MAIN_PATH = "C:/Users/prohe/OneDrive/Desktop/github_manage/DCC"
    origin_path = os.path.join(MAIN_PATH, "b_pad_data")
    dest_folder = os.path.join(MAIN_PATH, "b_pad_resized_data")

    # 새로 resized 된 파일을 저장할 폴더가 없다면 생성
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    resize_imgs(origin_path, dest_folder)