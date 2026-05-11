​
def switcheroo(s):
    return ''.join('a' if x == 'b' else 'b' if x == 'a' else x for x in s)
print(switcheroo('aabacbaa'))
​