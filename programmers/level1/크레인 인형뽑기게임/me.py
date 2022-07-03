def solution(board, moves):
    answer = 0
    stack = []
    for pos in moves:
        layer = 0
        while layer < len(board):
            if board[layer][pos-1]:
                if len(stack) != 0:
                    if stack[-1] == board[layer][pos-1]:
                        board[layer][pos-1] = 0
                        stack.pop(); answer += 2
                        break
                stack.append(board[layer][pos-1])
                board[layer][pos-1] = 0
                break
            else:
                layer += 1
    return answer

board = [[0,0,0,0,0,0],[0,0,1,0,3,0],[0,2,5,0,1,0],[0,2,4,4,2,0],[0,5,1,3,1,1]]
moves = [1,6,3,5,1,2,1,4]

solution(board, moves)