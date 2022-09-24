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
def format_data(account): #re-use it to format for account a and b
    """Format the account data into printable format"""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr} from {account_country}"


# Generate a random account from the game data.
account_a = random.choice(data)
account_b = random.choice(data)

if account_a == account_b:
    account_b = random.choice(data)

print(f"Compare A: {format_data(account_a)}") #format_data returns "name", "description" and "country" for account_a
print(f"Compare B: {format_data(account_b)}") #format_data returns "name", "description" and "country" for account_b

# #Format the account data into printable format
# account_name = account_a["name"]
# account_descr = account_a["description"]
# account_country = account_a["country"]
# print(f"{account_name}, a {account_description} from {account_country}")







