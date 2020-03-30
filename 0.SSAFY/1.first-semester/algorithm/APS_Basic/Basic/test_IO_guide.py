import sys
# 운영체제에게 사용할 파일에 접근해서 사용할 허가를 얻는 코드
# 인풋을 키보드로 받는 게 아니라 파일로 받아들이겠다는 코드
sys.stdin = open('input.txt', 'r')

# T = int(input())
T = 10
arr = []
for test_case in range(T):
    N = int(input())

    arr.append(list(map(int, input().split())))

print(arr)
