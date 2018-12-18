first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# full에 first와 second를 합쳐서 저장
full = first + second

# full_sorted에 full을 오름차순으로 정렬해서 저장
full_sorted = sorted(full)

# *reverse_sorted에 full을 내림차순으로 정렬해서 저장
full_sorted_reverse = sorted(full, reverse=True)

print(full)
print(full_sorted)
print(full_sorted_reverse)
