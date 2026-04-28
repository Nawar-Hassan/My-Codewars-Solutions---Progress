import math
def predict_age(*args):
    return math.sqrt(sum(x ** 2 for x in args))//2
print(predict_age(65, 60, 75, 55, 60, 63, 64, 45))