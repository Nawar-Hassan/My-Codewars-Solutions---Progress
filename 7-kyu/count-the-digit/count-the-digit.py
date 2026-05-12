def nb_dig(n, d):
    digits = [x*x for x in range(n+1)]    
    d_list = []
​
    for x in digits:
        if str(d) in str(x):
            d_list.append(str(x))
    return ''.join(d_list).count(str(d))
print(nb_dig(25, 1))