letterFrequencyEng = {'e': 12.0,
                      't': 9.10,
                      'a': 8.12,
                      'o': 7.68,
                      'i': 7.31,
                      'n': 6.95,
                      's': 6.28,
                      'r': 6.02,
                      'h': 5.92,
                      'd': 4.32,
                      'l': 3.98,
                      'u': 2.88,
                      'c': 2.71,
                      'm': 2.61,
                      'f': 2.30,
                      'y': 2.11,
                      'w': 2.09,
                      'g': 2.03,
                      'p': 1.82,
                      'b': 1.49,
                      'v': 1.11,
                      'k': 0.69,
                      'x': 0.17,
                      'q': 0.11,
                      'j': 0.10,
                      'z': 0.07}
letterFrequencyPol = {
    'a': 8.91,
    'ą': 0.99,
    'b': 1.47,
    'c': 3.96,
    'ć': 0.30,
    'd': 3.25,
    'e': 7.66,
    'ę': 1.14,
    'f': 0.30,
    'g': 1.42,
    'h': 1.08,
    'i': 8.21,
    'j': 2.28,
    'k': 3.51,
    'l': 2.10,
    'ł': 2.16,
    'm': 2.80,
    'n': 5.52,
    'ń': 0.20,
    'o': 7.75,
    'ó': 0.85,
    'p': 3.13,
    'r': 4.69,
    's': 4.32,
    'ś': 0.45,
    't': 3.98,
    'u': 2.50,
    'w': 4.65,
    'y': 3.76,
    'z': 5.64,
    'ź': 0.06,
    'ż': 1.11
}

# to input more words change file name to words_end.txt
with open('1250_eng_words.txt', 'r') as f:
    words = f.read()

allEnglishWords = words.split()

eng_3 = [word for word in allEnglishWords if len(word) == 3]
eng_4 = [word for word in allEnglishWords if len(word) == 4]
eng_5 = [word for word in allEnglishWords if len(word) == 5]
eng_6 = [word for word in allEnglishWords if len(word) == 6]
eng_7 = [word for word in allEnglishWords if len(word) == 7]
eng_8 = [word for word in allEnglishWords if len(word) == 8]
eng_9 = [word for word in allEnglishWords if len(word) == 9]
