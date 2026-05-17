​
def solve(arr):
    return list(dict.fromkeys(arr[::-1]))[::-1]       
print(solve([3, 4, 4, 3, 6, 3]))