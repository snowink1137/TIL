from collections import defaultdict


def solution(n, results):
    answer = 0

    winners = defaultdict(set)
    losers = defaultdict(set)

    for winner, loser in results:
        winners[loser].add(winner)
        losers[winner].add(loser)

    for i in range(1, n+1):
        for winner in winners[i]:
            losers[winner].update(losers[i])

        for loser in losers[i]:
            winners[loser].update(winners[i])

    for i in range(1, n+1):
        if len(winners[i]) + len(losers[i]) == n-1:
            answer += 1

    return answer


n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
print(solution(n, results))
