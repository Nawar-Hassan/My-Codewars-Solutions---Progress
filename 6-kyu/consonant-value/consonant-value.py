​
import string
def solve(s):
​
    alpha = {char: str(i + 1) for i, char in enumerate(string.ascii_lowercase)}    
    vowels = 'aeiou'
    
    new= []
    to_num = []
​
    for x in s:
        if x not in vowels:
            new.append(x)
        else:
            new.append(' ')
    new_1 = ''.join(new).split(' ')
   
    for x in new_1:
        # sum each substring separately
        subtotal = sum(int(alpha[ch]) for ch in x)
        to_num.append(subtotal)
​
    return max(to_num)        
    
print(solve("strength"))
​