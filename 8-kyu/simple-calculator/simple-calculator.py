def calculator(n1, n2, sign):
    if str(n1).isdigit() and str(n2).isdigit():
        if sign == '+':
            return n1 + n2
        elif sign == '-':
            return n1 - n2
        elif sign == '*':
            return n1 * n2
        elif sign == '/':
            return n1 / n2
        else:
            return "unknown value" 
    else:
        return "unknown value" 
print(calculator(2, 2, '//'))