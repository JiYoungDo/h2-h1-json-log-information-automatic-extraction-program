# **h2, h1 json 로그 정보 자동 추출 프로그램**

## **과제 선정 배경 및 필요성** 
h2의 목표 중 하나는 HTTP1.1의 성능 개선이다 웹페이지를 전송하는데는 HTTP1.1보다 일반적으로 더 h2가 빠르긴 하지만 항상 그런 것은 아니다.<br/>
성능에 영향을 주는 조건을 이해하는 것은 웹사이트를 , 최적화 하고 사용자 경험을 파악하는데 중요한 부분이다 . <br/><br/>

오늘 날에는 다양한 웹 서 웹서비스의 형태가 있다 이에 대해 각 별 성능평가의 객관적 지표를 제공하고자 한다 ,<br/> 위의 실험 수행 중 네트워크 Json파일을 읽는데에 번거로움이 있다고 생각했고 이를 편리하게 차트 . 로 표현하는 오픈 소스 프로그램을 만들어 필요한 사람들에게 기여하고자 한다.


## **과제 주요내용** 
1) 파일 분석 알고리즘 작성 
2) (Django) 프로그램 제작 환경 구축 
3) (Pythonanywhere) 웹 호스팅 서비스 사용 
4) (FusionChart) 외부 라이브러리 를 사용하여 시각화


## **과제 수행방법**
 1. django 웹 프레임워크를 사용하여서 웹사이트를 구축 
 2. pythonanywhere 호스팅 서비스를 사용하여 글로벌 서비스
    제공

<br/>
<br/>


► 과제수행 결과 오픈 소스 프로그램 코드
https://github.com/JiYoungDo/Capstone-Design 

► 오픈 소스 프로그램 주소
http://carrie.pythonanywhere.com/ 

► 성능 평가 엑셀 시트
https://docs.google.com/spreadsheets/d/1ifBqptXL09vX0zMQe1AGBAEvsHZwrHhqJvATiESnq1g/edit?usp=sharing 

### ► 서비스에서 사용하는 json 파일은 아래 링크를 통해 기록 할 수 있습니다. 
[chrome://net-export/](chrome://net-export/)


<br/>
<br/>

## **성능 평가 결과** 
✲ 이미지 개수와 무관하게 의 h2의 성능 이 h1에 비해 모두 우수 <br/>
✲ h1,h2 자체만을 봤을 때 이미지 사이즈 차이로 인한 성능 차이는 보이지 않으나 에 비해 h2 가 월등히 우수  <br/>
✲ 파일 사이즈가 클수록 가 더 우수한 성능을 보임 <br/>
> 결론 ) 이미지 개수, 이미지 사이즈, 파일 사이즈에 따른  send-recv 시간 차이 성능이 h2가 h1에 비해 우수함<br/>

## **오픈소스 프로그램 제작 결과**
✲ h2 로그에 대해서 작성한 알고리즘에 맞추어 를 send보낸 시간과 recv를 보낸시간의 차 값을 통해 해당 차이값을 쉽게 확인 할 수 있다<br/> 
✲ 사용자는 묶어서 그래프를 함게 보고 싶은 데이터를 group_id 의 이름을 같게 함으로써 설정 할 수 있는데 이를 통해 한눈에 데이터를 확인 할 수 있다<br/>

글로벌 서비스 주소는 아래와 같습니다. [carrie.pythonanywhere.com](http://carrie.pythonanywhere.com/)
<br/>
<br/>


## **기대효과 / 활용방안**
기대효과: 이미지 크기, 이미지 개수, 파일 사이즈 에 따른 웹 서비스를 설계하는 개발자들에게 참고 성능 지 표 제공 <br/>
네트워크 Json 파일을 업로드 하면,  send-recv 결과를 차트로 정리하여 보여주는 오픈소스 프로그램 기여 .<br/>

활용방안: 성능 평가 지표를 참고 자료로서 활용 가능/ 오픈 소스 프로그램을 통해 네트워크 로그를 쉽게 시각적으로 확인 가능<br/>


## **결론**
성능 평가의 면에서 이미지 개수 이미지 사이즈 파일 사이즈에 따른 send-recv 시간 차이 성능이 h2가 h1에 비해 우수하였습니다.<br/>

h2 에 대해서 오픈 소스 프로그램에서 json 파일을 읽고 원하는 데이터를 그래프로 그려주어 사용자들에게 쉽게 정보를 제공해줍니다 <br/>
추가적으로 h1 json 파일을 읽어 원하는 정보를 추출하는 알고리즘 및 서비스를 추가할 예정입니다 ,<br/>

<br/>
<br/>

## **오픈 소스 프로그램 그래프**
<br/>
<img width="633" alt="스크린샷 2021-06-29 오후 1 28 38" src="https://user-images.githubusercontent.com/48639426/123737466-f2559880-d8dd-11eb-9644-84886ed276c0.png">
<br/>
추가 디벨롭 부분<br/>
<img width="633" alt="스크린샷 2021-07-30 오후 7 04 13" src="https://user-images.githubusercontent.com/48639426/127637881-774f42b6-3eb7-417b-98bb-7b4d58cec190.png">

## **오픈소스 프로그램 영상**
https://drive.google.com/file/d/14MXKrivRkoumDcW90uZEFH2IxB6Ol4Jp/view?usp=sharing
<br/>
## **성능 평가 결과**
<br/>
<img width="633" alt="스크린샷 2021-06-29 오후 1 34 32" src="https://user-images.githubusercontent.com/48639426/123737899-c4bd1f00-d8de-11eb-9486-4bf8f1ae4322.png">



# KCSE 2022
## 추가 연구 진행: 동영상 스트리밍 서비스에 대한 h1, h2 성능 분석
<img width="400" src="https://user-images.githubusercontent.com/48639426/193160740-17c7ef7f-3280-47b5-bfd6-2d1d805fa143.png">
### KCSE 2022 논문집 링크:  (file:///C:/Users/SSG/Downloads/KCSE2022-proceedings-v5.pdf)

