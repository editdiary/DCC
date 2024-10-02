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

## [24/09/30]

### Update 3
> [Mission 1-2] skeletal code로 생각해주시면 좋을 것 같습니다.<br>
>
> Google Drive 경로만 맞춰주시면 코드는 아마 정상적으로 작동할 것입니다.<br>
> 기본 코드만 작성해둔 것이다 보니 학습을 진행해도 성능은 좋지 않게 나올 것으로 생각됩니다.<br>
> 데이터 전처리, 파라미터 설정, 세부 사항 변경은 추후 회의 간 상의하면 될 것 같습니다. 


## [24/10/02]

### Update 4
> 추후 mission2의 결과물도 저장하기 위해, mission1-1의 csv 파일의 파일명을 수정했습니다.<br>
> - 수정 전: `train_metadata.csv` / 수정 후: `train_mission1-1.csv`
> - 수정 전: `val_metadata.csv` / 수정 후: `val_mission1-1.csv`
>
> 이에 따라 `mission1-1.ipynb` 파일의 마지막 csv 저장 부분 코드도 약간 수정 되었습니다.