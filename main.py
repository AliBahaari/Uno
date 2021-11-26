import random
from more_itertools import grouper


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
        "cards": random.sample(all_cards, 7)
    },
    {
        "id": 2,
        "cards": random.sample(all_cards, 7)
    },
    {
        "id": 3,
        "cards": random.sample(all_cards, 7)
    },
    {
        "id": 4,
        "cards": random.sample(all_cards, 7)
    }
]


# Context Card
context_card = random.choice(all_cards)


# Direction
direction = 1


# First User
grouped_cards = grouper(random.sample(all_cards, 52), 4)
first_user = 0

for i in grouped_cards:
    for idx, j in enumerate(i):
        if j['value'] == 1:

            first_user = idx + 1
            break


# Game
