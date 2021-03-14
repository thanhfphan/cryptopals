
encodeStd = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def hexStr_to_text(str):
    result = ""
    for i in range (0, len(str), 2):
        block = str[i:i+2]
        result = result + chr(int(block, 16))

    return result

def text_to_binaryStr(text):
    result = ""
    for t in text:
        result = result + '{0:08b}'.format(ord(t))
    
    return result

            
# Encoding hex string to base64 string
def EncodeHex(hexStr):
    text = hexStr_to_text(hexStr)
    binText = text_to_binaryStr(text)
    l = len(binText) // 6 * 6
    
    for i in range(len(binText) - l):
        binText = text + '0'

    result = ""
    for i in range(0, len(binText), 6):
        block = binText[i:i+6]
        result = result + encodeStd[int(block, 2)]
   
    return result

print(EncodeHex('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'))