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
print(account_a)
print(account_b)
#Make sure the randomly chosen accounts are not the same.....2
if account_a == account_b:
    account_b = random.choice(data)



# Format account data into printable format.

# Ask user for a guess.

# Check if user is correct.
## Get follower count.
## If Statement

# Feedback.

# Score Keeping.

# Make game repeatable.

# Make B become the next A.

# Add art.

# Clear screen between rounds.