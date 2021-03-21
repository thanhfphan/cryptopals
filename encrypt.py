
def repeating_xor_key(plaintext, key):
    result = ""
    for i in range(0, len(plaintext)):
        mod = i%len(key)
        result = result + chr(ord(plaintext[i]) ^ ord(key[mod]))
    
    return result