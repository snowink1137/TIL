# 예제(Scheduler Program)

## Java로 배우는 자료구조

### Scheduler Program

- 4 종류의 이벤트
  - 일회성 이벤트
    - 생일, 식사 약속, 회의 등
  - 기간이 지정된 이벤트
    - 시험 기간, 축제 기간
    - 시작일과 종료일이 있는 경우
  - 데드라인이 있는 이벤트
    - 시작일은 없고 데드라인이 있는 일
  - 주기적 이벤트
    - 수업시간(3월 초에서 6월 말까지 매주 월, 목 등)
- 이벤트라는 하나의 클래스를 만들고 각각의 이벤트가 이를 상속하면 다형성 개념을 이용해서 하나의 배열에 모든 이벤트를 모아 놓을 수 있다! 각 이벤트를 따로 만들면 type이 달라서 배열을 각각 많들어야 하니까..
  - 이와 같은 식의 프로그래밍이 C와 Java의 가장 큰 차이점. 객체 지향적인 프로그래밍이다.
- String 객체에는 split 메소드가 있다.
  - return 값으로 String 배열을 반환한다.
  - split 메소드의 parameter는 String type으로써, 정규표현식을 적어줘야한다. 따라서 . 을 기준으로 구분하고자 한다면? "\\\\." 이라고 적어줘야 한다. 정규표현식에서 . 이 정규표현식에서 special symbol 이기 때문이다.



### 배열 재할당(Array Reallocation)

```java
private void reallocate() {
    Event [] tmpArray = new Event [capacity*2];
    for (int i=0; i<n; i++) {
        tmpArray[i] = events[i];
    }
    
    events = tmpArray;
    capacity *= 2;
}
```

- 이렇게 재할당하고 참조 변수 events에 새로운 배열을 가리키게 한다면 기존에 events가 가리키던 객체는 어떻게 되는가?
  - 이 객체는 garbage라고 불리고, Java 런타임이 자동으로 garbage collection을 시행한다.
  - C나 C++ 프로그래밍에서는 이를 직접 처리해줘야 함.





