from datetime import datetime

print("How Many Days Have You Lived?")

birth_input = input("Enter your date of birth (DD.MM.YYYY, e.g. 15.04.2002) = ")

birth_date = datetime.strptime(birth_input, "%d.%m.%Y")

today = datetime.now()

difference = today - birth_date

days_lived = difference.days

print("-" * 40)
print(f"Date of Birth = {birth_date.strftime('%d %B %Y')}")
print(f"Today's Date  = {today.strftime('%d %B %Y')}")
print(f"You have been living for exactly {days_lived} days.")