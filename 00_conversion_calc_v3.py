# functions go here

import re

# Heading
def statement_generator(text, decoration):
    
    # Make string with five characters
    ends = decoration * 5 

    #add decoration to start and ent of statement
    statement = "{} {} {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""


# ask user for number and first unit, check if valid, output error if not, respond if is
def unit_domain():



    valid = False 
    while not valid:

        global unit_1
        global number


        # valid responses
        length_unit = ["km", "cm", "mm"]
        weight_unit = ["mg", "g", "kg"]
        time_unit = ["h", "s", "ms",]

        valid_2 = False
        while not valid_2:

            response = str(re.split(r'(\d+)', input("What number would you like to convert, and what is it's unit?: ").lower()))
            unit_1 = re.sub(r"[^A-Za-z]+", '', response)
            number_str = re.sub(r"[^0.-9.]+", '', response)

            if number_str == "":
                print("Please input a number!")
                print()

            else:
                valid_2 = True

        number = float(number_str)

        # Checks for valid response and returns distance, time or weight
        
        if unit_1 in weight_unit:
            return "Weight"

        elif unit_1 in time_unit:
            return "Time"

        elif unit_1 in length_unit:
            return "Length"

        elif unit_1 == "m":
            want_minute = input("Press <enter> for minutes or any key for meter: ")
            if want_minute == "":
                return "Time"
            else:
                return "Length"

        else:
            # if response is not valid, output an error
            print(" Please choose a valid unit!")
            print()


# instructions for user
def instructions():

    statement_generator("Instructions / Information", "=")
    print()
    print("This conversion calculator only takes three types of units. (Time, Weight, and length).")
    print()
    print("Please input the number and unit you want to convert. When inputting the unit, please us the shortened version.")
    print("For example; cm for centimeters, kg for kilograms, h for hours.")
    print()
    print("Then input the unit you would like to convert into. Please make sure it is the same type of unit as the first. (Time / Weight / Length)")
    print()
    print("Complete as many calculations as necessary, pressing <enter> at the end of each calculation to continue, or any key to quit.")
    print()
    return ""


# calculations for converting length units
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


# calculations for converting time units
def time_domain():

    # Dictionary of time units, by how to turn them into hours
    time_dict = {
        "ms": 3600000,
        "s": 3600,
        "m": 60,
        "h": 1
    }

    # Valid time units
    time_unit = ["h", "m", "s", "ms"]

    valid = False 
    while not valid:

        # get the unit to convert into
        unit_2 = input("What unit would you like to convert to?: ").lower()
        unit_diff = re.match(unit_2, unit_1)

        # output error if second unit is not valid
        if unit_2 not in time_unit:
            print("Please input a valid unit.")
            print()

        elif unit_diff:
            print("Please input two different units.")
            print()

        else:
            valid = True

    # convert first unit into meters, then into second unit
    multiply_by_1 = time_dict[unit_1] 
    in_meters = number / multiply_by_1
    multiply_by_2 = time_dict[unit_2]
    result = in_meters * multiply_by_2

    # output the final result and round to 2 decimals
    print("%.2f" % number, unit_1, "=", "%.2f" % result, unit_2)


# calculations for converting weight units
def weight_domain():


    # Dictionary of weight units, by how to turn them into grams
    weight_dict = {
        "mg":1000,
        "g": 1,
        "kg": 0.001
    }

    # Valid Weight units
    weight_unit = ["mg", "g", "kg"]

    valid = False 
    while not valid:

        # get the unit to convert into
        unit_2 = input("What unit would you like to convert to?: ").lower()
        unit_diff = re.match(unit_2, unit_1)

        # output error if second unit is not valid
        if unit_2 not in weight_unit:
            print("Please input a valid unit.")
            print()

        elif unit_diff:
            print("Please input two different units.")
            print()
            
        else:
            valid = True

    # convert first unit into meters, then into second unit
    multiply_by_1 = weight_dict[unit_1]
    in_meters = number / multiply_by_1
    multiply_by_2 = weight_dict[unit_2]
    result = in_meters * multiply_by_2

    # output the final result and round to 2 decimals
    print("%.2f" % number, unit_1, "=", "%.2f" % result, unit_2)


# main routine goes here
statement_generator("Unit converter for Length, Weight, and Time", "-")

# Display instructions if user has not used the program before
first_time = input("Press <enter> to see the instructions or any key to continue ")

if first_time == "":
    instructions()

# Loop to allow multiple calculations per session
keep_going = ""
while keep_going == "":

    domain_unit = unit_domain()

    if domain_unit =="Weight":
        weight_domain()


    elif domain_unit =="Time":
        time_domain()

    else:
        length_domain()

    print()
    keep_going = input("Press <enter> to continue or any key to quit ")
    print()

statement_generator("Thanks for using the conversion calculator!", "*")
print()
