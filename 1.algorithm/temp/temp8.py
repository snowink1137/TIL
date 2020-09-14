from itertools import combinations


def solution(orders, course):
    answer = []
    dish_set = set()
    orders_list = []

    for order in orders:
        temp_set = set(order)
        dish_set = dish_set.union(temp_set)
        orders_list.append(list(order))

    cnt_dict = {}
    for c in course:
        cnt_dict[c] = {}
        for combi in combinations(dish_set, c):
            cnt = 0
            for order in orders_list:
                for i in range(c):
                    if combi[i] not in order:
                        break
                else:
                    cnt += 1

            if cnt > 1:
                cnt_dict[c][combi] = cnt

        if cnt_dict[c]:
            max_value = max(cnt_dict[c].values())
            for key, value in cnt_dict[c].items():
                if value == max_value:
                    answer.append(''.join(sorted(list(key))))

    answer.sort()

    return answer


orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course = [2,3,5]
print(solution(orders, course))
