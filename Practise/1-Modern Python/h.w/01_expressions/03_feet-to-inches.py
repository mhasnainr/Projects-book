def main():
    foot: int = 12
    ask: float = float(input("Enter feet (converting it to inches): "))
    result = ask * foot
    if ask == 1:
        unit = 'foot'
    else:
        unit = 'feet'
    print(f"There are {result} inches in {ask} {unit}")


main()
