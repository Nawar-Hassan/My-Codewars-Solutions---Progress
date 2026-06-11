def boredom(staff):
​
    dep = {'accounts': 1, 'finance': 2, 'canteen': 10, 'regulation': 3, 'trading': 6,
            'change': 6, 'IS': 8, 'retail': 5, 'cleaning': 4, 'pissing about': 25}
    
    new = sum(dep.get(x,0) for x in staff.values())
    
    return 'kill me now' if new <=80 else 'i can handle this' if new < 100 and new > 80 else 'party time!!'
    
​
print(boredom({
    "Alice": "accounts",
    "Bob": "finance",
    "Charlie": "canteen",
    "Diana": "regulation",
    "Evan": "trading",
    "Fiona": "change",
    "George": "IS",
    "Hannah": "retail",
    "Ian": "cleaning",
    "Jack": "pissing about",
​
    "Karen": "canteen",
    "Leo": "pissing about",