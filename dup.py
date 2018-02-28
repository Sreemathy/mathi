a='sreeeeeeeeeemathy'
print(''.join([j for i,j in enumerate(a) if j not in a[:i]]))
