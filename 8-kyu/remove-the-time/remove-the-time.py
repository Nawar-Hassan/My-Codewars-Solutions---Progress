​
def shorten_to_date(s):
    ind = s.find(", ")
    return s[:ind]
print(shorten_to_date("Friday May 2, 7pm"))