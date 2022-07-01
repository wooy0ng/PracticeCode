def solution(a, b):
    answer = sum([x * y for x, y in zip(a, b)])
    return answer

a = [1,2,3,4]
b = [-3,-1,0,2]
solution(a, b)