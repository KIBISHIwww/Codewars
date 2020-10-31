def clean_string(s):
    ans = []
    for i in s:
        if i != '#':
            ans.append(i)
        elif ans:
            ans.pop()
    return "".join(ans)
