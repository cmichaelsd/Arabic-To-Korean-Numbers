from arabic_to_sino_korean import arabic_to_sino_korean

def to_equal(result, expect):
    if expect == result:
        print("Passed")
    else:
        print(f"Failed: expected {expect}, result {result}.")
    


### Sino-Korean Tests ###
to_equal(arabic_to_sino_korean(3524761), "삼백오십이만사천칠백육십일")
to_equal(arabic_to_sino_korean(0), "공")
to_equal(arabic_to_sino_korean(1212), "천이백십이")
to_equal(arabic_to_sino_korean(1000), "천")
to_equal(arabic_to_sino_korean(1), "일")
to_equal(arabic_to_sino_korean(10), "십")
to_equal(arabic_to_sino_korean(50), "오십")
to_equal(arabic_to_sino_korean(999999999999), "구천구백구십구억구천구백구십구만구천구백구십구")

### Native Korean Tests ###
# Expect(ArabicToKorean("1", False)).to_equal("하나")
# Expect(ArabicToKorean("10", False)).to_equal("열")
# Expect(ArabicToKorean("55", False)).to_equal("쉰다섯")
# Expect(ArabicToKorean("0", False)).to_equal("$") # Fails correctly, returns $