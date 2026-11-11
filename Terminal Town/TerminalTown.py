import random
import time
import threading
class Player: 
    def __init__(self, player_id, name) :
        self.name = name
        self.id = player_id
        self.alive = True
        self.role = None
def start_timer(index):
    timer = phase_timers[phases[index]]
    while timer > 0 :
        print(f"\033[H\033[KTimer:{timer}", end="\r", flush=True)
        time.sleep(1)
        timer = timer - 1
#def start_Game()

def change_Phase(phase):
    if phase == 0:
        phase = 7
        return(phase)
    phase = phase + 1
    if phase == 8:
        phase = 1
    return(phase)
def start_phase(day_Count) :
    if phase_Index == 0 or phase_Index == 1 :
        print(f"Day {day_Count}")
    elif phase_Index == 2:
        print("the town may begin voting")
    elif phase_Index == 3:
        print(f"(playeronstand), what is ur defense")
    elif phase_Index == 4 :
        print("the town may now vote on the fate of (playeronstand)")
    elif phase_Index == 5:
        print("(playeronstand) do you have any last words?")
    elif phase_Index == 6 :
        print("it is too late to continue voting")
    elif phase_Index == 7:
        day_Count = day_Count + 1
        print(f"Night {day_Count}")
    return(day_Count)
def sendmsg(id):
    print(f"\033[1;1H{players[id].id} {players[id].name}:{input()}")

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
phase_timers = {
    "start": 15,
    "day": 60,
    "vote": 30,
    "trial": 2,
    "judge": 2,
    "final_words": 2,
    "end_day": 2,
    "night": 2
}
phases = [
    "start",
    "day",
    "vote",
    "trial",
    "judge",
    "final_words",
    "end_day",
    "night"
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
#start_Game()
phase_Index = 0
day_Count = 0
timer = 0
thread = threading.Thread(target=start_timer,args=(phase_Index,))

while True :
    day_Count = start_phase(day_Count)
    #start_timer(phase_Index)
    thread.start()
    phase_Index = change_Phase(phase_Index)
    while True :

    #if timer != 0:
            sendmsg(1)
#print (f"is {player1.name} correct?")
#print("[1] YES")
#print("[2] NO")
#name_Confirm = input()
#if name_Confirm == "1" :
 #   print("Good")
   # print("I will now bestow upon you: a reason to live and your way of life")
#else:
    #player_Name = input("Please Input Your Name:")
