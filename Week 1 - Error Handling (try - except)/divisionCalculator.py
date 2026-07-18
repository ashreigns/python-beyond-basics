def divisionstart():
    while True:
        try:
            dividend = int(input("Enter the number to be divided (Dividend) = "))
            divisor = int(input("Enter the divisor (Denominator) = "))
            result = dividend / divisor
            print(f"Result is = {result}")
            break
        except ZeroDivisionError:
            print("Error = A number cannot be divided by zero; please enter a denominator other than 0.")
        except ValueError:
            print("Error = Please enter a valid integer.")
divisionstart()