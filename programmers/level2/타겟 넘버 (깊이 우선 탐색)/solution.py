# 1)
def solution1(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution1(numbers[1:], target-numbers[0]) + solution1(numbers[1:], target+numbers[0])


# 2)
from itertools import product
def solution2(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)

numbers = [4, 1, 2, 1]
target = 4

print(solution1(numbers, target))