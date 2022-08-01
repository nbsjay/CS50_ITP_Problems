fruits = [{"name": "apple", "Calories": 130},
        {"name": "avocado", "Calories": 50},
        {"name": "banana", "Calories": 110},
        {"name": "cantaloupe", "Calories": 50},
        {"name": "grapefruit", "Calories": 60},
        {"name": "grapes", "Calories": 90},
        {"name": "honeydew", "Calories": 50},
        {"name": "kiwifruit", "Calories": 90},
        {"name": "lemon", "Calories": 15},
        {"name": "lime", "Calories": 20},
        {"name": "nectarine", "Calories": 60},
        {"name": "orange", "Calories": 80},
        {"name": "peach", "Calories": 60},
        {"name": "pear", "Calories": 100},
        {"name": "pineapple", "Calories": 50},
        {"name": "plums", "Calories": 70},
        {"name": "strawberries", "Calories": 50},
        {"name": "sweet cherries", "Calories": 100},
        {"name": "tangerine", "Calories": 50}
]        


nutri = input("Item:   ").casefold()

for fruit in fruits:
        if nutri == fruit["name"]:
                print("Calories:   ", fruit["Calories"])
