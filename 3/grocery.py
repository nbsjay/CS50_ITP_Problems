"""
In a file called grocery.py, implement a program that prompts the user for items,
one per line, until the user inputs control-d (which is a common way of ending one's input to a program).
Then output the user's grocery list in all uppercase, sorted alphabetically by item,
prefixing each line with the number of times the user inputted that item.
No need to pluralize the items. Treat the user's input case-insensitively.
"""

gl = {} # A dictionary for the grocery list

while True:
    try:
        # get item from user and change to uppercase
        item = input().upper()
        # if item (key) is in the dictionary
        if item in gl:
            # add one to its value
            gl[item] += 1
            # if its not in the dictionary
        else:
            # add item(key) to the dictionary and set its value to 1
            gl[item] = 1
    except EOFError:
        for key in sorted(gl):
            # print the value of the key and the key
            print(gl[key], key)
        break
