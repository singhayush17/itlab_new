import bisect
t=int(input())
for _ in range(t):
 a,b=map(int,input().split());l=list(map(int,input().split()));m=list(map(int,input().split()));l.sort();m.sort();i=0;j=0
 while(j!=b and i!=a):
  if(m[j]<=l[i] and (l[bisect.bisect_left(l,m[j])]==l[i])):i+=1;j+=1; 
  else:i+=1
 print("NO") if j!=b else print("YES")