n=153
sum=0
temp=n
for n in range(0,10):
  while(temp>0):
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
  if(n==sum):
    print("it is arm strong")
  else:
    print("not armstrong")
