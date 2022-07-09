def solution(x):
    return True if not x % sum(map(int, list(str(x)))) else False

x = 13
print(solution(x))