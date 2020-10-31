def maskify(cc):
    c = list(cc)
    if len(c) <= 4:
        return (''.join(c))
    else:
        return (((int(len(c))-4)*"#")+''.join(c[-4::1]))
