def adjacent_element_product(arr):    
    return max(arr[i] * arr[i+1] for i in range(len(arr)-1) if len(arr) >= 2)
print(adjacent_element_product([-23, 4, -5, 99, -27, 329, -2, 7, -921]))