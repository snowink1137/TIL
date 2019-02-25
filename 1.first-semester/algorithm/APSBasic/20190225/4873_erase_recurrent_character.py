import sys

sys.stdin = open('4873_sample_input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    string = input()
    stack = []
    for char in string:
        if len(stack) > 0 and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    print(f'#{test_case} {len(stack)}')
