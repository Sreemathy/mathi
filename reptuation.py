def f(n):
  if len(n) == 2:
    X = [n, (n[1] + n[0])]
    return X
  else:
    list1 = []
    for i in range(0, len(n)):
        Y = f(n[0:i] + n[i+1: len(n)])
        for j in Y:
            list1.append(n[i] + j)
    return list1
s = input("")
n=int(s)
z = f(s)
print (z) 
