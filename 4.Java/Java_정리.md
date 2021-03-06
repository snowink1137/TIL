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



### String 클래스

- 비교연산자 `==`는 기본형의 경우 값이 같은지 확인하고, 참조형의 경우에는 가리키는 인스턴스가 같은지 확인한다
- 문자열의 경우 참조형이므로 문자열의 내용을 비교하기 위해서는 `==`로 하면 안되고 `equals`메소드를 사용해야 한다
  - cf) switch 문에서도 내부적으로 `==`대신 `equals`메소드를 사용하는 것이다



### Wrapper Class

- 기본 자료형을 객체 형식으로 감싸는 역할을 하는 클래스

- 기본형 자료형(Primitive Type)을 참조형(Reference Type)처럼 다루어야할 때 Wrapper 클래스를 사용한다

  - 예를 들어 ArrayList같은 컬렉션을 사용할 때는 반드시 참조형을 사용해야 한다

- Wrapper 클래스의 인스턴스는 생성자로 생성할 수도 있고, 리터럴로 생성할 수도 있다

  - ```java
    Integer i = new Integer(123);
    Integer i = 123;
    
    System.out.println(123 == 123);  // true
    System.out.println(new Integer(123) == new Integer(123));  // false
    System.out.println(new Integer(123).equals(new Integer(123)));  // true
    ```



### ArrayList, HashMap

- ```java
  // ArrayList, HashMap 사용 예시
  import java.util.ArrayList;
  import java.util.HashMap;
  
  public class Main {
      public static void main(String[] args) {
          ArrayList<Pokemon> arrayList = new ArrayList<>();
          arrayList.add(new Pokemon("이상해씨"));
          arrayList.add(new Pokemon("이상해풀"));
          arrayList.add(new Pokemon("이상해꽃"));
          System.out.println(arrayList.get(0));
          System.out.println(arrayList.get(1));
          System.out.println(arrayList.get(2));
          
          HashMap<String, Pokemon> pokedex = new HashMap<>();
          pokedex.put("피카츄", new Pokemon("피카츄"));
          pokedex.put("파이리", new Pokemon("파이리"));
          pokedex.put("이상해씨", new Pokemon("이상해씨"));
          pokedex.put("이상해풀", new Pokemon("이상해풀"));
          pokedex.put("이상해꽃", new Pokemon("이상해꽃"));
          
          pokedex.remove("이상해풀");
          System.out.println(pokedex.get("피카츄"));
      }
  }
  ```



## 3. 자바 중급 개념

### 상속

- 코드 중복성을 제거하기 위해 사용한다

- 부모의 변수, 메소드를 사용하는 경우

  - ```java
    public class BankAccount {
        .
        .
        .
        boolean withdraw(int amount) {
            ...
        }
    }
    
    public class TransferLimitAccount extends BankAccount {
        private int transferLimit;
    
        @Override
        boolean withdraw(int amount) {
            if (amount > transferLimit) {
                return false;
            }
    
            return super.withdraw(amount);
        }
    }
    ```

  - 이런식으로 `super` 키워드를 사용해서 부모의 메소드를 사용할 수 있다

  - `@override` 어노테이션을 사용하면, 부모 클래스에 해당 메소드 이름이 없는 경우 오류 메세지를 준다

  - 부모의 private 변수는 자식에게도 상속되지 않는다

