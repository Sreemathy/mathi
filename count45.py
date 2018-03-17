a=int(input("enter a number"))
count=0
while(a>0):
  dig=a%10
  count=count+1
  a=a//10
print(count)
