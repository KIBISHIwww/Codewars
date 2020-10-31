def find_short(s):
    ans = []
    for i in s.split(' '):
        ans.append(len(i))
    return min(ans)
