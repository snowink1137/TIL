flag = False
answers = []


def dfs(now, visit, tickets, answer):
    global flag
    global answers

    if sum(visit) == len(visit):
        answers = [ans[:] for ans in answer]
        flag = True
        return

    for i in range(len(tickets)):
        if flag:
            return

        if visit[i] is not True and tickets[i][0] == now:
            next = tickets[i][1]
            visit[i] = True
            answer_copy = [ans[:] for ans in answer]
            answer.append(next)
            dfs(next, visit, tickets, answer)

            if flag:
                return

            visit[i] = False
            answer = answer_copy



def solution(tickets):
    answer = ['ICN']
    visit = [False for _ in range(len(tickets))]
    tickets.sort(key=lambda x: x[1])

    dfs(answer[-1], visit, tickets, answer)

    return answers


# tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
tickets = [["ICN", "BOO"], ["ICN", "COO"], ["COO", "DOO"], ["DOO", "COO"], ["BOO", "DOO"],["DOO", "BOO"], ["BOO", "ICN"], ["COO", "BOO"]]

print(solution(tickets))
