print("welcome to TT!")
input("Please enter your name:") 
import json
import random
with open("Roles.json", "r") as file:
    Roles = json.load(file)

class Player: 
    def __init__(self,player_id):
        self.id = player_id
        self.role = None
        self.Effects = {}
players = []

for x in range(15):
    player = Player(x + 1)
    players.append(player)

role_names = list(Roles.keys())
role_list = [
    "Jailor",
    "Town Investigative",
    "Town Investigative",
    "Town Protective",
    "Town Support",
    "Town Killing",
    "Random Town",
    "Random Town",
    "Random Town",
    "Godfather",
    "Mafioso",
    "Random Mafia",
    "Random Mafia",
    "Neutral Killing",
    "Neutral Evil",
]
assigned_roles = []

def get_roles(slot):
    candidates = []

    for role_name, role_data in Roles.items():
        if  role_name == slot :
            candidates.append(role_name)

        elif role_data["alignment"] == slot:
            candidates.append(role_name)

        elif role_data["sub_alignment"] == slot:
            candidates.append(role_name)

        if slot == "Random Town":
            if role_data["alignment"] == "Town":
                candidates.append(role_name)

        if slot == "Random Mafia":
            if role_data["alignment"] == "Mafia":
                candidates.append(role_name)

    return candidates
random.shuffle(role_list)
for player, slot in zip(players, role_list):
    if slot in Roles and Roles[slot]["unique"]:
        player.role = slot
        assigned_roles.append(slot)

for player, slot in zip(players, role_list):
    candidates = get_roles(slot)

    while candidates :
        role = random.choice(candidates)
        if Roles[role]["unique"] and role in assigned_roles:
            candidates.remove(role)
        else :
            player.role = role
            assigned_roles.append(role)
            print(player.id, player.role)
            break