- 부모의 생성자가 사용되는 경우

  - 자식 클래스의 인스턴스가 생성되기 위해서는 부모 클래스와 자식 클래스의 초기 설정을 모두 해주어야 한다. 즉, 부모 클래스의 생성자도 불려야 한다

  - 부모 클래스의 생성자는 `super.([변수])` 형식으로 부를 수 있다. `this` 키워드를 사용해서 자기 자신의 클래스를 부르는 것과 같은 개념이다

  - 부모 클래스의 생성자 사용 규칙 요약

    1. 자식 클래스의 인스턴스 생성시, 부모 클래스의 생성자는 반드시 불린다. 따라서 부모 클래스에 명시된 생성자가 없으면, 자동으로 제공되는 부모 클래스의 기본 생성자가 불린다  

       ```java
       public class Parent {
           ...
       }
       
       public class Child extends Parent {
           ...
       }
       
       Child c = new Child(); // Child 인스턴스 생성시 Parent의 생성자도 불림
       ```

    2. 부모 클래스에 기본 생성자가 없는 경우, 자식 클래스에서 반드시 직접 부모 클래스의 생성자 호출을 코드로 작성해야 한다  

       ```java
       public class Parent {
           // 별도로 생성자가 지정되어있는 경우 (파라미터 없는 기본 생성자가 없는 경우)
           public Parent(int a, int b) {
               ...
           }
           ...
       }
           
       public class Child extends Parent {
           public Child() {
               super(0, 0); // 자식 클래스에 생성자를 만들어 'super(int, int)'를 호출해 주어야 함
               ...
           }
       }
       ```

    3. 부모 클래스의 생성자를 명시적으로 호출하는 경우, 반드시 자식 클래스 생성자 맨 윗줄에 적어야 한다  

       ```java
       public class Child extends Parent {
           public Child() {
               int a = 0;
               ...
               super(0, 0); // 이 곳에서 호출할 수 없음. 반드시 첫 번째 줄에 있어야 함. 오류 난다.
           }
       }
       ```



### protected 접근 제어자

- private 접근 제어자와 유사하지만 **자식 클래스에선 접근 가능**하다

- ```java
  public class BankAccount {
      protected int balance;
      ...
  }
  
  public class MinimumBalanceAccount extends BankAccount {
      ...
      @Override
      public boolean withdraw(int amount) {
          // if (getBalance() - amount < minimum) {
          if (balance - amount < minimum) {
              System.out.println("적어도 " + minimum + "원은 남겨야 합니다.");
              return false;
          }
      
          // setBalance(getBalance() - amount);
          balance -= amount;
          return true;
      }
  }
  ```



### 객체를 위한 클래스(Object Class)

- Object 최상위 클래스, 모든 클래스의 부모 클래스

- 따라서 클래스를 만들어서 아무 메소드를 만들지 않더라도 Object 클래스가 갖고 있는 메소드는 쓸 수 있다

- [댓글 질문] Object Class equals 메소드에 대해서. 왜 같은 내용의 문자열로 생성한 두 객체가 equals 메소드로 비교했을 때 다른가?

  - ```java
    class Student {
        String name;
        Student(String name) {
            this.name = name;
        }
    }
    
    public class ObjectDemo {
        public static void main(String[] args) {
            Student s1 = new Student("전우치");
            Student s2 = new Student("전우치");
            System.out.println(s1 == s2);
            System.out.println(s1.equals(s2));
        }
    
    }
    ```

  - [댓글 답변] String 끼리 비교할 때 값으로 비교할 수 있었던 것은 String 클래스에서 equals 메소드를 overriding 해서 값으로 비교하는 방식으로 바꾼 것이다. 기본적으로 Object 클래스에서 제공하는 equals 메소드는 `==` 연산자와 같다



### 타입 캐스팅

- 업캐스팅
  - 부모 클래스를 타입으로 사용하는 것
  - 하나의 부모를 공유하는 자식 클래스 인스턴스들을 묶어서 다룰 때 편함  
    ex) 여러 인스턴스가 같은 메소드를 반복적으로 사용하는 경우
  - 업캐스팅을 하면 부모 클래스에 존재하는 메소드만 사용 가능하다
- 다운캐스팅
  - 부모 클래스를 타입으로 사용하다가 다시 해당 인스턴스를 생성했던 클래스를 타입으로 사용하는 것
  - 업캐스팅을 했을 때 부모 클래스에 존재하는 메소드만 사용할 수 있으므로 다시 다운캐스팅을 해서 원래 클래스에 있는 메소드를 사용한다
  - 반복문 안에서 `instanceof` 키워드로 자식 클래스들을 구분하는 로직을 만들 수 있다



### 제네릭(Generic)

- \<Generic\>을 사용하면 (Casting) 의 불편한 점을 해결할 수 있다

