​
import math
def find_difference(a,b):
    return abs(math.prod(a) - math.prod(b))
print(find_difference([2, 2, 3], [5, 4, 1]))