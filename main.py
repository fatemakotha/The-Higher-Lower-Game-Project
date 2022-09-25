import random
from art import logo, vs
from replit import clear

# print(vs)
from game_data import data

# # print(data)


# Generate a random account from the game data.....1
def get_random_account():
    """Get data from random account"""
    return random.choice(data)


# Format account data into printable format.....3
def format_data(account):
    """Format account into printable format: name, description and country"""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    # print(f'{name}: {account["follower_count"]}')
    return f"{name}, a {description}, from {country}"


#Check if user is correct.....6
def check_answer(guess, a_follower_count, b_follower_count):
    """Checks followers against user's guess 
  and returns True if they got it right.
  Or False if they got it wrong."""
    if a_follower_count > b_follower_count:
        return guess == "a"
    else:
        return guess == "b"


# Check if user is correct.....6
# if guess == "a" and follower_count_a > follower_count_b:
#     score += 1
#     print(f"You win, your score is {score}")
# elif guess == "b" and follower_count_b > follower_count_a:
#     score += 1
#     print(f"You win, your score is {score}")
# elif guess == "a" and follower_count_a < follower_count_b:
#     is_game_over = True
#     print("You Lose")
# elif guess == "b" and follower_count_b < follower_count_a:
#     is_game_over = True
#     print("You Lose")


#Define the game:
def game():
    print(logo)
    score = 0
    game_should_continue = True
    account_a = get_random_account()
    account_b = get_random_account()

    while game_should_continue:  #if guessed right account a becomes b
        account_a = account_b
        account_b = get_random_account(
        )  #if guessed right account b                                             selects randomly again
        if account_a == account_b:
            account_b = get_random_account(
            )  #incase the 2 randomly chosen                                          accounts end up the same

        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        print(f"Against B: {format_data(account_b)}.")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        is_correct = check_answer(guess, a_follower_count, b_follower_count)
        # is_correct = if a_followers > b_followers:
        #      return guess == "a"
        # else:
        #      return guess == "b"
        # is_correct = True

        clear()
        print(logo)
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")


game()

## Get follower count.
## If Statement

# Feedback.

# Score Keeping.

# Make game repeatable.

# Make B become the next A.

# Add art.

# Clear screen between rounds.
