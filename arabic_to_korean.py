class ArabicToKorean:
    def __init__(self, value):
        self.value = value
        # counter from zero is used to tell how many
        # decimal places from the last special character
        # or 1s place
        self.counter_from_zero = 0
        # non-repeating special characters which change every 4
        # decimal places from last special character
        # or 1s place
        self.special_decimal_place = {
            0: "",
            4: "만",
            8: "억",
        }
        # korean numbers
        self.numerals = {
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
        }
        # special postfix characters based on
        # distance from last special character
        # or 1s place
        self.decimal_places_from_zero = {
            1: "십",
            2: "백",
            3: "천"
        }
        print(self.conversion())

    def handle_counter_from_zero(self) -> None:
        if self.counter_from_zero == 4:
            # If true, reset
            self.counter_from_zero = 1
        else:
            # Otherwise increment
            self.counter_from_zero += 1

    def handle_special_character(self, special_char, c) -> str:
        if c > "1":
            # Add special character and current
            return special_char + self.numerals[c]
        elif c == "1":
            # Add only special character, its implied to be 1
            return special_char
        else:
            # If zero return blank
            return ""

    def conversion(self) -> str:
        # will return output string reversed
        output = ""
        for i, c in enumerate(self.value[::-1]):
            # 1)
            # If counter from zero is greater than zero
            # And if the counter is not a multiple of 4
            if self.counter_from_zero > 0 and self.counter_from_zero % 4 != 0:
                # Append character for decimal place after 0
                postfix = self.decimal_places_from_zero[self.counter_from_zero]
                output += self.handle_special_character(postfix, c)

            # 2)
            # If index is a multiple of 4
            if i % 4 == 0:
                # If the index is 0
                if i == 0:
                    # If first number is 0 see how many times 0 repeats
                    if c == "0":
                        # If all elements are zero
                        zero_count_is_len = self.value.count("0") == len(self.value)
                        output += self.numerals[c] if zero_count_is_len else ""
                    else:
                        # If the number is not zero
                        # Add the number
                        output += self.numerals[c]
                else:
                    # Otherwise get special character for decimal place
                    special_character = self.special_decimal_place[i]
                    output += self.handle_special_character(special_character, c)

            # At the end of the logic see if the counter is currently 4
            self.handle_counter_from_zero()

        return output[::-1]


ArabicToKorean("3524761") # 삼백오십이만사천칠백육십일
ArabicToKorean("0000") # 공
ArabicToKorean("1212") # 백이십이
ArabicToKorean("1000") # 천
ArabicToKorean("1") # 일
ArabicToKorean("10") # 십
ArabicToKorean("50") # 오십
