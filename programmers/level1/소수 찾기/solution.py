def solution(n):
    num=set(range(3,n+1,2))

    for i in range(3,int(n**(0.5)+1)):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)+1