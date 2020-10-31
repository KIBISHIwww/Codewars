def what_century(year):
    cen = ((int(year)+99)//100)
    return str(cen) + ("th" if cen < 20 else {1: "st", 2: "nd", 3: "rd"}.get(cen % 10, "th"))
