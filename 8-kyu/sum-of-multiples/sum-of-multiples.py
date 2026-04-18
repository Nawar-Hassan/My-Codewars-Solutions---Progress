def sum_mul(n, m): 
    return "INVALID" if n <= 0 or m <= 0 else sum(range(n, m, n))
print(sum_mul(4, 123))