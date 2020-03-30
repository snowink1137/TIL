# 20190116 Bootstrap / Grid System

## 수업

### python

- scope 이슈

  - LEGB rule

    - Local scope(정의된 함수) -> Enclosed scope(상위 함수) -> Global scope(함수 밖의 변수 혹은 import된 모듈) -> Built-in scope(파이썬 안에 내장되어 있는 함수 또는 속성)

  - ```python
    class Person:
        population = 0              # 클래스 변수 : 모든 인스턴스가 공유함.
        def __init__(self, name):   
            self.name = name
            population += 1
    
    ```

  - 여기 5번 줄에서 population이 함수 내부에서 정의되지 않았으므로 LEGB rule에 따라 population을 찾아 나서게 된다. 그래서 class 변수를 찾게 된다. 그러나.. 에러가 난다.

  - ```python
    ---------------------------------------------------------------------------
    UnboundLocalError                         Traceback (most recent call last)
    <ipython-input-9-8ccac2eac977> in <module>
          1 # 본인의 이름을 가진 인스턴스를 만들어봅시다.
    ----> 2 jy = Person('jy')
    
    <ipython-input-8-48f0ab03a895> in __init__(self, name)
          4     def __init__(self, name):
          5         self.name = name
    ----> 6         population += 1
          7 
    
    UnboundLocalError: local variable 'population' referenced before assignment
    ```

  - 이런 식으로 참조는 scope rule에 따라 참조는 되는데 그걸 수정하지는 못한다. Person.population 이런식으로 지정해서 이걸 해결할 수는 있지만 그렇게 하는 것은 좋지 않음. CSS에서 important같은 느낌이라서. 역할에 맞게 쓰는 게 안꼬이고 좋다.

- class, 자료 구조 등에 접근제어자를 사용하는 이유

  - class 안에서만 혹은 클래스를 통해서만 사용하고 싶었는데, 함수 안에서나 클래스 안에서도 결국 자료구조를 가리키는(참조하는) 형식으로 이루어져 있기 때문에 자료구조가 꼬이는 결과가 나오는 경우가 있다. 그래서 접근을 미리 접근을 통제하는 것이다.
  - 파이썬에서는 naming으로 접근제어를 한다.
    - public : 아무 밑줄 없이 하면 됨. ex) num
    - private : 두 개의 밑줄이 접두사여야 함. ex) __num
    - protected : 한 개의 밑줄이 접두사여야 함. ex) _num
  - protected : 상속 받은 클래스에서 접근 가능
  - private : 자기 클래스에서만 접근 가능(정보 은닉)

- instance method, static method, class method

  - class method는 @classmethod, static method는 @staticmethod, instance method는 데코레이터 없이 쓰면된다.
  - instance method & class method
    - instance method는 self라는 인자를, class method는 cls라는 인자를 반드시 넘겨야 한다.
      - 따라서 얘네 둘은 instance, class가 각각 혼자 쓸 method인 경우 만들면 좋다.
  - static method
    - static method는 반드시 넘겨야 하는 인자가 없다
      - 따라서 얘는 instance, class 둘 모두 쓸 method인 경우 만들면 된다.
      - 따라서 static method에는 인자를 기본으로 넘겨야 하는 instance method나 class method와는 다른 역할을 하는 (예를 들면 단순 조회 같은) 기능을 구현하면 된다.
  - 근데 어떻게든 instance가 class method를 사용할 수 있고, 반대의 경우도 가능하다. 하지만 그렇게는 사용하지 않는 것이 좋다. 권장되는 방법 및 설계가 아니다.
  - 데코레이터 써놓는 이유는 명시적인 기능이 강하기 때문이다. 물론 다른 기능도 들어있지만. OOP하는 이유와 비슷한 것으로 이해함.
    - 왜 귀찮게 데코레이터 써가면서 method를 만드는 단계에서부터 명시해서 static, class, instance method를 나눠놔야 하나... 했는데 클래스를 만들다보니 이해됨.
    - java에서는 parameter로 this를 명시하지 않았기 때문에 헷갈렸음. 왜 굳이 데코레이터를 써야하나 생각했었는데, 파이썬에서는 instance method 만들기 위해서는 parameter로 self를 꼭 쓰도록 설계되어 있으니까(인스턴스는 기본 parameter로 self를 넘기고, 클래스는 기본 parameter로 cls를 넘기기 때문에) 반드시 method를 만들때부터 데코레이터로 정의해줘야 parameter 오류가 안생긴다.
  - instance는 그냥 class method 가져다 써도 문제 없는 것으로 보아서, instance는 instance method 쓸 때 self를 자동으로 넘기는 것처럼 class method를 쓸 때는 cls를 자동으로 넘기는 것으로 보인다. instance를 만드는 설계도가 class 인 것을 생각해보면 아주 어색한 것은 아닌 것 같다.

