# https://flylib.com/books/en/2.480.1.81/1/#:~:text=The%20strange%20phrase%20%22ETAOIN%20SHRDLU,percent%20of%20total%20letter%20frequency.
frequencyLeaderBoard = {
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
