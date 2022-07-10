from audioop import reverse
import enum


def solution(n, arr1, arr2):
    def int_to_bit(arr):
        result = []
        for n in arr:
            reverse_base = ''
            while n > 0:
                n, mod = divmod(n, 2)
                reverse_base += str(mod)
            result.append(reverse_base[::-1])
        max_len = max([len(s) for s in result])
        
        for idx, s in enumerate(result):
            while len(s) != max_len:
                s = '0' + s
            result[idx] = s
        return [[int(c) for c in s] for s in result]
    
    arr1 = int_to_bit(arr1)
    arr2 = int_to_bit(arr2)
    
    return ["".join(['#' if arr1[r][c] | arr2[r][c] else ' ' for c in range(len(arr1[0]))]) for r in range(len(arr1))]

n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
print(solution(n, arr1, arr2))