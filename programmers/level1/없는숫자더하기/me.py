def solution(numbers):
    return sum([n for n in range(0, 10) if n not in numbers])
    
numbers = [1,2,3,4,6,7,8,0]	
print(solution(numbers))