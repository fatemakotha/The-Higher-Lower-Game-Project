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
print(follower_a)
a = choice_a["follower_count"]

guess = input("Who has more follower? a or b: ")


