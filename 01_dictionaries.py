# dictionaries for units

def domain_dictionaries():
  
    # length/distance unit dictionary
    length_dict = {
        "mm": 1000000,
        "cm": 100000,
        "m": 1000,
        "km": 1
    }

    # time unit dictionary
    time_dict = {
        "ms": 3600000,
        "s": 3600,
        "m": 60,
        "h": 1
        }

    # weight unit dictionary
    weight_dict = {
        "mg":1000000,
        "g": 1000,
        "kg": 1
    }

to_convert = input("What number would you like to convert?: ")
convert_to = input("What unit would you like to convert into?: ")
