​
def find_even_index(arr):    
    matches = [i for i in range(len(arr)) if sum(arr[:i]) == sum(arr[i+1:])]
    return matches[0] if matches else -1
print(find_even_index([1,2,3,4,3,2,1]))