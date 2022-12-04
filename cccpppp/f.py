t=int(input())
for _ in range(t):
 a,b=map(int,input().split());s=list(input());s.sort();c=0;x=0
 while(c<=b):c+=(91-ord(s[x]));a-=1
 print(a)