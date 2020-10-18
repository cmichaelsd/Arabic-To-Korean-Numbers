from arabic_to_sino_korean import arabic_to_sino_korean
from arabic_to_native_korean import arabic_to_native_korean

def to_equal(label, result, expect):
    if expect == result:
        print(f"{label} - Passed")
    else:
        print(f"{label} - Failed: expected {expect}, result {result}.")
    
### Sino-Korean Tests ###
sino_test_label = "SINO-KOREAN TEST"
to_equal(sino_test_label, arabic_to_sino_korean(3524761), "삼백오십이만사천칠백육십일")
to_equal(sino_test_label, arabic_to_sino_korean(0), "공")
to_equal(sino_test_label, arabic_to_sino_korean(1212), "천이백십이")
to_equal(sino_test_label, arabic_to_sino_korean(1000), "천")
to_equal(sino_test_label, arabic_to_sino_korean(1), "일")
to_equal(sino_test_label, arabic_to_sino_korean(10), "십")
to_equal(sino_test_label, arabic_to_sino_korean(50), "오십")
to_equal(sino_test_label, arabic_to_sino_korean(999999999999), "구천구백구십구억구천구백구십구만구천구백구십구")

### Native Korean Tests ###
native_test_label = "NATIVE-KOREAN TEST"
to_equal(native_test_label, arabic_to_native_korean(1), "하나")
to_equal(native_test_label, arabic_to_native_korean(10), "열")
to_equal(native_test_label, arabic_to_native_korean(55), "쉰다섯")
