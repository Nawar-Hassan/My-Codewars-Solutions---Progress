​
def same_case(c1, c2):
​
    if c1.isalpha() and c2.isalpha() and ((c1.isupper() and c2.isupper()) or (c1.islower() and c2.islower())):
        return 1 
    elif c1.isalpha() and c2.isalpha() and ((c1.isupper() and c2.islower()) or (c1.islower() and c2.isupper())):
        return 0
    else:
        return -1
print(same_case('B', 'c'))