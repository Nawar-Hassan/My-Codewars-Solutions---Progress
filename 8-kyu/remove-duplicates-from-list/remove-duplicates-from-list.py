def distinct(s):
    distinct = [x for i, x in enumerate(s) if x not in s[:i]]
    return distinct
print(distinct([1, 2, 1, 1, 3, 2]))