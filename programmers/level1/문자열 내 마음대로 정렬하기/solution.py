def solution(strings, n):
    
    # sort(key=lambda x: (기준1, 기준2)) 를 통해 기준 적용 우선순위를 둘 수 있다.
    return sorted(strings, key=lambda x: (x[n], x))