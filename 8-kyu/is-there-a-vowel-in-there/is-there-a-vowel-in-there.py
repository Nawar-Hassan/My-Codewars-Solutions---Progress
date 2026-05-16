​
def is_vow(s):
    v = ['a', 'e', 'i', 'o', 'u']
    return [x if x not in (ord(j) for j in v) else ''.join(j for j in v if x == ord(j)) for x in s]    
print(is_vow([100,100,116,105,117,121]))