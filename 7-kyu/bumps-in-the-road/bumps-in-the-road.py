def bumps(s):
    return 'Woohoo!' if s.count('n') <= 15 else 'Car Dead'
print(bumps('__n_n__nnnnnn_n_n_n___nnnn_n'))