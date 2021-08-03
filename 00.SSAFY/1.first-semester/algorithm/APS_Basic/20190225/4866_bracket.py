import sys

sys.stdin = open('4866_sample_input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    string = input()
    stack = []

    for char in string:
        if char == '{' or char == '}' or char == '(' or char == ')':
            stack.append(char)

    length = len(stack)
    flag1 = False
    flag2 = False
    result = 1
    if length % 2 != 0:
        result = 0
    else:
        for bracket in range(length):
            if bracket == '{':
                flag1 = True
            elif bracket == '(':
                flag2 = True

            if bracket == '}' and flag1 == False:
                result = 0
                break
            elif bracket == ')' and flag2 == False:
                result = 0
                break

            if bracket == '}' and flag1:
                flag1 = False
            elif bracket == ')' and flag2:
                flag2 = False

    print(f'#{test_case} {result}')
