def binary_array_to_number(arr):
    return sum(map(lambda x: 2 ** x, [index for index, value in enumerate(arr[::-1]) if value == 1] ))
