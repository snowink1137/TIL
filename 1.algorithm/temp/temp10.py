root


def solution(input: list):
    answer = []
    temp = 0
    input.sort(key=lambda x: x[0])

    start = input[0][0]
    for i in range(len(input)-1):
        if input[i][1] >= input[i+1][0]:
            continue
        else:
            answer.append((start, input[i][1]))
            start = input[i+1][0]

    return answer

temp = input[:]
input = list()
input


input = [(1, 3), (5, 8), (4, 10), (20, 25)]
print(solution(input))
