# Update INFO

## Update 1 (2024/10/02)
> [Mission 2-1] 해결했습니다. 자세한 코드는 `mission2-1.ipynb`를 확인해주세요<br>
> 결과 파일은 1-1처럼 추후 작성해야 할 "성별&스타일 통계치" 작성을 위해 csv로 저장해두었습니다.<br>
> 마찬가지로 train과 validation 각각 저장하였으니 확인해보시면 좋을 거 같습니다.

## Update 2 (2024/10/13)
> [Mission 2-1] 다시 해결했습니다.<br>
> 이때까지 저희가 많은 질문과 논의를 거치면서 유효한 데이터에 대한 기준을 다시 적립하였고, 현재 코드는 `이미지와 파일명이 동일한` label 데이터에 대해서만 filtering이 진행되었습니다.<br>
> `mission2-1.ipynb` 파일에 자세히 정리를 했습니다.<br>
> 유효한 label만 filtering 하는 코드는 mission2-1.ipynb 파일에 포함되어 있으나, `filtering_labels.py`도 따로 실행할 수 있도록 코드를 변경해두겠습니다.

> 유효한 label data를 필터링 후 분석의 코드는 구글드라이브 계정2에서 영채의 Mission1-1 코드를 바탕으로 작성되었습니다.<br>
> `training_df.csv`는 유효한 labeling 파일의 메타데이터가 정리된 파일이며, `training_count_data.csv`는 유효한 데이터에 대한 "성별&스타일"별 통계치입니다. 즉, 2-1 문제의 결과입니다.