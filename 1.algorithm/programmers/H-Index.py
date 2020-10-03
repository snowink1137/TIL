def solution(citations):
    answer = 0
    paper_number = len(citations)

    citations.sort(reverse=True)

    for n in range(paper_number, 1, -1):
        cnt = 0
        for i in range(n):
            if citations[i] < n:
                break

            cnt += 1

        if cnt >= n:
            answer = n
            break

    return answer


citations = [3, 0, 6, 1, 5]
print(solution(citations))
