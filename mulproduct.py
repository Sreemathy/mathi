a=int(input("enter  number a"))
tot=1
while(a>0):
  dig=a%10
  tot=tot*dig
  a=a//10
print(tot)
