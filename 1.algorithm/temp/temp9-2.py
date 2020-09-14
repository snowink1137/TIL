def solution(info, query):
    answer = []

    applicants = {
        'cpp': {
            'backend': {
                'junior': {
                    'chicken': [

                    ],
                    'pizza': [

                    ],
                },
                'senior': {
                    'chicken': [

                    ],
                    'pizza': [

                    ],
                },
            },
            'frontend': {
                'junior': {
                    'chicken': [

                    ],
                    'pizza': [

                    ],
                },
                'senior': {
                    'chicken': [

                    ],
                    'pizza': [

                    ],
                },
            },
        },
        'java': {
            'backend': {
                'junior': {
                    'chicken': [

                    ],
                    'pizza': [

                    ],
                },
                'senior': {
                    'chicken': [

                    ],
                    'pizza': [

                    ],
                },
            },
            'frontend': {
                'junior': {
                    'chicken': [

                    ],
                    'pizza': [

                    ],
                },
                'senior': {
                    'chicken': [

                    ],
                    'pizza': [

                    ],
                },
            },
        },
        'python': {
            'backend': {
                'junior': {
                    'chicken': [

                    ],
                    'pizza': [

                    ],
                },
                'senior': {
                    'chicken': [

                    ],
                    'pizza': [

                    ],
                },
            },
            'frontend': {
                'junior': {
                    'chicken': [

                    ],
                    'pizza': [

                    ],
                },
                'senior': {
                    'chicken': [

                    ],
                    'pizza': [

                    ],
                },
            },
        },
    }

    for ii in info:
        information = ii.split()
        applicants[information[0]][information[1]][information[2]][information[3]].append(int(information[4]))

    for qq in query:
        target = qq.split()
        target.remove('and')
        target.remove('and')
        target.remove('and')
        #target_list = applicants[target[0]][target[1]][target[2]][target[3]]

        a_list = []
        b_list = []
        c_list = []
        d_list = []

        if target[0] == '-':
            a_list.append('cpp')
            a_list.append('java')
            a_list.append('python')
        else:
            a_list.append(target[0])

        if target[1] == '-':
            b_list.append('backend')
            b_list.append('frontend')
        else:
            b_list.append(target[1])

        if target[2] == '-':
            c_list.append('junior')
            c_list.append('senior')
        else:
            c_list.append(target[2])

        if target[3] == '-':
            d_list.append('chicken')
            d_list.append('pizza')
        else:
            d_list.append(target[3])

        target_list = []
        for a in a_list:
            for b in b_list:
                for c in c_list:
                    for d in d_list:
                        target_list += applicants[a][b][c][d]

        target_list.sort(reverse=True)
        cnt = 0
        goal = int(target[4])
        for score in target_list:
            if score >= goal:
                cnt += 1
            else:
                break

        answer.append(cnt)

    return answer


info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(info, query))
