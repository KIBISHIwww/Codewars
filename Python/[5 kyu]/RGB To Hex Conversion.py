def rgb(r, g, b):
    valid_value = lambda x: min(max(x, 0), 255)
    return ("{:02X}" * 3).format(valid_value(r), valid_value(g), valid_value(b))
