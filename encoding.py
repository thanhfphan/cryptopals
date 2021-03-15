# base64 character
encodeStd = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

# Convert binary string to hext string
def binstr_to_hexstr(binstr):
    l = len(binstr) // 4 * 4
    for i in range(len(binstr) - l):
        binstr = "0" + binstr
    
    result = ""
    for i in range(0, len(binstr), 4):
        block = binstr[i:i+4]
        result = result + f'{int(block, 2):x}'
    
    return result
    
# Convert hext string to binary string
def hexstr_to_bintext(hexstr):
    text = hexstr_to_text(hexstr)

    return text_to_binarystr(text)

def hexstr_to_text(hexstr):
    result = ""
    for i in range (0, len(hexstr), 2):
        block = hexstr[i:i+2]
        result = result + chr(int(block, 16))

    return result

# Context text to binary string
def text_to_binarystr(text):
    result = ""
    for t in text:
        result = result + '{0:08b}'.format(ord(t))
    
    return result

            
# Encoding hex string to base64 string
def encode_hex_to_base64(hexstr):
    text = hexstr_to_text(hexstr)
    bintext = text_to_binarystr(text)
    l = len(bintext) // 6 * 6
    
    for i in range(len(bintext) - l):
        bintext = text + '0'

    result = ""
    for i in range(0, len(binText), 6):
        block = bintext[i:i+6]
        result = result + encodeStd[int(block, 2)]
   
    return result
