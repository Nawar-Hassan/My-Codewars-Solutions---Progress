​
def correct(s):
    mistakes ={'5':'S', '1':'I', '0':'O'}
    return ''.join(mistakes.get(x,x) for x in s)
print(correct('5orry 1 0we You'))