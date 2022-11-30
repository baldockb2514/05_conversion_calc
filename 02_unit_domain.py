# ask user for domain/unit
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

# Main routine goes here
keep_going = ""
while keep_going == "":
    unit_type = unit_domain()
    print("You chose", unit_type)

    print()