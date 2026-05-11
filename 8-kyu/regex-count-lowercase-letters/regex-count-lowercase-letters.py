​
def lowercase_count(s):
    
    counter = 0
    for x in s:
        if x.islower():
            counter += 1
    return counter
print(lowercase_count("by,0:y,>*c!C"))