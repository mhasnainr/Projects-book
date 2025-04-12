def main():
    sec_per_min = 60
    min_per_hour = 60
    hours_per_day = 24
    days_per_year = 365
    sec_per_year = sec_per_min * min_per_hour * hours_per_day * days_per_year
    print(f"There are {sec_per_year} seconds in a year")


main()
