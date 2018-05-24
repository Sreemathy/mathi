l=[]
s=[]
a=int(input())
for i in range(0,a):
  n=int(input())
  l.append(n)
for i in l:
  a=l.index(i)
  if(a==i):
    print(i)
    s.append(i)
    print("".join(str(i) for i in s)) 
  else:
    print('-1')
      
