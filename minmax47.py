list = []
count = int(input("How many numbers  : "))
for i in range(1,count+1):
  list.append(int(input("Enter number ".format(i))))
min = list[0]
max = list[0]
for no in list:
  if no < min : 
    min = no
  elif no > max :
    max = no
print("Minimum number : {}, Maximum number : {}".format(min,max))
