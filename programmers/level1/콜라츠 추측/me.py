def solution(num):
    answer = 0
    while num != 1:
        if not num % 2:
            num /= 2
        else:
            num = num * 3 + 1
        answer += 1
        if answer > 500: break
    
    return answer if num == 1 else -1

num = 6
print(solution(num))