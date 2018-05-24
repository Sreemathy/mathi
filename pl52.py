l=[]
k=int(input())
n=int(input())
for i in range(0,n):
  a=int(input())
  l.append(a)
  l.sort()
print(l[k])
