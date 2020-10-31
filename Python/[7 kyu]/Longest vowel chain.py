import re
from collections import Counter
def solve(s):
    str = re.sub('[^aeiou]',' ',s)
    c = 0
    ans = []
    for i, v in enumerate(str):
        if v != ' ':
            c+=1
            ans.append(c)
        else:
            c = 0
            ans.append(c)
    return max(ans)
