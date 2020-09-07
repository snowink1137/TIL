# JavaScript 정리

> 코드잇 인터랙티브 웹 토픽 1 JavaScript 기초 강의 중 다시볼 내용을 정리한 문서
>
> https://www.codeit.kr/learn/courses/interactive-web-programming



[TOC]



## 1. 데이터를 다루는 법

### 변수와 상수

```javascript
var score = 5;  // 변수
const MAX_LEVEL = 99;  // 상수
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

- 