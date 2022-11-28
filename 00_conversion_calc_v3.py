# functions go here


def statement_generator(text, decoration):
    
    # Make string with five characters
    ends = decoration * 5 

    #add decoration to start and ent of statement
    statement = "{} {} {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""


# ask user for domain/unit, checks domain is valid
def unit_domain():

    import re

    valid = False 
    while not valid:

        # ask user for choice and change response to lowercase
        response = str(re.split(r'(\d+)', input("What number would you like to convert?: ").lower()))
        global unit_1
        unit_1 = str(re.sub(r"[^A-Za-z]+", '', response))
        global number
        number = float(re.sub(r"[^0.-9.]+", '', response))
        print(unit_1)
        print(number)

        # valid responses
        length_unit_ok = ["km", "kilometer", "kilometre", "kilometers", "kilometres", "meter", "metre", "meters", "metres", "cm", "centimeter", "centimetre", "centimeters", "centimetres", "mm", "millimeter", "millimetre", "millimeters", "millimetres"]
        weight_unit_ok = ["mg", "milligram", "milligrams", "g", "gram", "grams", "kg", "kilogram", "kilograms"]
        time_unit_ok = ["h", "hour", "hours", "minute", "minutes", "s", "second", "seconds", "ms", "millisecond", "milliseconds"]


        # Checks for valid response and returns distance, time or weight
        
        if unit_1 in weight_unit_ok:
            return "Weight"

        elif unit_1 in time_unit_ok:
            return "Time"

        elif unit_1 in length_unit_ok:
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
    print("Please choose a unit domain (length / time / weight)")
    print()
    print("Please insert the number and it's unit seperatly. Then insert the unit the number will be converted to. ")
    print()
    print("Complete as many calculations as necessary, pressing <enter> at the end of each calculation or any key to quit.")
    print()
    return ""


# calculations for converting length units
def length_domain():

    # Dictionary of length units, by how to turn them into meters
    length_dict = {
        "mm": 1000,
        "cm": 100,
        "m": 1,
        "km": 0.01
    }

    # convert variable into string for use in dictionary
    mm_ok = "mm"
    cm_ok = "cm"
    meter_ok = "m"
    km_ok = "km"

    # Valid time units
    mm_ok = ["mm", "millimeter", "millimetre", "millimeters", "millimetres"]
    cm_ok = ["cm", "centimeter", "centimetre", "centimeters", "centimetres"]
    meter_ok = ["m", "meter", "metre", "meters", "metres"]
    km_ok = ["km", "kilometer", "kilometre", "kilometers", "kilometres"]
    length_unit_ok = ["km", "kilometer", "kilometre", "kilometers", "kilometres", "m", "meter", "metre", "meters", "metres", "cm", "centimeter", "centimetre", "centimeters", "centimetres", "mm", "millimeter", "millimetre", "millimeters", "millimetres"]

    # get the unit to convert into
    unit_2 = input("What unit would you like to convert to?: ").lower()

    # output error if second unit is not valid
    if unit_2 not in length_unit_ok:
        print("Please input a valid unit.")
        length_domain()

    # look up the value of the first unit
    multiply_by_1 = length_dict[unit_1]

    # convert the first numbers' unit into meters using division
    in_meters = number / multiply_by_1

    # look up the value of the second unit
    multiply_by_2 = length_dict[unit_2]

    # get the final result by multiplying the number in meters by the second unit
    result = in_meters * multiply_by_2

    # output the final result and rounds to 2 decimals
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

    # converts variable into string for use in dictionary
    ms_ok = "ms"
    s_ok = "s"
    minute_ok = "m"
    h_ok = "h"

    # Valid time units
    ms_ok = ["ms", "millisecond", "milliseconds"]
    s_ok = ["s", "second", "seconds"]
    minute_ok = ["m", "minute", "minutes"]
    h_ok = ["h", "hour", "hours"]
    time_unit_ok = ["h", "hour", "hours", "m", "minute", "minutes", "s", "second", "seconds", "ms", "millisecond", "milliseconds"]

    # get the unit to convert into
    unit_2 = input("What unit would you like to convert to?: ").lower()

    # outputs error if second unit is not valid
    if unit_2 not in time_unit_ok:
        print("Please input a valid unit.")
        time_domain()

    # look up the value of the first unit
    multiply_by_1 = time_dict[unit_1]
    
    # convert the first numbers' unit into hours using division  
    in_meters = number / multiply_by_1

    # look up the value of the second unit
    multiply_by_2 = time_dict[unit_2]

    # get the final result by multiplying the number in hours by the second unit
    result = in_meters * multiply_by_2

    # output the final result and rounds to 2 decimals
    print("%.2f" % number, unit_1, "=", "%.2f" % result, unit_2)


# calculations for converting weight univts
def weight_domain():

    # Dictionary of weight units, by how to turn them into grams
    weight_dict = {
        "mg":1000,
        "g": 1,
        "kg": 0.001
    }

    # converts variable into string for use in dictionary
    mg_ok = "mg"
    g_ok = "g"
    kg_ok = "kg"

    # Valid Weight units
    mg_ok = ["mg", "milligram", "milligrams"]
    g_ok = ["g", "gram", "grams"]
    kg_ok = ["kg", "kilogram", "kilograms"]
    weight_unit_ok = ["mg", "milligram", "milligrams", "g", "gram", "grams", "kg", "kilogram", "kilograms"]

    # get the unit to convert into
    unit_2 = input("What unit would you like to convert to?: ").lower()

    # outputs error if second unit is not valid
    if unit_2 not in weight_unit_ok:
        print("Please input a valid unit.")
        weight_domain()

    # look up the value of the first unit
    multiply_by_1 = weight_dict[unit_1]
    
    # convert the first numbers unit into grams using division
    in_meters = number / multiply_by_1

    # look up the value of the second unit
    multiply_by_2 = weight_dict[unit_2]

    # get the final result by multiplying the number in grams by the second unit
    result = in_meters * multiply_by_2

    # output the final result and rounds to 2 decimals
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


