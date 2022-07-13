# 1)
def solution(brown, yellow):
    for i in range(1, int(yellow**(1/2))+1):
        if yellow % i == 0:
            if 2 * (i + yellow // i) == brown - 4:
                return [yellow//i+2, i+2]


# 2) 근의 공식
# 변수가 2개인 2차 방정식이기 때문에 근의 공식 사용 가능
import math
def solution(brown, yellow):
    w = ((brown+4)/2 + math.sqrt(((brown+4)/2)**2-4*(brown+yellow)))/2
    h = ((brown+4)/2 - math.sqrt(((brown+4)/2)**2-4*(brown+yellow)))/2
    return [w,h]