def solution(s):
    if len(s) % 2:
        return s[len(s)//2]
    return s[len(s)//2-1:len(s)//2+1]

s = "abcde"
print(solution(s))