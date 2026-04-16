​
def remove_url_anchor(s):
    check = s.find('#')
    return s[:check] if check !=-1 else s
print(remove_url_anchor("www.codewars.com!about"))