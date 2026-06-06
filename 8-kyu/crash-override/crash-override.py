from preloaded import FIRST_NAME, SURNAME
​
def alias_gen(f_name: str, l_name: str) -> str:
​
    if f_name[0].isalpha() and l_name[0].isalpha():
        return '{} {}'.format(FIRST_NAME[f_name.upper()[0]] , SURNAME[l_name.upper()[0]])
    else:
        return "Your name must start with a letter from A - Z."
print(alias_gen('Nawar', 'Hassan'))