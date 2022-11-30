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
    distance_ok = ["length", "distance", "l", "d"]
    time_ok = ["time", "t"]
    mass_ok = ["mass", "weight", "m", "w"]

    valid = False 
    while not valid:

        # ask user for choice and change response to lowercase
        response = input("Unit type (distance/time/weight) ").lower()

        # Checks for valid response and returns distance, time or weight
        
        if response in distance_ok:
            return "distance"

        elif response in time_ok:
            return "time"

        elif response in mass_ok:
            return "weight"

        else:
            # if response is not valid, output an error
            print(" Please choose a valid unit type!")
            print()


# dictionaries depending on domain
def domain_dictionaries():

  
    # length/distance unit dictionary
    length_dict = {
        "mm": 1000,
        "cm": 100,
        "m": 1,
        "km": 1000
    }

    # time unit dictionary
    time_dict = {
        "ms": 60000,
        "s": 60,
        "m": 1,
        "h": 60
        }

    # weight unit dictionary
    weight_dict = {
        "mg":1000,
        "g": 1,
        "kg": 1000
    }


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

    # For integers, ask for the integer (must be more than / equal to 0)
    if chosen_domain =="integer":
        ()

    # For images, ask for width and height
    # (must be integers more than / equal to 1)
    

    # For text, ask for a string

    
    print()
    keep_going = input("Press <enter> to continue or any key to quit ")
    print()

