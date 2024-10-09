# Update INFO - Mission 1

## Update 1 (2024/09/26)
> [Mission 1-1]은 해결했습니다.<br>
> 자세한 내용은 `mission1-1.ipynb` 파일에서 확인하실 수 있습니다.

> [Mission 1-1]에서 추후 작성해야 할 "성별&스타일 통계치"를 위해 결과를 csv 파일로 저장해두었습니다.<br>
> train과 validation 각각 저장하였으니 확인해보시면 좋을 거 같습니다.

## Update 2 (2024/09/30)
> [Mission 1-2] skeletal code로 생각해주시면 좋을 것 같습니다.<br>
>
> Google Drive 경로만 맞춰주시면 코드는 아마 정상적으로 작동할 것입니다.<br>
> 기본 코드만 작성해둔 것이다 보니 학습을 진행해도 성능은 좋지 않게 나올 것으로 생각됩니다.<br>
> 데이터 전처리, 파라미터 설정, 세부 사항 변경은 추후 회의 간 상의하면 될 것 같습니다. 


## Update 3 (2024/10/02)
> 추후 mission2의 결과물과 파일명을 헷갈리지 않도록 하기 위해, mission1-1의 csv 파일의 파일명을 수정했습니다.<br>
> - 수정 전: `train_metadata.csv` / 수정 후: `train_mission1-1.csv`
> - 수정 전: `val_metadata.csv` / 수정 후: `val_mission1-1.csv`
>
> 이에 따라 `mission1-1.ipynb` 파일의 마지막 csv 저장 부분 코드도 약간 수정 되었습니다.

## Update 4 (2024/10/03)
> [Mission 1-2]에서는 모델을 불러오지 않고 직접 층을 쌓는 걸 목표로 두고 있는 것 같아 코드를 변경 해 보았습니다<br>
> 전이학습을 못하지 이미지 전처리 과정이 중요해 보이는데 albumentation, 객체 감지해서 자르기, 색상 정규화, 엣지검출 등 생각해 볼게 많아 보이네요<br>
> 학습 속도도 느려보여 오래 걸릴 것 같네요


## Update 5(2024/10/06)
> [Mission 1-2]의 train_model과 validate_model 부분을 분리한 후 다시 올려두었습니다.<br>
> 기존의 코드는 train과 validate를 동시에 진행한 후 Epoch마다 pth 파일을 저장하는 방식이었으나 학습 시간이 지나치게 오래 걸려 수정했습니다.<br>
> 현재 학습을 진행 중이며 Epoch 10번을 기준으로 한다면 train에만 8시간정도가 예상됩니다.<br>
> 학습이 종료되면 train과 validate 결과도 업데이트 해두겠습니다.<br>


## Update 6(2024/10/09)
> [Mission 1-2]를 base skeletal code 업로드하였습니다.<br>
> ____ 처리한 부분만 수정하면 아마 정상 작동할 것으로 예상됩니다.<br>
> 수정 필요해 보이는 부분 있으면 수정 후 다시 업로드해주시면 됩니다.<br>
> [가중치 초기화] 코드도 추가하였습니다!
