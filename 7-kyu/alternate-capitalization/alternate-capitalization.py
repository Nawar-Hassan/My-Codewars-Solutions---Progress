def capitalize(s):
    new =[]
    new.append(''.join(x.capitalize() if i % 2 == 0 else x for i, x in enumerate(s)))
    new.append(''.join(x.capitalize() if i % 2 != 0 else x for i, x in enumerate(s)))
    return new
print(capitalize("abcdef"))