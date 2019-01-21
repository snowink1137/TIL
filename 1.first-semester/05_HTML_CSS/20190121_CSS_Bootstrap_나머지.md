# 20190121 CSS Bootstrap 나머지

## 수업

### CSS, html

- float : block 요소들을 가로 정리할 때 쓰임.
- https://flexboxfroggy.com/#ko
  - css 코드 게임
- position
  - 크게 static, relative, absolute, fixed 옵션 있음
  - 기본적인 block의 배열에 변화를 준다.
  - static
    - 기본 옵션
    - top, bottom, left, right 옵션 안먹힌다. -> 다른 옵션들과 다른 점!
    - 보통 static은 잘 사용하지 않지만 설정된 position을 무시할 때 사용되기도 한다고 한다.
  - relative, absolute
    - top, bottom, left, right 옵션줄 때 absolute와 차이점이 생긴다.
    - absolute는 위치 옵션 기준을 자기 가장 가까운 상위 요소에만 맞춘다. 그리고 static은 무시한다.
    - relative는 static을 기준 정할 때 무시하지 않고 static의 원래 위치도 포함해서 위치를 계산한다.
  - https://thrillfighter.tistory.com/480
  - 이거보면서 ㄱㄱ하기
- 미디어 쿼리 개념 정리 하기



### django

- 설치
  - c9에서 진행하는 중.(ruby on rails 컴퓨터로 할당. 메모리가 더 많아서.)
  - 앞으로의 버전 관리를 위해 pyenv 설치하려함. c9 컴퓨터가 우분투라서 가능. 윈도우에서는 pyenv 불가능.
  - 그 전에 `sudo apt-get update` 한번 해줘야함. c9 컴퓨터 버전이 낮을 수 있어서. `sudo apt-get install openssl` 도. `sudo apt-get install zlib1g-dev` 도.
  - git에서 clone해와서 설치하면 되는데 readme에 방법 운영체제 별로 써있으니 읽어가면서 하면 된다.
  - 그리고나서 `pyenv install 3.7.1` 하면 파이썬 3.7.1 버전 설치 됨.







## 수업 이외

- semver(Semantic Versioning) => X.Y.Z
  - Major.Minor.Patch
  - Major: 많은 것이 바뀌어서, 새로 코드를 짜야한다.
  - Minor: 기능의 추가나 삭제가 있지만, 기존 코드를 부수진 않는다.
  - Patch: 버그 픽스
  - ex) python 3.6.7