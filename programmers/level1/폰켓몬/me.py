def solution(nums):
    nums_len = len(nums) // 2
    set_len = len(set(nums))

    return set_len if nums_len >= set_len else nums_len

nums = [3,1,2,3]		
print(solution(nums))

