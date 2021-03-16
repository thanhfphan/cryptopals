import encoding
import bitwise
 
#print(encoding.hexstr_to_text('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'))
#print("\n")
#print("Set 1 - Challenge 1")

#print("Set 1 - Challenge 2")
#str1 = encoding.hexstr_to_bintext("1c0111001f010100061a024b53535009181c")
#str2 = encoding.hexstr_to_bintext("686974207468652062756c6c277320657965")
#binstr = bitwise.xor_two_bit_string(str1, str2)
#print(encoding.binstr_to_hexstr(binstr))

print("Set 1 - Challenge 3")
binTextCipher = encoding.hexstr_to_bintext("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")
for i in range(0, 255):
    binI = '{0:08b}'.format(i)
    xorBinStr = bitwise.xor_two_bit_string(binTextCipher, binI)
    xorHexStr = encoding.binstr_to_hexstr(xorBinStr)
    decodeStr = encoding.hexstr_to_text(xorHexStr)
    # Look like 88 is the correct one xD
    if i == 88:
        print(decodeStr)

