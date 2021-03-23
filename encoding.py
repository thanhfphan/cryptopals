# base64 character
ENCODE_STD = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

# Convert binary string to hex string
def binary_to_hex(bintext):
    l = len(bintext) // 4 * 4
    for i in range(len(bintext) - l):
        bintext = "0" + bintext
    
    result = ""
    for i in range(0, len(bintext), 4):
        block = bintext[i:i+4]
        result = result + f'{int(block, 2):x}'
    
    return result
    
# Convert hex string to binary string
def hex_to_binary(hextext):
    text = hex_to_text(hextext)

    return text_to_binary(text)

def text_to_hex(text):
    binary_of_text = text_to_binary(text)
    return binary_to_hex(binary_of_text)

def hex_to_text(hexstr):
    result = ""
    for i in range (0, len(hexstr), 2):
        block = hexstr[i:i+2]
        result = result + chr(int(block, 16))

    return result

# Context text to binary string
def text_to_binary(text):
    result = ""
    for t in text:
        result = result + '{0:08b}'.format(ord(t))
    
    return result

def binary_to_text(binary_text):
    result = ""
    for i in range(0, len(binary_text), 8):
        block = binary_text[i:i+8]
        result = result + chr(int(block, 2))
    
    return result
            
# Encoding hex string to base64 string
def encode_hex_to_base64(hextext):
    text = hex_to_text(hextext)
    bintext = text_to_binary(text)
    l = len(bintext) // 6 * 6
    
    for i in range(len(bintext) - l):
        bintext = text + '0'

    result = ""
    for i in range(0, len(binText), 6):
        block = bintext[i:i+6]
        result = result + ENCODE_STD[int(block, 2)]
   
    return result

def decode_base64_to_text(base64text):
    base64text = base64text.replace("=","").replace("\r", "").replace("\n", "")
    binary_text = ""
    for i in base64text:
        index = ENCODE_STD.find(i)
        if index < 0:
            print(i)
        binary_text = binary_text + '{0:06b}'.format(index)
    
    return binary_to_text(binary_text)

    



