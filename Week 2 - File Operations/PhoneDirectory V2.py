import os
fileName = "directory.txt"

def loadDirectory():
    directory = {}
    if os.path.exists(fileName):
        with open(fileName, "r", encoding="utf-8") as file:
            for line in file:
                if "=" in line:
                    name, number = line.strip().split("=", 1)
                    directory[name] = number
    return directory

def saveDirectory(directory):
    with open(fileName, "w", encoding="utf-8") as file:
        for name, number in directory.items():
            file.write(f"Name = {name},1 Number = {number}\n")

directory = loadDirectory()

while True:
    print("Directory")
    print("1. Add Person")
    print("2. List People")
    print("3. Exit")

    choice = input("Select the operation you want to perform (1/2/3) = ")

    if choice == "1":
        name = input("Name of the person to be added = ").strip()
        number = input("Phone number = ").strip()
        directory[name] = number
        saveDirectory(directory)
        print(f"{name} has been saved to the directory.")
    elif choice == "2":
        if not directory:
            print("Your directory is currently empty")
        else:
            print("Registered People")
            for name, number in directory.items():
                print(f"Name = {name} - Number = {number}")
    elif choice == "3":
        print("Closing..")
        break
    else:
        print("Invalid choice, please try again")