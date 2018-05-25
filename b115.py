l=[]
n,k=list(map(int,input().split(" ")))
for i in range(0,n):
  m=int(input())
  l.append(m)
  l.sort()
print(l[k-1])
