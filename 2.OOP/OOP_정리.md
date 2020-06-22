# OOP(Object Oriented Programming) 정리 with Python

- codeit 객체 지향 프로그래밍 강의 정리 문서



## 1. 객체 지향 프로그래밍이란?

- 객체
  - 속성 & 행동으로 이루어진 존재
  - 우리가 살아가면서 보는 모든 존재를 객체라고 생각하면 됨
    - 현실에 존재하든, 가상으로 존재하든 속성 & 행동을 떠올릴 수 있다면 모든 것이 객체임
  - ex)
    - 자동차
      - 속성
        - 의자 갯수
        - 색깔
        - 높이
      - 행동
        - 시동
        - 전진
    - 인스타그램 유저
      - 속성
        - 이메일 주소
        - 비밀번호
        - 친구 목록
      - 행동
        - 좋아요
        - 친구 추가
  
- 객체 지향 프로그래밍
  - 프로그램을 여러 개의 독립된 객체들과 그 객체들 간의 상호 작용으로 파악하는 프로그래밍 접근법
    - 프로그램을 객체들과 객체들 간의 소통으로 바라보는 것
  - 모델링 방법
    1. 프로그램에 어떤 객체들이 필요할지 정한다
    2. 객체들의 속성(변수)과 행동(메소드)을 정한다
    3. 객체들이 서로 어떻게 소통할지 정한다
  - 절차 지향 프로그래밍과의 차이
    - 객체 지향 프로그래밍에서는 객체가 행동의 주체인데, 절차 지향 프로그래밍에서는 데이터만 있는 객체는 함수가 주도적으로 사용하는 대상일 뿐이다
      - C 언어에서는 데이터를 보통 구조체(struct)라는 단위로 묶어 놓는다. 그리고 함수를 정의해서 함수가 구조체를 사용하는 방식의 형태로 프로그래밍 한다
      - C 언어에서도 구조체에 함수를 정의해서 클래스처럼 사용할 수 있지만, 굳이 절차 지향 프로그래밍 언어를 객체 지향식으로 사용하는 것으로 볼 수 있어서 권장되지는 않는다
    - 객체 지향 프로그래밍이라고 해서 어떤 순차나 절차가 없다는 뜻은 아니다. 두 프로그래밍 방법의 차이는 데이터와 함수를 하나로 묶은 객체라는 존재가 행동의 주체가 되느냐, 함수가 주체가 되어 데이터를 다루느냐에 있다
  
- 클래스 vs 객체 vs 인스턴스
  - 클래스: 설계도
  - 객체: 클래스로 구현할 어떤 것
  - 인스턴스: 객체를 객체의 생성자를 통해 실체화 시킨 것. 실제로 메모리에 올려진 객체
  
- 인스턴스 메소드

  - 메소드를 사용할 때 첫 번째 인자로 해당 인스턴스를 받는다

  - ex)

    - ```python
      class User:
          def follow(self, another_user):
              pass
              return
      ```

- 특수 메소드(던더 메소드 ⇔ 더블 언더바 메소드)
  - 특정 상황에서 자동으로 호출되는 메소드. 앞 뒤로 언더바를 두 개씩 넣는 방식으로 표현된다
  - ex)
    - `__init__` 메소드
      - 인스턴스를 생성할 때 자동으로 실행되는 메소드
    - `__str__` 메소드
      - 인스턴스를 print로 출력할 때 실행되어 원하는 문자열을 반환하여 출력되도록 하는 메소드
- 인스턴스 변수를 만드려면 class 안에 `self.변수명`을 쓰면 되고, 클래스 변수를 만드려면 self 없이 그냥 변수명을 쓰면 된다

- 같은 이름의 클래스 변수 vs 같은 이름의 인스턴스 변수

  - 같은 이름의 인스턴스 변수에 우선권이 있다
  - 예를 들어 `count` 라는 클래스 변수가 존재할 때, `인스턴스.count = 123`이라 입력하면 클래스 변수가 수정되는 것이 아니라 `count`라는 같은 이름의 인스턴스 변수가 생성되는 것이다
  - 따라서 인스턴스 변수와 클래스 변수가 헷갈리게 이름 짓지 않는 것이 좋다

