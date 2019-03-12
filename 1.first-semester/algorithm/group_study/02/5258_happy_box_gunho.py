
memorize = {}

def happybox(a,b):
    if b == 0 and a < arr[b][0]:
        memorize[(a,b)] = 0
        return 0
    if b == 0 and a >= arr[b][0]:
        memorize[(a,b)] = arr[b][1]
        return arr[b][1]

    if (a,b) in memorize:
        return memorize[(a,b)]
    else:
        if a-arr[b][0] >= 0:
            result = max(happybox(a,b-1), arr[b][1] + happybox(a-arr[b][0],b-1))
        else:
            result = happybox(a,b-1)
        memorize[(a,b)] = result
        return result

T = 1
for _ in range(T):
    N, M =12, 5
    arr = [[7, 20],[3,10],[5,3],[3,8],[6,15]]
    # print('#{} {}'.format(_+1,result))
    happybox(N,M-1)
    result = memorize[N,M-1]
    print('#{} {}'.format(_+1,result))