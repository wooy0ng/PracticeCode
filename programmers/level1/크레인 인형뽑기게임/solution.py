# solution이라기 보다는 신기한 연산자를 처음 봐가지고 저장
'''
pseduo code
:= 연산자의 경우 python 3.8 이상부터 지원한다고 한다.

< EXAMPLE >
n = 30
if n > 10:
    print(f"{n} is greater than 10")

if (n := 30) > 10:
    print(f"{n} is greater than 10")

'''

def solution(board, moves):
    cols = list(map(lambda x: list(filter(lambda y: y > 0, x)), zip(*board)))
    a, s = 0, [0]

    for m in moves:
        if len(cols[m - 1]) > 0:
            if (d := cols[m - 1].pop(0)) == (l := s.pop()):
                a += 2
            else:
                s.extend([l, d])

    return a

board = [[0,0,0,0,0,0],[0,0,1,0,3,0],[0,2,5,0,1,0],[0,2,4,4,2,0],[0,5,1,3,1,1]]
moves = [1,6,3,5,1,2,1,4]

solution(board, moves)