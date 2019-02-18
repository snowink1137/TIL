# # 홀짝 구분
# n = 20
# if n % 2 == 0:
#     print('짝수')
# else:
#     print('홀수')
#
# n = 11
# if n & 1 == 0:
#     print('짝수')
# else:
#     print('홀수')
#
#
# # 비트연산자를 활용하여 조합 만들기
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# N = len(arr)
# for i in range(1 << N): # 0~1023
#     # 2^0 ~ 2^10에 해당하는 비트 값을 확인
#     sum_combination = 0
#     for j in range(N-1, -1, -1):
#         if i & (1 << j) != 0:
#             sum_combination += arr[N-1-j]
#
#     if sum_combination == 10:
#         for j in range(N-1, -1, -1):
#             if i & (1 << j) != 0:
#                 print(arr[N-1-j], end=', ')
#
#         print()


# # 이진 탐색
# def binary_search(arr, key):
#     start, end = 0, len(arr) - 1
#     while start <= end:
#         mid = (start + end) >> 1
#         if arr[mid] == key:
#             return mid
#         elif arr[mid] > key:
#             end = mid - 1
#         else:
#             start = mid + 1
#     return -1
#
#
# arr = [1, 2, 3, 4, 5, 6, 7, 11, 12, 13, 15, 16, 18, 20]
# print(binary_search(arr, 9))


# # 이진 탐색 (재귀 호출 방식)
# def binary_search(arr, start, end, key):
#     if start > end:
#         return -1
#
#     mid = (start + end) >> 1
#     if arr[mid] == key:
#         return mid
#     elif arr[mid] > key:
#         end = mid - 1
#         return binary_search(arr, start, end, key)
#     else:
#         start = mid + 1
#         return binary_search(arr, start, end, key)
#
#
# arr = [1, 2, 3, 4, 5, 6, 7, 11, 12, 13, 15, 16, 18, 20]
# start = 0
# end = len(arr) - 1
# print(binary_search(arr, start, end, 9))


# 선택 정렬
arr = [64, 25, 10, 22, 11]
N = len(arr)

for i in range(N-1):
    minIdx = i
    for j in range(minIdx + 1, N):
        if arr[minIdx] > arr[j]:
            minIdx = j

    arr[i], arr[minIdx] = arr[minIdx], arr[i]

print(arr)



