username = input("Please enter the name you want to save = ")

savedNames = open("names.txt", "a", encoding="utf-8")

savedNames.write(username + "\n")

savedNames.close()