def solution(n):
    l = sorted([(idx, c) for idx, c in enumerate(str(n))], key=lambda x: x[1], reverse=True)
    return int("".join([k[1] for k in l]))

n = 118372
print(solution(n))