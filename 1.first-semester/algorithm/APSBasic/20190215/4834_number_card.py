import sys


sys.stdin = open('4834_sample_input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    size = input()
    num_list = []
    for num in input():
        num_list.append(num)

    count_dict = {}
    for num in num_list:
        if count_dict.get(num):
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    max_key = 0
    max_val = 0
    for k, v in count_dict.items():
        if v > max_val:
            max_key = k
            max_val = v
        elif v == max_val:
            if k > max_key:
                max_key = k

    print(f'#{test_case} {max_key} {max_val}')


# 선생님 코드 일부    
# N = int(input())
# cards = input()
# cnt = [0] * 10
# for ch in cards:
#     val = int(ch)
#     cnt[val] += 1
#     
# Max = 0
# for i in range(1, len(cnt)):
#     if cnt[Max] < ...
# 
