import random

print("Dice Rolling Simulation")

num_dice = int(input("How many times should the dice be rolled? = "))

total_score = 0

for i in range(num_dice):
    dice_roll = random.randint(1, 6)

    total_score = total_score + dice_roll

average = total_score / num_dice

print("---------------------")
print(f"Total number of dice rolled = {num_dice}")
print(f"Total value of the dice     = {total_score}")
print(f"Average of the dice rolls   = {average:.2f}")