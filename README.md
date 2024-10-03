# 데이터 크리에이터 캠프(DCC)
> 해당 페이지는 `2024 데이터 크리에이터 캠프`의 `지불호호불락 ` 팀이 협업하는 공간입니다.
>
> (update 예정)


# Update INFO

## Update 1 (2024/09/26)
> `categorize_img.py`는 실행하면 이미지를 복사하여 class(style)별로 분류해주는 코드입니다. 이후 분류 모델을 학습 시킬 때 편하지 않을까 싶어 작성했습니다.
>
> dataset의 크기가 크다보니 github에는 폴더만 만들어두었습니다.<br>
> Mission에서 제공하는 데이터를 압축해제 후, 이름을 `dataset`으로 변경하면 코드가 동작하는데 문제 없을 것으로 생각됩니다.<br>
> 즉, 폴더의 구조는 다음과 같이 되어 있으면 됩니다.
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

## Update 2 (2024/10/02)
> `filtering_labels.py` 파일을 만들었습니다.<br>
> [Mission 2]부터는 image 파일과 label 파일을 비교하여 유효한 data만 사용해야 합니다.<br>
> 이를 위해서 유효한 데이터만 filtering 하여 `/filtered_labels` 폴더에 복사하는 코드를 작성했습니다.<br>
> 필터링 되어 유효하지 않은 데이터의 경우 `/filtered_labels/invalid` 폴더에 모이도록 하였습니다.<br>
> Update1에서 사용했던 데이터의 폴더 구조가 그대로 있다면 특별히 경로를 설정하지 않으셔도 괜찮지 않을까 싶습니다.