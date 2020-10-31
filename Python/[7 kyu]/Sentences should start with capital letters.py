def fix(paragraph):
    return '. '.join(s.capitalize() for s in paragraph.split('. '))
