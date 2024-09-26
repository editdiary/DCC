import os
import shutil

def categorize_imgs(src, dest_dir):
    # src_folder 지정
    src_folder = os.path.join('./dataset', src)
    
    # dest_folder 지정(폴더가 없다면 생성)
    dest_folder = os.path.join(dest_dir, src)
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    
    # 오류 발생을 대비하여 처리된 이미지 수 추적
    processed_count = 0
    error_count = 0
    
    # src_folder의 모든 파일을 가져옴
    for filename in os.listdir(src_folder):
        if filename.endswith('.jpg'):
            try:
                # 파일명에서 style 정보 추출
                style = filename.split('_')[-2]

                # style에 해당하는 폴더가 없다면 생성
                style_folder = os.path.join(dest_folder, style)
                if not os.path.exists(style_folder):
                    os.makedirs(style_folder)
                
                # 원본 이미지 복사(copy2: metadata까지 복사)
                src_path = os.path.join(src_folder, filename)
                dest_path = os.path.join(style_folder, filename)
                shutil.copy2(src_path, dest_path)

                # 정상적으로 처리하였을 경우 count 증가
                processed_count += 1
    
            except Exception as e:
                # 에러가 발생하여 변환에 실패하면 에러 메시지 출력
                error_count += 1
                print(f"Error processing {filename}: {str(e)}")

    print(f"Images are categorized successfully! ==> Total images processed: {processed_count} / Total images failed: {error_count}")


if __name__ == "__main__":
    # 데이터가 묶여서 저장될 폴더
    dest_dir = './categorized_data'
    # 새로 만들어질 폴더가 없다면 생성
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # source data가 있는 폴더 지정
    train_path = "training_image"
    val_path = "validation_image"

    # style 별로 이미지 분류
    categorize_imgs(train_path, dest_dir)
    categorize_imgs(val_path, dest_dir)