
def solution(w, h):
    if w == 1 or h == 1:
        squares = 0
    else:
        if w != h:
            squares = sum(list(int(((h * n) / w)) for n in range(w))) * 2
        else:
            squares = (w * h) - w
    return squares

w = 8
h = 12
print(solution(w, h))