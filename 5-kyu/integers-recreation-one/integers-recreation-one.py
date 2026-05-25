import math
​
def list_squared(m, n):
    
    result = []
​
    for k in range(m, n+1):
        total = 0
        root = int(math.sqrt(k))
​
        for d in range(1, root + 1):
            if k % d == 0:
                total += d*d
                other = k // d
                if other != d:
                    total += other*other
​
        if math.isqrt(total)**2 == total:
            result.append([k, total])
​
    return result 
​
print(list_squared(1, 250))