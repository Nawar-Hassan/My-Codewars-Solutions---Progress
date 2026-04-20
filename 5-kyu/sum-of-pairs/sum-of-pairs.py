​
def sum_pairs(arr, n):
    seen = set()
    for x in arr:
        target = n - x
        if target in seen:
            return [target, x]
        seen.add(x)
    return None
print(sum_pairs([10, 5, 2, 3, 7, 5], 10))