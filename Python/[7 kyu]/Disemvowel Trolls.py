def disemvowel(string):
    #return [v for i, v in enumerate(list(string)) if v != 'a' and v != 'A' and v != 'e' and v != 'E' and v != 'i' and v != 'I' and v != 'o' and v != 'O' and v != 'u' and v != 'U']
    for i in "aeiouAEIOU":
        string = string.replace(i,"")
    return string
