def string_clean(s):
    return ''.join(x.replace(x,'') if x in ['0','1','2','3','4','5','6','7','8','9'] else x for x in s)
print(string_clean('This looks5 grea8t!'))