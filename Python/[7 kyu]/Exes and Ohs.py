def xo(s):
    ans_o, ans_x = 0, 0
    for i in s:
        if i == 'o' or i == 'O':
            ans_o+=1
        elif i == 'x' or i == 'X':
            ans_x+=1
    return True if ans_o == ans_x or (ans_o == 0 and ans_x == 0) else False
