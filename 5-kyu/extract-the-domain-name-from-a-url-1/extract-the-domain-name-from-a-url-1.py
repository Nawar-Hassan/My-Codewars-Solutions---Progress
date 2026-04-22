def domain_name(s):
    
    if s.count('.') == 1 and s.count(':') == 1:
        return (s.replace('/','!').replace('.','!').replace('!!','!')).split('!')[1]
    elif s.count('.') == 1 and s.count(':') == 0:
        return s.split('.')[0]
    elif s.count('.') > 1 and s.count(':') == 1 and s.count('www.')== 1:
        return (s.replace('www.','!').replace('.','!').replace('!!','!').replace('!!!','!')).split('!')[1]
    elif s.count('.') > 1 and s.count(':') == 1:
        return (s.replace('/','!').replace('.','!').replace('!!','!')).split('!')[1]  
    elif s.count('//') == 0 and s.count('www.') == 0:
        return (s.replace('/','!').replace('.','!').replace('!!','!')).split('!')[0]  
    else:
        return s.replace('.','!').split('!')[1]
​
print(domain_name("3jn9n4kvb4sj5a4mwg5uxk00oc5bh.co.uk/users"))