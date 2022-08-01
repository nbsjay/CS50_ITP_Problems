"""
A program that prompts the user for the name of a variable in camel case
and outputs the corresponding name in snake case. Assume that the user's
input will indeed be in camel case
"""

# get user's input
camelcase = input("camelCase:  ")

# print snake case
print("snake_case: ", end="")

# check every character in string
for letter in camelcase:

    # check if the letter is uppercase
    if letter.isupper():
        # print underscore and the letter in lowercase
        print("_" + letter.lower(), end="")
    # if not upper, print the letter
    else:
        print(letter, end="")
print()