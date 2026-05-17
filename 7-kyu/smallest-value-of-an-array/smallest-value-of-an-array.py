​
def find_smallest(arr, s):
    return min(arr) if s =='value' and len(arr) >=1 else arr.index(min(arr)) if s =='index' and len(arr) >=1 else 0
print(find_smallest([], "index"))