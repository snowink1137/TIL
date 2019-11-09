def solution(board, moves):
    answer = 0
    stack = []
    new_board = [[] for _ in range(len(board[0]))]

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != 0:
                new_board[j].insert(0, board[i][j])

    for index in moves:
        if new_board[index-1]:
            doll = new_board[index-1].pop()
        else:
            continue

        if len(stack) == 0:
            stack.append(doll)
        elif stack[-1] == doll:
            stack.pop()
            answer += 2
        else:
            stack.append(doll)

    return answer


board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board, moves))
