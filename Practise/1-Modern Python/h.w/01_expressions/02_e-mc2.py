def main():
    c = 299792458  # speed of light
    while True:
        try:
            mass = float(input("Enter mass (in kg): "))
            if mass == 0:
                print('Exiting!')
                break
            e = mass * c**2  # formula
            print(f"{e} joules of energy!")
        except ValueError:
            print("Invalid input. Please enter valid number")


main()
