import random
from art import logo
print(logo)
from art import vs
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


# Generate a random account from the game data.
choice_a = random.choice(data)
choice_b = random.choice(data)
print(f"Compare A: {choice_a} \n {vs} \n Against B: {choice_b}")

a = choice_a["follower_count"]
print(a)
b = choice_b["follower_count"]
print(b)
#Let the user make a guess
guess = input("Who has more follower? a or b: ")
#Assign values according to the guess
if guess == "a":
    guess = a
    vari = b
    print(guess)
else:
    guess == "b"
    guess = b
    vari = a
    print(guess)
    if guess > vari:
        print("You're right")
    else:
        print("You loose")




