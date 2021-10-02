from collections import deque


def solution(p):
    answer = translate(p)

    return answer


def translate(w):
    if w == '' or is_right(w):
        return w

    # 분리
    left = 0
    right = 0
    if w[0] == '(':
        left += 1
    else:
        right += 1

    for i in range(1, len(w)):
        if left == right:
            break

        if w[i] == '(':
            left += 1
        else:
            right += 1

    u = w[0:left+right]
    v = w[left+right:]

    if is_right(u):
        return u + translate(v)
    else:
        result = '(' + translate(v) + ')'
        uu = u[1:-1]
        for uuu in uu:
            if uuu == '(':
                result += ')'
            else:
                result += '('

        return result


def is_right(w):
    check_list = deque()

    for ww in w:
        if ww == ')':
            if not check_list:
                return False

            check_list.pop()
        else:
            check_list.append('(')

    return True


p = "()))((()"
print(solution(p))
