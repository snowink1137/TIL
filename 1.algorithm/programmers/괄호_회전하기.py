from collections import deque


def check(queue):
    new_queue = []
    check_dict = {
        ']': '[',
        ')': '(',
        '}': '{'
    }

    while queue:
        q = queue.popleft()
        if check_dict.get(q):
            if not new_queue:
                return 0

            if new_queue[-1] != check_dict[q]:
                return 0

            new_queue.pop()
        else:
            new_queue.append(q)

    if new_queue:
        return 0

    return 1


def solution(s):
    answer = 0
    string_queue = deque(s)

    check_queue = string_queue.copy()
    answer += check(check_queue)
    for _ in range(len(s)-1):
        string_queue.rotate()
        check_queue = string_queue.copy()
        answer += check(check_queue)

    return answer


s = "[](){}"
print(solution(s))
