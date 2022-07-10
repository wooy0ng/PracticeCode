def solution(n):
    s = "수박"
    return "".join([s[idx%2] for idx in range(n)])

n = 3
print(solution(n))