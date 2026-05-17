def max_diff(arr):
    return max(arr) - min(arr) if len(arr) > 1 else 0
print(max_diff([1, 2, 3, -4]))