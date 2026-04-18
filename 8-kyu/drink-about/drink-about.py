​
def people_with_age_drink(age):
    match age:
        case a if a < 14: return "drink toddy"
        case a if a < 18: return "drink coke"
        case a if a < 21: return "drink beer"
        case _: return "drink whisky"
print(people_with_age_drink(18))