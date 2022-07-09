def solution(d, budget):
    d.sort() # ascending
    answer = 0
    for k in d:
        budget -= k
        if budget < 0:
            break
        answer += 1
    
    return answer


d = [2,2,3,3]	
budget = 10
print(solution(d, budget))