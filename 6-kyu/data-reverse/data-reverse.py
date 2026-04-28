​
def data_reverse(arr):
    if len(arr) % 8 == 0:
        copy = arr[:]
        new = []    
        while copy:
            new.append(copy[0:8])    
            del copy[0:8]        
    return sum(new[::-1], []) 
print(data_reverse([1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]))