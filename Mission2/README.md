# Update INFO - Mission 2
> 아래는 프로젝트 진행 상황을 공유하면서 남겼던 세부 업데이트 내용입니다.

## Update 1 (2024/10/02)
[Mission 2-1] 해결했습니다. 자세한 코드는 `mission2-1.ipynb`를 확인해주세요<br>
결과 파일은 1-1처럼 추후 작성해야 할 "성별&스타일 통계치" 작성을 위해 csv로 저장해두었습니다.<br>
마찬가지로 train과 validation 각각 저장하였으니 확인해보시면 좋을 거 같습니다.

## Update 2 (2024/10/13)
[Mission 2-1] 다시 해결했습니다.<br>
이때까지 저희가 많은 질문과 논의를 거치면서 유효한 데이터에 대한 기준을 다시 적립하였고, 현재 코드는 `이미지와 파일명이 동일한` label 데이터에 대해서만 filtering이 진행되었습니다.<br>
`mission2-1.ipynb` 파일에 자세히 정리를 했습니다.<br>
유효한 label만 filtering 하는 코드는 mission2-1.ipynb 파일에 포함되어 있으나, `filtering_labels.py`도 따로 실행할 수 있도록 코드를 변경해두겠습니다.

유효한 label data를 필터링 후 분석의 코드는 구글드라이브 계정2에서 영채의 Mission1-1 코드를 바탕으로 작성되었습니다.<br>
`training_df.csv`는 유효한 labeling 파일의 메타데이터가 정리된 파일이며, `training_count_data.csv`는 유효한 데이터에 대한 "성별&스타일"별 통계치입니다. 즉, 2-1 문제의 결과입니다.

## Update 2 (2024/10/15)
[Mission 2-2] 거의 다 완료했습니다.<br>
다만 마지막 데이터 그룹화에서 좀 어려움이 있습니다.

## Update 3 (2024/10/15)
[Mission 2-2] 완료했습니다.<br>
문제로 제시되었던 형식과 완전히 동일하게 출력될 수 있도록 코드를 수정했습니다.<br>
다만, 코드를 파일을 살펴보면 아시겠지만 <u>설문 응답을 많이 한 상위 100명을 모두 출력하면 출력이 너무 길어지는 문제</u>가 있습니다.<br>
현재 파일에는 상위 10명만 보이도록 해뒀는데, 어떻게 할 지 논의가 필요할 거 같습니다.

## Update 4 (2024/10/23)
ppt 내용을 채우면서 [Mission 2-1]의 코드를 일부 refactoring 하였습니다.<br>
대부분의 내용은 동일하지만, 메일로 공지가 왔었던 `W_27750_60_mods_M_146696.json` 파일을 제외하도록 수정된 부분이 있습니다.<br>
라벨링 파일 1개 차이기 때문에 큰 영향은 없을 거라고 생각은 들지만, 혹여나 [Mission3]에 영향을 미칠 수도 있을 거 같습니다.<br>
<u>[Mission3]을 수행하시기 전에 새로 바뀐 코드를 실행해서 라벨링 파일을 filtering 해주시기 바랍니다.</u>