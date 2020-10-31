def namelist(names):
    namelist =  [i['name'] for i in names]
    if len(namelist) <= 1:
        return ''.join(namelist)
    else:
        lastTwo = ' & '.join(namelist[-2:])
        first = [n + ',' for n in namelist[:-2]]
        first.append(lastTwo)
        return ' '.join(first)

    3 hours ago
