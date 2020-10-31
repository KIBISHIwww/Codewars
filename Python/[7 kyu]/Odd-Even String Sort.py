def sort_my_string(S):
    str = list(S)
    a = []
    b = []
    for i, v in enumerate(str):
        if (i % 2) == 0:
            a.append(str[i])
        else:
            b.append(str[i])
    return (''.join(a)+" "+''.join(b))
