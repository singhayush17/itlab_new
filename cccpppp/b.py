import bisect;t=int(input())
while(t):
 a,b=map(int,input().split());l=sorted(list(map(int,input().split())));m=sorted(list(map(int,input().split())));i=0;j=0;t-=1
 while(j!=b and i!=a):
  if(m[j]<=l[i] and l[bisect.bisect_left(l,m[j])]==l[i]):i+=1;j+=1
  else:i+=1
 if(j!=b):print("NO")
 else:print("YES")
