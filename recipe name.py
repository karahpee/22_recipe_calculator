# functions go below

def not_blank(question):
    valid = False

    while not valid:
        response = input(question)

        if response != " ":
            return response
        else:
            print("Enter a valid recipe name.")

# main routine goes below

name = not_blank("Recipe: ")
