​
def final_grade(g, n):
    return 100 if g > 90 or n > 10 else 90 if g > 75 and n >=5 else 75 if g > 50 and n >=2 else 0
print(final_grade(5, 0))
​