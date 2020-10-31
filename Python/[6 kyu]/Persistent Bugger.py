from functools import reduce
def persistence(n):
    count = 0
    while len(str(n)) > 1:
        count+=1
        n = reduce(lambda x,y:x*y,[int(x) for x in str(n)])
    return count
