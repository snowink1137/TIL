def dfs(now, visit, tickets, answer):
    if sum(visit) == len(visit):
        return

    next = 'zzzzzzzzzzz'
    temp = 0
    for i in range(len(tickets)):
        if visit[i] is not True and tickets[i][0] == now and tickets[i][1] < next:
            next = tickets[i][1]
            temp = i

    visit[temp] = True
    answer.append(next)
    dfs(next, visit, tickets, answer)


def solution(tickets):
    answer = ['ICN']
    visit = [False for _ in range(len(tickets))]

    dfs(answer[-1], visit, tickets, answer)

    return answer

print(solution([['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL','SFO']]))
