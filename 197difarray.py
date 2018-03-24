x=[]
n=int(input("Enter number of elements:"))
for i in range(1,n+1):
    b=int(input("Enter element:"))
    x.append(b)
min(x)
print(min(x))
max(x)
print(x[n-1])
print("diff",(x[n-1]-min(x)))
