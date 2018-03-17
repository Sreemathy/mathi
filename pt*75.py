word = 'python'
index = 3
char = '*'
if((len(word))%2==0):
  word = word[:index] + char + word[index + 1:]
  print (word)
