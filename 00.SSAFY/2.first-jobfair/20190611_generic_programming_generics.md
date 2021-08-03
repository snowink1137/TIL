# Generic 프로그래밍과 Generics

## Java로 배우는 자료 구조

### Generic Programming

- 제네릭 프로그래밍(Generic programming)은 데이터 형식에 의존하지 않고, 하나의 값이 여러 다른 데이터 타입들을 가질 수 있는 기술에 중점을 두어 재사용성을 높일 수 있는 프로그래밍 방식이다.

- 따라서 약간은 상대적인 개념일 수 밖에 없다. '좀더 generic하다' 이런식으로.

- generic <-> specific

- Generic한 변수/자료 구조

  - ```java
    // Event type을 쓰면 OneDayEvent, DurationEvent type을 각각 쓰는 것보다 상대적으로 generic하다!
    Event ev;
    Event [] events = new Event [capacity];
    
    // generic 끝판왕은 Object type이다.
    Object obj;
    ```

- Generic한 알고리즘(method)

  - ex) `Array.sort(shapes, 0, n)`

- Generic 클래스
  - Generic 클래스를 구현하기 위해서 새로운 문법이 필요한데 이를 Generics(C++ 에서는 이것을 class Template 라고 부른다)라고 부른다.



### Generics

- 제네릭(**Generic**)은 클래스 내부에서 사용할 데이터 타입을 외부에서 지정하는 기법을 의미한다.

- ```java
  // T라는 가상의 타입에 의해서 parameterized된 클래스
  // 이때 T는 type parameter라고 불리기도 함.
  public class Box<T> {
      private T t;
      public void set(T t) {
          this.t = t;
      }
      public T get() {
          return t;
      }
  }
  
  // 객체를 생성하는 시점에 가상의 타입 T를 실제 객체 안에서 사용하는 타입으로 지정해준다.
  Box<Integer> integerBox = new Box<Integer>();
  integerBox.set(new Integer(10));
  Box<Event> eventBox = new Box<Event>();
  eventBox.set(new OneDayEvent("dinner", new MyDate(2017, 2, 10)));
  ```

- 사실 꼭 Generics 개념을 사용해야하는 것은 아니다. 그냥 class 만들 때 변수들을 Object type으로 지정해놓고 나중에 객체로 만들어서 쓸 때 type casting 하면 된다. 하지만 계속 type casting하는 것이 안전한 프로그래밍 기법은 아니다. Generics를 사용하는 것이 좋다.



### Vector와 ArrayList

- Java API java.util은 Vector와 ArrayList라는 두 가지 유사한 기능의 클래스를 제공
- 우리가 작성한 MyArrayList는 ArrayList의 축소판
- Vector 보다 ArrayList가 좀 더 효율적이며 주로 사용됨
- 병렬성 이야기
  - ArrayList와는 달리 Vector 클래스는 synchronized됨, 즉 다수의 thread가 충돌 없이 Vector 객체를 액세스 할 수 있음.
  - CopyOnWriteArrayList 클래스