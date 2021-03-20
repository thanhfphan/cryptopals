import encoding
import bitwise
import calculation

def xor_single_hex_string(cipherText):
    binTextCipher = encoding.hexstr_to_bintext(cipherText)
    highestScore = 0
    result = ""
    for i in range(0, 255):
        binI = '{0:08b}'.format(i)
        xorBinStr = bitwise.xor_two_bit_string(binTextCipher, binI)
        xorHexStr = encoding.binstr_to_hexstr(xorBinStr)
        decodeStr = encoding.hexstr_to_text(xorHexStr)
        textScore = calculation.character_frequency_score(decodeStr)
        if textScore > highestScore:
            highestScore = textScore
            result = decodeStr

    return result