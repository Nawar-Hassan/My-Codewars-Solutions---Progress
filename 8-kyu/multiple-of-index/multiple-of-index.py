def multiple_of_index(arr):
    return [x for i, x in enumerate(arr) if i != 0 and x % i == 0 or x == 0]
print(multiple_of_index([0, -95, -20, 13, 34, 68, 50, 70, 80, 59]))