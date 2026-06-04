def rev_rot(s, sz):  
        
    new = []    
    s_list = list(s)
    if not s or sz == 0:
        return ''
    else:
        while len(s_list[:sz]) == sz:
            new.append(''.join(s_list[:sz]))
            del s_list[:sz]
        result = [x[::-1] if (sum(int(d) for d in x)) % 2 == 0 else x[1:]+x[0] for x in new]
​
    return ''.join(result)
    
print(rev_rot("123456987654", 6))