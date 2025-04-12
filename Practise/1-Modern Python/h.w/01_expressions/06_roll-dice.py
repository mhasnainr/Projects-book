import random


def main():
    d1: int = random.randint(1, 6)
    d2: int = random.randint(1, 6)
    print(f"Dice 1: {d1}")
    print(f"Dice 2: {d2}")

    total: int = d1 + d2
    print(f"Total of 2 dice is: {total}")


main()
