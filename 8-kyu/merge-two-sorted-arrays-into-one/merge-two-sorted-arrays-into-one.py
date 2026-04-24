def merge_arrays(a1,a2):
    return list(sorted(set(a1+a2)))
print(merge_arrays([1, 3, 5, 7, 9, 11, 12], [1, 2, 3, 4, 5, 10, 12]))