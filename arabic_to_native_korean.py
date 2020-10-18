from helpers import *

def arabic_to_native_korean(value):
    if value > 99 or value <= 0:
        print("Error: Native Korean number must be greater than 0 and less than 100.")
        return

    result = []
    decimal_index = 0
    native_numerals = ["", "하나", "둘", "셋", "넷", "다섯", "여섯", "일곱", "여덟", "아홉"]
    native_tens_place = ["", "열", "스물", "서른", "마흔", "쉰", "예순", "일흔", "여든", "아흔"]

    while True:
        current_decimal = get_decimal_place(value, 1)
        value = remove_decimal_place(value, 1)

        if decimal_index == 0:
            result.append(native_numerals[current_decimal])
        
        if decimal_index == 1:
            result.append(native_tens_place[current_decimal])


        decimal_index += 1

        if value == 0:
            break
    
    return "".join(result[::-1])

