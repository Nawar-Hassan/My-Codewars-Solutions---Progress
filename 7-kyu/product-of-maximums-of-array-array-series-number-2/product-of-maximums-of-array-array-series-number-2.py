import math
def max_product(arr, k):
    return math.prod(sorted(arr)[::-1][:k])
print(max_product([10, 8, 3, 2, 1, 4, 10], 5))