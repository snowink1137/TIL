def solution(record):
    result = []

    split_record = []
    for r in record:
        split_record.append(tuple(r.split()))

    names = dict()
    for sr in split_record:
        if sr[0] == 'Enter' or sr[0] == 'Change':
            names[sr[1]] = sr[2]

    for sr in split_record:
        if sr[0] == 'Enter':
            result.append('{}님이 들어왔습니다.'.format(names[sr[1]]))
        elif sr[0] == 'Leave':
            result.append('{}님이 나갔습니다.'.format(names[sr[1]]))

    return result


record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]
print(solution(record))
