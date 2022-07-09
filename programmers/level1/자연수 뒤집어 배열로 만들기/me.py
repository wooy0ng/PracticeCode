def solution(n):
    return list(map(int, str(n)[::-1]))

n = 12345
print(solution(n))