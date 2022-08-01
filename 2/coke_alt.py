"""
An alternate solution to the coke.py problem using a list
"""

exp_amount = 50

while exp_amount > 0:
    print("Amount Due:   ", exp_amount)
    coin = int(input("Insert a coin:   "))
    if coin in [5, 10, 25]:
       exp_amount = exp_amount - coin
    else:
        print("Wrong Denomination!!")
print("Change Owed:   " ,abs(exp_amount))
        
