import random
import time
class Player: 
    def __init__(self, player_id, name) :
        self.name = name
        self.id = player_id
        self.alive = True
        self.role = None
def start_timer(phase):
    if phase == "start" :
            timer = 4
            phase = "night"
    elif phase == "day" :
        timer = 5
        phase = "vote"
    elif phase == "vote":
        timer = 6
        phase = "night"
    elif phase == "night":
        timer = 7
        phase = "day"
    while timer > 0 :
            time.sleep(1)
            print(    timer, end="\r")
            timer = timer - 1
    return(phase)
players = []
test_names = [
    "Alex",
    "Benjamin",
    "Charlie",
    "Diana",
    "Ethan",
    "Felix",
    "Grace",
    "Hannah",
    "Isaac",
    "Jake",
    "Kevin",
    "Luna",
    "Marcus",
    "Nathan",
    "Olivia"
]
print("Welcome to Termial Town!")
name = input("Please Input Your Name:")
new_Player = Player(1,name)
players.append(new_Player)
random.shuffle(test_names)
for x in range(1,4):
    new_Player = Player(x + 1,test_names[x])
    players.append(new_Player)
Roles = ["Mafia", "Townie", "Doctor","Townie"]
random.shuffle(Roles)
for x in range(len(players)) :
    players[x].role = Roles[x]
    print(f"{players[x].name} - {players[x].role}")
print("Starting Game...")
phase = "start"
timer = 0
day_count = 1
print("Day 0")
while True :
    if phase == "day":
        print(f"Day {day_count}")
        day_count = day_count + 1
    elif phase == "night" :
        print(f"Night {day_count}")
    phase = start_timer(phase)
    print(phase)

print("it is too late to continue this discusstion")


























#print (f"is {player1.name} correct?")
#print("[1] YES")
#print("[2] NO")
#name_Confirm = input()
#if name_Confirm == "1" :
 #   print("Good")
   # print("I will now bestow upon you: a reason to live and your way of life")
#else:
    #player_Name = input("Please Input Your Name:")
