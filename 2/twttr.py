"""
implement a program that prompts the user for a str of text and then outputs that same text but
with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.
"""

# get text from the user
text = input("Input:  ")

# define list of vowels
vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

# loop through user's input 
for letter in text:
    # if the letter is a vowel,
    if letter in vowels:
        # replace it with nothing
        print(letter.replace(letter, ""), end="")
    # if not a vowel, print as is
    else:
        print(letter, end="")

# print the content of the list