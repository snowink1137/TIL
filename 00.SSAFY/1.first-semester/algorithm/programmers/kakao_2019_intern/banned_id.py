answer = 0
answer_list = []


def combi(depth, current_list, full_list):
    global answer

    if depth == len(full_list):
        current_list.sort()
        if current_list not in answer_list:
            answer += 1
            answer_list.append(current_list)

        return

    for x in full_list[depth]:
        if x in current_list:
            continue

        current_list_copy = current_list[:]
        current_list.append(x)
        combi(depth+1, current_list, full_list)
        current_list = current_list_copy


def solution(user_id, banned_id):
    global answer
    full_list = [[] for _ in range(len(banned_id))]

    for i in range(len(banned_id)):
        for id in user_id:
            if len(id) != len(banned_id[i]):
                continue

            for j in range(len(id)):
                if banned_id[i][j] == '*' or id[j] == banned_id[i][j]:
                    continue
                else:
                    break
            else:
                full_list[i].append(id)

    combi(0, [], full_list)

    return answer


user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["*rodo", "*rodo", "******"]
print(solution(user_id, banned_id))
