import itertools
def solution(numbers):
    def isPrime(n):
        if n <= 1:
            return False
        else:
            for i in range(2, int(n**0.5)+1):
                if n % i == 0:
                    return False
        return True
    
    answer = 0
    numbers = list(map(int, numbers))
    complete = []
    for k in range(1, len(numbers)+1):
        com = set(map(lambda x: int("".join(list(map(str, x)))), itertools.permutations(numbers, k)))
        for n in com:
            if n not in complete:
                complete.append(n)
                if isPrime(n):
                    answer += 1
    return answer



numbers = "011"	
print(solution(numbers))