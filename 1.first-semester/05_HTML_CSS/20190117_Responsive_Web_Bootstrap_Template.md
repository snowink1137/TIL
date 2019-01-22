# 20190117 Responsive Web/ Bootstrap Template

## 수업

### CSS

- 반응형 웹
  - 기계에 맞춰서 화면의 x% 만큼만 쓰겠다. 이런식으로 렌더링 하는 것.
- 크롬 개발자 도구에서 margin, border, padding, content 그림 나와 있다.
  - 여기서 border는 구역을 얘기하는 것이 아니라 선인데 글씨 쓰려고 구역처럼 그려져 있는 거다. 경계선을 두껍게 쓰는 경우가 있기도 하고.
  - margin은 박스 끼리의 거리를 얘기함. border 바깥쪽 거리라고 이해해도 될듯.
  - padding은 박스 안에서 content와 border의 거리를 얘기함. border 안쪽 거리라고 이해해도 될듯.
- width 옵션은 반응 없음. 브라우저가 작아도 안줄어듦.
  - max-width 옵션은 브라우저가 작으면 너비 줄여서 보여준다!
  - div 같은 박스 모델은 기본적으로 가로를 모두 차지하기 때문에 margin: auto 옵션은 max-width 옵션 하에서 의미가 있다.
- bootstrap 사용하면 편하게 css 사용할 수 있다.
  - bootstrap css 링크를 사용해서 파일을 보면 클래스 정의로 가득차 있다.
  - 이 클래스들을 html 구성할 때 사용하면되는 것이다.
  - documentation 읽어보면서 하면 됨
- 코딩 도장에서 파일 입출력 한번 보고 오기.

## 수업이외

- 어제 생겼던 문제(class 두번 선언하면 \_\_del\_\_ 작동 제대로 안하는 문제)
  - python tutor에서는 오류가 나지 않고, jupyter notebook에서 오류 나는 것은 그냥 내부적인 오류라고 생각하고 넘어갔었는데, vs code 에서도 그래서 다시 보게 됨.
  - debuger로 살펴보니.. 클래스를 새로 선언하면 클래스 객체의 주소가 바뀐다. 근데 기존에 생성했던 인스턴스는 여전히 예전 클래스 객체로부터 할당받은 주소를 가리키고 있는다. 따라서 새로운 클래스 객체로부터 다시 생성된다면, 기존 인스턴스가 삭제될 때도 이전에 가리키고 있던 클래스 객체의 소멸자 함수가 실행되어야 하는데, 새로운 클래스의 소멸자 함수가 실행된다. 이 과정에서 원하지 않는 결과가 나온다.
  - 클래스 변수는 새로 선언 되면서, 소멸자 함수는 예전의 인스턴스에도 영향을 끼쳐버리는 결과가 나온다.
  - 찾아보니 소멸자 함수는 웬만하면 안건드리는 것이 좋다고 한다. 가비지 컬렉터에 영향을 끼칠 수도 있어서. 그리고 애초에 클래스를 두번 선언하는 것도 비정상적인 상황이니.. 더 이상 신경쓰지 않고 이런게 있었다는 것만 기억하면 될 것 같다.
  - http://localhost:8888/notebooks/1.first-semester/01_basic/jupyter_notebooks/python101-students/07_OOP.ipynb
  - [출처] https://stackoverflow.com/questions/1935153/del-method-being-called-in-python-when-it-is-not-expected