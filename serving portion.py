# function goes below

def not_blank(question):
    valid = False

    while not valid:
        response = input(question)

        if response != "":
            return response
        else:
            print("Enter a valid serving amount.")


# main routine goes below

name = not_blank("Serving amount: ")
name = not_blank("Portion of single serving: ")
