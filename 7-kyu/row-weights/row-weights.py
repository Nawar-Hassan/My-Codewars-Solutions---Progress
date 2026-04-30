def row_weights(arr):
​
    row_1 = 0
    row_2 = 0
​
    for i, x in enumerate(arr):
        if i % 2 == 0:
            row_1 += x
        else:
            row_2 += x
​
    return (row_1, row_2)
​
print(row_weights([50, 60, 70, 80]))