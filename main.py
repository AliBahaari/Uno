import random


# Config
all_cards = []

for i in range(1, 14):
    for j in ['Heart', 'Spade', 'Diamond', 'Club']:

        sample_card = {
            "type": j,
            "value": i
        }
        all_cards.append(sample_card)


# All Users
all_users = [
    {
        "id": 1,
        "cards": random.choices(all_cards, k=7)
    },
    {
        "id": 2,
        "cards": random.choices(all_cards, k=7)
    },
    {
        "id": 3,
        "cards": random.choices(all_cards, k=7)
    },
    {
        "id": 4,
        "cards": random.choices(all_cards, k=7)
    }
]

print(all_users)


# Context Card
context_card = random.choice(all_cards)

print(context_card)


# Direction
direction = 1


# First Person
users_found = []

for i in all_users:
    user_number = i['id']

    for j in i['cards']:
        if j['value'] == 1:

            users_found.append(user_number)

print(users_found[0])


# Game
