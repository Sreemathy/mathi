a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
if(a>b):
    minimum1=a
else:
    minimum1=b
while(1):
    if(minimum1%a==0 and minimum1%b==0):
        print("LCM is:",minimum1)
        break
    minimum1=minimum1+1
