def reverse(arr):
    result = list()
    for x in arr:
        result.insert(0, x)
    return result
print(reverse(['r', 'e', 'v', 'e', 'r', 's', 'e']))