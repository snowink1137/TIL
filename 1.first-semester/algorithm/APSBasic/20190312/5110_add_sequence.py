import sys

sys.stdin = open('5110.txt', 'r')


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert_first(self, val):
        node = Node(val)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node

        self.size += 1

    def insert_last(self, val):
        node = Node(val)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            cur = self.tail
            cur.next = node
            self.tail = node

        self.size += 1

    def insert_at(self, idx, val):
        if self.head is None:
            self.insert_first(val)
        elif idx >= self.size:
            self.insert_last(val)
        else:
            prev, cur = None, self.head
            for i in range(idx):
                prev = cur
                cur = cur.next

            if prev is None:
                self.insert_first(val)
            else:
                node = Node(val)
                node.next = prev.next
                prev.next = node

                self.size += 1




T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())

    sequence = List()
    temp = list(map(int, input().split()))
    for i in range(N):
        sequence.insert_last(temp[i])

    for _ in range(M-1):
        check = -1
        temp = list(map(int, input().split()))
        cur = sequence.head
        for i in range(sequence.size):
            if cur.data > temp[0]:
                check = i
                break
            cur = cur.next

        if check == -1:
            for i in range(N):
                sequence.insert_last(temp[i])
        else:
            for i in range(N-1, -1, -1):
                sequence.insert_at(check, temp[i])

    result = []
    cur = sequence.head
    for i in range(sequence.size-1, -1, -1):
        if i >= 10:
            cur = cur.next
            continue
        else:
            result.append(str(cur.data))
            cur = cur.next

    print('#{} {}'.format(test_case, ' '.join(reversed(result))))
