# 상속(inheritance)

## Java로 배우는 자료구조

### 상속

- A Computer has
  - manufacturer
  - processor
  - RAM
  - disk
  - processor speed
- plus,
  - screen size
  - weight
  - ==> Notebook!
- A Notebook is a Computer. Notebook과 Computer는 IS-A 관계다.
  - Notebook(subclass), Computer(superclass)



### 상속과 생성자

- 생성자가 하나도 없을 경우 자동으로 no-parameter 생성자가 만들어진다. 생성자가 하나라도 있을 경우 자동으로 만들어지지 않는다.
- 모든 서브 클래스의 생성자는 먼저 수퍼 클래스의 생성자를 호출한다.
  - super(...)를 통해 명시적으로 호출해 주거나,
  - 그렇지 않을 경우에는 자동으로 no-parameter 생성자가 호출된다.
- 흔한 오류
  - 수퍼 클래스에 no-parameter 생성자가 없는데, 서브클래스의 생성자에서 super(...) 호출을 안해주는 경우



### Method Overriding

- 부모로부터 물려받은 메소드가 100% 만족스럽지 않을 때, 새롭게 수정해서 사용하는 것.



### 다형성(Polymorphism)

- Java의 객체 지향 프로그래밍에서 가장 중요한 개념.
- "수퍼클래스 타입의 변수가 서브클래스 타입의 객체를 참조할 수 있다."
  - `Computer theComputer = new Notebook("Bravo", "Intel", 4, 240, 2/4, 15.07.5);`
- static binding vs. dynamic binding
  - 다형성이 적용되었을 때, superclass와 subclass에 같은 이름의 메소드가 있으면 어떤 메소드가 실행될까?
    - static binding: 컴파일러가 참조 변수의 type을 기준으로 객체의 멤버를 판단해서 실행을 결정하는 방식. 즉, 다형성이 적용되었을 때 superclass의 메소드를 실행한다.
    - dynamic binding: 런타임에 참조 변수의 type이 아닌 실제 참조되고 있는 객체의 멤버를 판단해서 실행을 결정하는 방식. 즉, 다형성이 적용되었을 때 subclass의 메소드를 실행한다.
    - Java의 규칙은? 동적바인딩!





