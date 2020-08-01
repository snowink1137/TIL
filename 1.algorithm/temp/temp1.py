user_input = input()

rules = [8, 5, 2, 4, 3, 7, 6, 1, 0, 9]
visit = [0 for i in range(10)]

user_input_list = user_input.split()
for num in user_input_list:
    visit[int(num)] += 1

result = []
for rule in rules:
    if visit[rule]:
        for _ in range(visit[rule]):
            result.append(str(rule))

output = ' '.join(result)
print(output)
