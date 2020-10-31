def name_value(s):
    return [sum(ord(c) - 96 for c in s[i] if c != ' ') * (i + 1) for i in range(0,len(s))]
