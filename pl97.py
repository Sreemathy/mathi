a,b=map(int,input().split(" "))
m=0
for i in range(a,b):
  if(i%2!=0):
    m=m+i
print(m)
