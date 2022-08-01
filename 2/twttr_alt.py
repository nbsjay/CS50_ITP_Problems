# an alternate solution to the twitter problem

# get input from user
text = input("Input:  ")

# a variabe for vowels
vowels = ["a","e","i","o","u"]

# check the string for vowels
for letter in text:
    if not letter.lower() in vowels:
        print(letter, end="")
print()
#