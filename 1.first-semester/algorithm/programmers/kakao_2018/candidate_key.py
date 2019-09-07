combination = []


def loop(current, column_length, temp_list):
    if current == column_length:
        return

    temp_list.append(current)
    combination.append(temp_list[:])

    for i in range(current+1, column_length+1):
        loop(i, column_length, temp_list)

    temp_list.pop()


def solution(relation):
    result = 0
    candidate_keys = []
    column_length = len(relation[0])

    temp_list = []
    for i in range(column_length):
        loop(i, column_length, temp_list)

    combination.sort(key=len)

    for combi in combination:
        temp_list2 = []

        flag = True
        for candidate_key in candidate_keys:
            cnt = 0
            for col in candidate_key:
                if col in combi:
                    cnt += 1

            if cnt == len(candidate_key):
                flag = False
                break

        if not flag:
            continue

        for rel in relation:
            temp_list3 = []
            for col in combi:
                temp_list3.append(rel[col])

            if temp_list3 in temp_list2:
                break
            else:
                temp_list2.append(temp_list3)
        else:
            candidate_keys.append(combi)

    result = len(candidate_keys)

    return result


relation = [['a',1,4],[2,1,5],['a',2,4]]
print(solution(relation))
