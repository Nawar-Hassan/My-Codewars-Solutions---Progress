from datetime import datetime
​
def check_coupon(ec,cc,d1: str,d2: str)-> bool:    
    return  True if (ec== cc and type(ec) == type(cc)) and datetime.strptime(d1, "%B %d, %Y") <= datetime.strptime(d2, "%B %d, %Y") else False
print(check_coupon("123", "123", "July 9, 2015", "July 2, 2015"))