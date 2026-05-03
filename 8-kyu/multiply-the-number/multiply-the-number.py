​
def multiply(num):
    return num * (5 ** len(str(num).lstrip('-')))
print(multiply(10))