​
def sum_of_minimums(arr):   
    return sum(min(x) for x in arr)
print(sum_of_minimums([[ 1, 2, 3, 4, 5 ], [ 5, 6, 7, 8, 9 ], [ 20, 21, 34, 56, 100 ]]))