def convert_units(value, unit_in, unit_out):
    conversion_sets = {"feet":{"meters": 0.3048}}

    conversion_rate = conversion_sets[unit_in][unit_out]
    new_value = value * conversion_rate

    return new_value

def main():
    while True:
        unit1 = "feet"
        unit2 = "meters"

        num_of_unit1 = float(input(f"\nPlease enter the number of {unit1} you'd like converted to {unit2} ('q' to quit): "))
        num_of_unit2 = convert_units(num_of_unit1, unit1, unit2)

        print(f"{num_of_unit1} {unit1} is equivalent to {num_of_unit2} {unit2}")
        if str(num_of_unit1).lower() == "q":
            break

main()