def get_size(l, w, h):
    calc = [2*(l*w + l*h + w*h), l*w*h]  
    return calc
print(get_size(10,10,10))