def remove_bmw(string):
    try:
        return string.translate(str.maketrans("", "", 'bmwBMW'))
    except AttributeError:
        raise TypeError("This program only works for text.")
