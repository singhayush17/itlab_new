t=int(input())
for _ in range(t):
 a,b=map(int,input().split());s=list(input());s.sort();c=0;x=0
 for i in s:
  c+=(91-ord(i));x+=1
  if(c>b):break
 print(a-x)