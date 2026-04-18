​
def min_value(arr):
    return int(''.join(str(x) for x in sorted(set(arr))))
print(min_value([1, 9, 3, 1, 7, 4, 6, 6, 7]))