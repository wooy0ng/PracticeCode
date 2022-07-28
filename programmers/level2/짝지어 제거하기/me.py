def solution(s):
    stack = []
    for c in s:
        if stack:
            if stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)
        else:
            stack.append(c)
    return 0 if stack else 1

s = "baabaa"
print(solution(s))