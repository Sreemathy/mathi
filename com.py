n=int(input("enter a number")
for i in range(1,n):
  if n%i==0:
     fact=i
  if fact>1:
    print ('The number is a composite number',fact)
  elif(n==1):
    print("prime number")
    
