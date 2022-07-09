def solution(left, right):
    def get_divisor(n):
        return [k for k in range(1, (n//2)+1) if n % k == 0] + [n]
    
    answer = 0
    for n in range(left, right+1):
        if len(get_divisor(n)) % 2 != 0:
            answer -= n
        else:
            answer += n
    return answer


left = 13
right = 17 
print(solution(left, right))