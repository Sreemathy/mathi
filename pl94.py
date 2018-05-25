l=[]
a=int(input())
for i in  range(0,a):
  n=int(input())
  l.append(n)
for i in l:
  a=l.count(i)
  if(a!=1):
    print("yes")
    break
