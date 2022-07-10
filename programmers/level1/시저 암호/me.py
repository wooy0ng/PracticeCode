def solution(s, n):
    s = list(s)
    for idx, c in enumerate(s):
        if c.isupper():
            s[idx] = chr((ord(c) - ord('A') + n) % 26 + ord('A'))
        elif c.islower():
            s[idx] = chr((ord(c) - ord('a') + n) % 26 + ord('a'))
    return "".join(s)
    
s = "a B z"		
n = 4
print(solution(s, n))