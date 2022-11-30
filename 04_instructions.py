def statement_generator(text, decoration):
    
    # Make string with five characters
    ends = decoration * 5 

    #add decoration to start and ent of statement
    statement = "{} {} {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""


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

