# 1. 조합 재귀호출로 만들어 쓰기.
arr = 'ABCDE'
N = len(arr)
R = 3
pick = [0] * R

def comb(k, start):
    if k == R:
        print(arr[pick[0]], arr[pick[1]], arr[pick[2]])
        return

    # N은 k 써서 줄일 수 있다! 예를 들어 1~5인 5개의 수 중에서 3개를 뽑는 경우, 조합의 시작은 앞에서 3번째인 3까지 밖에 할 수가 없다. 뒤에서 선택할 수 있는 수를 남겨두어야 하기 때문이다. 마찬 가지로 조합 두번째 요소는 뒤에서 선택할 수 있는 수를 한 개는 남겨두어야 한다.
    for i in range(start, N):
        pick[k] = i
        comb(k+1, i+1)

comb(0, 0)
