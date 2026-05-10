def partlist(arr):   
    return [(" ".join(arr[:i])," ".join(arr[i:])) for i in range(1, len(arr))]        
print(partlist(["az", "toto", "picaro", "zone", "kiwi"]))