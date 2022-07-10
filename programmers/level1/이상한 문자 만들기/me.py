def solution(s):
    l = []
    count = 0
    for c in s:
        if c not in ' ':
            if count % 2:
                l.append(c.lower())      
            else:
                l.append(c.upper())
            count += 1
        else:
            l.append(c)
            count = 0
    return "".join(l)

s = "try hello world"	 
print(solution(s))