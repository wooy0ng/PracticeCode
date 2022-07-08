def solution(arr):
    '''
    너무 복잡하게 생각한듯
    '''
    answer = sorted([(idx, num) for idx ,num in enumerate(arr)], key=lambda x: x[1], reverse=True)
    answer = sorted([(idx, num) for idx, num in answer[:-1]], key=lambda x: x[0])
    return [num for _, num in answer] if len(answer) > 0 else [-1]

arr = [1, 3, 2, 4]
print(solution(arr))