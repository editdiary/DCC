# 데이터 크리에이터 캠프(DCC)
> 해당 페이지는 `2024 데이터 크리에이터 캠프`의 `지불호호불락 ` 팀이 협업하는 공간입니다.
>
> (update 예정)


# Update INFO

## [24/09/26]

### Update 1 
> [Mission 1-1]은 해결했습니다.<br>
> 자세한 내용은 `/dataset` 폴더에서 확인하실 수 있습니다.

### Update 2
> `categorize_img.py`는 실행하면 이미지를 복사하여 class(style)별로 분류해주는 코드입니다. 이후 분류 모델을 학습 시킬 때 편하지 않을까 싶어 작성했습니다.
>
> dataset의 크기가 크다보니 폴더만 만들어두었습니다.<br>
> Mission에서 제공하는 데이터를 압축해제 후, 해당 폴더의 하위 폴더로 넣으면 코드가 동작하는데 문제 없을 것으로 생각됩니다.<br>
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