- 함수 호출방식(call-by-value, call-by-reference, call-by-assignment)

  - call-by-value (값에 의한 호출)
    - call-by-value 값에 의한 호출방식은 함수 호출시 전달되는 변수의 값을 복사하여 함수의 인자로 전달한다.
    - 복사된 인자는 함수 안에서 지역적으로 사용되는 local value의 특성을 가진다.
    - 따라서 함수 안에서 인자의 값이 변경되어도, 외부의 변수의 값은 변경되지 않는다.
    - Java의 경우 함수에 전달되는 인자의 데이터 타입에 따라서 (원시자료형 / 참조자료형) 함수 호출 방식이 달라진다.
      - 원시 자료형 (primitive type) : call-by-value 로 동작 (int, short, long, float, double, char, boolean )
      - 참조 자료형 (reference type): call-by-reference 로 동작 (Array, Class Instance)
  - call-by-reference (참조에 의한 호출)
    - call-by-reference 참조에 의한 호출방식은 함수 호출시 인자로 전달되는 변수의 레퍼런스를 전달한다. (해당 변수를 가르킨다.)
    - 따라서 함수 안에서 인자의 값이 변경되면, 아규먼트로 전달된 객체의 값도 함께 변경된다.
  - call-by-assignment
    - 파이썬의 함수 호출 방식.
    - 파이썬에서는 모든 것이 객체이고, 객체에는 2가지 종류가 있다.
    - immutable object
      - int, float, str, tuple
      - immutable 객체가 함수의 arguments로 전달되면 처음에는 call by reference로 받지만, 값이 변경되면 call by value로 동작한다. 
        즉 함수 내에서 formal parameter 값이 바뀌어도, actual parameter에는 영향이 없다.
    - mutable object
      - list, dict, set
      - mutable 객체가 함수의 argument로 넘어가면 call by reference로 동작한다. 즉, object reference가 전달되어 actual parameter의 값에 영향을 미칠 수 있다.
  - [출처] https://wayhome25.github.io/cs/2017/04/11/cs-13/

- 모두 대문자로 쓴 변수는 상수로 쓰자는 컨벤션이다.

- \_\_repr\_\_, \_\_str\_\_

  -   repr() 은 \_\_repr\_\_ 메소드를 호출하고, str() 이나 print 는 \_\_str\_\_ 메소드를 호출하도록 되어있는데, \_\_str\_\_ 은 객체의 비공식적인(informal) 문자열을 출력할 때 사용하고, \_\_repr\_\_ 은 공식적인(official) 문자열을 출력할 때 사용한다.

  - \_\_str\_\_ 은 사용자가 보기 쉬운 형태로 보여줄 때 사용하는 것이고, \_\_repr\_\_ 은 시스템(python interpreter)이 해당 객체를 인식할 수 있는 공식적인 문자열로 나타내 줄 때 사용하는 것이다.

  - 따라서 eval(repr(object)) 를 실행하면 해당 object 를 얻어올 수 있다.

  - eval(expression)은 실행 가능한 문자열(1+2, 'hi' + 'a' 같은 것)을 입력으로 받아 문자열을 실행한 결과값을 리턴하는 함수이다.

  - > 즉 위의 실수 변수인 f 를 예로 들면, 실수변수의 경우 유효값이 소수점 17자리이기 때문에 repr 로 출력할 경우 해당 실수객체를 완전하게 표현할 수 있는 값을 출력해주고 있고, str 의 경우는 사용자가 보기 편한 수준에서 보여주는 정도만 구현되어있다. 
    >
    > eval(repr(f)) 를 하는 경우 리턴값은 f 를 나타내는 스트링을 표현한 식을 다시 객체로 만들어준다. 아래 결과를 보면, eval 은 repr 을 사용하여 문자열로 변경된 객체를 새로 생성해준다는 것을 알 수 있다. 즉 f 와 g 의 값은 같으나, f와 g 가 가리키는 객체는 다르게 된다.
    >
    > ```bash
    > >>> f = 1.12345678901234567
    > >>> id(f)
    > 36252424
    > >>> g = eval(repr(f))
    > >>> id(g)
    > 46032032
    > >>> f is g
    > False
    > >>> f == g
    > True
    > ```

  - [출처] http://pinocc.tistory.com/168

  - [출처] https://wikidocs.net/32#eval

- 클로저 개념 찾아보기

  - http://schoolofweb.net/blog/posts/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%81%B4%EB%A1%9C%EC%A0%80-closure/

- freecodecamp



### 기타

- 프로그램 설치는 느리고 삭제는 빠른 이유?
  - 설치는 디스크에 기록 + 프로그램이 어디부터 어디까지 인지 가리키는 정보 기록 해야함.
  - 삭제는 가리키는 정보만 없애면 되기 때문에 빠른 것임.
  - 실제 데이터는 나중에 그 부분에 뭔가 데이터를 기록하면 정말 지워지는 것임.

- [참고] 요즘 언어들은 가리키는 정보를 지우면 가비지 컬렉터가 알아서 참조했던 데이터도 메모리에서 지워줌. 근데 C 같은 언어들은 참조를 없애고 데이터도 메모리에서 직접 없애줘야 함.

- 수업 교재 08_module.ipynb 의 마지막 부분 timedelta 부분 잊어버릴 것 같은 것들.

  - timedelta 인스턴스 변수에 days, seconds, microseconds 밖에 없어서 hours, minutes, seconds 같은 것은 다 계산해줘야함..

  - ```python
    days = td.days
    hours, remainder = divmod(td.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    # If you want to take into account fractions of a second
    seconds += td.microseconds / 1e6
    ```

  - [출처] https://stackoverflow.com/questions/2119472/convert-a-timedelta-to-days-hours-and-minutes





## 수업 이외

- jupyter notebook에서 class 선언하고 코드 실행한 이후에 커널 재시작 안한 상태로 class 재선언 및 코드 재실행하면 결과 꼬이는 이유가 뭘까?
  - \_\_del\_\_ 작동때문에 그렇다.
  - class 만들고 첫 코드 실행 때는 당연히 \_\_del\_\_ 실행될 일 없지만.. class 갈아 엎으면 첫 코드 실행 때부터 \_\_del\_\_ 실행되므로 꼬인다.

- 파이썬에서 locale 문제 없도록 설정하는 코드

  - ```python
    import locale
    locale.setlocale(locale.LC_ALL, '')
    ```

  - 1번째 인자는 모든 locale을 선택하는 변수인 것 같고 2번째 인자는 원래 명시적인 locale 입력해도 되는데 저렇게 쓰면 시스템의 locale로 설정해준다고 한다.