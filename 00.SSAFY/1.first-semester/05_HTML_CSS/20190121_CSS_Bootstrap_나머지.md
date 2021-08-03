# 20190121 CSS Bootstrap 나머지

## 수업

### CSS, html

- inline-block

  - block과 inline 레벨 요소의 특징을 모두 갖는다. **inline 레벨 요소와 같이 한 줄에 표현되면서 width, height, margin 프로퍼티를 모두 지정할 수 있다.**

- float : 주로 block 레벨 요소들을 가로 정렬할 때 쓰임.

  - float 프로퍼티는 해당 요소를 다음 요소 위에 떠 있게(부유하게) 한다. 여기서 떠 있다(float)는 의미는 요소가 기본 레이아웃 흐름에서 벗어나 요소의 모서리가 페이지의 왼쪽이나 오른쪽에 이동하는 것이다. float 프로퍼티를 사용할 때 요소의 위치를 고정시키는 position 프로퍼티의 absolute를 사용하면 안된다.
  - width 프로퍼티를 선언하지 않은 block 레벨 요소에 float 프로퍼티가 선언되면 width가 inline 요소와 같이 content에 맞게 최소화되고 다음 요소 위에 떠 있게(부유하게) 된다.
  - float가 선언된 요소는 일반적인 흐름 상에 존재하지 않기 때문에 이후의 요소들과 정렬에서 문제가 생기는 경우도 있다.
    - `overflow: hidden;` 혹은 `::after 가상 요소 선택자` 를 사용해서 해결하는 경우가 많다고 한다.
    - 다른 방법 및 구체적인 방법은 출처를 참고.
  - [출처] https://poiemaweb.com/css3-float

- https://flexboxfroggy.com/#ko

  - css 코드 게임하며 연습할 수 있는 사이트.
  - display: flex 옵션 연습할 수 있음.
  - float 대신에 flex 옵션을 쓰면 편하지만.. 익스플로러에서 지원 안됨.. 그래도 알아두자.

- position
  - 크게 static, relative, absolute, fixed 옵션 있음
  - `position` 프로퍼티는 요소의 위치를 정의한다. top, bottom, left, right 프로퍼티와 함께 사용하여 위치를 지정한다.
  - static
    - static은 position 프로퍼티의 기본값으로 position 프로퍼티를 지정하지 않았을 때와 같다.
    - 기본적인 요소의 배치 순서에 따라 위에서 아래로, 왼쪽에서 오른쪽으로 순서에 따라 배치되며 부모 요소 내에 자식 요소로서 존재할 때는 **부모 요소의 위치를 기준으로 배치**된다.
    - top, bottom, left, right 옵션 안먹힌다. -> 다른 옵션들과 다른 점!
    - 기본적으로 이 값을 지정할 일은 없지만 이미 설정된 position을 무력화하기 위해 사용될 수 있다.
  - relative, absolute
    - relative
      - 기본 위치(static으로 지정되었을 때의 위치)를 기준으로 좌표 프로퍼티(top, bottom, left, right)를 사용하여 위치를 이동시킨다. static을 선언한 요소와 relative를 선언한 요소의 차이점은 좌표 프로퍼티의 동작 여부뿐이며 그외는 동일하게 동작한다.
    - absolute
      - 부모 요소 또는 가장 가까이 있는 조상 요소(static 제외)를 기준으로 좌표 프로퍼티(top, bottom, left, right)만큼 이동한다. 즉, relative, absolute, fixed 프로퍼티가 선언되어 있는 부모 또는 조상 요소를 기준으로 위치가 결정된다.
      - 만일 부모 또는 조상 요소가 static인 경우, document body를 기준으로 하여 좌표 프로퍼티대로 위치하게 된다.
      - 따라서 부모 요소를 배치의 기준으로 삼기 위해서는 부모 요소에 relative를 정의하여야 한다.
      - 이때 다른 요소가 먼저 위치를 점유하고 있어도 뒤로 밀리지 않고 덮어쓰게 된다. (이런 특성을 부유 또는 부유 객체라 한다)
      - absolute 선언 시, block 레벨 요소의 width는 inline 요소와 같이 content에 맞게 변화되므로 적절한 width를 지정하여야 한다.
    - relative, absolute 차이점!
      - relative 프로퍼티는 기본 위치(static으로 지정되었을 때의 위치)를 기준으로 좌표 프로퍼티(top, bottom, left, right)을 사용하여 위치를 이동시킨다. 따라서 **무조건 부모를 기준으로 위치**하게 된다.
      - absolute 프로퍼티는 부모에 static 이외의 position 프로퍼티가 지정되어 있을 경우에만 부모를 기준으로 위치하게 된다. 만일 부모, 조상이 모두 static 프로퍼티인 경우, document body를 기준으로 위치하게 된다.
      - 따라서 absolute 프로퍼티 요소는 부모 요소의 영역을 벗어나 자유롭게 어디든지 위치할 수 있다.
    - [출처] https://poiemaweb.com/css3-position#12-relative-%EC%83%81%EB%8C%80%EC%9C%84%EC%B9%98
    - [출처] https://poiemaweb.com/css3-position#13-absolute-%EC%A0%88%EB%8C%80%EC%9C%84%EC%B9%98

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