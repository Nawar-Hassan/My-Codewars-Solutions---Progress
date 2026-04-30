def mix(s1, s2):
     
    check_1 = []
    check_2 = []
    mixed   = []
    for x in s1:
        if x.islower() and x.isalpha() and s1.count(x) > 1 :
            check_1.append(x)
    for y in s2:
        if y.islower() and y.isalpha() and s2.count(y) > 1 :
            check_2.append(y)
    alpha   = ''.join(sorted(set(check_1 + check_2)))
​
    abbr_1 = ''.join(sorted(check_1))
    abbr_2 = ''.join(sorted(check_2))
​
    for x in alpha:
        if abbr_1.count(x) > abbr_2.count(x):
            mixed.append('1:'+ x*abbr_1.count(x))
        elif abbr_1.count(x) < abbr_2.count(x):
            mixed.append('2:'+ x*abbr_2.count(x))
        else:
            mixed.append('=:'+ x*abbr_2.count(x))
    
    return '/'.join(sorted(mixed,key=lambda x: (-len(x), x)))
print(mix("my&friend&Paul has heavy hats! &", "my friend John has many many friends &"))