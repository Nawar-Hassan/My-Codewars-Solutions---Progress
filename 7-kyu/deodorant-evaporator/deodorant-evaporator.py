def evaporator(content, evap_per_day, threshold):
​
    min     = content * threshold / 100 
    balance = content    
    days    = 0
​
    while balance >= min:
        balance -= balance * (evap_per_day/100)
        days += 1
    
    return days
print(evaporator(10,10,5))