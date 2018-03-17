list = []
count = int(input("How many numbers  : "))
for i in range(1,count+1):
  list.append(int(input("Enter number ".format(i))))
sum=list[0]+list[1]
average=sum/2
print("sum",sum)
print("average",average)
