def uefa_euro_2016(arr1, arr2):
    return f"At match {' - '.join(arr1)}, {arr1[0] if arr2[0] > arr2[1] else arr1[1]} won!" if arr2[0] != arr2[1] else  f"At match {' - '.join(arr1)}, teams played draw."
print(uefa_euro_2016(['Germany', 'Ukraine'],[2, 2]))