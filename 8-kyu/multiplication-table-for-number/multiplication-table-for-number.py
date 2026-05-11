​
def multi_table(n):
    return "\n".join(["{} * {} = {}".format(x, n, x * n) for x in range(1,11)])
print(multi_table(5))