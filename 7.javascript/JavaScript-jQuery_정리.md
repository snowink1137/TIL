> 코드잇 인터랙티브 웹 강의 중 다시볼 내용을 정리한 문서
>
> https://www.codeit.kr/learn/courses/interactive-web-programming

[TOC]

# JavaScript

## 1. 데이터를 다루는 법

### 변수와 상수

- let, const는 es6 이후에 나온 문법이다. var는 기존의 javascript에서 사용하던 변수 선언 방식이다. let과 const로 var를 대체할 수 있기 때문에, 기본적으로 es6 이후에는 var를 권장하지 않는다

- ```javascript
  var score = 5;  // 변수
  const MAX_LEVEL = 99;  // 상수
  
  let score = 5;  // 변수
  score = 10;  // 괜찮음
  let score = 6;  // error! 재할당이 불가능하게 함으로써 변수를 좀더 안전하게 사용하게 한다
  ```



### 스타일 가이드

- https://github.com/tipjs/javascript-style-guide



### 숫자형

- 자바 스크립트에서는 정수와 실수를 특별히 구분하지 않고 type을 그냥 number라고 한다

- ```javascript
  typeof 3;  // "number"
  typeof 3.14;  // "number"
  ```



### 논리형

- ==: 값만 비교
- ===: 값과 데이터 타입까지 비교

- ```javascript
  3 == '3';  // true
  3 === '3';  // false
  ```



### Boolean의 활용

#### undefined vs null

- null은 비어있는 값, undefined는 변수에 아무것도 할당되지 않았을 때의 값이다

- ```javascript
  var n = null;
  var u;
  
  console.log(n);  // null
  console.log(u);  // undefined
  ```



#### NaN

- Not a Number

- ```javascript
  var n = parseInt('abcd');
  console.log(n);  // NaN
  ```



#### false와 true로 간주되는 것들

- ```javascript
  // 0은 false. 이외의 수 들은 true
  if (0) {
    console.log('0은 true');
  } else {
    console.log('0은 false');  // 출력되는 값
  }
  
  // 비어있는 문자열은 false. 이외의 문자열은 true
  if ('') {
    console.log('비어있는 문자열은 true');
  } else {
    console.log('비어있는 문자열은 false');  // 출력되는 값
  }
  
  // null, undefined, NaN는 false
  if (null || undefined || NaN) {
      console.log('null은 true');
  } else {
      console.log('null은 false');  // 출력되는 값
  }
  ```




### 형 변환

- Number(), String() 함수 등을 사용해서 형 변환이 가능하다
- window.prompt("표시할 문구") 같은 함수로 사용자로부터 값을 받아올 때 주로 쓰인다



### 배열

- ```javascript
  var iPad = [800, 'Black', true];  // 다양한 값을 담을 수 있다
  typeof brands;  // 배열이라고 나오지 않고 "object"라고 나온다 
  ```



### 문자열과 배열

- 문자+열 이기 때문에 문자열도 배열과 비슷한 부분이 있다

  - ```javascript
    // 배열처럼 대괄호로 인덱싱이 가능하다
    var text1 = 'Hello';
    console.log(text1[0]);  // H
    console.log(text2[0]);  // e
    
    // 길이를 측정하는 것도 비슷하다
    var text2 = ['H', 'e', 'l', 'l', 'o'];
    console.log(text1.length);  // 5
    console.log(text2.length);  // 5
    ```

- 문자열과 배열의 다른 점도 있다

  - ```javascript
    var text1 = 'Hello';
    var text2 = ['H', 'e', 'l', 'l', 'o'];
    
    console.log(typeof text1)  // string
    console.log(typeof text2)  // object
    
    console.log(text1 == text2);  // false
    ```

- 배열은 mutable이고 문자열은 immutable이다

  - ```javascript
    // 배열은 mutable
    var text1 = ['h', 'e', 'l', 'l', 'o'];
    text1[0] = 'b';
    console.log(text1);  // ["b", "e", "l", "l", "o"]
    
    // 문자열은 immutable
    var text2 = 'hello';
    text2[0] = 'b';
    console.log(text2);  // hello
    ```



## 2. 코드의 흐름 1

### 함수

- ```javascript
  function logTask(task) {
      console.log(task + ": 완료");
      console.log("-");
  }
  
  logTask("보고서 작성");
  ```



