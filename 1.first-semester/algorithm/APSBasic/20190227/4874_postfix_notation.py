import sys

sys.stdin = open('4874_sample_input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    information = input().split()

    if len(information) == 0:
        print(f'#{test_case} error')
        continue

    stack = []
    result = 0
    for _ in range(len(information)):
        if information[_] == '.':
            if len(stack) == 1:
                print(f'#{test_case} {stack.pop()}')
                break
            else:
                print(f'#{test_case} error')
                break
        elif information[_] == '+':
            if len(stack) < 2:
                print(f'#{test_case} error')
                break
            else:
                a = stack.pop()
                b = stack.pop()
                result = b + a
                stack.append(result)
        elif information[_] == '-':
            if len(stack) < 2:
                print(f'#{test_case} error')
                break
            else:
                a = stack.pop()
                b = stack.pop()
                result = b - a
                stack.append(result)
        elif information[_] == '*':
            if len(stack) < 2:
                print(f'#{test_case} error')
                break
            else:
                a = stack.pop()
                b = stack.pop()
                result = b * a
                stack.append(result)
        elif information[_] == '/':
            if len(stack) < 2:
                print(f'#{test_case} error')
                break
            else:
                a = stack.pop()
                b = stack.pop()
                result = b // a
                stack.append(result)
        else:
            stack.append(int(information[_]))
    else:
        print(f'#{test_case} error')
