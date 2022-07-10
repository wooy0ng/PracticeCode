def solution(numbers):
    import itertools
    return sorted(list(set([sum(t) for t in itertools.combinations(numbers, 2)])))


numbers = [1,1,1,1,0]	
print(solution(numbers))