
# Return a bit string
def xor_two_bit_string(str1, str2):
    if len(str1) == 0 | len(str2) == 0:
        return ""
    
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
