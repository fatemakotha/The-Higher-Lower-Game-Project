import random
from art import logo, vs
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
def get_random_account():
  """Get data from random account"""
  return random.choice(data)
    
#Make sure the randomly chosen accounts are not the same.....2
if account_a == account_b:
    account_b = random.choice(data)



# Format account data into printable format.....3
def format_data(account):
  """Format account into printable format: name, description and country"""
  name = account["name"]
  description = account["description"]
  country = account["country"]
  # print(f'{name}: {account["follower_count"]}')
  return f"{name}, a {description}, from {country}"


#checking answer:
def check_answer(guess, a_followers, b_followers):
  """Checks followers against user's guess 
  and returns True if they got it right.
  Or False if they got it wrong.""" 
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"


# Ask user for a guess......4
guess = input("Who has more followers? Type 'A' or 'B': ").lower()

#Set the follower count.....5
follower_count_a = account_a["follower_count"]
follower_count_b = account_b["follower_count"]

#Set score.....7
print(logo)
score = 0
#Set game status
is_game_over = False

while not is_game_over:
    # Check if user is correct.....6
    if guess == "a" and follower_count_a > follower_count_b:
        score += 1
        print(f"You win, your score is {score}")
    elif guess == "b" and follower_count_b > follower_count_a:
        score += 1
        print(f"You win, your score is {score}")
    elif guess == "a" and follower_count_a < follower_count_b:
        is_game_over = True
        print("You Lose")
    elif guess == "b" and follower_count_b < follower_count_a:
        is_game_over = True
        print("You Lose")
    












## Get follower count.
## If Statement

# Feedback.

# Score Keeping.

# Make game repeatable.

# Make B become the next A.

# Add art.

# Clear screen between rounds.