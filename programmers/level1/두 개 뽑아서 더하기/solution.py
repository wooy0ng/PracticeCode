def solution(numbers):
    import itertools
    return sorted(list(set([sum(t) for t in itertools.combinations(numbers, 2)])))