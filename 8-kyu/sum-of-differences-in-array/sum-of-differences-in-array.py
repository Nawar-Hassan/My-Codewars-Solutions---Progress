​
def sum_of_differences(arr):
 
    result = 0
    asc = sorted(arr, reverse=True)
    if arr or len(arr) > 1:
        for i in range(len(asc)-1):
            result += asc[i]-asc[i+1]
    else:
        return 0
    return result
print(sum_of_differences([2, 1, 10]))