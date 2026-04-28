def pillars(n, d, w):
    return (n - 1) * (d * 100) + (n-2) * w if n > 1 else 0
print(pillars(4, 25, 100))