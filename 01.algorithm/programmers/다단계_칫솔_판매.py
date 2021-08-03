from collections import deque


def solution(enroll, referral, seller, amount):
    answer = []
    relations = dict()
    answer_dict = dict()

    for e, f in zip(enroll, referral):
        relations[e] = f
        answer_dict[e] = 0

    relations['-'] = False

    for s, a in zip(seller, amount):
        money = a * 100
        queue = deque()
        queue.append(s)

        while queue:
            q = queue.popleft()
            if int(money * 0.1) < 1:
                answer_dict[q] += money
                break

            if relations[q] and relations[q] != '-':
                my_money = money - int(money * 0.1)
                money = int(money * 0.1)
                queue.append(relations[q])
                answer_dict[q] += my_money
            else:
                answer_dict[q] += money - int(money * 0.1)
                break

    for e in enroll:
        answer.append(answer_dict[e])

    return answer


enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]
print(solution(enroll, referral, seller, amount))
