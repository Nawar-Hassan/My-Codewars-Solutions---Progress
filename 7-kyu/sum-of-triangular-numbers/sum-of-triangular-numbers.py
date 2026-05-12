​
def sum_triangular_numbers(n):
    tn = []
    for x in range(1,n+1):
        current= x + sum(range(n+1)[:x])
        tn.append(current)
    return sum(tn)
print(sum_triangular_numbers(4))