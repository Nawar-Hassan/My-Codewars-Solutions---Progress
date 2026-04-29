def encrypt_this(s):
    words = s.split()
    result = []
    for w in words:
        if len(w) == 1:
            result.append(str(ord(w[0])))
        elif len(w) == 2:
            result.append(str(ord(w[0])) + w[1])
        else:
            result.append(str(ord(w[0])) + w[-1] + w[2:-1] + w[1])
    return " ".join(result)