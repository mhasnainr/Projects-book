import random


def main():
    def dice():

        d1: int = random.randint(1, 6)
        d2: int = random.randint(1, 6)

        total: int = d1 + d2

        print(f"Total of two dice is {total}")

    dice()
    dice()
    dice()


main()
