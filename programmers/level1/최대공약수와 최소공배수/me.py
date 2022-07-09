def solution(n, m):
    # 최대 공약수
    def gcd(n, m):
        while m:
            n, m = m, n % m
        return n

    # 최소 공배수
    def lcm(n, m):
        return (n * m) // gcd(n, m)

    return [gcd(n, m), lcm(n, m)]

n = 2
m = 5
print(solution(n, m))