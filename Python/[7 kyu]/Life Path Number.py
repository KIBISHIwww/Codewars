def life_path_number(birthdate):
    birth = birthdate.split('-')
    ans = sum(int(x) for i in range(len(birth)) for x in birth[i])
    ans_f = 0
    while ans > 0:
        a = ans % 10
        ans_f+=a
        ans = ans // 10
    while ans_f > 0:
        a = ans_f % 10
        ans+=a
        ans_f = ans_f // 10
    return ans
