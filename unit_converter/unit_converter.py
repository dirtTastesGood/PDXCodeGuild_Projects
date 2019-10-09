def convert_units(value, unit_in, unit_out):
    conversions = {
                    "feet":
                            {
                             "feet": 1,
                             "kilometers": 0.0003048,
                             "meters": 0.3048,
                             "miles":  0.00018939393939394
                            },
                    "kilometers": 
                            {
                             "feet": 3280.8399,
                             "kilometers": 1,
                             "meters": 1000,
                             "miles": 0.62137
                            },
                    "meters":
                            {
                             "feet": 3.2808399,
                             "kilometers": 0.001,
                             "meters": 1,
                             "miles": 0.000621371192                              
                            },
                    "miles":
                            {
                             "feet": 5280, 
                             "kilometers": 1.609344,
                             "meters": 1609.344,
                             "miles": 1
                            }
                      }
    conversion_rate = conversions[unit_in][unit_out]
    new_value = value * conversion_rate

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