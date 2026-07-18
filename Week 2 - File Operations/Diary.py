from datetime import datetime
import os

fileName = "diary.txt"

print("Diary")

noteInput = input("Enter what you want to write in the diary = ").strip()

currentTime = datetime.now()

formattedDate = currentTime.strftime("%d.%m.%Y %H:%M")

with open(fileName, "a", encoding="utf-8") as file:
    file.write(f"date = [{formattedDate}] paragraph = {noteInput}\n")

print("Diary saved.")