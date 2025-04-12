def add_num():
    num1: str = input("Enter first number: ")
    num1: int = int(num1)

    num2: str = input("Enter second number: ")
    num2: int = int(num2)

    sum: int = num1 + num2

    print(f"Sum of {num1} and {num2} is {sum}")


add_num()
