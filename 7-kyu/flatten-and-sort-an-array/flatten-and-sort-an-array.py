​
def flatten_and_sort(arr):
    return sorted(sum(arr, []))
print(flatten_and_sort( [[3, 2, 1], [4, 6, 5], [], [9, 7, 8]]))