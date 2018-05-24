l=[]
c=int(input())
for i in range(0,c):
  n=int(input())
  l.append(n)
for i in l:
  a=l.count(i)
  if(a==1):
    print(i)
