def max_rot(n): 
    s = str(n)
    max_num = n
    for i in range(len(s)):
        s = s[:i] + s[i+1:] + s[i]
        max_num = max(max_num, int(s))
    return max_num
print(max_rot(56789))