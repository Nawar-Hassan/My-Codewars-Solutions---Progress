def filter_string(s):
    return int([''.join(x for x in s if x in '0123456789')][0])
print(filter_string('n1a2w3r4'))