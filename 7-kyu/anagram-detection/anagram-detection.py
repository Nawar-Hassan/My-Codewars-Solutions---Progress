def is_anagram(s1, s2):
    return True if sorted(s1.lower()) == sorted(s2.lower()) else False
print(is_anagram("Nawar", "rawan"))