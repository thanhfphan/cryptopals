import encoding
import bitwise
import calculation
import decrypt

#print(encoding.hexstr_to_text('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'))
#print("\n")
#print("Set 1 - Challenge 1")

#print("Set 1 - Challenge 2")
#str1 = encoding.hexstr_to_bintext("1c0111001f010100061a024b53535009181c")
#str2 = encoding.hexstr_to_bintext("686974207468652062756c6c277320657965")
#binstr = bitwise.xor_two_bit_string(str1, str2)
#print(encoding.binstr_to_hexstr(binstr))

#print("Set 1 - Challenge 3")
#print(decrypt.xor_single_hex_string("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"))


print("Set 1 -- Challenge 4")
# download from https://cryptopals.com/static/challenge-data/4.txt
fileSet1Challenge4 = open("files/set1-challenge4.txt")
contentSet1Challenge4 = fileSet1Challenge4.read()
for line in contentSet1Challenge4.splitlines():
    decodedStr = decrypt.xor_single_hex_string(line)
    scoreDecodedStr = calculation.character_frequency_score(decodedStr)
    if scoreDecodedStr > 4:
        print(decodedStr) # look like the plain text is "Now that the party is jumping" :)))
