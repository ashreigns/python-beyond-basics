def divisionOperation():
    while True:
        try:
            firstNumber = int(input("Enter the number to be divided (Numerator) = "))
            secondNumber = int(input("Enter the divisor (Denominator) = "))
            resultValue = firstNumber / secondNumber
            print(f"Division result = {resultValue}")
            break
        except ValueError:
            print("Please enter a valid number, not a letter!")
        except ZeroDivisionError:
            print("In mathematics, a number cannot be divided by 0. Enter another number for the denominator.")
divisionOperation()