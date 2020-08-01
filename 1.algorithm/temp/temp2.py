import json


def get_summary(data, target_value):
    summary = target_value

    first = None
    for d in data:
        if d['value'] == target_value:
            if d['is_active']:
                first = d
                parent_pk = d['parent']
                break
            else:
                return 'INACTIVE'

    second = None
    for d in data:
        if d['pk'] == parent_pk:
            if d['is_active']:
                second = d
                parent_pk = d['parent']
                break
            else:
                return 'INACTIVE'

    third = None
    for d in data:
        if d['pk'] == parent_pk:
            if d['is_active']:
                third = d
                parent_pk = d['parent']
                break
            else:
                return 'INACTIVE'

    while parent_pk:
        for d in data:
            if d['pk'] == parent_pk:
                if d['is_active']:
                    parent_pk = d['parent']
                    break
                else:
                    return 'INACTIVE'

    if third:
        summary = third['value'] + '>' + second['value'] + '>' + first['value']
    elif second:
        summary = second['value'] + '>' + first['value']
    elif first:
        summary = first['value']

    return summary


user_input = input().split('/')
user_input[0] = json.loads(user_input[0])
data = user_input[0]
target_value = user_input[1]
print(get_summary(data, target_value))
