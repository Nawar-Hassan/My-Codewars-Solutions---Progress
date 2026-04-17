​
def sum_digits(num):   
    return sum(int(x) for x in list(str(abs(num))))
print(sum_digits(-99))