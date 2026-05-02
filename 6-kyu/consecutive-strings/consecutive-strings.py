​
def longest_consec(arr, k):  
​
    if len(arr) == 0 or len(arr) < k or k <= 0:
        return ''
    else:
        copy = arr[:]
        new = []
            
        while len(copy) >= k:
            new.append(''.join(copy[0:k]))    
            del copy[0] 
        
        return [x for x in new if len(x) == max(len(x) for x in new)][0]
     
print(longest_consec(["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"], 2))