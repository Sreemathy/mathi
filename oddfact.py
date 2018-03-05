x=int(input("enter a number"))
for i in range(1,x):
     if x% i == 0:
       if(i%2!=0):
           print("the odd factors of ",x,"are",i)

