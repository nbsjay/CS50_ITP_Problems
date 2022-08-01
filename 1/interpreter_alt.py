"""
    implement a program that prompts the user for an arithmetic expression and then calculates and outputs the result as
    a floating-point value formatted to one decimal place. Assume that the user’s input will be formatted as x y z,
    with one space between x and y and one space between y and z, wherein:
    x is an integer
    y is +, -, *, or /
    z is an integer
"""

expression = input("input a mathematical expression   ")

x, y , z = expression.split()

new_x = float(x)
new_z = float(z)

if y == "+":
    result = new_x + new_z
elif y == "-":
    result = new_x - new_z
elif y == "*":
    result = new_x * new_z
elif y == "/":
    result = new_x / new_z

print(result)