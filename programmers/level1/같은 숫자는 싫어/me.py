def solution(arr):
    stack = []
    for k in arr:
        if not stack:
            stack.append(k)
        else:
            if stack[-1] != k:
                stack.append(k)
    return stack

arr = [1,1,3,3,0,1,1]	
print(solution(arr))