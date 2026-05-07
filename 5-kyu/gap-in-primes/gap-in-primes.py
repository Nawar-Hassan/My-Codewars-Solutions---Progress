def is_prime(x):
    if x < 2:
        return False
    if x % 2 == 0:
        return x == 2
    for i in range(3, int(x**0.5) + 1, 2):
        if x % i == 0:
            return False
    return True
​
def gap(g, m, n):
    prev = None
    for i in range(m, n+1):
        if is_prime(i):
            if prev and i - prev == g:
                return [prev, i]   # return the first pair only
            prev = i
    return None   # if no pair found