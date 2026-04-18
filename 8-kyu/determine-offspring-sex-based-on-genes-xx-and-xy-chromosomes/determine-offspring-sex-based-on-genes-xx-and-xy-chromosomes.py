def chromosome_check(chromosome):
    
    if chromosome == "XX":
        return "Congratulations! You're going to have a daughter."
    else:  # chromosome == "XY"
        return "Congratulations! You're going to have a son."
print(chromosome_check("XX"))
print(chromosome_check("XY"))