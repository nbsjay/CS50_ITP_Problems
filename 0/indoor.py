"""
In a file called indoor.py, implement a program in Python that prompts the user for input and then outputs that same input in lowercase.
Punctuation and whitespace should be outputted unchanged. You’re welcome, but not required, to prompt the user explicitly,
as by passing a str of your own as an argument to input
"""

def main():
    # ask for the user's input
    x = input("type something here ")
    # call the low function
    low(x)

# define low function with parameter 'ask'

def low(ask):
    # casefold() from python's documentation converts strings to lowercase
    print(ask.casefold())


main()
