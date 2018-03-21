word='sreemathy'
for char in word:
    if word.count(char) > 1:
        print(word, "False")
        print("not isogram",char)
    else:
        print(word, "True")
        print("isogram",char)
