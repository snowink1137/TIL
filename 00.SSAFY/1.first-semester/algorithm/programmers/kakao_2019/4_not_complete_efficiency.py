def solution(words, queries):
    answer = []

    for query in queries:
        cnt = 0
        front = 0
        end = len(query) - 1
        left = True

        if query[0] == '?':
            for i in range(1, len(query)):
                if query[i] == '?':
                    continue
                else:
                    end = i
                    check = query[end:]
                    break
        else:
            for i in range(1, len(query)):
                if query[i] == '?':
                    front = i
                    check = query[:front]
                    left = False
                    break

        for word in words:
            if len(word) != len(query):
                continue

            if left:
                if word[end:] == check:
                    cnt += 1
            else:
                if word[:front] == check:
                    cnt += 1

        answer.append(cnt)

    return answer

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words, queries))
