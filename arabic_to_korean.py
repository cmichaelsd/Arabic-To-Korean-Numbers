from typing import Any

class ArabicToKorean:
    def __new__(cls, value, sino = True) -> str:
        instance = super(ArabicToKorean, cls).__new__(cls)
        instance.__init__(value, sino)
        if sino:
            return instance.__sino_conversion()
        else:
            return instance.__native_conversion()

    def __init__(self, value, sino) -> None:
        self.value = value
        # counter from zero is used to tell how many
        # decimal places from the last special character
        # or 1s place
        self.__counter_from_zero = 0
        self.__s = {
            # non-repeating special characters which change every 4
            # decimal places from last special character
            # or 1s place
            "special_decimal_place": {
                0: "",
                4: "만",
                8: "억",
            },
            # korean numbers
            "numerals": {
                "0": "공",
                "1": "일",
                "2": "이",
                "3": "삼",
                "4": "사",
                "5": "오",
                "6": "육",
                "7": "칠",
                "8": "팔",
                "9": "구"
            },
            # special postfix characters based on
            # distance from last special character
            # or 1s place
            "decimal_places_from_zero": {
                1: "십",
                2: "백",
                3: "천"
            }
        }

        self.__n = {
            "tens": {
                "1": "열",
                "2": "스물",
                "3": "서른",
                "4": "마흔",
                "5": "쉰",
                "6": "예순",
                "7": "일흔",
                "8": "여든",
                "9": "아흔"
            },
            "numerals": {
                "0": "",
                "1": "하나",
                "2": "둘",
                "3": "셋",
                "4": "넷",
                "5": "다섯",
                "6": "여섯",
                "7": "일곱",
                "8": "여덟",
                "9": "아홉"
            }
        }

    @property
    def counter_from_zero(self) -> int:
        return self.__counter_from_zero

    @counter_from_zero.setter
    def counter_from_zero(self, value) -> None:
        self.__counter_from_zero = value

    @counter_from_zero.deleter
    def counter_from_zero(self, value) -> None:
        self.__counter_from_zero = value

    @property
    def s(self) -> Any:
        return self.__s

    @property
    def n(self) -> Any:
        return self.__n

    def __handle_counter_from_zero(self) -> None:
        if self.counter_from_zero == 4:
            # If true, reset
            self.counter_from_zero = 1
        else:
            # Otherwise increment
            self.counter_from_zero += 1

    def __handle_special_character(self, special_char, c) -> str:
        if c > "1":
            # Add special character and current
            return special_char + self.s["numerals"][c]
        elif c == "1":
            # Add only special character, its implied to be 1
            return special_char
        else:
            # If zero return blank
            return ""

    def __sino_conversion(self) -> str:
        # Number must be less than 999,999,999,999
        if int(self.value) > 999999999999:
            print("Error: Sino-Korean number must be less than 999,999,999,999.")
            return "$"
        # Will return output string reversed
        output = ""
        for i, c in enumerate(self.value[::-1]):
            # 1)
            # If counter from zero is greater than zero
            # And if the counter is not a multiple of 4
            if self.counter_from_zero > 0 and self.counter_from_zero % 4 != 0:
                # Append character for decimal place after 0
                postfix = self.s["decimal_places_from_zero"][self.counter_from_zero]
                output += self.__handle_special_character(postfix, c)

            # 2)
            # If index is a multiple of 4
            if i % 4 == 0:
                # If the index is 0
                if i == 0:
                    # If first number is 0 see how many times 0 repeats
                    if c == "0":
                        # If all elements are zero
                        zero_count_is_len = self.value.count("0") == len(self.value)
                        output += self.s["numerals"][c] if zero_count_is_len else ""
                    else:
                        # If the number is not zero
                        # Add the number
                        output += self.s["numerals"][c]
                else:
                    # Otherwise get special character for decimal place
                    special_character = self.s["special_decimal_place"][i]
                    output += self.__handle_special_character(special_character, c)

            # At the end of the logic see if the counter is currently 4
            self.__handle_counter_from_zero()

        return output[::-1]
    
    def __native_conversion(self) -> str:
        # Number must be less than 99
        if int(self.value) > 99:
            print("Error: Native Korean number must be less than 99.")
            return "$"
        elif int(self.value) == 0:
            print("Error: Native Korean number must be greater than 0.")
            return "$"
        output = []
        for i, c in enumerate(self.value[::-1]):
            if i == 0:
                output.append(self.n["numerals"][c])
            else:
                output.append(self.n["tens"][c])
                

        return "".join(output[::-1])
