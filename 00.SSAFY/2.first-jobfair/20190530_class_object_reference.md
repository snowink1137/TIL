# 클래스, 객체, 참조 변수

## Java로 배우는 자료구조(Chapter02.Code01~)

- 클래스
  - 같이 붙어다녀야 하는 데이터를 서로 별개의 변수에 저장하면 이름 데이터를 옮길 때마다 관련 있는 데이터도 따로 옮겨줘야한다.
  - 따라서, 서로 관련있는 데이터들을 하나의 단위로 묶어두면 편할 것이다. 이것이 클래스라는 개념이 등장하는 가장 기본적인 이유이다.
  - 클래스는 결국 하나의 "타입"이다. 마치 int, double 처럼.
  - 다만 Java가 미리 정해놓은 타입이 아니라서 "사용자 정의 타입"이라고 부르기도 한다.

- primitive 타입과 class 차이점
  - primitive 타입은 변수 "안"에 값을 저장한다.
  - 하지만 class는 변수 "안"에 값을 저장하는 것이 아니라, 값은 다른 객체에 따로 저장하고 변수에는 그 객체의 주소(참조)를 저장하는 것이다.

- "primitive 타입이 아닌 모든 변수는 참조 변수이다."

  - 따라서 `int [] members = new int [8]` 로 생성되는 members도 참조 변수이다! 물론 배열의 각 칸은 int 타입의 primitive 변수이다.

  - `Person1 [] members = new Person1 [100];` 에서 배열의 각 칸은 Person1 타입의 참조 변수이다.

    - 따라서 배열의 칸을 그냥 쓸 수 없다. `new` 명령어로 객체를 생성한 후에 그 주소를 배열의 칸에 저장하는 식으로 써야한다.

    - ```java
      members[2] = new Person1();
      members[2].name = "David";
      members[2].number = "2983582395";
      ```

- C에서는 primitive 타입과 사용자 정의 타입 둘 모두에서 보통 변수(직접 변수에 값을 넣을 수 있는 변수)와 참조 변수(포인터)를 사용할 수 있지만, Java에서는 안된다. primitive 타입에서는 보통변수 밖에 못쓰고, 사용자 정의 타입에서는 참조 변수 밖에 못씀!

- 



