t=int(input())
for _ in range(t):
    n=int(input())
    dp=[]
    for i in range(n):
        l=list(map(int,input().split()))
        dp.append(l)
    print(dp)