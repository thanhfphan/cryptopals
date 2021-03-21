import encoding
import bitwise
import calculation

# input is hexa format
def xor_single_hex(ciphertext):
    bincipher = encoding.hex_to_binary(ciphertext)
    highest_score = 0
    result = ""
    for i in range(0, 255):
        bin_i = '{0:08b}'.format(i)
        xor_bin_text = bitwise.xor_two_bit_string(bincipher, bin_i)
        xor_hex_text = encoding.binary_to_hex(xor_bin_text)
        decdode_text = encoding.hex_to_text(xor_hex_text)
        text_score = calculation.character_frequency_score(decdode_text)
        if text_score > highest_score:
            highest_score = text_score
            result = decdode_text

    return result