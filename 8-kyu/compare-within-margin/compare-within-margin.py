def close_compare(a, b, margin = 0):
    return 0 if margin >= abs(a-b) and margin >=0 else -1 if a < b else 1
print(close_compare(3, 5, 0))