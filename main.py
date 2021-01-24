#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


total_symbols = []
total_letters =[]
total_numbers = []

# outputstring to be used to use the .join command
output_string = " "

for ra_symbols in range(0, nr_symbols):
	random_symbol = random.randint(0, 8)
	total_symbol = symbols[random_symbol]
	total_symbols.append(total_symbol)
	symbol_str = output_string.join(total_symbols)


for ra_letters in range(0, nr_letters):
	random_letter = random.randint(0, 50)
	total_letter = letters[random_letter]
	total_letters.append(total_letter)
	letter_str = output_string.join(total_letters)


for ra_numbers in range(0, nr_numbers):
	random_number = random.randint(0, 9)
	total_number = numbers[random_number]
	total_numbers.append(total_number)
	number_str = output_string.join(total_numbers)

#detaching while attaching password list to Strings Separated by spaces
password = f"{symbol_str} {letter_str} {number_str}"

# detaching password to form one list 
password_array = password.split(" ")

# randomizing the list order
random_pass = random.sample(password_array, len(password_array))

# attaching the list to form one string
password = "".join(random_pass)

# lenght of the string
password_length = len(password)

print(f"\nYour desired passwod length is {password_length} characters and we suggest you use this: {password}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P