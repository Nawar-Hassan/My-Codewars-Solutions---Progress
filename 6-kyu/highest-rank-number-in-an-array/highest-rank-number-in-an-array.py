def highest_rank(arr):
    highest = 0
    number = 0
    for x in arr:
        
        if arr.count(x) > highest:
            highest = arr.count(x)
            number = x
        elif arr.count(x) == highest and x > number:            
            number = x
        else:            
            number = number
    return number
print(highest_rank([3, 35, 21, 45, 29, 13, 50, 21, 17, 2, 37, 25, 33, 10, 42, 41, 45, 19, 37]))