### if 문

- ```javascript
  var inputNumber = window.prompt('숫자를 입력해주세요!')
  
  if (inputNumber === '7') {
      alert('Lucky!');
  } else if (inputNumber === '0'){
      alert('Zero!');
  } else {
      alert('Unlucky!');
  }
  ```



### switch 문

- ```javascript
  var courseName = 'A';
  switch (courseName) {
      case 'a':
      case 'A':
          console.log('course A');
          break;
      case 'b':
      case 'B':
          console.log('course B');
          break;
      default:
          console.log('주문이 잘못되었습니다.');
          break;
  }
  ```



## 3. 코드의 흐름 2

### for 반복문

- ```javascript
  var brands = ['A', 'B', 'C', 'D', 'E', 'F'];
  for (var i=0; i<6; i=i+1) {
      console.log(brands[i]);
  }
  ```



### for of 반복문

- 파이썬의 `for x in X:`랑 비슷하다고 생각하면 될 듯. ES6 부터 가능한 기능

- ```javascript
  for (value of values) {
      console.log(value);
  }
  ```



### for in 반복문

- 인덱스를 편하게 가져오는 반복문이라고 생각하면 됨
- 하지만 별로 추천되는 반복문은 아니다. IE8에서 오류가 나기도 하며, 실행 황경에 따라 배열에 저장된 값의 순서가 보장되지 않는 문제점이 있다. ES6에서 삭제하려고 했지만 이미 for in 반복문을 사용하는 코드가 많아서 삭제하지 못했다

- ```javascript
  var arr =  ['Americano', 'Latte', 'Tea'];
  
  for (var k in arr) {
    console.log(k);
  }
  
  /* result
  0
  1
  2
  */
  ```



### while 반복문

- ```javascript
  var i = 0;
  while (i < 6) {
      console.log(arr[i]);
      i++;
  }
  ```



### Math

- ```javascript
  console.log(Math.abs(-10));  // 10
  console.log(Math.max(2, -1, 4, 5, 0));  // 5
  console.log(Math.min(2, -1, 4, 5, 0));  // -1
  console.log(Math.pow(2, 3));  // 8
  console.log(Math.sqrt(25));  // 5
  console.log(Math.round(2.3));  // 2
  console.log(Math.floor(2.49));  // 2
  console.log(Math.random());  // 0 이상 1 미만의 유리수 랜덤으로 추출
  ```



### String

- ```javascript
  var str = 'Codeit';
  console.log(str.length);  // 6
  console.log(str.toUpperCase());  // CODEIT
  console.log(str.toLowerCase());  // codeit
  
  var str = 'Codeit';
  console.log(str.charAt(2));  // d
  
  var str = 'Hello World!';
  console.log(str.indexOf('z'));  // -1
  console.log(str.indexOf('o'));  // 4. 처음 발견된 인덱스가 리턴됨
  console.log(str.lastIndexOf('o'));  // 7. 가장 나중 인덱스가 리턴됨
  console.log(str.substring(2, 5));  // llo. 인덱스 2부터 인덱스 4까지 잘라서 리턴
  console.log(str.substr(2, 5));  // llo W. 인덱스 2부터 길이를 5만큼 잘라서 리턴
  
  var str = '        Hello World!      ';
  console.log(str.trim());  // Hello World!
  ```



### Array

- ```javascript
  var brands = ['Apple', 'Coca-Cola', 'Starbucks'];
  console.log(brands.length);  // 3
  console.log(brands.indexOf('Starbucks'));  // 2
  console.log(brands.indexOf('Kakao'));  // -1
  
  brands.push('Samsung', 'LG', 'Facebook');
  console.log(brands);  // ['Apple', 'Coca-Cola', 'Starbucks', 'Samsung', 'LG', 'Facebook']
  
  var lastBrand = brands.pop();
  console.log(brands);  // ['Apple', 'Coca-Cola', 'Starbucks', 'Samsung', 'LG']
  
  console.log(brands.join());  // Apple,Coca-Cola,Starbucks,Samsung,LG
  console.log(brands.join('#'));  // Apple#Coca-Cola#Starbucks#Samsung#LG
  ```



### Date

