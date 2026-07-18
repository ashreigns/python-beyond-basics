class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return "Animal sound is not defined."


class Cat(Animal):
    def make_sound(self):
        return "meow"


class Dog(Animal):
    def make_sound(self):
        return "woof"


animals = []

while True:
    print("\n1. Add Cat")
    print("2. Add Dog")
    print("3. Make Animals Speak")
    print("4. Exit")

    choice = input("Your choice = ").strip()

    if choice == "1":
        name = input("Cat's name = ").strip()
        new_cat = Cat(name)
        animals.append(new_cat)
        print(f"{name} has been added to the list.")
    elif choice == "2":
        name = input("Dog's name = ").strip()
        new_dog = Dog(name)
        animals.append(new_dog)
        print(f"{name} has been added to the list.")
    elif choice == "3":
        print("\n--- Animal Sounds ---")
        for animal in animals:
            print(f"{animal.name} the Animal goes = {animal.make_sound()}")
    elif choice == "4":
        print("Closing...")
        break