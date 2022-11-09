# dictionaries for units

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

to_convert = input("What number would you like to convert?: ")
unit_convert = input("What unit is this number in?: ")
convert_to = input("What unit would you like to convert into?: ")

