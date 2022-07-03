def solution(nums):
    import itertools
    answer = 0
    for a, b, c in itertools.combinations(nums, 3):
        tmp = a + b + c
        answer += 1
        for k in range(tmp-1, 1, -1):
            if not tmp % k:
                answer -= 1
                break
    return answer

nums = [1,2,7,6,4]	
print(solution(nums))