def solution(s):
    try:
        int(s)
    except ValueError as e:
        return False
    return True if len(s) == 4 or len(s) == 6 else False

s = "1234"	
print(solution(s))