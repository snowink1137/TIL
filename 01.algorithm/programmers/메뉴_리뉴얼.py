from itertools import combinations


def solution(orders, course):
    answer = []

    orders = sorted(orders, key=lambda x: len(x), reverse=True)
    for c in course:
        flag = {}
        new_menu = {}

        for order in orders:
            if len(order) < c:
                break

            order_list = list(''.join(order))
            for combi in combinations(order_list, c):
                new = ''.join(sorted(combi))
                if flag.get(new):
                    if new_menu.get(new):
                        new_menu[new] += 1
                    else:
                        new_menu[new] = 2
                else:
                    flag[new] = True

        if new_menu:
            max_value = max(new_menu.values())
            for key, value in new_menu.items():
                if value == max_value:
                    answer.append(''.join(list(key)))

    answer.sort()

    return answer


orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course = [2,3,5]
print(solution(orders, course))
