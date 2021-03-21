import encoding
import bitwise
import calculation
import decrypt
import encrypt

print("Set 1 - Challenge 1")
print(encoding.hex_to_text('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'))

print("\n")
print("Set 1 - Challenge 2")
str1 = encoding.hex_to_binary("1c0111001f010100061a024b53535009181c")
str2 = encoding.hex_to_binary("686974207468652062756c6c277320657965")
binstr = bitwise.xor_two_bit_string(str1, str2)
print(encoding.binary_to_hex(binstr))

print("\n")
print("Set 1 - Challenge 3")
print(decrypt.xor_single_hex("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"))

print("\n")
print("Set 1 -- Challenge 4")
## download from https://cryptopals.com/static/challenge-data/4.txt
fileSet1Challenge4 = open("files/set1-challenge4.txt")
contentSet1Challenge4 = fileSet1Challenge4.read()
for line in contentSet1Challenge4.splitlines():
    decodedStr = decrypt.xor_single_hex(line)
    scoreDecodedStr = calculation.character_frequency_score(decodedStr)
    if scoreDecodedStr > 4:
        print(decodedStr) # look like the plain text is "Now that the party is jumping" :)))

print("\n")
print("Set 1 --  Challenge 5")
fileSet1Challenge5 = open("files/set1-challenge5.txt")
contentSet1Challenge5 = fileSet1Challenge5.read()
keySet1Challenge5 = "ICE"
cipherSet1Challenge5 = encrypt.repeating_xor_key(contentSet1Challenge5, keySet1Challenge5)
print(encoding.binary_to_hex(encoding.text_to_binary(cipherSet1Challenge5)))
