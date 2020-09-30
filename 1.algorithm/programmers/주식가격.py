def solution(prices):
    answer = [0 for _ in range(len(prices))]

    for i in range(len(prices)):
        cnt = 0
        for j in range(i+1, len(prices)):
            if prices[j] < prices[i]:
                cnt += 1
                break

            cnt += 1

        answer[i] = cnt

    return answer


prices = [1, 2, 3, 2, 3]
print(solution(prices))
