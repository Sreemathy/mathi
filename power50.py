def is_power(a):
    a = a/2
    if a == 2:
        return True
    elif a > 2:
        return is_power(a)
    else:
        return False
if is_power(32):
           print ('yes')
else:
    print ('no')
