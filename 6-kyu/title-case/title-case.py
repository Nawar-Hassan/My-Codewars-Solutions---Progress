def title_case(text, minor=''):
    if not text:
        return ""
​
    words = text.lower().split()
​
    minor_words = set(minor.lower().split())
 
    res = [words[0].capitalize()]
​
    for word in words[1:]:
        if word in minor_words:
            res.append(word)
        else:
            res.append(word.capitalize())
​
    return " ".join(res)
print(title_case('THE WIND IN THE WILLOWS', 'The In'))