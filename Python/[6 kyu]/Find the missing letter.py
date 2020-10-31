def find_missing_letter(chars):
    s = [ord(c) for c in chars]
    return next(chr(i) for i in range(min(s),max(s)) if i not in s)
