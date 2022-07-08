def solution(a, b):
    if a > b:
        a, b = b, a
    return sum([k for k in range(a, b+1)])


a = 3
b = 5
print(solution(a, b))