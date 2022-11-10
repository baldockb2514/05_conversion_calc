# functions go here

# Puts series of symbols at start and end of text (for emphasis)
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

    # list of valid domains
    weight_ok = ["length", "distance", "l", "d"]
    time_ok = ["time", "t"]
    mass_ok = ["mass", "weight", "m", "w"]

    valid = False 
    while not valid:

        # ask user for choice and change response to lowercase
        response = input("Unit type (distance/time/weight) ").lower()

        # Checks for valid response and returns distance, time or weight
        
        if response in weight_ok:
            return "weight"

        elif response in time_ok:
            return "time"

        elif response in mass_ok:
            return "weight"

        else:
            # if response is not valid, output an error
            print(" Please choose a valid unit type!")
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


# dictionary and valid answers for length domain
def length_units():

    length_dictionary = {
        mm_ok: 1000,
        cm_ok: 100,
        meter_ok: 1,
        km_ok: 0.001
    }

    mm_ok = ["mm", "millimeter", "millimetre"]
    cm_ok = ["cm", "centimeter", "centimetre"]
    meter_ok = ["m", "meter", "metre"]
    km_ok = ["km", "kilometer", "kilometre"]
    length_unit_ok = ["mm", "millimeter", "millimetre", "cm", "centimeter", "centimetre", "m", "meter", "metre", "km", "kilometer", "kilometre"]


# dictionary and valid answers for time domain
def time_units():

    time_dict = {
        ms_ok: 3600000,
        s_ok: 3600,
        minute_ok: 60,
        h_ok: 1
    }

    ms_ok = ["ms", "millisecond"]
    s_ok = ["s", "second"]
    minute_ok = ["m", "minute"]
    h_ok = ["h", "hour", "hours"]
    time_unit_ok = ["ms", "millisecond", "s", "second", "m", "minute", "h", "hour", "hours"]


# dictionary and valid answers for weight domain
def weight_units():

    weight_dict = {
        mg_ok:1000,
        g_ok: 1,
        kg_ok: 0.001
    }

    mg_ok = ["mg", "milligram"]
    g_ok = ["g", "gram"]
    kg_ok = ["kg", "kilogram"]
    weight_unit_ok = ["mg", "milligram", "g", "gram", "kg", "kilogram"]



# main routine goes here
statement_generator("Unit Conversion calculator for Length, Time, & Weight", "-")

# Display instructions if user has not used the program before
first_time = input("Press <enter> to see the instructions or any key to continue ")

if first_time == "":
    instructions()

# Loop to allow multiple calculations per session
keep_going = ""
while keep_going == "":

    # Aks the user for the file type
    chosen_domain = unit_domain()
    print("You chose", chosen_domain)

    # 
    if chosen_domain =="weight":
        int_bits()

    # For images, ask for width and height
    # (must be integers more than / equal to 1)
    elif data_type == "image":
       image_bits()

    # For text, ask for a string
    else:
        text_bits()
    
    print()
    keep_going = input("Press <enter> to continue or any key to quit ")
    print()

