"""
Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.
implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due. Once the user has inputted
at least 50 cents, output how many cents in change the user is owed. Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.
"""
# variable for the expected amount
exp_amount = 50

while exp_amount > 0:
    # print the expected amount
    print("Amount Due:  ", exp_amount)

    # prompt the user for input. 25, 10, 5 cents
    inserted = int(input("Insert Coin:  "))
    if inserted == 5 or inserted == 10 or inserted == 25: # check for this condition
        exp_amount = exp_amount - inserted # decrement syntax
    else:
        print("Wrong Denomination")

change_owed = abs(exp_amount)
print("Change Owed:  ", change_owed)
