# # %, / 이용해서 각 자리값을 뽑을 수 있다.
# num = 12345
# A = []
# A.append(num % 10)
# num = num // 10
# A.append(num % 10)
# num = num // 10
# A.append(num % 10)
# num = num // 10
# A.append(num % 10)
# num = num // 10
# A.append(num % 10)
# print(A)

# # 패턴 매칭
# p = "CATTCCCTGCGCCGC"
# t = "ATTTGTGCATGTTTGAGCTTTTACGTACGAGAAACTGAACGTACCTACGACATTCCCTGCGCCGCCACCCGCTTTTTGAA"
# n, m = len(t), len(p)
#
# for i in range(n - m + 1):
#     j = 0
#     while j < m:
#         if t[i + j] != p[j]:
#             break
#         j += 1
#     if j == m:
#         print(t[i:i+m])
#         print(i)
#         break
#

# KMP 패턴 매칭
p = 'abcdabcef'                                                                       # pattern
t = 'alksdabcdabcflaskjflkabcdjsaflkjasdkdsajfabcdabceflksadjabcdaksfjffsdaf'      # text

m, n = len(p), len(t)
next = [0] * (m + 1)

# 전처리
next[0] = -1
i, j = 0, -1
while i < m:
    while j >= 0 and p[j] != p[i]:
        j = next[j]

    i, j = i + 1, j + 1
    next[i] = j

print(next)

# 매칭
i = j = 0
while i < n:
    while j >= 0 and p[j] != t[i]:
        j = next[j]

    i, j = i + 1, j + 1

    if j == m:
        print(t[i - j:])
        break