- ```javascript
  var date = new Date();  // 현재 날짜 Date 객체 리턴
  
  // 1988년 6월 11일 5시 25분 30초
  var date1 = new Date('June 11, 1988 05:25:30');
  var date2 = new Date('1988-06-11T05:25:30');
  
  // 1999년 12월 15일 (날짜만)
  var date3 = new Date('1999-12-15');
  var date4 = new Date('12/15/1999');
  var date5 = new Date('December 15 1999');
  var date6 = new Date('Dec 15 1999');
  
  var date = new Date('June 11, 1988 05:25:30');
  console.log(date.getDate());  // 6. 일요일을 0으로 시작하여 숫자로 표현됨
  console.log(date.getMonth());  // 5. 0부터 시작해서 6월을 뜻함
  console.log(date.getSeconds());  // 30
  console.log(date.getMilliseconds());  // 0
  console.log(date.toString());  // Sat Jun 11 1988 05:25:30 GMT+1000 (KDT)
  console.log(date.toLocaleString());  // 6/11/1988, 5:25:30 AM
  console.log(date.getTime());  // 581973930000. timestamp
  ```




# jQuery

## 1. jQuery 기초

### jQuery 개요

- 자바스크립트를 편하게 사용할 수 있는 라이브러리
  
  - 순수 자바스크립트(Vanilla)로 동적인 변화를 주려면 코드가 길어지기 때문이다
  
  - ```javascript
    // Vanilla javascript 예시
    document.getElementById('home').addEventListener('click', clickHome);
    document.getElementById('seoul').addEventListener('click', clickSeoul);
    document.getElementById('tokyo').addEventListener('click', clickTokyo);
    document.getElementById('paris').addEventListener('click', clickParis);
    
    // jQuery 사용 코드 예시
    $('#home').on('click', clickHome);
    $('#seoul').on('click', clickSeoul);
    $('#tokyo').on('click', clickTokyo);
    $('#paris').on('click', clickParis);
    ```
  
  - 실무에서는 점차 사용하지 않는 것이 추세이다. 현재 프론트엔드 개발에는 angular, react, vue 같은 것들을 많이 사용한다. 하지만 jQuery로 쓰여진 코드들이 많기 때문에 알아는 두는 것이 좋다



### 이벤트 & 이벤트 핸들링

- 이벤트: HTML 요소들에게 일어나는 여러 가지 일들  
  ex) 요소 클릭, 마우스 커서 올리기, 마우스 커서 내리기, 페이지 로딩, 키보드 입력 등

- 이벤트 핸들링: 이벤트가 일어났을 때 어떤 동작이 일어나도록 하는 것  
  ex) 키보드 'q'를 누르면 게임이 끝나게 하는 것 등

- ```javascript
  // 이벤트 및 이벤트 핸들링 예시
  <!DOCTYPE html>
  <html>
  <head>
    <title>로그인</title>
    <meta charset="utf-8">
    <link rel="stylesheet" href="styles.css">
    <link href="https://fonts.googleapis.com/earlyaccess/notosanskr.css" rel="stylesheet">
  </head>
  <body>
    <div class="login-form">
      <form>
        <input type="text" name="email" id="email-input" class="text-field" placeholder="아이디"><br>
        <input type="password" name="password" id="password-input" class="text-field" placeholder="비밀번호"><br>
        <input type="submit" value="로그인" id="submit-btn">
      </form>
  
      <div class="links">
        <a href="#">비밀번호를 잊어버리셨나요?</a>
      </div>
    </div>
  
    <script
    src="https://code.jquery.com/jquery-3.2.1.min.js"
    integrity="sha256-hwg4gsxgFZhOsEEamdOYGBf13FyQuiTwlAQgxVSNgt4="
    crossorigin="anonymous"></script>
    <script>
      // 여기에 코드를 작성하세요.
      $('#email-input').on('input', checkInput);
      $('#password-input').on('input', checkInput);
  
      function checkInput() {
          var email = $('#email-input').val();
          var password = $('#password-input').val();
          
          if (email === '' || password === '') {
              $('#submit-btn').css('background-color', '#9B9B9B');
          } else {
              $('#submit-btn').css('background-color', '#1BBC9B');
          }
      }
    </script>
  </body>
  </html>
  ```



## 2. jQuery 활용

