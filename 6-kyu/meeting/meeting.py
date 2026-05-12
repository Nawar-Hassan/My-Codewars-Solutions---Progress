def meeting(s):
    new = []
    for x in s.split(';'):
        new.append(x.replace(':',', ').upper())
    tuples = sorted([tuple(n.split(", ")[::-1]) for n in new],key=lambda t: (t[0], t[1]))
    return "".join(f"({t[0]}, {t[1]})" for t in tuples)
print(meeting("Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill"))