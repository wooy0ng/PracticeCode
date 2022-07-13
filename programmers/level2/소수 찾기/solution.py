

# 1) set을 사용한 풀이
from itertools import permutations
def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)

numbers = "011"	
print(solution(numbers))


# 2) 재귀를 사용한 풀이
'''
primeSet = set()
def isPrime(number):
    if number in (0, 1):
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def makeCombinations(str1, str2):
    if str1 != "":
        if isPrime(int(str1)):
            primeSet.add(int(str1))
    for i in range(len(str2)):
        makeCombinations(str1 + str2[i], str2[:i] + str2[i + 1:])


def solution(numbers):
    makeCombinations("", numbers)
    answer = len(primeSet)
    return answer
'''