
# Return a bit string
def xor_two_bit_string(str1, str2):
    if len(str1) < len(str2):
        loop = True
        while loop:
            for i in str1:
                str1 = str1 + i
                if len(str1) == len(str2):
                    loop = False
                    break
    elif len(str1) > len(str2):
        loop = True
        while loop:
            for i in str2:
                str2 = str2 + i
                if len(str1) == len(str2):
                    loop = False
                    break

    if len(str1) != len(str2):
        return ""

    result = ""
    for i in range(0, len(str1)):
        sumtext = str1[i] + str2[i]
        if sumtext in ["10","01"]:
            result = result + "1"
        else:
            result = result + "0"
    
    return result
