​
def solve(s):
    return s.upper() if sum(c.isupper() for c in s) > sum(c.islower() for c in s) else s.lower()
print(solve("COde"))