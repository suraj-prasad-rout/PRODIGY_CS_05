import string

# Get the password from the user
password = input("Enter your password\n")

# Check for different types of characters in the password
upper_case = any((1 if c in string.ascii_uppercase else 0 for c in password))
lower_case = any((1 if c in string.ascii_lowercase else 0 for c in password))
special = any((1 if c in string.punctuation else 0 for c in password))
digits = any((1 if c in string.digits else 0 for c in password))

# List to store the presence of different character types
charecter = [upper_case, lower_case, special, digits]

# Calculate the length of the password
length = len(password)

# Read the common password list
with open('commonpass.txt', 'r') as f:
    common_pass = f.read().splitlines()

# Check if the password is a common password
if password in common_pass:
    print("password found in common password list. Score 0 / 7 ")
    exit()

# Initialize the score
score = 0

# Score based on length of the password
if length > 8:
    score += 1
if length > 12:
    score += 1
if length > 17:
    score += 1
if length > 20:
    score += 1

# Print the password length and the points added based on length
print(f"password lenght is {str(length)}, adding {str(score)} points!")

# Score based on the presence of different character types
if sum(charecter) > 1:
    score += 1
if sum(charecter) > 2:
    score += 1
if sum(charecter) > 3:
    score += 1

# Print the number of different character types and the updated score
print(
    f"password contain {str(sum(charecter))} different charecter type adding points to a total of {score}")

# Print the strength of the password based on the score
if score <= 4:
    print(f"your password is quite weak {str(score)} / 7")
elif score > 4 and score <= 6:
    print(f"your password is pretty good {str(score)} / 7")
else:
    print(f"your password is strong ! {str(score)} / 7")
