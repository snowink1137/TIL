# Object 클래스와 Wrapper 클래스

## Java로 배우는 자료 구조

### class Object

- 클래스 Object는 Java에서 모든 클래스의 superclass이다.
- class Object의 멤버 메서드
  - equals
  - hashCode
  - toString
  - getClass
- Java의 모든 클래스는 내가 만들어 주지 않아도 이미 equals와 toString 메서드를 가지고 있다.
  - 다만 내 의도대로 작동하지는 않을 것이다.
  - 따라서 제대로 쓰기 위해서는 overriding 해서 써야 함.
- toString()
  - toString 메서드를 따로 만들어주지 않은 클래스의 객체에 대해서 toString 메서드를 호출하면 다음과 같은 String이 반환된다.
  - ex) PhoneBook@ef08879 (클래스이름@객체의hashcode)
- equals()
  - Object 클래스의 equals 메서드의 매개변수는 Object 타입이다.
  - 매개 변수로 제공된 객체와 자기 자신의 동일성을 검사한다.
  - 이 메서드를 의도대로 사용하려면(내용이 같은지 확인하는 것 등..) override 해야 한다.
    - override 안하면 진짜 그냥 같은 객체인지 다른 객체인지 판단해줌.
  - return 값은 boolean type



### class Class

- 모든 클래스는 하나의 Class 객체를 가진다.
- 이 객체는 각각의 클래스에 대해서 유일(unique)하다.
- 메서드 getClass()는 Object 클래스가 제공하는 메서드이며, 이 유일한 Class 객체 반환한다.
- 앞 페이지의 예에서 만약 `this.getClass()==obj.getClass()`가 true라면 우리는 비교 대상인 두 객체 (this와 obj)가 동일한 클래스의 객체임을 알 수 있다.



### Wrapper class

- 기본 타입의 데이터를 하나의 객체로 포장해주는 클래스.

- Java에서 primitive type 데이터와 non-primitive type 데이터, 즉 객체는 근본적으로 다르게 처리된다.

- 가령 Object 타입의 배열에는 다형성의 원리에 의해서 모든 종류의 객체를 저장할 수 있다. 하지만 int, double, char 등의 primitive type 데이터는 저장할 수 없다. 객체가 아니므로...

- 따라서 이와 같이 때때로 primitive type 데이터를 객체로 만들어야 할 경우가 있다. 이럴 때 Integer, Double, Character 등의 wrapper class를 이용한다.

- ```java
  // 이용 예시
  int a = 20;
  Integer age = new Integer(a);
  int b = age.intValue();  // b becomes 20
  ```

- 위의 과정을 Java 일정 버전 이후부터는 자동으로 제공해주긴 한다. Autoboxing, Unboxing.

- ```java
  // 데이터 타입간의 변환 기능도 제공
  String str = "1234";
  int d = Integer.parseInt(str);  // d becomes 1234
  ```

- 