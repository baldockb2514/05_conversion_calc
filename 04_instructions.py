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
    print("Please choose a unit domain (length / time / weight)")
    print()
    print("Please insert the number and it's unit seperatly. Then insert the unit the number will be converted to. ")
    print()
    print("Complete as many calculations as necessary, pressing <enter> at the end of each calculation or any key to quit.")
    print()
    return ""