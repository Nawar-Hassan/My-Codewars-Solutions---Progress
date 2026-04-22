​
def derive(a, b):
    return "{}x^{}".format(a*b, b-1) if a > 0 and b > 1 else 0
print(derive(5, 9))