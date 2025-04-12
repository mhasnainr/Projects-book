import math


def main():
    base = float(input("Enter the length of AB: "))
    height = float(input("Enter the length of AC: "))
    hypot: float = math.sqrt((base ** 2) + (height ** 2))
    print(f"Length of BC (hypotenuse) is {hypot} unit")


main()
