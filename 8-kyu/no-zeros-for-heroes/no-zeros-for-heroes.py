def no_boring_zeros(n):
    if not str(n).endswith('0'):
        return n    
    elif not n:
        return 0
    return int(no_boring_zeros(str(n)[0:-1]))
print(no_boring_zeros(-3045000000))