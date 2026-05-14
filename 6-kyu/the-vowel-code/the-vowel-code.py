def encode(s):
        return s.translate(str.maketrans("aeiou", "12345"))
def decode(s):
    return s.translate(str.maketrans("12345", "aeiou"))
print(encode('hello'))
print(decode('h2ll4'))