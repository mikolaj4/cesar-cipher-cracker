import math
from collections import *
from string import ascii_lowercase
import re
import data
import random

ALPHABET_ENG = ascii_lowercase
ALPHABET_POL = "aąbcćdeęfghijklłmnńoóprsśtuwyzźż"
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


def lclear(text):
    return re.sub(r'[^a-ząćęłńóśźż]', '', text.lower())


def encrypt(plaintext: str, key: int, alphabet: str):
    # plaintext = plaintext.lower().replace(" ", "").replace(",", "").replace(".", "")
    plaintext = lclear(plaintext)
    alphabet_size = len(alphabet)
    ciphertext = ''

    for char in plaintext:
        char_index = alphabet.index(char)
        encrypted_char = alphabet[(key + char_index) % alphabet_size]
        ciphertext += encrypted_char
    return ciphertext


def decrypt_with_key(ciphertext: str, key: int, alphabet: str):
    alphabet_size = len(alphabet)
    plaintext = ''
    for char in ciphertext:
        char_index = alphabet.index(char)
        decrypted_char = alphabet[(char_index - key) % alphabet_size]
        plaintext += decrypted_char
    return plaintext


def difference(text: str, alphabet: str, frequency: dict):
    alphabet_size = len(alphabet)
    counter = Counter(text)
    return sum([abs(counter.get(letter, 0) * 100 / len(text) - frequency[letter]) for letter in
                alphabet]) / alphabet_size


def break_cipher(ciphertext: str, alphabet: str, frequency: dict):
    lowest_difference = math.inf
    encryption_key = 0
    alphabet_size = len(alphabet)

    for key in range(1, alphabet_size):
        current_plaintext = decrypt_with_key(ciphertext, key, alphabet)
        current_difference = difference(current_plaintext, alphabet, frequency)
        if current_difference < lowest_difference:
            lowest_difference = current_difference
            encryption_key = key
    return encryption_key


def read_file(filename):
    counter = 0
    longtxt = ''
    with open(filename, encoding='utf8') as f:
        for line in f:
            longtxt += lclear(line.strip())
            counter += 1
    f.close()
    return lclear(longtxt)

def write_to_file(filename, content):
    with open(filename, 'w') as f:
        current_line_length = 0
        for word in content:
            word_length = len(word)
            while word_length > 0:
                if current_line_length + word_length > 200:
                    f.write('\n')
                    current_line_length = 0
                chars_to_write = min(word_length, 200 - current_line_length)
                f.write(word[:chars_to_write] + '')
                current_line_length += chars_to_write
                word = word[chars_to_write:]
                word_length -= chars_to_write


plaintext = read_file('input_plaintext.txt')
ciphertext = encrypt(plaintext, 6, ALPHABET_ENG)
write_to_file('input_cesar.txt', ciphertext)




plaintextPol1 = 'Cześć, oto przykładowy tekst po Polsku ze znakami interpunkcyjnymi;,/$!? i kropkami..'
ciphertextPol1 = encrypt(plaintextPol1, 5, ALPHABET_POL)
ciphertextPol1_key = break_cipher(ciphertextPol1, ALPHABET_POL, data.letterFrequencyPol)
ciphertextPol1_decrypted = decrypt_with_key(ciphertextPol1, ciphertextPol1_key, ALPHABET_POL)


print('\nThe program shows success rates in cracking cesar ciphers\n')
print('Example of long plaintext in Polish: ', plaintextPol1)
print('Encrypted text with key 5: ', ciphertextPol1)
print('Result of ciphertext-only attack: ', ciphertextPol1_decrypted, '\n')

plaintextEng1 = 'Once upon a time I decrypt some texts.'
ciphertextEng1 = encrypt(plaintextEng1, 9, ALPHABET_ENG)
ciphertextEng1_key = break_cipher(ciphertextEng1, ALPHABET_ENG, data.letterFrequencyEng)
ciphertextEng1_decrypted = decrypt_with_key(ciphertextEng1, ciphertextEng1_key, ALPHABET_ENG)

print('Example of long plaintext in English: ', plaintextEng1)
print('Encrypted text with key 9: ', ciphertextEng1)
print('Result of ciphertext-only attack: ', ciphertextEng1_decrypted, '\n\n')

print(
    'Now I will check how short of a word can be decrypted using this frequency analyzer.\n')


def check_success_rate(wordlist: list):
    correct_counter = 0
    for word in wordlist:
        ciphertext = encrypt(word, random.randint(1, 26), ALPHABET_ENG)
        key = break_cipher(ciphertext, ALPHABET_ENG, data.letterFrequencyEng)
        if decrypt_with_key(ciphertext, key, ALPHABET_ENG) == word:
            correct_counter += 1
    return correct_counter / len(wordlist)


percentage = "{:.0%}".format(check_success_rate(data.eng_3))
print(len(data.eng_3), ' 3-letters long English words. Decryption succes rate: ', percentage, "\n")

percentage = "{:.0%}".format(check_success_rate(data.eng_4))
print(len(data.eng_4), ' 4-letters long English words. Decryption succes rate: ', percentage, "\n")

percentage = "{:.0%}".format(check_success_rate(data.eng_5))
print(len(data.eng_5), ' 5-letters long English words. Decryption succes rate: ', percentage, "\n")

percentage = "{:.0%}".format(check_success_rate(data.eng_6))
print(len(data.eng_6), ' 6-letters long English words. Decryption succes rate: ', percentage, "\n")

percentage = "{:.0%}".format(check_success_rate(data.eng_7))
print(len(data.eng_7), ' 7-letters long English words. Decryption succes rate: ', percentage, "\n")

percentage = "{:.0%}".format(check_success_rate(data.eng_8))
print(len(data.eng_8), ' 8-letters long English words. Decryption succes rate: ', percentage, "\n")

percentage = "{:.0%}".format(check_success_rate(data.eng_9))
print(len(data.eng_9), ' 9-letters long English words. Decryption succes rate: ', percentage, "\n")

print('the Random words were generated using https://randomwordgenerator.com/')
# print('I also uploaded the file with 370105 english words. To pass it as input data change line 62 in file data.py')



