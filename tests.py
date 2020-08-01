from arabic_to_korean import ArabicToKorean
from typing import Any

class Expect:
    def __init__(self, result):
        self.__result = result
    
    @property
    def result(self) -> str:
        return self.__result
    
    def to_equal(self, expect) -> None:
        if expect == self.result:
            print("Passed")
        else:
            print(f"Failed: expected {expect}, result {self.result}.")
    


### Sino-Korean Tests ###
Expect(ArabicToKorean("3524761")).to_equal("삼백오십이만사천칠백육십일")
Expect(ArabicToKorean("0000")).to_equal("공")
Expect(ArabicToKorean("1212")).to_equal("천이백십이")
Expect(ArabicToKorean("1000")).to_equal("천")
Expect(ArabicToKorean("1")).to_equal("일")
Expect(ArabicToKorean("10")).to_equal("십")
Expect(ArabicToKorean("50")).to_equal("오십")
Expect(ArabicToKorean("999999999999")).to_equal("구천구백구십구억구천구백구십구만구천구백구십구")

### Native Korean Tests ###
Expect(ArabicToKorean("1", False)).to_equal("하나")
Expect(ArabicToKorean("10", False)).to_equal("열")
Expect(ArabicToKorean("55", False)).to_equal("쉰다섯")
Expect(ArabicToKorean("0", False)).to_equal("$") # Fails correctly, returns $