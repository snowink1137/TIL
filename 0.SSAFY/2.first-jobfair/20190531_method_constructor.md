# 메서드와 생성자

## Java로 배우는 자료구조

- 클래스는 서로 관련있는 데이터들을 하나의 단위로 묶어두기 위한 것이다. 하지만 이것이 전부가 아니다.
  - 서로 관련있는 데이터들 뿐 아니라, 그 데이터와 관련이 깊은 메서드도 함께 묶어 둘 수 있다.
  - 이렇게 함으로써 코드의 응집도(cohesion)를 높이고 결합도(coupling)를 낮출 수 있다.
- 클래스는 설계도다. 쓰고 싶으면 객체를 만들어서 써야한다.
- 객체지향 프로그래밍에서 객체란 "데이터" + "메서드"이다. 데이터는 객체의 "정적 속성"을 표현하며, 메서드는 객체의 "기능(동적 속성)"을 표현한다.
- 클래스 안에 그 클래스와 동일한 이름을 가지며 return 타입이 없는 특별한 메서드를 둘 수 있다. 이것을 생성자(constructor)라고 부른다.
- 생성자는 new 명령으로 객체가 생성될 때 자동으로 실행된다. 주 목적은 객체의 데이터 필드의 값을 초기화하는 것이다.
- 객체지향 프로그래밍은 "Bottom-up 방식"이 많다.
  - 이 방식은 집을 짓는데 전체 설계부터 할 수도 있지만 일단 벽돌이 필요하니까 벽돌 만들어 놓고 생각하고 이런 방식을 말한다.
  - 물론 현실에서는 bottom-up top-down 다 섞어가며 프로그래밍한다.
- 