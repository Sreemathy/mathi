l=[]
s=[]
n,k=list(map(int,input().split(" ")))
for i in range(0,n):
  m=int(input())
  l.append(m)
for i in l:
  if(i%2!=0):
    s.append(i)
    s.sort()
print(s[k-1])
