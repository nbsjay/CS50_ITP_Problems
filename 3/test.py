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