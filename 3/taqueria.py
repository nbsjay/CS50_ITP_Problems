"""
In a file called taqueria.py, implement a program that enables a user to place an order,
prompting them for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program).
After each inputted item, display the total cost of all items inputted thus far, prefixed with a dollar sign ($) and formatted to two decimal places.
Treat the user's input case insensitively. Ignore any input that isn’t an item. Assume that every item on the menu will be titlecased.
"""



menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

# total's value to 0
total = 0

# create an infinite loop
while True:
    try:
        # convert user's input to title case
        item = input("Item:  ").title()
        # loop through the menu
        for ord in menu:
            # if user's input matches an item
            if ord == item:
                # get the item's price
                order = menu[ord]
                # add the price to total's value
                total = total + order
                # print the total, format it to two decimal places and add a preceeding dollar sign
                print(f"Toatal: ${total:.2f}")
    # if 'control d' is entered
    except EOFError:
        # print a new line
        print("\n")
        # exit the loop
        break


"""
An important note:

David failed to mention that windows users cannot use 'control d' to exit out of a running code.
because of this, the exception will not catch the keyboard combination
if you are working on a locally installed vscode on windows, rather use 'control z'
"""