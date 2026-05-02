​
def is_sorted_and_how(arr):
    asc = []
    des = []
    equ = []
    for i in range(len(arr)-1):
        if arr[i] < arr[i+1]:
            asc.append(i)
        elif arr[i] > arr[i+1]:
            des.append(i)
        else:  # arr[i] == arr[i+1]
            equ.append(i)
    
    if len(des) == 0:   
        return "yes, ascending"
    elif len(asc) == 0: 
        return "yes, descending"
    else:
        return "no"
print(is_sorted_and_how([1,1, 1, 1, 1, 2, 1]))
​