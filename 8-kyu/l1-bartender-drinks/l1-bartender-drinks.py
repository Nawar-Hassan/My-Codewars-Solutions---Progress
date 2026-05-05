​
def get_drink_by_profession(s):
    menu = {"Jabroni": "Patron Tequila",
    "School Counselor": "Anything with Alcohol",
    "Programmer":   "Hipster Craft Beer",
    "Bike Gang Member": "Moonshine",
    "Politician":   "Your tax dollars",
    "Rapper":   "Cristal"}
    
    return menu.get(s.lower().title(),'Beer')
print(get_drink_by_profession("pOLitiCIaN"))