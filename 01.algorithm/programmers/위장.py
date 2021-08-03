def solution(clothes):
    cache = {}
    for cloth in clothes:
        if cache.get(cloth[1]):
            cache[cloth[1]] += 1
        else:
            cache[cloth[1]] = 1

    print(cache)
    answer = 0
    temp = 1
    for i in cache:
        temp *= cache[i] + 1

    if temp != 1:
        answer = temp - 1

    return answer


clothes = [['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]
print(solution(clothes))
