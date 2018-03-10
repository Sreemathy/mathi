str = 'aIbohPhoBiA'
str = str.casefold()
rev_str = reversed(str)
if list(str) == list(rev_str):
   print("It is palindrome")
else:
   print("It is not palindrome")
