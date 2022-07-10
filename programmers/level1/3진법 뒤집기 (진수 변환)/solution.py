def solution(n):
    reverse_base = ''
    while n > 0:
        n, mod = divmod(n, 3)
        reverse_base += str(mod)
    
    return int(reverse_base, base=3)