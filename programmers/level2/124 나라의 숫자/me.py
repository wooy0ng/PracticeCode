def solution(n):
    reversed_base = ""
    table = {0: 4, 1: 1, 2: 2}
    while n > 0:
        n, mod = divmod(n, 3)        
        reversed_base += str(table[mod])
        if mod == 0:
            n -= 1
    return reversed_base[::-1]

nums = [n for n in range(1, 15)]
print([solution(k) for k in nums])