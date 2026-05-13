​
def show_sequence(n):
    return '{} = {}'.format('+'.join(str(x) for x in range(n+1)), sum(range(n+1))) if n > 0 else f'{n}=0' if n == 0 else f'{n}<0'
print(show_sequence(6))