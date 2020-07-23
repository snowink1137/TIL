# 자바 정리

- codeit 자바 기초 강의 메모



## 1. 자바 왕기초

### 꾸준한 인기 언어, 자바

- Fortune 500 기업의 90%가 백엔드 언어로 자바를 사용 중
- 오랫동안 인기를 얻어왔기 때문에, 커뮤니티와 정보가 많음
- 따라서, 개발자 수요도 가장 많은 언어이다



### 자바와 객체 지향

- 자바는 객체 지향의 개념이 언어에 강하게 드러난다

  - ```java
    public class HelloWorld {
        public static void main(String[] args) {
            System.out.println("Hello");
        }
    }
    ```
  
  - 프린트 한 줄을 해도 public, class, static, void, System, out 등 객체 지향적 구조와 설계를 **정확히** 표현하는 것에 특화된 언어이다
  
  - cf) 파이썬 역시 객체 지향이 적용된 언어이지만, 객체 지향이 강하게 드러나는 언어는 아니다. 많은 내용을 생략하고, 쉽게 코드를 작성하는 것에 초점이 맞춰져 있다



### Hello World 이해하기

- ```java
  public class HelloWorld {
      public static void main(String[] args) {  // 자바 프로그램을 실행하면 가장 먼저 main을 찾아서 실행시킨다. 따라서 실행시키고 싶은 자바 코드가 있다면, main 안에 넣어주면 된다. static은 그 부분을 바로 실행 가능하게 만든다. 따라서 main은 가장 첫 번째로 실행되어야 하기 때문에, main 앞에는 항상 static을 붙인다
          System.out.println("Hello");  //System이라는 클래스의, out이라는 변수의, println이라는 메소드 호출
      }
  }
  ```



### 자료형

```java
long x = 12345678910L; // 정수 자료형의 기본은 int. long은 큰 정수를 다룰 때 씀. 수 뒤에 L을 붙여줘야 한다

float f = 3.14f;  // 소수 자료형의 기본은 double. float은 double보다 정밀도가 낮다. float 자료형을 사용할 때는 수 뒤에 f를 붙여줘야 한다

char a1 = 'a';
char a2 = 97;  // 이런식으로 'a'에 해당하는 아스키코드인 97을 쓸 수도 있다
char a3 = '\u0061';  // 이런 식으로 유니코드를 담을 수도 있다
char a4 = '가';
```



### 연산자

- 나누기 연산할 때 피연산자 중 하나라도 소수형이 있으면 결과도 소수형으로 나온다. 소수형이 정수형보다 랭크가 높다
- `!true == false`
- 이스케이프 문자로 줄 바꿈 할 때, 맥에서는 "\n", 윈도우에서는 "\r\n"을 사용해야 함



### 형 변환

- 숫자형 랭킹은 더 넓은 범위를 가질 수록 높다(∴ double ~ byte 순으로 랭크가 높다)

- 바꾸고자 하는 형이 기존의 형보다 넓은 데이터를 담을 수 있는 자료형일 경우 특별한 처리 없이 형 변환이 가능하다. 반대의 경우에는 타입 캐스팅을 해줘야 한다  

  ```java
  int a = 36;
  double b = a;     // int to double
  
  short c = 17;
  long d = c;       // short to long
  
  float e = 3.14f;
  double f = e;     // float to double
  
  int a = 3;
  double b = (double) a;
  long c = (long) a;
  ```



### switch문

- 조건문의 조건 부분의 결과가 boolean 말고 int, String 같은 것일때 주로 쓴다

- ```java
  // switch문 예시
  switch (grade) {
      case "A+":  // 이렇게 case 부분에 break 안달아주면 해당 case 수행 부분을 거친 후 다른 case 부분에도 들어간다
      case "A":
      case "B":
          System.out.println("참 잘했어요!");
          break;
      case "C":
      case "D":
          System.out.println("조금만 더 노력해 볼까요?");
          break;
      case "F":
          System.out.println("Fail입니다.");
      default:  // default 부분은 항상 실행
          System.out.println("다시 수강해주세요.");
          break;
  }
  ```



### for문

- while문과 달리 초기화식이 있고 for문 안에서만 쓸 수 있는 변수를 만들 수 있다. 이러한 장점에 따른 쓰임새는 다음과 같다
  - 반복의 인덱스가 필요한 경우
  - 반복의 최대 횟수가 정해진 경우
  - 갯수가 정해진 데이터 셋(배열, 리스트 등)의 내용을 하나씩 봐야할 경우



### 배열

- ```java
  // 생성 방법 1
  int[] intArray = new int[5];
  
  // 생성 방법 2
  int[] intArray;
  intArray = new int[5];
  
  // 생성 방법 3
  int[] intArray = {1, 2, 3, 4, 5};
  
  // 오류나는 생성 방법
  int[] intArray;
  intArray = {1, 2, 3, 4, 5};
  
  // 배열 복사하기
  int[] arr1 = {1, 2, 3, 4, 5};
  int[] arr2 = arr1.clone();
  
  // 배열 크기 알아내기
  intArray.length;
  
  // for-each 문법 활용
  for (int i : intArray) {
      System.out.println(i);
  }
  
  for (double i : intArray) {
      System.out.println(i);
  }
  ```



### 다중 배열

- ```java
  // 다중 배열 생성 방법 1
  int[][] multiArray = new int[3][4];  // 3 * 4 사이즈의 빈 배열
  
  // 다중 배열 생성 방법 2
  int[][] multiArray = {
      {1, 2, 3, 4},
      {5, 6, 7, 8},
      {9, 10, 11, 12}
  };
  ```




