def solution(x, n):
    return [x+(x*k) for k in range(n)]

x = 2
n = 5
print(solution(x, n))
