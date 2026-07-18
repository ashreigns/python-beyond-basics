def indexController():
    names = ["ash", "john", "pal", "william"]
    print("Names on the list")
    print("Theres 4 people on the list")
    while True:
        try:
            wantedIndex = int(input("Enter the number of the person you want to see. (0-3): "))
            chosenName = names[wantedIndex]
            print(f"The person you selected in the Index = {chosenName}")
            break
        except IndexError:
            print("The index you entered is outside the list boundaries; please enter a number between 0 and 3.")
        except ValueError:
            print("The index must be an integer; please do not enter letters.")
indexController()