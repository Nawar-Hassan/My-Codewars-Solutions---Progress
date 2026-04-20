def human_years_cat_years_dog_years(n):
    return [
        n,
        15 if n == 1 else 24 if n == 2 else (n - 2) * 4 + 24,
        15 if n == 1 else 24 if n == 2 else (n - 2) * 5 + 24
    ]
​
print(human_years_cat_years_dog_years(3))