import helper

print("Prime number checker")
number = int(input("Please enter the number you want to check = "))

if helper.is_prime(number):
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")

print("Palindrome text checker")
text = input("Enter the text you want to check = ")

if helper.is_palindrome(text):
    print(f"'{text}' is a palindrome")
else:
    print(f"'{text}' is not a palindrome")

print("Gcd Lcm checker")

num1 = int(input("Please enter the 1st number = "))
num2 = int(input("Please enter the 2nd number = "))

gcd = helper.find_gcd(num1, num2)
lcm = helper.find_lcm(num1, num2)

print(f"GCD of {num1} and {num2} = {gcd}")
print(f"LCM of {num1} and {num2} = {lcm}")