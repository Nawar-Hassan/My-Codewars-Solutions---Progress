def array(s):
    parts = s.replace(',', ' ').split()
    return ' '.join(parts[1:-1]) if len(parts) > 2 else None
​
print(array("1 2 3 4 5"))