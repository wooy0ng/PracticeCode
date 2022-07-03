def solution(absolutes, signs):
    return sum([x if y is True else -x for x, y in zip(absolutes, signs)])

absolutes = [4, 7, 12]
signs = [True, False, True]
print(solution(absolutes, signs))