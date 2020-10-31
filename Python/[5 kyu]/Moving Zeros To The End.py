def move_zeros(array):
    x, y = 0, 0
    while (y < len(array)):
        if not str(array[y]).isalpha() and array[y] == 0:
            y+=1
        else:
            temp = array[y]
            array[y] = array[x]
            array[x] = temp
            x+=1
            y+=1
    return array
