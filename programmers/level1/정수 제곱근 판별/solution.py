def solution(n):
    sqrt_ = int(n ** 0.5)
    return pow(sqrt_+1, 2) if n == pow(sqrt_, 2) else -1
