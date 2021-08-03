def solution(genres, plays):
    answer = []
    cache = {}
    play_cache = {}
    for i in range(len(genres)):
        if cache.get(genres[i]):
            if cache[genres[i]].get('represent2'):
                if plays[i] > cache[genres[i]]['represent1'][1]:
                    cache[genres[i]]['represent2'] = cache[genres[i]]['represent1']
                    cache[genres[i]]['represent1'] = (i, plays[i])
                elif plays[i] > cache[genres[i]]['represent2'][1]:
                    cache[genres[i]]['represent2'] = (i, plays[i])
            else:
                if plays[i] > cache[genres[i]]['represent1'][1]:
                    cache[genres[i]]['represent2'] = cache[genres[i]]['represent1']
                    cache[genres[i]]['represent1'] = (i, plays[i])
                else:
                    cache[genres[i]]['represent2'] = (i, plays[i])

            play_cache[genres[i]] += plays[i]
        else:
            cache[genres[i]] = {'represent1': (i, plays[i])}
            play_cache[genres[i]] = plays[i]

    res = sorted(cache.items(), key=lambda x: play_cache[x[0]], reverse=True)

    for r in res:
        if cache[r[0]].get('represent2'):
            answer.append(cache[r[0]]['represent1'][0])
            answer.append(cache[r[0]]['represent2'][0])
        else:
            answer.append(cache[r[0]]['represent1'][0])

    return answer


# genres = ['classic', 'pop', 'classic', 'classic', 'pop']
# plays = [500, 600, 150, 800, 2500]
# genres = ['a', 'b', 'c', 'd', 'e', 'f']
# plays = [1, 2, 3, 4, 5, 6]
# genres = ['classic', 'pop', 'classic', 'pop', 'classic', 'classic']
# plays = [400, 600, 150, 2500, 500, 500]
# genres = ['classic', 'pop', 'classic', 'classic', 'pop', 'zazz', 'zazz']
# plays = [500, 600, 150, 800, 2500, 2000, 6000]
genres = ['classic', 'pop', 'classic', 'classic', 'pop']
plays = [500, 600, 501, 800, 900]
print(solution(genres, plays))
