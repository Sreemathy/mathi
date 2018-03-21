def lexicographi_sort(a):
    return sorted(sorted(a), key=str.upper)

print(lexicographi_sort('sreemathy'))
print(lexicographi_sort('kavi'))
