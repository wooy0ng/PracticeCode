def solution(absolutes, signs):
    return sum([x if y is True else -x for x, y in zip(absolutes, signs)])