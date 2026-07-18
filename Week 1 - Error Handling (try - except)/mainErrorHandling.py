def startErrorFindingComplex():
    availableLanguages = ["Python", "JavaScript", "Java", "C++"]
    print("Data Entry System")
    while True:
        try:
            enteredInteger = int(input("Enter an integer = "))
            divisor = int(input("Enter the divisor for division = "))
            divisionResult = enteredInteger / divisor
            print(f"Division result = {divisionResult}")
            print(f"Available Languages List = {availableLanguages}")
            requestedIndex = int(input("Enter the index number of the language you want (0-3) = "))
            selectedProgrammingLanguage = availableLanguages[requestedIndex]
            print(f"Selected Programming Language = {selectedProgrammingLanguage}")
            print("Transaction Successful. All data entries verified.")
            break
        except ValueError:
            print(
                "Invalid character detected. Please enter only numeric values into the input fields.")
            print("-" * 50)
        except ZeroDivisionError:
            print(
                "Undefined operation. A number cannot be divided by zero. Please enter a divisor other than 0.")
            print("-" * 50)
        except IndexError:
            print(
                "Boundary Error. List range exceeded. The index you entered is outside the bounds of the existing array. (Enter between 0-3).")
            print("-" * 50)
startErrorFindingComplex()