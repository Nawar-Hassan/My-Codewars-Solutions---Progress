​
def sort_my_string(s):
    return '{} {}'.format(''.join(e for i, e in enumerate(s) if i % 2 == 0), ''.join(e for i, e in enumerate(s) if i % 2 != 0))
print(sort_my_string("CodeWars"))