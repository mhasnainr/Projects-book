import math


def main():
    num1 = float(input("Please enter an integer to be divided: "))
    num2 = float(input("Please enter an integer to divide: "))
    result: int = num1 // num2
    remainder: float = num1 % num2
    print(f"Result of this division is {result} and remainder is {remainder}")


main()
