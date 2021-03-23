import encoding
import bitwise
import calculation
import decrypt
import encrypt

#print("Set 1 - Challenge 1")
#print(encoding.hex_to_text('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'))
#
#print("\n")
#print("Set 1 - Challenge 2")
#str1 = encoding.hex_to_binary("1c0111001f010100061a024b53535009181c")
#str2 = encoding.hex_to_binary("686974207468652062756c6c277320657965")
#bin_text = bitwise.xor_two_bit_string(str1, str2)
#print(encoding.binary_to_hex(bin_text))
#
#print("\n")
#print("Set 1 - Challenge 3")
#print(decrypt.xor_single_hex("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"))
#
#print("\n")
#print("Set 1 -- Challenge 4")
### download from https://cryptopals.com/static/challenge-data/4.txt
#file_set1_challenge4 = open("files/set1-challenge4.txt")
#content_set1_challenge4 = file_set1_challenge4.read()
#for line in content_set1_challenge4.splitlines():
#    decoded_text = decrypt.xor_single_hex(line)
#    score_decoded_text = calculation.character_frequency_score(decoded_text)
#    if score_decoded_text > 4:
#        print(decoded_text) # look like the plain text is "Now that the party is jumping" :)))
#
#print("\n")
#print("Set 1 --  Challenge 5")
#file_set1_challenge5 = open("files/set1-challenge5.txt")
#content_set1_challenge5 = file_set1_challenge5.read()
#key_set1_challenge5 = "ICE"
#cipher_set1_challenge5 = encrypt.repeating_xor_key(content_set1_challenge5, key_set1_challenge5)
#print(encoding.text_to_hex(cipher_set1_challenge5))

print("\n")
print("Set 1 -- Chanllenge 6")
file_set1_challenge6 = open("files/set1-challenge6.txt")
content_set1_challenge6_base64 = file_set1_challenge6.read()
content_set1_challenge6 = encoding.decode_base64_to_text(content_set1_challenge6_base64)
length_of_the_key = -1
smallest_normalized = 99999
# KEYSIZE from 2 to 40
for i in range(2, 41):
    text11 = content_set1_challenge6[i:2*i]
    text12 = content_set1_challenge6[2*i:2*i+i]
    hs1 = calculation.hamming_distance_2text(text11, text12)

    text21 = content_set1_challenge6[3*i:3*i+i]
    text22 = content_set1_challenge6[4*i:4*i+i]
    hs2 = calculation.hamming_distance_2text(text21, text22)

    text31 = content_set1_challenge6[6*i:6*i+i]
    text32 = content_set1_challenge6[7*i:7*i+i]
    hs3 = calculation.hamming_distance_2text(text31, text32)

    avg_normalized = (hs1 + hs2 + hs3)/(3*i)
    if avg_normalized < smallest_normalized:
        smallest_normalized = avg_normalized
        length_of_the_key = i

block_dictionary = {}
for i in range(0, len(content_set1_challenge6), length_of_the_key):
    to_index = i + length_of_the_key
    if to_index > len(content_set1_challenge6):
        to_index = len(content_set1_challenge6)
    block = content_set1_challenge6[i:to_index]
    for i in range(0, len(block)):
        if i in block_dictionary:
            block_dictionary[i] = block_dictionary[i] + block[i]
        else:
            block_dictionary[i] = block[i]
