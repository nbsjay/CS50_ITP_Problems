"""
In a file called grocery.py, implement a program that prompts the user for items,
one per line, until the user inputs control-d (which is a common way of ending one's input to a program).
Then output the user's grocery list in all uppercase, sorted alphabetically by item,
prefixing each line with the number of times the user inputted that item.
No need to pluralize the items. Treat the user's input case-insensitively.
"""

gl = {}

while True:
    try:
        # get item from user and change to uppercase
        item = input().upper()
        # if item is in the dictionary, add one to its value
        if item in gl:
            # add one to its value
            gl[item] += 1
            # if its not in the dictionary
        else:
            # set its value to 1
            gl[item] = 1
    except EOFError:
        for thing in sorted(gl):
            # print the key and the value of the key
            # [thing] is the name of the item, and 'thing' is the value
            print(gl[thing], thing)
        break
