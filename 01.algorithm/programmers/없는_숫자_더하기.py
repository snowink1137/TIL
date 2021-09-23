def solution(numbers):
    numbers_set = set(numbers)
    full_numbers_set = set([i for i in range(10)])

    answer = sum(full_numbers_set.difference(numbers_set))
    return answer
