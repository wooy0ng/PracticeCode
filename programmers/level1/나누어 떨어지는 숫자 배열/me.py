def solution(arr, divisor):
    answer = []
    for n in arr:
        if not n % divisor:
            answer.append(n)
    return sorted(answer) if answer else [-1]


arr = [5, 9, 7, 10]	
divisor = 5
print(solution(arr, divisor))