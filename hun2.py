l=[]
a=int(input())
for i in range(0,a):
  n=int(input())
  l.append(n)
  l.sort()
a=l[::-1]
print("".join(str(i) for i in a))
