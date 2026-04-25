​
def cube_checker(v,s):
    return 0 if (v <=0 or s <= 0) else True if s ** 3 == v  else False
print(cube_checker(0,0))