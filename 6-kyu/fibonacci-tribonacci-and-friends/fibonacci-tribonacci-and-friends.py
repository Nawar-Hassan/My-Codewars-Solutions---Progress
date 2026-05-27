def xbonacci(arr, n):
    new = arr[:]
    s   = len(arr)
    while len(new) < n:
        new.append(sum( new[-s:]))
    return new[:n]
print(xbonacci([1,1,1,1], 10))