import random
from art import logo, vs
print(logo)
from replit import clear

# print(vs)
from game_data import data
# # print(data)
# data = [
#     {
#         'name': 'Instagram',
#         'follower_count': 346,
#         'description': 'Social media platform',
#         'country': 'United States'
#     },

# Generate a random account from the game data.....1
account_a = random.choice(data)
account_b = random.choice(data)
# print(account_a)
# print(account_b)
#Make sure the randomly chosen accounts are not the same.....2
if account_a == account_b:
    account_b = random.choice(data)



# Format account data into printable format.....3
#For account_a:
name = account_a["name"]
descr = account_a["description"]
country = account_a["country"]
print(f"Compare A {name}, {descr}, from {country}")
print(vs)
#For account_a:
name = account_b["name"]
descr = account_b["description"]
country = account_b["country"]
print(f"Compare B {name}, {descr}, from {country}")


# Ask user for a guess......4
guess = input("Who has more followers? Type 'A' or 'B': ").lower()

#Set the follower count.....5
follower_count_a = account_a["follower_count"]
follower_count_b = account_b["follower_count"]

#Set score.....7
score = 0

# Check if user is correct.....6
if guess == "a" and follower_count_a > follower_count_b:
    
    print("You win")
elif guess == "b" and follower_count_b > follower_count_a:
    print("You win")
elif guess == "a" and follower_count_a < follower_count_b:
    print("You Lose")
elif guess == "b" and follower_count_b < follower_count_a:
    print("You Lose")
    












## Get follower count.
## If Statement

# Feedback.

# Score Keeping.

# Make game repeatable.

# Make B become the next A.

# Add art.

# Clear screen between rounds.