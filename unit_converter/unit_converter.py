def convert_units(value, unit_in, unit_out):
    conversions = {
                    "feet":
                            {"meters": 0.3048},
                    "inches": {"meters": 0.0254},
                    "kilometers": 
                            {"meters": 1000},
                    "meters":
                            {
                             "feet": 3.2808399,
                             "inches": 0.0254,
                             "kilometers": 0.001,
                             "meters": 1,
                             "miles": 0.000621371192,
                             "yards": 1.0936133                             
                            },
                    "miles":
                            {"meters": 1609.344},
                    "yards": {"meters": 0.9144}
                      }

    new_value = conversions[unit_in]["meters"] * value

    return new_value

def main():

    print("\nLet's convert some units!")

    while True:
        unit1 = input("\nEnter the starting unit: ")
        unit2 = "meters" #input(f"\nEnter the unit into which you'd like to convert {unit1}: ")

        num_of_unit1 = float(input(f"\nPlease enter the number of {unit1} you'd like converted to {unit2} ('q' to quit): "))
        num_of_unit2 = convert_units(num_of_unit1, unit1, unit2)

        print(f"{num_of_unit1} {unit1} is equivalent to {num_of_unit2} {unit2}")
        if str(num_of_unit1).lower() == "q":
            break

main()