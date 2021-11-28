# https://www.geeksforgeeks.org/advanced-encryption-standard-aes/

def sub_byte(input):

    return ""

# input is hex format
def shift_row(input):
    if len(input) != 4*2*4:
        print("invalid len")
        return

    result = input[:8]
    result = result + input[8*1+2:8*1+8] + input[8*1:8*1+2]
    result = result + input[8*2+4:8*2+8] + input[8*2:8*2+4]
    result = result + input[8*3+6:8*3+8] + input[8*3:8*3+6]

    return result

