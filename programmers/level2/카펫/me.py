import itertools
def solution(brown, yellow):
    def get_divisor(n):
        result = [i for i in range(1, (n//2)+1) if n % i == 0] + [n]
        return result + result
    answer = []
    com = set([(x, y) for x, y in list(itertools.combinations(get_divisor(yellow), 2)) if x * y == yellow])
    for width, height in com:
        if width < height:
            width, height = height, width
        pred_brown = (width * 2) + (height * 2) + 4
        if pred_brown == brown:
            answer.extend([width+2, height+2])
            break
    return answer

brown = 8
yellow = 1
print(solution(brown, yellow))