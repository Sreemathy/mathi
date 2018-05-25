l=[]
a=int(input())
b=int(input())
for i in range(0,a):
  n=int(input())
  l.append(n)
if b in l:
  a=l.count(b)
  print(a)
