nterms = 5
n1 = 0
n2 = 1
count = 0
if nterms <= 0:
   print("enter pos int")
elif nterms == 1:
   print("Fibonacci sequence")
   print(n1)
else:
   print("Fibonacci sequence ")
   while count < nterms:
       print(n1,end=' , ')
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1