- ```java
  // 제네릭을 사용하지 않을 경우의 불편함 예시
  
  // 이렇게 어떤 타입이라도 담을 수 있도록 Box라는 클래스를 정의할 수 있다
  public class Box {
      private Object something;
      
      public void set(Object object) {
          this.something = object;
      }
      
      public Object get() {
          return something;
      }
  }
  
  // 그래서 이런 식을 사용할 수 있다
  Box box = new Box();
  Phone phone = new Phone();
  box.set(phone);
  
  Phone unboxed = (Phone) box.get();  // 다시 꺼낼 때는 Object 타입으로 반환되므로 반드시 타입캐스팅을 해줘야 한다. 만약 box.get()에서 나오는 타입이 Phone이 아니라면 오류가 날 수도 있으므로 위험한 방식이다
  ```

- 따라서 Box라는 클래스를 정의할 때 약간 느슨하게(?) 타입을 강제해놓지 않는 방식이 제네릭이다. 따라서 각 타입에 맞는 Box를 새로 만들지 않고도 타입 캐스팅 및 오류를 줄일 수 있는 문법이다

- ```java
  public class Box<T> {  // <T>: 타입 파라미터, 타입 변수. 이러한 것을 받는 클래스를 제네릭 클래스라고 부른다
      private T something;
      
      public void set(T object) {
          this.something = object;
      }
      
      public T get() {
          return something;
      }
  }
  
  // 사용 예시
  Box<Phone> box = new Box<>();  // 이렇게 Box 인스턴스를 생성할 때 필요한 타입을 정의한다
  Phone phone = new Phone();
  box.set(phone);
  
  Phone unboxed = box.get();  // 그러면 이제 get() 메소드를 사용할 때 타입 캐스팅을 해줄 필요도 없고, 타입 오류가 날 경우를 줄일 수도 있다
  ```

- 보통 타입 파라미터의 경우 T나 E를 많이 쓴다. 하지만 아무렇게나 정의해도 괜찮다. 예를 들어 HashMap<K, V> 와 같은 경우에는 Key, Value를 뜻하는 파라미터로 정의해 놓았다

- 상속의 개념이 더해지면 제네릭을 더 다양한 방식으로 사용할 수 있다

  - 단순한 상속

    - ```java
      public class PhoneBox extends Box<Phone> {
          public void handsFreeCall(String numberString) {
              object.call(numberString);  // 이 Phone 타입의 object가 Phone의 자식 클래스 인 경우, 타입 캐스팅이 필요할 것이다
          }
      }
      ```

    - 이렇게 Box에 Phone만 담을 수 있도록 고정하고, Phone이 담긴 Box에 맞게 고치고 싶을 때 상속을 이용할 수 있다. 하지만 Phone을 상속받아서 여러 가지 Phone의 자식들이 있는 경우 다시 Generic을 사용하기 전과 같은 문제가 생긴다. 타입이 Phone으로 고정되어 있으므로 Phone의 자식들이 오버라이딩 해 둔 메소드라던지 자식들만 가지고 있는 메소드를 사용할 때 또 타입 캐스팅을 해줘야 하기 때문이다. 그래서 이러한 경우 다음과 같은 방식이 사용될 수 있다

  - 타입 파라미터를 상속으로 정의하기

    - ```java
      public class PhoneBox<T extends Phone> extends Box<T> {
          public void handsFreeCall(String numberString) {
              object.call(numberString);  // 애초에 object의 타입을 Phone으로부터 상속되었다고 정의했기 때문에, object가 Phone의 자식 클래스 인스턴스여도 타입 캐스팅이 필요 없다
          }
      }
      ```

    - 이러한 방식으로 T 라는 타입 파라미터 자체를 Phone을 상속받는다고 명시해두면, Phone 자식들의 메소드를 타입캐스팅 문제 없이 사용할 수 있다



### 인터페이스(Interface)와 추상 클래스(Abstract Class)

