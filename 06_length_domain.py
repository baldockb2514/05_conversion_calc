import re

response = str(re.split(r'(\d+)', input("What number would you like to convert, and what is it's unit?: ").lower()))
unit_1 = re.sub(r"[^A-Za-z]+", '', response)
number_str = re.sub(r"[^0.-9.]+", '', response)

number = float(number_str)

def length_domain():

    # Valid time units
    length_unit = ["km", "m", "cm", "mm"]

    # Dictionary of length units, by how to turn them into meters
    length_dict = {
        "mm": 1000,
        "cm": 100,
        "m": 1,
        "km": 0.01
    }

    valid = False 
    while not valid:

        # get the unit to convert into
        unit_2 = input("What unit would you like to convert to?: ").lower()
        unit_diff = re.match(unit_2, unit_1)

        # output error if second unit is not valid
        if unit_2 not in length_unit:
            print("Please input a valid unit.")
            print()

        elif unit_diff:
            print("Please input two different units.")
            print()

        else:
            valid = True
        

    # convert first unit into meters, then into second unit
    multiply_by_1 = length_dict[unit_1]
    in_meters = number / multiply_by_1
    multiply_by_2 = length_dict[unit_2]
    result = in_meters * multiply_by_2

    # output the final result and round to 2 decimals
    print("%.2f" % number, unit_1, "=", "%.2f" % result, unit_2)






