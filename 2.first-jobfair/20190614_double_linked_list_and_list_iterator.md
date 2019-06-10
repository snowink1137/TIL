# 이중연결리스트와 list iterator

## Java로 배우는 자료구조

### 이중연결리스트

- 단방향 연결 리스트의 한계
  - 단방향의 순회만이 가능
  - 어떤 노드 앞에 새로운 노드를 삽입하기 어려움
  - 삭제의 경우에 항상 삭제할 노드의 앞노드가 필요
- 이중 연결 리스트
  - 각각의 노드가 다음(next) 노드와 이전(previous) 노드의 주소를 가지는 연결 리스트
  - 양방향의 순회가 가능



### ListIterator 인터페이스

- Iterator의 한계
  - 단방향으로만 순회할 수 있다.
  - remove() 메서드는 지원하지만 add() 메서드를 지원하지 않는다.
  - 항상 리스트의 처음에서 시작한다.
- ListIterator는 Iterator를 확장한다.
- Iterator 처럼 ListIterator 역시 개념적으로 노드와 노드 사이를 가리킨다.
  - 따라서, ListIterator의 위치는 0에서 size까지의 인덱스로 표현한다.
  - 다만 양방향 연결 리스트이므로 이전에 어디서 왔는지가 중요하다. 그에 따라 next와 previous가 가리키는 것이 달라진다. history dependant.
- 