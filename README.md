# CNN을 이용한 재활용 쓰레기 분류 프로젝트 

### "지구온난화, 더 빨라진다…1.5도 상승 10년 당겨질듯"
최근 올라온 한 기사의 제목처럼 지구온난화는 점점 더 빠르고 심각한 문제로 대두되고 있습니다. 터키에서 발생하고 있는 국가재난급의 산불과 유럽전역의 이상고온현상은, 지구온난화가 가져온 뚜렷한 기후변화를 우리로 하여금 체감하게 합니다. 현대인들이 발생시키는 무작위한 자원낭비와 그로 인해 발생하는 환경오염은 개개인의 자원낭비를 막기 위한 노력만으로는 해결할 수 없는 상황에 이르렀습니다. 이렇게 환경 문제가 국제적으로 더욱 심각한 이슈가 되고 있는 가운데, 우리가 일상적으로 실천하고 있는 '쓰레기 재활용'의 중요성이 재조명되고 있습니다.

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

- 그 결과, val_acc가 0.92를 기록하였으나, 이것은 동일한 물체가 train데이터와 test데이터에 함께 포함되게 split하여 나온 결과였습니다. 
- 정확한 모델링을 위하여 데이터를 코드를 통하여 수동으로 split하여 다시 모델링을 진행한 결과 val_acc가 0.7가량으로 확연히 낮아짐을 확인하였습니다.
- 모델 성능을 높이기 위하여, 카테고리별로 특징을 추출을 위한 수동라벨링을 진행하였습니다.

![unknown](https://user-images.githubusercontent.com/80455724/128831442-016b766f-5cc3-47cc-afbb-42b428fe60da.png)

- 특징추출한 데이터를 포함하여 모델링을 하였을 때 오히려 val_acc가 큰 변화가 없음을 확인하였습니다.


### 1-6.  CNN modeling

- 전처리한 이미지데이터의 모델링 성능을 높이기 위하여 바닐라CNN, lenet, VGGnet, Alexnet, Resnet 50, Google-net, X-ception 등을 활용하였습니다
- 가장 성능이 좋았던 모델은 X-ception모델이었으며, imagenet으로 전이학습을 한 모델보다, 일반 모델이 더 좋은 성능을 보임을 확인하였습니다.

<img width="725" alt="스크린샷 2021-08-10 오후 5 38 53" src="https://user-images.githubusercontent.com/80455724/128835861-ce0e8093-ac33-4483-8412-ad263d7f0010.png">
- 최신 모델의 경우 에포크마다 들쭉날쭉한 모습을 보이는 반면, lenet이나 바닐라cnn같은 고전적인 모델의 경우 전체적인 성능이 낮아도 에포크마다 안정적인 모습을 보여주었습니다.

### 1.7. Conclusion

<img width="719" alt="스크린샷 2021-08-10 오후 5 15 12" src="https://user-images.githubusercontent.com/80455724/128832616-941202b0-552b-4eac-877d-768bcc9c7676.png">

- 가장 높은 성능을 보여준 모델은 Xception모델로 Val_accuracy가 0.8635를 기록하였습니다. 

![download](https://user-images.githubusercontent.com/80455724/128834354-f50f88be-d87c-47fa-ba94-c45b790043ad.png)

- paper를 plastic으로 잘못 예측하는 경우가 많았습니다.

## 2. File 설명


## 3. 개선점 및 프로젝트를 통해 배운 점
- 모델링 결과 종이를 플라스틱으로 잘못 예측하는 경우가 많았으나, 보다 많은 데이터와 이미지 전처리를 통해 개선할 예정입니다.
- 수동라벨링이 모델 성능 개선에 영향을 주지 못한 부분이 아쉬웠습니다.
- 이미지 필터링을 적용해보는 접근방법이 부족하였습니다.

## 4. Members
- 지영
- 상구
- 경수

