
def repeating_xor_key(plainText, key):
    result = ""
    for i in range(0, len(plainText)):
        mod = i%len(key)
        result = result + chr(ord(plainText[i]) ^ ord(key[mod]))
    
    return result