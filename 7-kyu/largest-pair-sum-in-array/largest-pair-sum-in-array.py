​
def largest_pair_sum(arr):
    return max((arr[i] + arr[j]) for i in range(len(arr)) for j in range(i+1, len(arr)))
print(largest_pair_sum([99, 2, 2, 23, 19]))