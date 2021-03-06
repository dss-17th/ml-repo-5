# CNN을 이용한 재활용 쓰레기 분류 프로젝트 

### "지구온난화, 더 빨라진다…1.5도 상승 10년 당겨질듯"
최근 한 기사의 제목처럼 지구온난화는 점점 더 빠르고 심각한 문제로 대두되고 있습니다. 현대인들이 발생시키는 무작위한 자원낭비와 그로 인해 발생하는 환경오염은 개개인의 자원낭비를 막기 위한 노력만으로는 해결할 수 없는 상황에 이르렀습니다. 이렇게 환경 문제가 국제적으로 더욱 심각한 이슈가 되고 있는 가운데, 우리가 일상적으로 실천하고 있는 '쓰레기 재활용'의 중요성이 재조명되고 있습니다.

![title2](https://user-images.githubusercontent.com/80030759/128589633-c48a05f4-eae2-4bce-8bfe-f642f77bcbdf.jpeg)

쓰레기 재활용은 현재 심각하게 대두되고 있는 환경오염을 해결하기 위한 하나의 중요한 방법으로 각광받고 있습니다. 이미 사용된 자원을 재가공 후 재사용하여 자원낭비를 줄이고 폐기물을 감소시킬 수 있기 때문입니다. 쓰레기 재활용의 효율성을 재고하면 매년 막대하게 발생하는 폐기물들을 획기적으로 감소시킬 수 있기에 국제적으로 AI를 활용한 재활용에 관한 연구가 활발하게 진행되고 있습니다.

재활용에 있어 가장 핵심적인 부분은 쓰레기의 재가공에 앞서 재활용 가능한 자원을 효율적이고 정확하게 분류하는 것입니다. 저희 팀은 이러한 쓰레기 재활용을 위한 개인적 노력의 일환으로써, 우리 일상에서 많이 볼 수 있는 재활용 쓰레기를 각종 CNN모델을 활용하여 분류하는 프로젝트를 진행해 보았습니다.


## 1. Abstract

저희는 종이, 플라스틱, 유리, 캔 4개의 카테고리로 구성된 재활용 쓰레기를 분류하는 프로젝트를 진행하였습니다. 프로젝트를 진행한 결과 가장 성능이 좋은 모델은 Xception모델이며, validation accuracy는 0.863을 기록하였습니다. 

### 1-1. Data 소개

- Recycle_Classification_Dataset
- Jinyeong Wang - https://www.kaggle.com/paultimothymooney/kermany2018 

### 1-2. Target

- 이미지 전처리 및 각종 CNN모델을 활용한 재활용 쓰레기(캔,플라스틱,유리,종이) 분류

### 1-3. Process
- 데이터 수집
- 베이스라인 설정을 위한 바닐라 CNN모델링
- 오토라벨링
- CNN모델링
- 수동라벨링(카테고리별 특징추출)
- 각종 CNN 모델 활용한 분류
- 각종 모델별 특징 EDA
  - epoch당 변화 관찰
    - Fit time
    - loss 


### 1-4. Baseline 설정

<img width="648" alt="2021-07-08_2 49 51" src="https://user-images.githubusercontent.com/80455724/128825189-6fec566f-1ee2-46e1-8293-d9091c4a9e8d.png">

- 베이스라인을 설정하기 위하여 바닐라 CNN을 사용하였습니다.
- 이미지 전처리를 진행하지 않은 원본데이터를 모델링한 결과 val_acc가 0.4를 넘지 못했으며, val_loss는 1 이상을 기록하여, 이것을 베이스라인으로 하였습니다.

### 1-5. 이미지 전처리 과정

![unknown](https://user-images.githubusercontent.com/80455724/128831748-22251803-e9c9-4f9c-88b9-20ba9e4b6f48.png)


- 위쪽에 보이는 원본 이미지를, 오토라벨링을 통하여 아래와 같이 오브젝트에 맞게 이미지를 크롭하였으며, 오토라벨링한 이미지로 모델링을 다시 한번 진행하였습니다.

![rhZsZhGdVacAAAAASUVORK5CYII](https://user-images.githubusercontent.com/80455724/128827237-51196cf0-840f-41f4-876f-c19e30650862.png)

- 그 결과, val_acc가 0.92를 기록하였으나, 이것은 동일한 물체가 train데이터와 test데이터에 함께 포함되게 split하여 나온 결과 
- 정확한 모델링을 위하여 데이터를 코드를 통하여 수동으로 split하여 다시 모델링을 진행한 결과 val_acc가 0.7가량으로 확연히 낮아짐을 확인하였습니다.
- 모델 성능을 높이기 위하여, 카테고리별로 특징을 추출을 위한 수동라벨링을 진행

![unknown](https://user-images.githubusercontent.com/80455724/128831442-016b766f-5cc3-47cc-afbb-42b428fe60da.png)

- 특징추출한 데이터를 포함하여 모델링을 하였을 때 오히려 val_acc가 큰 변화가 없음을 확인하였습니다.


### 1-6.  CNN modeling

- 전처리한 이미지데이터의 모델링 성능을 높이기 위하여 바닐라CNN, lenet, VGGnet, Alexnet, Resnet 50, Google-net, X-ception 등을 활용
- 가장 성능이 좋았던 모델은 X-ception모델이었으며, imagenet으로 전이학습을 한 모델보다, 일반 모델이 더 좋은 성능을 보임을 확인하였습니다.

<img width="725" alt="스크린샷 2021-08-10 오후 5 38 53" src="https://user-images.githubusercontent.com/80455724/128835861-ce0e8093-ac33-4483-8412-ad263d7f0010.png">
- 최신 모델의 경우 에포크마다 들쭉날쭉한 모습을 보이는 반면, lenet이나 바닐라cnn같은 고전적인 모델의 경우 전체적인 성능이 낮아도 에포크마다 안정적인 모습을 보여줌

### 1.7. Conclusion

<img width="719" alt="스크린샷 2021-08-10 오후 5 15 12" src="https://user-images.githubusercontent.com/80455724/128832616-941202b0-552b-4eac-877d-768bcc9c7676.png">

- 가장 높은 성능을 보여준 모델은 Xception모델로 Val_accuracy가 0.8635를 기록

![download](https://user-images.githubusercontent.com/80455724/128834354-f50f88be-d87c-47fa-ba94-c45b790043ad.png)

- 전반적으로 양호한 예측결과를 보여주었으나, 가장 오분류가 많았던 카테고리는 플라스틱과 종이였습니다.
- 특히 종이를 플라스틱으로 잘못 예측하는 경우가 가장 많았습니다.
- 차후 이미지데이터를 추가하고, 카테고리별로 세부분류(종이백,우유곽 등)를 진행하여 예측성능 개선을 시도해 볼 예정입니다.

## 2. File 설명
- auto_labeling.ipynb : 라벨링 자동화(jpg -> json) & 인코더(json -> jpg)
  - Idea : 많은 사진들이 흰색배경에 객체가 놓여있는 경우가 많았다. 그래서 Clustering을 이용해서 색을 나누어 줬고, closest_color라는 함수로 RGB로 두 개의 색으로 나누어 줘서 색이 나뉘는 경계 부분을 기록해서 JSON으로 만들었다.
 
- model별 accu.ipynb : 각각의 모델들을 모아놓은 file, 모델 뒤에 128이라고 써있는 부분은 input_size가 (128, 128, 3)인 경우, 없는 경우는 모델에 최적화 된 input_size를 사용한 경우다.
  - 데이터 특징 : sklearn의 train_test_split을 이용한 split이 아닌, 수동으로 split한 모델이다.

- model별accu.csv : 위의 파일에서 모델별 각 에포크당 loss, accu, fit_time을 정리해놓은 파일

- model data EDA : 최적의 model을 찾는 동안, 한 가지 특징을 찾았는데, 좀 더 면밀히 보기 위해서 위의 파일에서 csv로 빼서 각각의 모델 별 특징을 보았다.
  - Idea : 우선 XceptionNet을 제외한 나머지 모델은 비슷한 결과를 가졌다. 그러나 vanilla CNN, LeNet 등의 고전의 모델들의 특징이 있었는데, 에포크의 변화에도 크게 loss, accu의 변화가 없었다는 것이다. 파일의 맨 밑의 그래프에 그려져 있다시피 다른 모델들은 위아레 진폭이 크게 있는 반면, vanillaCNN, LeNet은 일정한 accu, loss를 가지고 있었다.

## 3. 개선점 및 프로젝트를 통해 배운 점
- 모델링 결과 종이를 플라스틱으로 잘못 예측하는 경우가 많았으나, 보다 많은 데이터와 이미지 전처리를 통해 개선할 예정입니다.
- 수동라벨링이 모델 성능 개선에 영향을 주지 못한 부분이 아쉬웠습니다.
- 이미지 필터링을 적용해보는 접근방법이 부족하였습니다.

## 4. Members
- 지영 : 적용모델 탐색을 통한 모델적용, 데이터 라벨링
- 상구 : 데이터 오토라벨링, 수동 train_test_split, 모델 적용, 모델 EDA
- 경수 : 카테고리별 핸드라벨링, 베이스라인 설정, 다양한 CNN모델 탐색 및 적용, 리드미 작성

