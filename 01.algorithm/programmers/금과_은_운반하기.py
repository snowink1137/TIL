def solution(a, b, g, s, w, t):
    start = 0
    end = (a + b) * max(t) * 2

    while start < end:
        mid = (start + end) // 2

        total = 0
        gold = 0
        silver = 0

        for i in range(len(g)):
            if mid >= t[i]:
                remain = mid - t[i]
                time = ((remain // 2) // t[i]) + 1  # 1번은 편도
                total += min(w[i] * time, g[i] + s[i])
                gold += min(w[i] * time, g[i])
                silver += min(w[i] * time, s[i])

        if total >= a + b and gold >= a and silver >= b:
            end = mid
        else:
            start = mid + 1

    return start


a, b, g, s, w, t = 10, 10, [100], [100], [7], [10]
print(solution(a, b, g, s, w, t))
