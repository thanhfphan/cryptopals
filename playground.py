import encoding
import bitwise
 
print("Set 1 - Challenge 1")
print(encoding.hexstr_to_text('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'))
print("\n")

print("Set 2 - Challenge 2")
str1 = encoding.hexstr_to_bintext("1c0111001f010100061a024b53535009181c")
str2 = encoding.hexstr_to_bintext("686974207468652062756c6c277320657965")
binstr = bitwise.xor_two_bit_string(str1, str2)
print(encoding.binstr_to_hexstr(binstr))