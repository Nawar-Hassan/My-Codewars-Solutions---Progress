def whatday(n):
    weekdays  = {   1: "Sunday",
                    2: "Monday",
                    3: "Tuesday",
                    4: "Wednesday",
                    5: "Thursday",
                    6: "Friday",
                    7: "Saturday"
                    }
    if n in weekdays:
        return weekdays[n]
    else:
        return "Wrong, please enter a number between 1 and 7"
print(whatday(3))