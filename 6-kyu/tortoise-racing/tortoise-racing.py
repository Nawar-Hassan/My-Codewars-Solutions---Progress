def race(v1, v2, g):
    if v1 >= v2:
        return None
​
    # total time in seconds
    total_seconds = g * 3600 // (v2 - v1)
​
    h, rem = divmod(total_seconds, 3600)
    m, s = divmod(rem, 60)
​
    return [h, m, s]