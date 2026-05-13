​
def solve(arr):
    new = []
    counter = 0
    for x in arr:
        for i, y in enumerate(x, 1):
            if i == ord(y.lower())-96:                
                counter += 1                                
        new.append(counter)
        counter = 0
    return new
print(solve(["abode","ABc","xyzD"]))