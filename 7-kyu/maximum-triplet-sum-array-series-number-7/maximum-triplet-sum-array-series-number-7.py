​
def max_tri_sum(arr):
    new = set(arr)
    return sum(sorted(new)[-3:])
print(max_tri_sum([2,1,8,0,6,4,8,6,2,4]))