# 데이터 크리에이터 캠프(DCC)
> 해당 페이지는 `2024 데이터 크리에이터 캠프`의 `지불호호불락` 팀이 협업했던 공간입니다.

## Final Update INFO
> 캡프를 진행하면서 <u>private로 생성했던 repo를 public으로 전환</u>하였습니다.

> 최종으로 제출했던 코드와 파일 구조에 맞춰 github를 재구성했습니다.<br>
> - `dataset` : 각 Mission 코드에서 사용되거나 생성되는 데이터를 모아둔 폴더
> - `Mission N.ipynb` : Mission을 수행한 코드입니다.
> - `Missino 1/2/3` : 각 Mission 코드를 실행하면 새로 생성되는 파일을 모아둔 폴더.
> - `requirements.txt` : 패키지 및 환경 정보입니다. Colab에서 만들어졌습니다.

## 최종 프로젝트 파일 구조
```
MyDrive/
│
├── dataset/
│   ├── filtered_label/
│   ├── origin_dataset/
│   └── tensor/
│
├── Mission1/
│   └── (Mission1 실행 결과 생성된 파일)
│
├── Mission2/
│   └── (Mission2 실행 결과 생성된 파일)
│
├── Mission3/
│   └── (Mission3 실행 결과 생성된 파일)
│
├── Mission1.ipynb
├── Mission2.ipynb
├── Mission3.ipynb
└── requirements.txt

```

## 협업 진행 과정
> 아래는 프로젝트 진행 상황을 공유하면서 남겼던 세부 업데이트 내용입니다.

### Update 1 (2024/09/26)
`categorize_img.py`는 실행하면 이미지를 복사하여 class(style)별로 분류해주는 코드입니다. 이후 분류 모델을 학습 시킬 때 편하지 않을까 싶어 작성했습니다.

dataset의 크기가 크다보니 github에는 폴더만 만들어두었습니다.<br>
Mission에서 제공하는 데이터를 압축해제 후, 이름을 `dataset`으로 변경하면 코드가 동작하는데 문제 없을 것으로 생각됩니다.<br>
즉, 폴더의 구조는 다음과 같이 되어 있으면 됩니다.
```
dataset/
│
├── training_image/
│   └── (training image files)
│
├── training_label/
│   └── (training label files)
│
├── validation_image/
│   └── (validation image files)
│
└── validation_label/
    └── (validation label files)
```

### Update 2 (2024/10/02)
`filtering_labels.py` 파일을 만들었습니다.<br>
[Mission 2]부터는 image 파일과 label 파일을 비교하여 유효한 data만 사용해야 합니다.<br>
이를 위해서 유효한 데이터만 filtering 하여 `/filtered_labels` 폴더에 복사하는 코드를 작성했습니다.<br>
필터링 되어 유효하지 않은 데이터의 경우 `/filtered_labels/invalid` 폴더에 모이도록 하였습니다.<br>
Update1에서 사용했던 데이터의 폴더 구조가 그대로 있다면 특별히 경로를 설정하지 않으셔도 괜찮지 않을까 싶습니다.

### Update 3 (2024/10/06)
2-2 문제를 80%정도 완료 하였습니다. <br>
20% 정도는 논의가 필요해보입니다.

### Update 4 (2024/10/06)
`resize_img.py` 파일을 추가했습니다.<br>
원본 이미지를 ResNet18에 입력되는 이미지의 크기인 224x224로 변환시켜주는 코드입니다.<br>
코랩에는 categorize_img.py 코드를 거쳐 스타일 별로 카테고리를 나눈 후, `resized_categorized_data` 폴더로 업로드 해두겠습니다.

### Update 5 (2024/10/09)
기존 `categorize_img.py`를 실행하면 label이 27개로 분류되었습니다.<br>
gender는 다르나 style이 겹치는 문제가 있는 것이 확인되어 현재는 {style}_{gender} 형식으로 31개의 label이 분류되도록 수정되었습니다.<br>
