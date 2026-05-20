def ordered_count(s):
    unique = []
    for x in s:
        if x not in unique:
            unique.append(x)
    return [(i, s.count(i)) for i in unique]
print(ordered_count("abracadabra"))