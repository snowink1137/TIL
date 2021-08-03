# 변수, 배열, 반복문

## Java로 배우는 자료구조(Code01~Code15)

- C 프로그래밍이 함수들의 집합이라면, Java 프로그래밍은 Class들의 집합이다.

- Java에서는 variable length array를 만들 수 있다. 예전 C에서는 안됐던 기능. 요즘 C 버전들은 된다.

  - ```java
    // variable length array 예시
    int n = 100;
    int [] grades = new int [n];
    ```

- 변수를 선언할 수 있는 곳은?

  - method 내부
  - class 내부
  - class 외부는? 안됨!