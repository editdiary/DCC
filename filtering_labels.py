import os
import shutil

def process_dataset(src_image, src_label):
    # src_folder 지정
    img_folder = os.path.join('./dataset', src_image)
    lbl_folder = os.path.join('./dataset', src_label)

    # 필터링된 label을 저장할 폴더 생성
    filtered_folder = "./filtered_labels"
    if not os.path.exists(filtered_folder):
        os.makedirs(filtered_folder)

    # 하위 폴더(training_label or validation_label) 생성
    dest_dir = os.path.join(filtered_folder, src_label)
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # 오류 발생을 대비하여 처리된 이미지 수 추적
    processed_count = 0
    error_count = 0

    # img 폴더에서 고유한 이미지 ID 추출(중복을 막기 위해 set 사용)
    image_ids = set()
    for filename in os.listdir(img_folder):
        if filename.endswith('.jpg'):
            image_id = filename.split('_')[1]
            image_ids.add(image_id)

    # label 폴더의 json 파일 처리
    for filename in os.listdir(lbl_folder):
        if filename.endswith('.json'):
            try:
                # label 파일에서 이미지 ID 추출
                image_id = filename.split('_')[1]

                # label의 이미지 ID가 목록에 있는 경우 파일을 처리
                src_path = os.path.join(lbl_folder, filename)
                if image_id in image_ids:
                    # 파일을 복사하여 저장
                    dest_path = os.path.join(dest_dir, filename)
                    shutil.copy2(src_path, dest_path)
                else:
                    # 유효하지 않은 이미지 ID인 경우 invalid 폴더에 저장
                    invalid_dir = os.path.join(dest_dir, "invalid")
                    if not os.path.exists(invalid_dir):
                        os.makedirs(invalid_dir)

                    dest_path = os.path.join(invalid_dir, filename)
                    shutil.copy2(src_path, dest_path)
                
                # 정상적으로 처리하였을 경우 count 증가
                processed_count += 1
            
            except Exception as e:
                # 에러가 발생하여 변환에 실패하면 에러 메시지 출력
                error_count += 1
                print(f"Error processing {filename}: {str(e)}")

    print(f"Labels are filtered successfully! ==> Total labels processed: {processed_count}/{len(os.listdir(lbl_folder))} | Total labels failed: {error_count}/{len(os.listdir(lbl_folder))}")


if __name__ == "__main__":
    # 데이터셋 경로 설정
    src_train_img = 'training_image'
    src_train_label = 'training_label'
    src_val_img = 'validation_image'
    src_val_label = 'validation_label'

    process_dataset(src_train_img, src_train_label)
    process_dataset(src_val_img, src_val_label)