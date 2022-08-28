"""
implement a program in Python that prompts the user for mass as an integer (in kilograms)
and then outputs the equivalent number of Joules as an integer. Assume that the user will input an integer.
formula is E = mc²
where
c = 300000000 meters per second
m is mass in kiligrams
E is energy in joules
"""

def energy(mass):
    c = 300000000
    e = mass * (c ** 2)
    print(f"C: {c}")
    print(f"E: {e}")

m = int(input("M: "))
energy(m)
