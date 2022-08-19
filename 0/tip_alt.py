def tip (cost, rate):
    cost = float(cost.replace("$", ""))
    rate = (float(rate.replace("%", ""))) / 100
    tip  = cost * rate
    print(f"Leave ${tip:.2f}")

meal = input("How much was the meal? ")
perc = input("What percentage will you like to tip? ")

tip(meal, perc)
