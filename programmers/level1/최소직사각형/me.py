from sympy import arg


def solution(sizes):
    widths, heights = [], []
    for t in sizes:
        if t[0] > t[1]:
            widths.append(t[0]); heights.append(t[1])
        else:
            widths.append(t[1]); heights.append(t[0])
    return max(widths) * max(heights)


sizes = [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]	

print(solution(sizes))