- 데코레이터(decorator)

  - 함수를 꾸며서 새로운 함수를 만들어 주는 역할. 데코레이터가 함수라면? 데코레이터 함수

  - ex)

    - ```python
      # 데코레이터 ex1
      def print_hello():
          print("안녕하세요!")
      
      
      # 데코레이터 함수
      # original이라는 함수를 꾸며서 wrapper라는 새로운 함수를 만들어 내는 함수
      def add_print_to(original):  # parameter로 함수를 받음
          def wrapper():
              print("함수시작")
              original()
              print("함수 끝")
          return wrapper
      
      
      print_hello = add_print_to(print_hello)
      print_hello()
      ```

    - ```python
      # 데코레이터 ex2 ⇔ 데코레이터 ex1
      def add_print_to(original):
          def wrapper():
              print("함수시작")
              original()
              print("함수 끝")
          return wrapper
      
      
      @add_print_to  # ex1의 print_hello = add_print_to(print_hello) 이 과정을 @데코레이터함수 방식으로 자동화할 수 있음
      def print_hello():
          print("안녕하세요!")
      
          
      print_hello()
      ```

- 클래스 메소드

  - `@classmethod`라는 데코레이터로 클래스 메소드를 만들 수 있다
  - 클래스 메소드는 첫 번째 인자로 클래스를 받는다
    - 이 때 첫 번째 인자를 `cls`로 쓰는 것이 관습
    - cf) 인스턴스 메소드는 `self`로 인스턴스를 첫 번째 인자로 받음

- 인스턴스 메소드 vs 클래스 메소드

  - ```python
    # 인스턴스 메소드(ex: say_hello) 사용
    User.say_hello(user1)
    user1.say_hello()  # 이 경우에만 say_hello 함수에 user1이 첫 번째 파라미터로 전달 됨
    
    # 클래스 메소드(ex: number_of_users) 사용
    User.number_of_users()  # 이 경우에 number_of_users 함수에 User 클래스가 첫 번째 파라미터로 전달 됨
    user1.number_of_users()  # 이 경우에도 number_of_users 함수에 User 클래스가 첫 번째 파라미터로 전달 됨
    ```

  - 인스턴스 변수만 사용할 때: 인스턴스 메소드 사용

  - 클래스 변수만 사용할 때 or 인스턴스 없이도 필요한 정보가 있을 때: 클래스 메소드 사용

  - 인스턴스 변수와 클래스 변수 둘 다 사용할 때: 인스턴스 메소드 사용(∵ 클래스 메소드에서는 인스턴스 인자를 받을 수 없다)

- 정적 메소드(static method)

  - `@staticmethod` 데코레이터를 사용해서 만든다

  - `self`, `cls` 처럼 자동으로 넘어가는 인자가 없다

  - 정적 메소드는 인스턴스, 클래스 두 가지 모두를 통해 사용 가능하다

    - ```python
      # ex)
      class User:
          ...
          @staticmethod
          def is_valid_email(email_address):
              return "@" in email_address
          
      
      print(User.is_valid_email("taehosung"))
      print(User.is_valid_email("taehosung@codeit.kr"))
          
      print(user1.is_valid_email("taehosung"))
      print(user1.is_valid_email("taehosung@codeit.kr"))
      ```

  - 인스턴스 변수나 클래스 변수와 같은 어떤 속성을 다루지 않고, 단기 기능(행동)적인 역할만 하는 메소드를 정의할 때 정적 메소드를 사용한다

- 파이썬은 순수 객체 지향 언어이다

  - 파이썬에서는 모든 것이 객체다

    - ```python
      # ex)
      print(type(2))  # 정수. <class 'int'> 로 만들어진 객체
      print(type('string'))  # 문자열. <class 'str'> 로 만들어진 객체
      print(type([]))  # 리스트. <class 'list'> 로 만들어진 객체
      print(type({}))  # 딕셔너리. <class 'dict'> 로 만들어진 객체
      print(type(()))  # 튜플. <class 'tuple'> 로 만들어진 객체
      print(type(print))  # 함수. <class 'builtin_function_or_method'> 로 만들어진 객체
      
      # 위의 클래스들은 파이썬 개발자들이 미리 만들어 놓은 class
      ```

  - 다른 언어에는 type이 객체가 아닌 것들도 있다. JAVA와 같은 경우 객체 지향 언어이기는 하지만 순수 객체 지향 언어는 아니다

