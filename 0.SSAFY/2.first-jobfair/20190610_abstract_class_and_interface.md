# 추상클래스와 인터페이스

## Java로 배우는 자료구조

### abstract class

- 추상(abstract) 메서드는 선언만 있고 구현이 없는 메서드
- "추상 메서드를 포함한 클래스는 추상 클래스"
- 추상 메서드와 추상 클래스는 키워드 abstract로 표시
- 추상 클래스는 객체를 만들 수 없음. 따라서 서브 클래스를 만드는 용도로만 사용됨.
  - 클래스의 목적이 객체를 만들기 위한 것 만은 아님. 서브 클래스를 만드는 용도로만 사용되는 경우도 있음..! ex) 이전에 실습했던 Event 객체는 직접 사용되지 않고 구체적인 Event들(duration, oneday 등..)의 상위클래스로서의 역할만 했었다. 그리고 다형성의 원리에 의해 하나의 배열을 사용할 때만 썼었다.
  - 그래도 굳이 쓸 필요는 없지 않나?
  - 써야할 때가 있다. Event 클래스를 통해 만들어진 서브 클래스들이 같은 역할을 하지만 내용은 조금씩 다른 메서드(isRelevant 메소드) 를 사용할 때, 만약 Event 클래스에 isRelevant 메소드가 없다면 컴파일러가 오류를 잡아낸다. 다형성의 원리에 의해 하나의 배열에 여러 구체적인 Event들(duration, oneday 등..)이 담겼는데, 그들의 타입은 Event로 되어있는 상황에서 isRelevant 메소드는 없기 때문이다. 따라서 이런 경우에는 Event 클래스에 추상 메소드를 만들어서 Event 클래스를 추상 클래스로 만드는 것이 적절하다.



### interface

- 추상 메서드만을 가진 순수한! 추상 클래스. 극단적인 추상 클래스라고 생각하면 됨. 약간씩 차이는 있음.

  - static final 데이터 멤버(상수)는 가질 수 있음.

  - ```java
    // example
    public interface Payble{
        public double calcSalary();
        public boolean salaried();
        public static final double DEDUCTIONS = 25.5;
    }
    
    public class Professor implements Payble {
        ...
        public boolean calcSalary(){...}
        public boolean salaried(){...}
        ...
    }
    ```

- Array.sort(Object [] a, int fromIndex, int toIndex)

  - 배열을 정렬해주는 API
  - 어떻게 이런 애들은 미리 작성된 코드인데 내가 무슨 타입의 배열을 정렬할지도 모르면서 정렬을 해줄까?
  - 이 sort 메소드는 사용자에게 한가지를 요구한다. Comparable 인터페이스를 implements 할 것을!
  - 이를 바탕으로 sort 메소드를 짜놓았기 때문에.. 내가 무슨 타입의 데이터를 쓰던지 간에 Comparable 인터페이스를 목적에 맞게 구현만 해놓았다면 항상 sort 메소드를 통해 정렬된 배열을 받을 수 있게 코드를 미리 짜놓을 수 있었던 것이다.
  - 만약 Comparable 인터페이스를 구현 안해놓은 타입의 배열을 정렬하려고 하면? 오류난다.
  - 이런식의 메소드를 generic하다고 한다.
  - generic: 포괄적인, 총칭[통칭]의
  - 인터페이스의 대표적인 사용 예.



### Interface vs. Abstract Class

- 추상 메서드로만 구성된 추상 클래스는 인터페이스와 완전히 동일한가?
- 다중 상속(multiple inheritance)
  - Java에서는 다중 상속을 허용하지 않는다. 하지만 하나의 클래스가 여러 개의 Interface를 implement하는 것은 가능.