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