- 가변 타입 객체 vs 불변 타입 객체

  - 한번 생성한 인스턴스의 속성 변경 가능(ex: list, dict, 직접 작성하는 클래스)
  - 한번 생성한 인스턴스의 속성 변경 불가(ex: bool, int, float, str, tuple)

- 절차 지향 프로그래밍 vs 객체 지향 프로그래밍

  - 절차 지향 프로그래밍은 프로그램에 필요한 동작들 만을, 함수라는 단위로 묶어서 사용한다. 객체 지향 프로그래밍은 프로그램에 필요한 동작과 관련된 데이터도 클래스라는 단위로 함께 묶어서 관리한다

  - ```python
    # 절차 지향 프로그래밍 예시
    # 반복적으로 사용하는 코드를 함수로 정의한다
    def print_person_info(person_name, person_age, person_gender):
        # 사람의 이름, 나이, 성별을 파라미터로 받으면 받은 정보를 이해할 수 있는 문자열로 출력해주는 함수
        print("사람 한 명을 소개합니다")
        print("{}님은 {}살이고 {}입니다".format(person_name, person_age, person_gender))
        
    def is_underage(person_age):
        # 사람의 나이를 파라미터로 받아서 미성년자인지를 리턴해주는 함수
        return person_age < 20
        
    # 영훈이의 정보
    young_name = "영훈"
    young_age = 10
    young_gender = "남자"
        
    # 윤수의 정보
    yoonsoo_name = "윤수"
    yoonsoo_age = 20
    yoonsoo_gender = "남자"
        
    # 영훈/윤수 정보 출력
    print_person_info(young_name, young_age, young_gender)
    print_person_info(yoonsoo_name, yoonsoo_age, yoonsoo_gender)
        
    # 영훈/윤수가 미성년자인지 출력
    print(is_underage(young_age))
    print(is_underage(yoonsoo_age))
    
    
    # 객체 지향 프로그래밍 예시
    # 속성과 행동을 갖는 객체들이 행동을 하는 방식으로 작성한다
    class Person:
        # 사람을 나타내는 클래스
        def __init__(self, name, age, gender):
            # 사람은 이름, 나이, 성별을 속성으로 갖는다
            self.name = name
            self.age = age
            self.gender = gender
        
        def print_info(self):
            # 자신의 정보를 출력하는 메소드
            print("사람 한 명을 소개합니다")
            print("{}님은 {}살이고 {}입니다".format(self.name, self.age, self.gender))
        
        def is_underage(self):
            # 사람의 나이를 파라미터로 받아서 미성년자인지를 리턴해주는 메소드
            return self.age < 20
        
    # 영훈/윤수을 나타내는 객체 생성
    young = Person("영훈", 10, "남자")
    yoonsoo = Person("윤수", 20, "남자")
        
    # 영훈/윤수 정보 출력
    young.print_info()
    yoonsoo.print_info()
        
    # 영훈/윤수가 미성년자인지 출력
    print(young.is_underage())
    print(yoonsoo.is_underage())
    ```

  - 객체 지향 프로그래밍이라고 해서 순서가 없는 것은 아니다. 절차 지향 프로그래밍은 프로그램을 명령어를 순서대로 실행하는 것으로 이해하는 것이고, 객체 지향 프로그래밍은 프로그램을 객체들이 순서대로 소통하는 것으로 이해하는 것이다

  - 어떤 방식이 더 낫다고 할 수는 없지만, 복잡한 프로그램은 객체 지향적으로 하는 것이 나은 경우가 많다

- 모듈(module)

  - 변수, 함수, 클래스 등을 모아놓은 파일

  - 모듈을 만들어 두면 다른 곳에서 가져다 쓸 수 있다

    - `from 모듈의 이름 import 불러올 변수/함수/클래스 이름`

  - ```python
    # ex)
    # calculator.py
    # calculator 모듈
        
    
    # 합
    def sum(x, y):
        return x + y
    ```

    - ```python
      # test.py
      
      # calculator.py에서 sum 함수 불러오기
      from calculator import sum
          
      print(sum(3, 5))
      ```



## 2.

