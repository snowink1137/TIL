import sys

sys.stdin = open('5648_sample_input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    result = 0
    atom_list = [None for _ in range(N)]

    for i in range(N):
        atom_list[i] = list(map(int, input().split()))

    for i in range(N):
        atom_list[i][0] *= 2
        atom_list[i][1] *= 2

    for step in range(4002):
        atom_map = {}
        for i in range(N):
            if atom_list[i]:
                if atom_list[i][2] == 0:
                    atom_list[i][1] += 1
                elif atom_list[i][2] == 1:
                    atom_list[i][1] -= 1
                elif atom_list[i][2] == 2:
                    atom_list[i][0] -= 1
                elif atom_list[i][2] == 3:
                    atom_list[i][0] += 1

                if atom_map.get((atom_list[i][0], atom_list[i][1])):
                    atom_map[(atom_list[i][0], atom_list[i][1])].append(i)
                else:
                    atom_map[(atom_list[i][0], atom_list[i][1])] = [i]

        for check_list in atom_map.values():
            if len(check_list) >= 2:
                for atom_idx in check_list:
                    result += atom_list[atom_idx][3]
                    atom_list[atom_idx] = None

    print('#{} {}'.format(test_case, result))

# 테스트 케이스 답
# #1 24
# #2 0
# #3 6
# #4 10
