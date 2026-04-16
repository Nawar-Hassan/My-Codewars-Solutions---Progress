​
def round_to_next5(num):
    if num % 5 == 0:
        return num
    return ((num // 5) + 1) * 5
print(round_to_next5(1))