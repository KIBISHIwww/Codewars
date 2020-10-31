def least_larger(a, i): 
    ans = []
    [ans.append(x) for x in a if x > a[i]]
    return -1 if len(ans) == 0 else a.index(min(ans))
