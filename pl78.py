l=[]
s=[]
a=int(input())
for i in  range(0,a):
  n=int(input())
  l.append(n)
b=int(input())
for i in range(0,b):
  m=int(input())
  s.append(m)
z=l+s
z.sort()
print(z)
