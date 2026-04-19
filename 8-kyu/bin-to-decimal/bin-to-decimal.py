​
def bin_to_decimal(bina):        
    return sum(int(x) * (2 ** i) for i, x in enumerate(bina[::-1]))
print(bin_to_decimal('1101'))