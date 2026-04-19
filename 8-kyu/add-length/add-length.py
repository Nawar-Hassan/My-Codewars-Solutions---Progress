​
def add_length(s):
    return [x+ ' ' + str(len(x)) for x in s.split()]
print(add_length("you will win"))