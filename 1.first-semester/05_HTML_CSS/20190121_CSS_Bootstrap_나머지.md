# 20190121 CSS Bootstrap 나머지

## 수업

### CSS, html

- float : block 요소들을 가로 정리할 때 쓰임.

- https://flexboxfroggy.com/#ko

  - css 코드 게임하며 연습할 수 있는 사이트.
  - display: flex 옵션 연습할 수 있음.
  - flex 옵션을 쓰면 편하지만.. 익스플로러에서 지원 안됨.. 그래도 알아두자.

- display
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

- 가상 클래스 셀렉터(Pseudo-Class Selector)

  - 가상 클래스는 **요소의 특정 상태**에 따라 스타일을 정의할 때 사용된다.

  - ex)

    - 마우스가 올라와 있을때
    - 링크를 방문했을 때와 아직 방문하지 않았을 때
    - 포커스가 들어와 있을 때

  - ```html
    <!DOCTYPE html>
    <html>
    <head>
      <style>
        /* a 요소가 hover 상태일 때 */
        a:hover { color: red; }
        /* input 요소가 focus 상태일 때 */
        input:focus { background-color: yellow; }
      </style>
    </head>
    <body>
      <a href="#">Hover me</a><br><br>
      <input type="text" placeholder="focus me">
    </body>
    </html>
    ```

- 가상 요소 셀렉터(Pseudo-Element Selector)

  - 가상 요소는 **요소의 특정 부분**에 스타일을 적용하기 위하여 사용된다.

  - ex)

    - 요소 콘텐츠의 첫글자 또는 첫줄
    - 요소 콘텐츠의 앞 또는 뒤

  - ```html
    <!DOCTYPE html>
    <html>
    <head>
      <style>
        /* p 요소 콘텐츠의 첫글자를 선택 */
        p::first-letter { font-size: 3em; }
        /* p 요소 콘텐츠의 첫줄을 선택 */
        p::first-line   { color: red; }
    
        /* h1 요소 콘텐츠의 앞 공간에 content 어트리뷰트 값을 삽입한다 */
        h1::before {
          content: " HTML!!! ";
          color: blue;
        }
        /* h1 요소 콘텐츠의 뒷 공간에 content 어트리뷰트 값을 삽입한다 */
        h1::after {
          content: " CSS3!!!";
          color: red;
        }
    
        /* 드래그한 콘텐츠를 선택한다 */
        ::selection {
          color: red;
          background: yellow;
        }
      </style>
    </head>
    <body>
      <h1>This is a heading</h1>
      <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Explicabo illum sunt distinctio sed, tempore, repellat rerum et ea laborum voluptatum! Quisquam error fugiat debitis maiores officiis, tenetur ullam amet in!</p>
    </body>
    </html>
    ```


- 미디어 쿼리

  - 반응형 웹을 구성할 수 있도록 하는 기능

  - @media 를 붙여놓은 css 코드는 이를 구현하는 것이다.

  - 디바이스의 크기에 따라 css를 다르게 적용할 수 있다.

  - bootstrap의 grid 개념과 비슷한 것 같다.

  - ex)

    - ```css
      @media screen and (min-width:600px) {
        nav {
          float: left;
          width: 25%;
        }
        section {
          margin-left: 25%;
        }
      }
      @media screen and (max-width:599px) {
        nav li {
          display: inline;
        }
      }
      ```



### django

- 설치
  - c9에서 진행하는 중.(rails tutorial template로 컴퓨터 할당받기. 메모리가 더 많아서.)
  - 앞으로의 버전 관리를 위해 pyenv 설치하려함. c9 컴퓨터가 우분투라서 가능. 윈도우에서는 pyenv 불가능.
  - 그 전에 `sudo apt-get update` 한번 해줘야함. c9 컴퓨터 버전이 낮을 수 있어서. `sudo apt-get install openssl` 도. `sudo apt-get install zlib1g-dev` 도.
  - git에서 clone해와서 설치하면 되는데 readme에 방법 운영체제 별로 써있으니 읽어가면서 하면 된다.
  - 그리고나서 `pyenv install 3.6.8` 하면 파이썬 3.6.8 버전 설치 됨.
  - 설치 다 되고나면 `pyenv global 3.6.8` 입력해서 사용할 python 버전 바꿔주면 됨.







## 수업 이외

- semver(Semantic Versioning) => X.Y.Z
  - Major.Minor.Patch
  - Major: 많은 것이 바뀌어서, 새로 코드를 짜야한다.
  - Minor: 기능의 추가나 삭제가 있지만, 기존 코드를 부수진 않는다.
  - Patch: 버그 픽스
  - ex) python 3.6.7