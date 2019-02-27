import sys

sys.stdin = open('1224_input.txt', 'r')

for test_case in range(1, 11):
    N = int(input())

    stack = []
    result = []
    string = input()
    for i in range(N):
        if len(stack) > 0:
            if string[i] == '(':
                stack.append(string[i])
            elif string[i] == '*' and (stack[-1] == '+' or stack[-1] == '('):
                stack.append(string[i])
            elif string[i] == '+' and stack[-1] == '(':
                stack.append((string[i]))
            elif string[i] == ')':
                for j in range(len(stack)):
                    if stack[-1] == '(':
                        stack.pop()
                        break
                    else:
                        result.append(stack.pop())
            elif string[i] == '*':
                result.append(stack.pop())
                stack.append(string[i])
            elif string[i] == '+':
                result.append(stack.pop())
                stack.append(string[i])
            else:
                result.append(int(string[i]))
        else:
            if string[i] == '(' or string[i] == '*' or string[i] == '+':
                stack.append(string[i])
            else:
                result.append(int(string[i]))

    stack = []
    output = 0
    for _ in range(len(result)):
        if result[_] == '+':
            if len(stack) < 2:
                print(f'#{test_case} error')
                break
            else:
                a = stack.pop()
                b = stack.pop()
                output = b + a
                stack.append(output)
        elif result[_] == '*':
            if len(stack) < 2:
                print(f'#{test_case} error')
                break
            else:
                a = stack.pop()
                b = stack.pop()
                output = b * a
                stack.append(output)
        else:
            stack.append(int(result[_]))

    print(f'#{test_case} {stack.pop()}')



