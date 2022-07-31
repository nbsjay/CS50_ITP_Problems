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
