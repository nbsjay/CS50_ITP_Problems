"""
implement a program that prompts users to input a fruit (case-insensitively) and then outputs the number of calories
in one portion of that fruit, per the FDA's poster for fruits, which is also available as text. Capitalization aside, assume that
users will input fruits exactly as written in the poster (e.g., strawberries, not strawberry). Ignore any input that isn't a fruit.
https://www.fda.gov/food/food-labeling-nutrition/raw-fruits-poster-text-version-accessible-version
"""

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
