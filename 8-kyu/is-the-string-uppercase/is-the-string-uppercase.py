def is_uppercase(s):
    
    letters = []   
    
    for x in s:
        if x.isalpha():
            letters.append(x)    
    if not letters:
        return True
    else:
        return ''.join(letters).isupper()
​
print(is_uppercase("AB0^"))