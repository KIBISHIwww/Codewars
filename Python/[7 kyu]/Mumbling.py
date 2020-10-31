def accum(s):
    return '-'.join((i * v).title() for i, v in enumerate(s, 1))
