def power_of_two(n):
    result = n
    while result > 1:
        if result % 2 != 0:
            return False
        result //= 2
    return result == 1
print(power_of_two(4096))