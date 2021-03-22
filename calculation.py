# https://flylib.com/books/en/2.480.1.81/1/#:~:text=The%20strange%20phrase%20%22ETAOIN%20SHRDLU,percent%20of%20total%20letter%20frequency.
frequency_leader_board = {
    "E": 12.51,
    "T": 9.25,
    "A": 8.04,
    "O": 7.60,
    "I": 7.26,
    "N": 7.09,
    "S": 6.54,
    "H": 5.49,
    "R": 6.12,
    "D": 3.99,
    "L": 4.14,
    "U": 2.71
}


# for simplicity purposes only check space characters for now
def character_frequency_score(text):
    score = 0
    for t in text:
        if t == " ":
            score = score + 1
    return score

# caculate hamming distance between 2 bin text
def hamming_distance(text1, text2):
    if len(text1) != len(text2):
        print("diff length")
        return -1
    
    result = 0
    for i in range(0, len(text1)):
        if text1[i] != text2[i]:
            result = result + 1
    
    return result