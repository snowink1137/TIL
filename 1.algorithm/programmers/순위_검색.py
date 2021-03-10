# 처음에는 applicants를 nested dictionary 구조로 짰다가 시간 초과가 났다.
#

from itertools import combinations
from collections import defaultdict


def solution(info, query):
    answer = []

    applicants = defaultdict(list)

    for ii in info:
        information = ii.split()
        key = information[:-1]
        value = int(information[-1])
        for i in range(5):
            for combi in combinations(key, i):
                extended_key = ''.join(combi)
                applicants[extended_key].append(value)

    for key in applicants.keys():
        applicants[key].sort()

    for qq in query:
        target = qq.split()
        score = int(target[7])
        query_key = ''
        if target[0] != '-':
            query_key += target[0]

        if target[2] != '-':
            query_key += target[2]

        if target[4] != '-':
            query_key += target[4]

        if target[6] != '-':
            query_key += target[6]

        target_list = applicants[query_key]

        if not target_list:
            answer.append(0)
            continue

        left, right = 0, len(target_list)
        while left != right and left != len(target_list):
            mid = (left + right) // 2
            if target_list[mid] >= score:
                right = mid
            else:
                left = mid + 1

        answer.append(len(target_list)-left)

    return answer


info = ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
        "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
         "- and - and - and - 150"]
print(solution(info, query))
