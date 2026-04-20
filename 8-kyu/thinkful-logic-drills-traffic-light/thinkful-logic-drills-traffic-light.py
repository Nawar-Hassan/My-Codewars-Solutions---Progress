def update_light(s):
    color_order = {"red": 1, "green": 2, "yellow": 3}    
    return next(k for k, v in color_order.items() if v == ((color_order.get(s) or 0) % len(color_order)) + 1)
print(update_light('Blue'))