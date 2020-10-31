def string_task(s):
    ans = '.'.join(s.lower().translate(str.maketrans("", "", 'aeiouy')))
    return ('.'+ans if ans else ans)
