def cookie(arr):
    name = 'Zach' if type(arr) == str else 'Monica' if type(arr) == int or type(arr) == float else 'the dog'
    return f"Who ate the last cookie? It was {name}!"
print(cookie('Nawar'))