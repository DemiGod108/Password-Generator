import random


alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

letters = int(input("How many letter do you want in your password: "))

nums = int(input("How many numbers you want to include in your password: "))

sy = int(input("How many symbols do you wanna include in your password: "))


temp_password = []
c = letters+nums+sy

for i in range(c):
	if i<letters:
		temp_password.append(random.choice(alpha))
		
	if i<nums:
		temp_password.append(random.choice(numbers))
		
	if i<sy:
		temp_password.append(random.choice(symbols))

random.shuffle(temp_password)

result = "".join(temp_password)

print(f"Your password: {result}\nTotal number of letter(s): {letters}\nTotal number of number(s): {nums}\nTotal number of symbol(s): {sy}")
