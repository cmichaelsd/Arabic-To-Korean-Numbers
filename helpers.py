def remove_decimal_place(value, decimal_place):
    decimal_place *= 10
    difference = value - (value % decimal_place)
    result = difference / decimal_place
    return int(result)

def get_decimal_place(value, decimal_place):
    decimal_place *= 10
    return value % decimal_place
