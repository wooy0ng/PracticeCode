# using tree list
from math import *
def solution(numbers, target):
    height = int(ceil(len(numbers)+1))
    node_cnt = 1 << (height)
    tree = [None, None] + [0] * (node_cnt - 2)
    
    for layer, number in enumerate(numbers):
        layer += 1
        pos = int(pow(2, layer))
        sign = -1
        while pos < pow(2, layer+1):
            tree[pos] = (number:=number * sign)
            pos += 1
        
    def querySolution(sum_, idx):
        nonlocal answer
        if tree[idx] != None:
            sum_ += tree[idx]

        if height >= int(log2(idx*2))+1:
            querySolution(sum_, idx*2)      # left
            querySolution(sum_, idx*2+1)    # right
        else:
            if sum_ == target:
                answer += 1

    answer = 0
    querySolution(0, 1)
    return answer


numbers = [4, 1, 2, 1]
target = 4

print(solution(numbers, target))