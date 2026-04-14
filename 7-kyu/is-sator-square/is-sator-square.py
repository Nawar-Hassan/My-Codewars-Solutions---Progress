def is_sator_square(arr):   
    
    transposed = [list(row) for row in zip(*arr)]    
    reversed_rows = [row[::-1] for row in arr]
    inverted_rows = arr[::-1]    
    rot_180 = [row[::-1] for row in arr[::-1]]
    return arr == transposed == rot_180 == [list(row) for row in zip(*rot_180)]
    
print(is_sator_square([["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]))