- 추상 클래스 vs 인터페이스

  - ```
    [Best 답변]
    abstract클래스는 이름 그대로 클래스로 생각하셔야 합니다. 그런데, 강의에서 말씀 드렸던 것 처럼 미완성된 클래스(미완성된 부분은 빈 메소드로 표현)라고 생각 할 수 있습니다.
    
    미완성으로 비워두는 부분은 "작성자의 의도를 반영하라" 라는 명령이 될 수도 있고, "무조건 하위클래스를 만들어야만 한다" 라는 뜻일 수도 있습니다.
    
    실제 자바 API소스들 중에 abstract로 구현된 애들이 많이 있으며, 기회가 된다면 강의에서 분석해 보는 것도 해 보도록 하겠습니다.
    
    Interface는 Abstract 클래스처럼 사용할 수도 있지만 다른 부분이 더 많습니다. abastract 클래스는  상속으로 확장을 하기 때문에 하나의 부모로 부터 상속할 수 밖에 없지만, Interface는 상속이 아니라 구현(implement)방식으로 진행되기 때문에 여러개의 인터페이스를 구현할 수 있습니다.
    
    즉 인터페이스 구현은, 부모 자식 상관관계가 있어야 하는 클래스의 상속과는 달리 어떤 클래스(이미 부모를 많이 두고 있는 클래스 등)에서든 구현이 가능하기 하기 때문에 훨씬 유연하게 사용 가능합니다.
    
    [interface 사용 이유 - Best 답변]
    클래스를 이용한 상속은 A -> A1 -> A2 처럼 하나의 부모만 가질 수 있습니다.
    
    하지만 인터페이스는 상속과는 다른 "구현"이라는 방식을 쓰는데, 클래스 하나가 여러개의 인터페이스를 구현할 수 있습니다.
    
    클래스를 통한 상속이 뼈대를 이어 받는 것 처럼 생각한다면 인터페이스를 구현하는 것은 기능을 붙인다고 생각할 수 있습니다.
    
    하나의 부모로 부터 큰 뼈대를 상속 받고 필요한 기능들은 여러 인터페이스를 구현함으로써 붙일 수 있겠죠.
    
    인터페이스를 통한 기능 구현은 결국 메소드를 붙이는 것입니다. 그런데 그냥 메소드를 추가하는 것과 인터페이스를 구현하여 메소드를 붙이는 것의 차이는 있을까요?
    
    바로 인터페이스라는 이름과 관계가 있는데요, 인터페이스를 구현함으로써 이 클래스가 이 메소드를 가지고 있다는 것을 다른 클래스에게 알려주는 역할을 할 수 있게 됩니다. 즉, 다른 클래스와의 교류를 목적으로 한다고 할 수 있겠죠:)
    ```

- 인터페이스의 접근제어자는 public이다. private는 안된다. 다른 클래스와의 교류를 위해 반드시 구현해야하는 항목을 정해놓은 인터페이스의 의미를 생각해본다면 public이 맞다. 따라서 인터페이스에서는 접근제어자를 생략해도 된다.  
  또한 인터페이스는 추상 메소드만 있기 때문에, abstract도 생략해도 된다

- | 설계도      | 변수 | 메소드 | 빈 메소드(추상 메소드) |
  | ----------- | ---- | ------ | ---------------------- |
  | 일반 클래스 | O    | O      | X                      |
  | 추상 클래스 | O    | O      | O                      |
  | 인터페이스  | X    | X      | O                      |

- 추상 클래스는 상속용으로만 쓰이지 않고 익명 클래스라는 방식으로 직접 쓰일 수도 있다

  - ```java
    // 익명 클래스 예시
    // 어차피 한번만 쓰일 클래스라면 따로 클래스 파일을 만드는 수고를 덜 수 있다
    AbstractAnimal horse = new AbstractAnimal("말") {
        @Override
        public void cry() {
            System.out.println("히이잉");
        }
    }
    ```

- Comparable 인터페이스

  - API로 존재하는 인터페이스이다. `Collections.sort(리스트)`를 사용할 때 기준이 되는 `compareTo(비교할_목적_객체_인스턴스)`를 구현하도록 하는 인터페이스이다
  - `implements Comparable<목적_객체>` 를 사용해서 구현하면 된다

