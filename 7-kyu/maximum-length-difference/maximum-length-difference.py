​
def mxdiflg(a1, a2):
    if not a1 or not a2:
        return -1
    max_a1 = max(len(x) for x in a1)
    min_a1 = min(len(x) for x in a1)
    max_a2 = max(len(y) for y in a2)
    min_a2 = min(len(y) for y in a2)
    
    return max(abs(max_a1 - min_a2), abs(max_a2 - min_a1))
​
print(mxdiflg(["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"],
                                 ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]))