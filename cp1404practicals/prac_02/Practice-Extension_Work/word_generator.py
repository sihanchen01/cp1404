"""
CP1404/CP5632 - Practical
Random word generator - based on format of words

Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""
import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"

# word_format = "ccvcvvc"
# word_format = input("Enter a word format: ").lower()
word_format = input(
    "Enter a word format (% for consonants, # for vowels, * for either): ").lower()

word = ""
for kind in word_format:
    # if kind == "c":
    #     word += random.choice(CONSONANTS)
    # else:
    #     word += random.choice(VOWELS)
    if kind == "%":
        word += random.choice(CONSONANTS)
    elif kind == "#":
        word += random.choice(VOWELS)
    elif kind == "*":
        word += random.choice(VOWELS + CONSONANTS)
    else:
        word += kind


print(word)
