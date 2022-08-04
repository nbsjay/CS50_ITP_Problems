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

"""
create an infinite loop
Convert to lowercase
convert to title case
loop through the menu
for each order in the menu,
if the item ordered is in the menu,
get the price and add to the total
"""


i = 1
total = 0

while True:
    try:
        item = input("Item:  ").title()
        for ord in menu:
            if ord == item:
                order = menu[ord]
                total = total + order
                print(f"Toatal: ${total:.2f}")
    except EOFError:
        print("\n")
        break


"""
An important note:

David failed to mention that windows users do cannot use 'control d' to exit out of a running code.
becuase of this the exception will not catch the keyboard combination
if you are working on a locally installed vscode, rather use 'control z'
"""