## 2. 자바 객체 지향 프로그래밍

### 객체 지향이란?

- 정보와 동작들을 객체 단위로 묶고, 이런 객체들을 연결시키면서 정리하는 프로그래밍 방식



### 접근 제어자

- 접근 제어뿐만 아니라 변수에 원하지 않는 값이 들어가는 것도 방지하는 역할
  - ex) 음수가 들어가면 안되는 변수



### 메소드 오버로딩

- 똑같은 이름으로 파라미터 구성만 다르게 메소드 작성하면 됨

  - cf) 파이썬에서는 기본 값 설정을 통해 하나의 메소드로 작성했었음

  - ```python
    def stackoverflow(self, i=None):
        if i is None:
            print('first form')
        else:
            print('second form')
    ```



### this

- 현재 인스턴스 가리키는 역할뿐만 아니라 생성자로 쓸 수도 있다  

  ```java
  // 이렇게 생성자가 여러 개인 경우 this의 반복이 많다
  public Person(String name) {
      this.name = name
      age = 12;
      cashAmount = 0;
  }
  
  public Person(String name, int age) {
      this.name = name;
      this.age = age;
      cashAmount = 0;
  }
  
  public Person(String name, int age, int cashAmount) {
      if (age < 0) {
          this.age = 12;
      } else {
          this.age = age;
      }
  
      if (cashAmount < 0) {
          this.cashAmount = 0;
      } else {
          this.cashAmount = cashAmount;
      }
      this.name = name;
  }
  
  // 위와 같은 여러 개의 생성자를 this를 생성자로 사용하면 더 간단하게 표현할 수 있다
  public Person(String name) {
      this(name, 12, 0); // 12살을 기본 나이로 설정, 초기 현금 보유액은 0원.
  }
  
  public Person(String name, int age) {
      this(name, age, 0); // 초기 현금 보유액은 0원.
  }
  
  public Person(String name, int age, int cashAmount) {  // 이렇게 가장 많은 파라미터를 가진 생성자를 직접 작성한 후 this 생성자를 활용하는 것이 좋다
      if (age < 0) {
          this.age = 12;
      } else {
          this.age = age;
      }
  
      if (cashAmount < 0) {
          this.cashAmount = 0;
      } else {
          this.cashAmount = cashAmount;
      }
      this.name = name;
  }
  ```

  

### 기본형(Primitive Type) vs. 참조형(Reference Type)

- 기본형
  - 변수가 값 자체를 보관
  - ex) int, boolean, char, double
- 참조형
  - 변수는 값이 보관되어 있는 영역을 가리킴
  - ex) Person, String, int[]
- null
  - '비어있음'을 표현하는 값
  - 참조형 변수만 가질 수 있는 값이다
  - 어떤 객체를 가리키는 이름표, 즉 변수는 있는데 가리키는 대상이 없는 경우
    - 따라서 `null != ""`이다



### 변수 안전하게 만들기(final)

- 변수를 정의할 때 final을 써주면 '상수'가 된다. 즉, 한 번 정의하고 나서 다시 바꿀 수 없다
- 배열의 length 변수는 상수로 만들어져 있다
- final로 상수를 만들면 getter, setter 없이 바로 가져다 쓰는 식으로 코딩하면 된다



### 인스턴스 변수 vs. 클래스 변수

- ```java
  // 인스턴스 변수 예시
  public class Person {
      int count;
  }
  
  // 클래스 변수 예시 1
  public class Person {
      static int count;
  }
  
  // 클래스 변수 예시 2
  public class Person {
      static int count;
  
      public Person() {
          count++;
      }
  }
  
  // 상수는 보통 클래스 변수로 쓴다
  public class CodeitConstants {
      public static final double PI = 3.141592653589793;
      public static final double EULERS_NUMBER = 2.718281828459045;
      public static final String THIS_IS_HOW_TO_NAME_CONSTANT_VARIABLE = "Hello";
  
      public static void main(String[] args) {
          System.out.println(CodeitConstants.PI + CodeitConstants.EULERS_NUMBER);  // 클래스 변수 사용법
      }
  }
  ```

- 클래스 변수는 인스턴스가 아닌 클래스에 속한 변수라고 생각하면 됨

- 모두가 공유하는 값을 쓸 때는 클래스 변수로 쓰자



### 인스턴스 메소드 vs. 클래스 메소드

- 클래스 변수와 마찬가지로, 클래스 메소드는 인스턴스가 아닌 클래스에 속한 메소드라고 생각하면 됨

- ```java
  // 클래스 메소드 사용 예시 1
  import java.lang.Math;
  
  public class Driver {
      public static void main(String[] args) {
          System.out.println(Math.abs(-10));   // 절댓값
          System.out.println(Math.max(3, 7));  // 두 값 중 최댓값
          System.out.println(Math.random());   // 0.0과 1.0 사이의 랜덤값
      }
  }
  // 클래스 메소드 사용 예시 2
  public static void main(String[] args) {
      ...
  }
  ```

  - 이처럼 인스턴스의 생성 없이 메소드만 모아서 사용하고 싶을 때, 클래스 메소드를 만들어 쓰면 된다
  - main은 자바 프로그램의 시작점이다. 첫 번째로 실행되는 코드이니, 어떤 인스턴스도 생성되어 있지 않다. 따라서 클래스 메소드여야 하는 것이다

- "생성된 인스턴스가 하나도 없더라도 이 메소드를 호출하는 것이 말이 되는가?" 가 맞는 경우에 클래스 메소드를 사용하면 된다