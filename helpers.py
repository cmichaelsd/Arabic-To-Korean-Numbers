def remove_decimal_place(value, tensPower):
    difference = value - get_decimal_place(value, tensPower)
    result = difference / (10 ** tensPower)
    return int(result)

def get_decimal_place(value, tensPower):
    return value % (10 ** tensPower)
