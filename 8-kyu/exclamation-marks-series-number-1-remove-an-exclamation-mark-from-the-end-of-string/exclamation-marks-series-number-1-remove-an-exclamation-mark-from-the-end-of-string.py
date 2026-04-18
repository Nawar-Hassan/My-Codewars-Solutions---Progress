​
def remove(s):
    return  s[0:-1] if s.endswith('!') else s
print(remove("!Hello World!!!!!"))