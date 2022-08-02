"""
prompt for a fraction
separate the characters in x / y
check if the middle character is /
check if x and y are integers
perform the division if it is is and round to the nearest integer
if above 1%, output % full
if 99% or more, output F
if 1% and below output E
do nothing if it is not a division
"""

# while forever
while True:
    # get user input
    fuel = input("Fraction:  ")
    try:
        # split the input
        a, b = fuel.split("/")

        # convert into integers
        x = int(a)
        y = int(b)

        # calculate the percentage
        if x < y or x == y:
            answer = x / y
            # the f-string literal converts the answer into a percentage format
            percentage = f"{answer:.0%}"
            break        
    except (ValueError, ZeroDivisionError):
        pass
# is the fuel equal to or above 99%
if answer >= 0.99:
    print("F")
# is the fuel-level less than or equal to 1%
elif answer <= 0.01:
    print("E")
else:
    print(percentage)