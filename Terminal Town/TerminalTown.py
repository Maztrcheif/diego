import random
import time
import threading
import curses
class Game:
    def __init__(self):
        self.main_phase = "Day"
        self.sub_phase = "Start"
        self.players = []
        self.messages = []
        self.day_Count = 0
        self.timer = 0
        self.phase_timer = 15
        self.elapsed = 0
        self.time_start = 0
        self.game_State = "Game"
        self.player_on_stand = False
        self.Judgement_voting = False
        self.player_voting = False
        self.day_abilities = False
        self.night_abilities = False
        self.dead_player = False
        self.vote_counter = 0
        self.verdict = None
        self.input = ""
class Player: 
    def __init__(self, player_id, name) :
        self.name = name
        self.id = player_id
        self.alive = True
        self.role = None
        self.effects = []
class Messages:
    def __init__(self, content, sender_name, sender_id,) :
        self.content = content
        self.sender_name = sender_name
        self.sender_id = sender_id
        self.time_sent = None
        self.message_id = None
def draw_screen_game(stdscr,game):
    stdscr.clear()
    stdscr.addstr(0,0, f"Time left:{game.timer}")
    stdscr.addstr(1,0, f"{game.main_phase} {game.day_Count}")
    stdscr.addstr(2,0, f"{game.sub_phase}")
    stdscr.addstr(3,0, f"{game.messages}")
    stdscr.addstr(10,0,game.input)
    time.sleep(0.05)
    stdscr.refresh()
def get_input(stdscr,game):
    key = stdscr.getch()
    if 32 <= key <= 126:
        game.input += chr(key)
    elif key == curses.KEY_BACKSPACE or key == 127:
        game.input = game.input[:-1]
    elif key == 10:
        message = game.input
        game.input = ""
        game.messages.append(message)
def start_timer(game):
    game.time_start = time.monotonic()
    game.elapsed = 0
def phase_timer(game):
    game.elapsed = time.monotonic() - game.time_start
    game.timer = max(0,game.phase_timer - int(game.elapsed))
#def day_phase(game):
#def night_phase(game):
def change_main_phase(game):
    if game.main_phase == "Day":
        game.phase_timer = 60
        game.main_phase = "Night"
        game.day_Count = game.day_Count + 1
        game.night_abilities = True
        game.day_abilities = False
    elif game.main_phase == "Night":
        game.main_phase = "Day"
        game.night_abilities = False
        game.day_abilities = True
        if game.dead_player == True :
            game.sub_phase = "The_dead"
        else: 
            game.phase_timer = 60
            game.sub_phase = "Discussion"
def change_sub_phase(game):
    if game.sub_phase == "Discussion":
        game.phase_timer = 30
        game.sub_phase = "Voting"
        game.player_voting = True
    elif game.sub_phase == "The_dead":
        game.phase_timer = 60
        game.sub_phase = "Discussion"
    elif game.sub_phase == "Voting":
        game.player_voting = False
        if game.player_on_stand == True:
            game.sub_phase = "Defense"
            game.phase_timer = 10
        else:
            game.sub_phase = "End_of_day"
    elif game.sub_phase == "Defense":
        game.phase_timer = 20
        game.sub_phase = "Judgement"
        game.Judgement_voting = True
    elif game.sub_phase == "Judgement":
        game.Judgement_voting = False
        if game.verdict == "Guilty":
            game.sub_phase = "Last_words"
            game.phase_timer = 5
            game.vote_counter = 0
        elif game.verdict == "Innocent":
            game.vote_counter = game.vote_counter + 1
            if game.vote_counter == 3:
                game.sub_phase = "End_of_day"
                game.vote_counter = 0
            else:
                game.sub_phase = "Voting"
                game.phase_timer = 10
                game.player_on_stand = False
    elif game.sub_phase == "Last_words":
        game.sub_phase = "End_of_day"
        game.player_on_stand = False
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

game = Game()
def Main_Game(stdscr):
    stdscr.timeout(100)
    start_timer(game)
    while game.game_State == "Game":
        phase_timer(game)
        draw_screen_game(stdscr,game)
        get_input(stdscr,game)
        if game.main_phase == "Day":
            if game.day_Count == 0 :
                game.sub_phase = "Start"
            #day_phase(game)
            True
        elif game.main_phase == "Night":
            #night_phase(game)
            True
        if game.timer <= 0 :
            if game.main_phase == "Day":
                if game.sub_phase == "Start":
                    change_main_phase(game)
                elif game.sub_phase == "End_of_day":
                    change_main_phase(game)
                else:
                    change_sub_phase(game)
            elif game.main_phase == "Night":
                change_main_phase(game)
            start_timer(game)
        elif game.sub_phase == "Voting" and game.player_on_stand == True:
            change_sub_phase(game)
            start_timer(game)
curses.wrapper(Main_Game)

