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
                    '-': [

                    ]
                },
                'senior': {
                    'chicken': [

                    ],
                    'pizza': [

                    ],
                    '-': [

                    ]
                },
                '-': {
                    'chicken': [

                    ],
                    'pizza': [

                    ],
                    '-': [

                    ]
                }
            },
            'frontend': {
                'junior': {
                    'chicken': [

                    ],
                    'pizza': [

                    ],
                    '-': [

                    ]
                },
                'senior': {
                    'chicken': [

                    ],
                    'pizza': [

                    ],
                    '-': [

                    ]
                },
                '-': {
                    'chicken': [

                    ],
                    'pizza': [

                    ],
                    '-': [

                    ]
                }
            },
            '-': {
                'junior': {
                    'chicken': [

                    ],
                    'pizza': [

                    ],
                    '-': [

                    ]
                },
                'senior': {
                    'chicken': [

                    ],
                    'pizza': [

                    ],
                    '-': [

                    ]
                },
                '-': {
                    'chicken': [

                    ],
                    'pizza': [

                    ],
                    '-': [

                    ]
                }
            }
        },
        'java': {
            'backend': {
                'junior': {
                    'chicken': [

                    ],
                    'pizza': [

                    ],
                    '-': [

                    ]
                },
                'senior': {
                    'chicken': [

                    ],
                    'pizza': [

                    ],
                    '-': [

                    ]
                },
                '-': {
                    'chicken': [

                    ],
                    'pizza': [

                    ],
                    '-': [

                    ]
                }
            },
            'frontend': {
                'junior': {
                    'chicken': [

                    ],
                    'pizza': [

                    ],
                    '-': [

                    ]
                },
                'senior': {
                    'chicken': [

                    ],
                    'pizza': [

                    ],
                    '-': [

                    ]
                },
                '-': {
                    'chicken': [

                    ],
                    'pizza': [

                    ],
                    '-': [

                    ]
                }
            },
            '-': {
                'junior': {
                    'chicken': [

                    ],
                    'pizza': [

                    ],
                    '-': [

                    ]
                },
                'senior': {
                    'chicken': [

                    ],
                    'pizza': [

                    ],
                    '-': [

                    ]
                },
                '-': {
                    'chicken': [

                    ],
                    'pizza': [

                    ],
                    '-': [

                    ]
                }
            }
        },
        'python': {
            'backend': {
                'junior': {
                    'chicken': [

                    ],
                    'pizza': [

                    ],
                    '-': [

                    ]
                },
                'senior': {
                    'chicken': [

                    ],
                    'pizza': [

                    ],
                    '-': [

                    ]
                },
                '-': {
                    'chicken': [

                    ],
                    'pizza': [

                    ],
                    '-': [

                    ]
                }
            },
            'frontend': {
                'junior': {
                    'chicken': [

                    ],
                    'pizza': [

                    ],
                    '-': [

                    ]
                },
                'senior': {
                    'chicken': [

                    ],
                    'pizza': [

                    ],
                    '-': [

                    ]
                },
                '-': {
                    'chicken': [

                    ],
                    'pizza': [

                    ],
                    '-': [

                    ]
                }
            },
            '-': {
                'junior': {
                    'chicken': [

                    ],
                    'pizza': [

                    ],
                    '-': [

                    ]
                },
                'senior': {
                    'chicken': [

                    ],
                    'pizza': [

                    ],
                    '-': [

                    ]
                },
                '-': {
                    'chicken': [

                    ],
                    'pizza': [

                    ],
                    '-': [

                    ]
                }
            }
        },
        '-': {
            'backend': {
                'junior': {
                    'chicken': [

                    ],
                    'pizza': [

                    ],
                    '-': [

                    ]
                },
                'senior': {
                    'chicken': [

                    ],
                    'pizza': [

                    ],
                    '-': [

                    ]
                },
                '-': {
                    'chicken': [

                    ],
                    'pizza': [

                    ],
                    '-': [

                    ]
                }
            },
            'frontend': {
                'junior': {
                    'chicken': [

                    ],
                    'pizza': [

                    ],
                    '-': [

                    ]
                },
                'senior': {
                    'chicken': [

                    ],
                    'pizza': [

                    ],
                    '-': [

                    ]
                },
                '-': {
                    'chicken': [

                    ],
                    'pizza': [

                    ],
                    '-': [

                    ]
                }
            },
            '-': {
                'junior': {
                    'chicken': [

                    ],
                    'pizza': [

                    ],
                    '-': [

                    ]
                },
                'senior': {
                    'chicken': [

                    ],
                    'pizza': [

                    ],
                    '-': [

                    ]
                },
                '-': {
                    'chicken': [

                    ],
                    'pizza': [

                    ],
                    '-': [

                    ]
                }
            }
        }
    }

    for ii in info:
        information = ii.split()
        #applicants[information[0]][information[1]][information[2]][information[3]].append(information[4])

        for a in [information[0], '-']:
            for b in [information[1], '-']:
                for c in [information[2], '-']:
                    for d in [information[3], '-']:
                        applicants[a][b][c][d].append(int(information[4]))

    for qq in query:
        target = qq.split()
        target.remove('and')
        target.remove('and')
        target.remove('and')
        target_list = applicants[target[0]][target[1]][target[2]][target[3]]

        cnt = 0
        for score in target_list:
            if score >= int(target[4]):
                cnt += 1

        answer.append(cnt)

    return answer


info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(info, query))
