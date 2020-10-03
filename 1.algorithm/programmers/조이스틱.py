def solution(name):
    answer = 0
    name_ord_list = list(map(lambda x: abs(ord(x)-ord('A')) if abs(ord(x)-ord('A')) < 13 else 26-abs(ord(x)-ord('A')), name))

    index = 0
    while True:
        right = 1
        left = 1

        if not sum(name_ord_list):
            break

        if name_ord_list[index]:
            answer += name_ord_list[index]
            name_ord_list[index] = 0

        for i in range(1, len(name)):
            if name_ord_list[(index+i)%len(name)]:
                break
            else:
                right += 1

        for i in range(1, len(name)):
            if name_ord_list[index-i]:
                break
            else:
                left += 1

        if right > left:
            answer += left
            index -= left
        else:
            answer += right
            index = (index + right) % len(name)

    return answer


name = 'BBBBAAAAB'
print(solution(name))
