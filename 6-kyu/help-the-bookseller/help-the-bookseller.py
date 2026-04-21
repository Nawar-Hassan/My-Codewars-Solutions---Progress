​
def stock_list(listOfArt, listOfCat):
    if not listOfArt or not listOfCat:
        return ""
​
    totals = {}
    for cat in listOfCat:
        totals[cat] = 0
​
    for art in listOfArt:
        code, qty = art.split()
        if code[0] in totals:
            totals[code[0]] += int(qty)
​
    return " - ".join(f"({c} : {totals[c]})" for c in listOfCat)
​
print(stock_list(["ABART 20", "CDXEF 50", "BKWRK 100", "BTSQZ 1000", "DRTYM 60"], ["A", "B", "C", "W"]))