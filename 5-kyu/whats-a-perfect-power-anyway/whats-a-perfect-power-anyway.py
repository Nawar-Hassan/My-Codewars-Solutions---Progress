def isPP(n):
    
    for i in range(2, int(n ** 0.5) + 1):
        power = i * i
        j = 2
       
        while power <= n:
            if power == n:
                return [i, j]
            j += 1
            power *= i  
    return None
print(isPP(81))