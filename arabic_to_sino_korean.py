from helpers import *

def arabic_to_sino_korean(value):
    if value > 999999999999:
        print("Error: Sino-Korean number must be less than 999,999,999,999.")
        return

    result = ""
    decimal_index = 0
    sino_numerals = ["공", "일", "이", "삼", "사", "오", "육", "칠", "팔", "구"]
    sino_ten_thousands_place = { 0: "", 4: "만", 8: "억" }
    sino_decimal_place = { 1: "십", 2: "백", 3: "천" }

    if value == 0: return sino_numerals[value]

    while True:
        current_decimal = get_decimal_place(value, 1)
        value = remove_decimal_place(value, 1)

        if decimal_index % 4 == 0:
            result += sino_ten_thousands_place[decimal_index]
            
        elif decimal_index > 0 and current_decimal > 0:
            result += sino_decimal_place[decimal_index % 4]

        if current_decimal > 1 or (current_decimal > 0 and decimal_index == 0):   
            result += sino_numerals[current_decimal]

        decimal_index += 1

        if value == 0:
            break
    
    return result[::-1]
