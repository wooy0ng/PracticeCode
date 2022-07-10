
# 1)
solution = lambda sizes: max(sum(sizes, [])) * max(min(size) for size in sizes)


# 2)
def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)