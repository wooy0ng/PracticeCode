def solution(s):
    p_cnt = 0
    y_cnt = 0
    for c in s.lower():
        if c == 'p':    p_cnt += 1
        elif c == 'y':  y_cnt += 1
    return p_cnt == y_cnt

s = "pPoooyY"	
print(solution(s))