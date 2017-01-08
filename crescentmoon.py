#!/usr/bin/python
# -*- coding: utf-8 -*

#      ______                                    __   _______
#     |      |.----.-----.-----.----.-----.-----|  |_|   |   |-----.-----.-----.
#     |   ---||   _|  -__|__ --|  __|  -__|     |   _|       |  _  |  _  |     |
#     |______||__| |_____|_____|____|_____|__|__|____|__|_|__|_____|_____|__|__|

#Author: Immunity

#This music’s the only thing keeping the peace when I’m falling to pieces
#             https://www.youtube.com/watch?v=p6uBo-vC-Ro

#Keep my boys around, all you others bore me
#Don't talk to no one, don't steal my glory
#Fuck, fuck my glory, the whole world ignores me

#2 Sad 4 U
#https://www.youtube.com/watch?v=tMgkt9jdjTU&start=81

#Color console
W  = '\033[0m'  # white
R  = '\033[31m' # red
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
G = '\033[32m'  # green
GR = '\033[37m' # gray

import random
import sys
import os
import time
import pickle

version = "Yoshi City"
serial = "0540021"

poster ="""          Which part of

272  +  138  +  341  +  131  +  151

 +       +       +       +       +

366  +  199  +  130  +  320  +  18

 +       +       +       +       +

226  +  245  +  91   +  245  +  226

 +       +       +       +       +

18   +  320  +  130  +  199  +  366

 +       +       +       +       +

151  +  131  +  341  +  138  +  272

      didn't you understand
                ?\n"""

post = """Sometimes I cannot stand this place
Sometimes it's my life I can't taste
Sometimes I cannot feel my face\n"""

note = """
          G o o d V i b e s

Yann Tiersen - La Valse d'Amelie (piano)
$uicideboy$ - Kill Yourself Part III
FORXST - Diamond Life/London's Tears
Yung Lean & Thaiboy Digital - Diamonds
Lil Peep - Star Shopping
Yung lean - Hurt
Prismo - Senses
Oliver - tunchi\n"""

paper = """I be a the silhouhette of a sunset
Smoke a cigarette while I compress my depression
Stare into the violet fluorescent lights makes me violent
I'm trying to get the highest I can get before I overdose and die.\n"""

key_desc = """A golden key.\n"""

sword_desc = """This sword is made of steel. The hilt has three pieces to it
a simple crosspiece a square “scent stopper” pommel with 4
citrines set in it and a ribbed grip made of ebony.\n"""

ruby_desc = """A medium piece of ruby.\n"""

amulet_desc = """A amulet with strange runes carved into it.\n"""

knife_desc = """A kitchen knife.\n"""

name = "Sadboy"
attack = 5
bonus = 0
moves = 0
score = 0
health = 75
health_max = 75
coins = 0
lock = False
chest_open = False
killed = False
reward = False
printed = False
passed = False
passed2 = False
lantern_on = False
trapdoor_open = False
trapdoor_close = True
trapdoor1_open = False
trapdoor1_close = True
unlocked = False
troll_life = 65
taken = False
taken2 = False
taken3 = False
taken4 = False
local = ''
rank = ''
inventory = []
achievement = []
can_eat = ['bread', 'apple', 'carrot', 'tomato', 'potato', 'onion']
skill = ['sadness']

def continue_game():
    #Milkshake with them crushed up oreos
    global inventory, local, moves, score, rank
    global trapdoor_open, trapdoor_close, trapdoor1_open, trapdoor1_close
    global coins, bonus, health, chest_open, killed, reward, printed, passed
    global passed2, unlocked, taken, taken2, lock, achievement, lantern_on, attack
    global troll_life
    with open('savefile') as f:
        (taken3, taken4, troll_life, trapdoor_open, trapdoor_close, trapdoor1_open, trapdoor1_close, rank, moves, score, local, inventory,
        coins, bonus, health, chest_open, killed, reward, printed, passed, passed2, unlocked, taken, taken2,
        lock, achievement, lantern_on, attack) = pickle.load(f)
        os.system("clear")
        print("(type help to get a list of actions)")
        print("CrescentMoon: The Sad Text Adventure")
        print("Copyright (c) 2016, 2017 By Immunity. All rights reserved.")
        print("Version: %s / Serial Number: %s\n")%(version, serial)
        if local == 'House':
            h = House()
            h.inicio()

        elif local == 'House2':
            h2 = House2()
            h2.inicio()

        elif local == 'House3':
            h3 = House3()
            h3.inicio()

        elif local == 'ForestPath':
            fp = ForestPath()
            fp.inicio()

        elif local == 'Forest':
            f = Forest()
            f.inicio()

        elif local == 'WhiteHouse':
            wh = WhiteHouse()
            wh.inicio()

        elif local == 'Room':
            r = Room()
            r.inicio()

        elif local == 'InRoom':
            ir = InRoom()
            ir.inicio()

        elif local == 'SecondFloor':
            sf = SecondFloor()
            sf.inicio()

        elif local == 'OutHouse':
            oh = OutHouse()
            oh.inicio()

        elif local == 'Clearing':
            c = Clearing()
            c.inicio()

        elif local == 'Waterfall':
            wf = Waterfall()
            wf.inicio()

        elif local == 'TrapDoor':
            tp = TrapDoor()
            tp.inicio()

        elif local == 'TrapDoor2':
            tp2 = TrapDoor2()
            tp2.inicio()

        elif local == 'CanyonView':
            c = Canyon()
            c.inicio()

        elif local == 'RockyLedge':
            rl = RockyLedge()
            rl.inicio()

        elif local == 'CanyonBottom':
            cb = CanyonBottom()
            cb.inicio()

        elif local == 'SmallRoom':
            sr = SmallRoom()
            sr.inicio()

        elif local == 'SmallRoom2':
            sr2 = SmallRoom2()
            sr2.inicio()

        elif local == 'PreAltar':
            pa = PreAltar()
            pa.inicio()

        elif local == 'Altar':
            ar = Altar()
            ar.inicio()

        elif local == 'Cave3':
            c3 = Cave3()
            c3.inicio()

        elif local == 'Mountain':
            m = Mountain()
            m.inicio()

        elif local == 'Tunnel':
            t = Tunnel()
            t.inicio()

        elif local == 'Tunnel2':
            t2 = Tunnel2()
            t2.inicio()

        elif local == 'Cave':
            c = Cave()
            c.inicio()

        elif local == 'Cave2':
            c2 = Cave2()
            c2.inicio()

        elif local == 'MineEntrance':
            me = MineEntrance()
            me.inicio()

        elif local == 'Out':
            ot = Out()
            ot.inicio()

        elif local == 'PreRoom':
            pr = PreRoom()
            pr.inicio()

        elif local == 'Room2':
            r2 = Room2()
            r2.inicio()

        elif local == 'Room3':
            r3 = Room3()
            r3.inicio()

        elif local == 'Room4':
            r4 = Room4()
            r4.inicio()

        elif local == 'Depository':
            d = Depository()
            d.inicio()

        elif local == 'Temple':
            t = Temple()
            t.inicio()

def save():
    print("Done.\n")
    try:
        with open('savefile', 'w') as f:
            pickle.dump([taken3, taken4, troll_life, trapdoor_open, trapdoor_close, trapdoor1_open, trapdoor1_close, rank, moves, score, local, inventory,
            coins, bonus, health, chest_open, killed, reward, printed, passed, passed2, unlocked, taken, taken2, lock,
            achievement, lantern_on, attack], f, protocol=2)
    except:
          print("Error saving.\n")

class character:
    def status(self):
        print("Name: %s")% name
        print("Health: %d/%d") % (health, health_max)
        print("Sad Attack: %d") % attack
        print("Special Skill:\n%s") % skill[0]
        print("Coins: %d\n")% coins
        #https://www.youtube.com/watch?v=-VxOwSNvXTA&start=30

    def achievement(self):
        if 'sadness' and 'outside' in achievement:
            print("""                     +---------+
                 --- |   ???   |
                |    +---------+
                |
+---------+     |  +-----------+
| Sadness | ------ |  Outside  |
+---------+     |  +-----------+
                |
                |    +---------+
                 --- |   ???   |
                     +---------+
                     """)

        elif 'sadness' in achievement:
            print("""                     +---------+
                 --- |   ???   |
                |    +---------+
                |
+---------+     |  +-----------+
| Sadness | ------ |    ???    |
+---------+     |  +-----------+
                |
                |    +---------+
                 --- |   ???   |
                     +---------+
                     """)

        else:
            print("""                     +---------+
                 --- |   ???   |
                |    +---------+
                |
+---------+     |  +-----------+
|   ???   | ------ |    ???    |
+---------+     |  +-----------+
                |
                |    +---------+
                 --- |   ???   |
                     +---------+
                     """)

    def ajuda(self):
        print("Commands:\n")
        print("  help: print this message.")
        print("  save: save the game.")
        print("  quit: ask if you want to leave the game.")
        print("  score: print your score.")
        print("  achievement: print your achievement.")
        print("  restart: ask if you want to restart the game.")
        print("  inventory: lists the objects in your inventory.")
        print("  status: print your status.")
        print("  north: go north.")
        print("  south: go south.")
        print("  west: go west.")
        print("  east: go east.")
        print("  down: go down.")
        print("  up: go up.")
        print("  take: take something. Syntax: take <item>.")
        print("  drop: drop something. Syntax: drop <item>.")
        print("  read: read something. Syntax: read <item>.")
        print("  look: look something. Syntax: look at <item>.")
        print("  turn: turn lantern on/off. Syntax: turn lantern on/off.")
        print("  open: open something. Syntax: open <something>.")
        print("  close: close something. Syntax: close <something>.")
        print("  eat: eat something. Syntax: eat <food>.")
        print("  buy: buy something. Syntax: buy <item>.")
        print("  say: say something. Syntax: say <something>.")
        print("  hit: hit a creature. Syntax: hit <creature> with <item>.\n")

    def restart(self):
        check_restart = raw_input("Are you sure you want to restart? ")
        if check_restart == 'y':
            global troll_life
            global trapdoor1_close
            global trapdoor1_open
            global trapdoor_open
            global bonus
            global health
            global coins
            global lock
            global chest_open
            global killed
            global reward
            global printed
            global skill
            global lantern_on
            global unlocked
            global passed
            global passed2
            global inventory
            global achievement
            global moves
            global score
            global taken
            global taken2
            global taken3
            global taken4
            global rank
            rank = ''
            taken = False
            taken2 = False
            taken3 = False
            taken4 = False
            score = 0
            moves = 0
            achievement = []
            bonus = 0
            health = 75
            bonus = 0
            coins = 0
            lock = False
            chest_open = False
            killed = False
            reward = False
            printed = False
            passed = False
            passed2 = False
            lantern_on = False
            troll_life = 65
            trapdoor_open = False
            trapdoor_close = True
            trapdoor1_open = False
            trapdoor1_close = True
            unlocked = False
            inventory = []
            skill = ['sadness']
            os.system("clear")
            print("(type help to get a list of actions)")
            print("CrescentMoon: The Sad Text Adventure")
            print("Copyright (c) 2016, 2017 By Immunity. All rights reserved.")
            print("Version: %s / Serial Number: %s\n")%(version, serial)
            h = House()
            h.inicio()

        else:
            print("")

    def quit(self):
        check_restart = raw_input("Are you sure you want to quit? ")
        if check_restart == 'y':
            print("\n     Sadboy has dead by depression\n")
            print("     ****    You have died    ****\n")
            sys.exit()
            #https://www.youtube.com/watch?v=MRNkf6BU-Bc&start=42

        else:
            print("")

    def score(self):
        global score, moves, rank
        if 0 <= score < 10:
             rank = 'Beginner'

        elif 10 < score < 25:
             rank = 'Experient'

        elif 25 < score < 50:
             rank = 'S A D'

        elif 50 < score < 100:
             rank = 'King of Sadness'

        print("Your score is %d, in %d moves.")%(score, moves)
        print("Your rank is %s\n")%rank

class Depository:
    def __init__(self):
        self.state = 'depository'

    def quit(self):
        c = character()
        c.quit()

    def save(self):
        save()

    def status(self):
        c = character()
        c.status()

    def ajuda(self):
        c = character()
        c.ajuda()

    def restart(self):
        c = character()
        c.restart()

    def score(self):
        c = character()
        c.score()

    def inventory(self):
        if len(inventory) > 0:
            print("You have:")
            print inventory
            print("")
        else:
            print("Your inventory is empty.\n")

    def achievement(self):
        c = character()
        c.achievement()

    def inicio(self):
        global local
        local = 'Depository'
        complete = False
        global moves, taken3, taken4
        print("Depository")
        print("You are in a abandoned depository, there is a lot of boxes around you.\n")
        if taken3 == True:
            itens = {
            1 : {}
            }
            currentRoom = 1

        else:
            itens = {
            1 : {"item": 'box'}
            }
            currentRoom = 1

        commands = {
        'help': Depository.ajuda,
        'quit': Depository.quit,
        'save': Depository.save,
        'score': Depository.score,
        'achievement': Depository.achievement,
        'north': Depository.north,
        'west': Depository.west,
        'east': Depository.east,
        'south': Depository.south,
        'up': Depository.up,
        'down': Depository.down,
        'status': Depository.status,
        'inventory': Depository.inventory,
        'restart': Depository.restart
        }

        d = Depository()

        while complete == False:
            line = raw_input("> ")
            args = line.split()
            if len(args) == 0:
                print("What you want to do?\n")

            elif len(args) > 0:
                commandFound = False
                for c in commands.keys():
                    if args[0] == c[:len(args[0])]:
                        commands[c](d)
                        commandFound = True
                        break

                if args[0] == "take":
                    try:
                        if "item" in itens[currentRoom] and args[1] in itens[currentRoom]["item"]:
                            moves += 1
                            inventory.append(args[1])
                            print(args[1]+":" + " This box looks like can be opened.\n")
                            taken3 = True
                            del itens[currentRoom]["item"]

                        else:
                            print("Can't get this.\n")

                    except:
                        print("Invalid.\n")

                if args[0] == "drop":
                    try:
                        if args[1] in inventory:
                            moves += 1
                            inventory.remove(args[1])
                            print(args[1]+":" + " Dropped.\n")

                        else:
                            print("Can't drop this.\n")
                    except:
                        print("Invalid.\n")

                if args[0] == "eat":
                      try:
                           if args[1] in inventory and args[1] in can_eat:
                                 global health, health_max
                                 if args[1] == can_eat[0]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 5 > health_max:
                                             inventory.remove('bread')
                                             health = 75
                                             print("You eat the bread.\n")
                                       else:
                                             inventory.remove('bread')
                                             health += 5
                                             print("You eat the bread.\n")

                                 elif args[1] == can_eat[1]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 5 > health_max:
                                             inventory.remove('apple')
                                             health = 75
                                             print("You eat the apple.\n")
                                       else:
                                             inventory.remove('apple')
                                             health += 5
                                             print("You eat the apple.\n")

                                 elif args[1] == can_eat[2]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 3 > health_max:
                                             inventory.remove('carrot')
                                             health = 75
                                             print("You eat the carrot.\n")
                                       else:
                                             inventory.remove('carrot')
                                             health += 3
                                             print("You eat the carrot.\n")

                                 elif args[1] == can_eat[3]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 4 > health_max:
                                             inventory.remove('tomato')
                                             health = 75
                                             print("You eat the tomato.\n")
                                       else:
                                             inventory.remove('tomato')
                                             health += 4
                                             print("You eat the tomato.\n")

                                 elif args[1] == can_eat[4]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 4 > health_max:
                                             inventory.remove('potato')
                                             health = 75
                                             print("You eat the potato.\n")
                                       else:
                                             inventory.remove('potato')
                                             health += 4
                                             print("You eat the potato.\n")

                                 elif args[1] == can_eat[5]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 2 > health_max:
                                             inventory.remove('onion')
                                             health = 75
                                             print("You eat the onion.\n")
                                       else:
                                             inventory.remove('onion')
                                             health += 2
                                             print("You eat the onion.\n")

                                 else:
                                     print("You can't eat this.\n")
                           else:
                               print("You don't have this.\n")
                      except:
                            print("Eat what?\n")

                if args[0] == "turn":
                    try:
                        if args[1] == 'lantern':
                            if 'lantern' in inventory:
                                global lantern_on
                                if args[2] == 'on':
                                    lantern_on = True
                                    moves += 1
                                    print("The lantern is now on.\n")

                                elif args[2] == 'off':
                                    lantern_on = False
                                    moves += 1
                                    print("The lantern is now off.\n")
                            else:
                                print("You don't have a lantern.\n")
                    except:
                        print("Invalid.\n")

                if args[0] == "say":
                    try:
                        if args[1] != None:
                            moves += 1
                            print("You say:" + " " + args[1])
                            print("")

                        else:
                            pass
                    except:
                        print("Say what?\n")

                if args[0] == 'read':
                    try:
                        if args[1] == 'paper':
                            if 'paper' in inventory:
                                global paper
                                moves += 1
                                print(paper)
                            else:
                                pass

                        elif args[1] == 'note':
                            if 'note' in inventory:
                                global note
                                moves += 1
                                print(note)
                            else:
                                pass

                        elif args[1] == 'post-it':
                            if 'post-it' in inventory:
                                global post
                                moves += 1
                                print(post)
                            else:
                                pass

                        elif args[1] == 'poster':
                            if 'poster' in inventory:
                                global poster
                                moves += 1
                                print(poster)
                            else:
                                pass

                        else:
                            pass

                    except:
                        print("Read what?\n")

                if args[0] == 'open':
                    try:
                        if args[1] == 'box':
                            if taken4 == True:
                                print("You open the box.")
                                print("But it's empty.\n")

                            else:
                                print("You open the box.")
                                print("This reveals:")
                                print("  A gold bar")
                                print("  A chalice")
                                print("")
                                taken4 = True
                                inventory.append('chalice')
                                inventory.append('gold')

                        else:
                            print("Open what?\n")

                    except:
                        print("Open what?\n")

                if args[0] == 'close':
                    try:
                        if args[1] == 'box':
                            moves += 1
                            print("You close the box.\n")

                        else:
                            print("Close what?\n")

                    except:
                        print("Close what?\n")

                if args[0] == 'look':
                    global key_desc
                    global sword_desc
                    global knife_desc
                    global ruby_desc
                    global amulet_desc
                    try:
                        if args[1] == 'at':
                            try:
                                if args[2] in inventory:
                                    if args[2] == 'key':
                                        print(key_desc)

                                    elif args[2] == 'sword':
                                        print(sword_desc)

                                    elif args[2] == 'knife':
                                        print(knife_desc)

                                    elif args[2] == 'ruby':
                                        print(ruby_desc)

                                    elif args[2] == 'amulet':
                                        print(amulet_desc)

                                    else:
                                        print("I see nothing special about this.\n")

                                else:
                                    print("You don't have this item.\n")

                            except:
                                print("Look at what?\n")

                    except:
                        print("Look at what?\n")

    def down(self):
        global moves
        moves += 1
        complete = True
        print("You can't go that way.\n")

    def up(self):
        global moves
        moves += 1
        complete = True
        print("You can't go that way.\n")

    def north(self):
        global moves
        moves += 1
        complete = True
        pass

    def west(self):
        global moves
        moves += 1
        pass

    def east(self):
        global moves
        moves += 1
        pass

    def south(self):
        global moves
        moves += 1
        d = Door()
        d.inicio()

class TrapDoor2:
    def __init__(self):
        self.state = 'trapdoor2'

    def quit(self):
        c = character()
        c.quit()

    def ajuda(self):
        c = character()
        c.ajuda()

    def status(self):
        c = character()
        c.status()

    def restart(self):
        c = character()
        c.restart()

    def save(self):
        save()

    def score(self):
        c = character()
        c.score()

    def achievement(self):
        c = character()
        c.achievement()

    def inventory(self):
        if len(inventory) > 0:
            print("You have:")
            print inventory
            print("")
        else:
            print("Your inventory is empty.\n")

    def inicio(self):
        complete = False
        global moves
        global lantern_on
        global trapdoor_open
        global trapdoor_close
        global local
        local = 'TrapDoor2'
        if lantern_on == False:
            print("You have moved into a dark place.\n")
            itens = {
            1 : {}
            }
            currentRoom = 1

        else:
            print("Cellar")
            print("You are in a dark and damp cellar.\n")
            itens = {
            1 : {}
            }
            currentRoom = 1

        commands = {
        'help': TrapDoor2.ajuda,
        'quit': TrapDoor2.quit,
        'save': TrapDoor2.save,
        'score': TrapDoor2.score,
        'achievement': TrapDoor2.achievement,
        'north': TrapDoor2.north,
        'west': TrapDoor2.west,
        'east': TrapDoor2.east,
        'south': TrapDoor2.south,
        'up': TrapDoor2.up,
        'down': TrapDoor2.down,
        'status': TrapDoor2.status,
        'restart': TrapDoor2.restart,
        'inventory': TrapDoor2.inventory
        }

        td2 = TrapDoor2()

        while complete == False:
            line = raw_input("> ")
            args = line.split()
            if len(args) == 0:
                print("What you want to do?\n")

            elif len(args) > 0:
                commandFound = False
                for c in commands.keys():
                    if args[0] == c[:len(args[0])]:
                        commands[c](td2)
                        commandFound = True
                        break

                if args[0] == "take":
                    try:
                        if "item" in itens[currentRoom] and args[1] in itens[currentRoom]["item"]:
                            inventory.append(args[1])
                            moves += 1
                            print(args[1]+":" + " Taken.\n")
                            del itens[currentRoom]["item"]
                        else:
                            print("Can't get this.\n")

                    except:
                        print("Invalid.\n")

                if args[0] == "drop":
                    try:
                        if args[1] in inventory:
                            inventory.remove(args[1])
                            moves += 1
                            print(args[1]+":" + " Dropped.\n")

                        else:
                            print("Can't drop this.\n")

                    except:
                        print("Invalid.\n")

                if args[0] == "eat":
                      try:
                           if args[1] in inventory and args[1] in can_eat:
                                 global health, health_max
                                 if args[1] == can_eat[0]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 5 > health_max:
                                             inventory.remove('bread')
                                             health = 75
                                             print("You eat the bread.\n")
                                       else:
                                             inventory.remove('bread')
                                             health += 5
                                             print("You eat the bread.\n")

                                 elif args[1] == can_eat[1]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 5 > health_max:
                                             inventory.remove('apple')
                                             health = 75
                                             print("You eat the apple.\n")
                                       else:
                                             inventory.remove('apple')
                                             health += 5
                                             print("You eat the apple.\n")

                                 elif args[1] == can_eat[2]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 3 > health_max:
                                             inventory.remove('carrot')
                                             health = 75
                                             print("You eat the carrot.\n")
                                       else:
                                             inventory.remove('carrot')
                                             health += 3
                                             print("You eat the carrot.\n")

                                 elif args[1] == can_eat[3]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 4 > health_max:
                                             inventory.remove('tomato')
                                             health = 75
                                             print("You eat the tomato.\n")
                                       else:
                                             inventory.remove('tomato')
                                             health += 4
                                             print("You eat the tomato.\n")

                                 elif args[1] == can_eat[4]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 4 > health_max:
                                             inventory.remove('potato')
                                             health = 75
                                             print("You eat the potato.\n")
                                       else:
                                             inventory.remove('potato')
                                             health += 4
                                             print("You eat the potato.\n")

                                 elif args[1] == can_eat[5]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 2 > health_max:
                                             inventory.remove('onion')
                                             health = 75
                                             print("You eat the onion.\n")
                                       else:
                                             inventory.remove('onion')
                                             health += 2
                                             print("You eat the onion.\n")

                                 else:
                                     print "You can't eat this.\n"
                           else:
                               print("You don't have this.\n")
                      except:
                            print("Eat what?\n")

                if args[0] == "turn":
                    try:
                        if args[1] == 'lantern':
                            if 'lantern' in inventory:
                                if args[2] == 'on':
                                    moves += 1
                                    lantern_on = True
                                    print("The lantern is now on.\n")

                                elif args[2] == 'off':
                                    moves += 1
                                    lantern_on = False
                                    print("The lantern is now off.\n")
                            else:
                                print("You don't have a lantern.\n")
                    except:
                        print("Invalid.\n")

                if args[0] == "say":
                    try:
                        if args[1] != None:
                            moves += 1
                            print("You say:" + " " + args[1])
                            print("")
                        else:
                            pass
                    except:
                        print("Say what?\n")

                if args[0] == 'read':
                    try:
                        if args[1] == 'paper':
                            if 'paper' in inventory:
                                global paper
                                moves += 1
                                print(paper)
                            else:
                                pass

                        elif args[1] == 'note':
                            if 'note' in inventory:
                                global note
                                moves += 1
                                print(note)
                            else:
                                pass

                        elif args[1] == 'post-it':
                            if 'post-it' in inventory:
                                global post
                                moves += 1
                                print(post)
                            else:
                                pass

                        elif args[1] == 'poster':
                            if 'poster' in inventory:
                                global poster
                                moves += 1
                                print(poster)
                            else:
                                pass

                        else:
                            pass

                    except:
                        print("Read what?\n")

                if args[0] == 'open':
                    try:
                        if args[1] == 'trapdoor':
                            moves += 1
                            trapdoor_open = True
                            trapdoor_close = False
                            print("You open the trapdoor.\n")

                        else:
                            print("Open what?\n")

                    except:
                        print("Open what?\n")

                if args[0] == 'close':
                    try:
                        if args[1] == 'trapdoor':
                            moves += 1
                            trapdoor_open = False
                            trapdoor_close = True
                            print("You close the trapdoor.\n")

                        else:
                            print("Close what?\n")

                    except:
                        print("Close what?\n")

                if args[0] == 'look':
                    global key_desc
                    global sword_desc
                    global knife_desc
                    global ruby_desc
                    global amulet_desc
                    try:
                        if args[1] == 'at':
                            try:
                                if args[2] in inventory:
                                    if args[2] == 'key':
                                        print(key_desc)

                                    elif args[2] == 'sword':
                                        print(sword_desc)

                                    elif args[2] == 'knife':
                                        print(knife_desc)

                                    elif args[2] == 'ruby':
                                        print(ruby_desc)

                                    elif args[2] == 'amulet':
                                        print(amulet_desc)

                                    else:
                                        print("I see nothing special about this.\n")

                                else:
                                    print("You don't have this item.\n")

                            except:
                                print("Look at what?\n")

                    except:
                        print("Look at what?\n")

    def up(self):
        global moves
        moves += 1
        if trapdoor_open == True and trapdoor_close == False:
            complete = True
            h2 = House2()
            h2.inicio()
        print("The trapdoor is closed.\n")

    def down(self):
        global moves
        moves += 1
        print("You can't go that way.\n")

    def north(self):
        global moves
        moves += 1
        print("You can't go that way.\n")

    def south(self):
        global moves
        moves += 1
        print("Nothing here.\n")

    def east(self):
        global moves
        moves +=1
        print("Nothing here.\n")

    def west(self):
        global moves
        moves += 1
        print("Nothing here.\n")

class Door:
    def __init__(self):
        self.state = 'door'

    def quit(self):
        c = character()
        c.quit()

    def ajuda(self):
        c = character()
        c.ajuda()

    def status(self):
        c = character()
        c.status()

    def save(self):
        save()

    def restart(self):
        c = character()
        c.restart()

    def score(self):
        c = character()
        c.score()

    def achievement(self):
        c = character()
        c.achievement()

    def inventory(self):
        if len(inventory) > 0:
            print("You have:")
            print inventory
            print("")
        else:
            print("Your inventory is empty.\n")

    def inicio(self):
        complete = False
        global moves
        global score
        global lantern_on
        global local, unlocked
        local = 'Door'
        if unlocked == True:
            print("Door\n")
        else:
            print("Door")
            print("There's a door here, but it's locked with a numeric lock")
            print("of 4 digits. What is the password?\n")

        itens = {
        1 : {}
        }
        currentRoom = 1

        commands = {
        'help': Door.ajuda,
        'quit': Door.quit,
        'save': Door.save,
        'score': Door.score,
        'achievement': Door.achievement,
        'north': Door.north,
        'west': Door.west,
        'east': Door.east,
        'south': Door.south,
        'up': Door.up,
        'down': Door.down,
        'status': Door.status,
        'restart': Door.restart,
        'inventory': Door.inventory
        }

        d = Door()

        while complete == False:
            line = raw_input("> ")
            args = line.split()
            if len(args) == 0:
                print("What you want to do?\n")

            elif len(args) == 0:
                print("What you want to do?\n")

            elif len(args) > 0:
                commandFound = False
                for c in commands.keys():
                    if args[0] == c[:len(args[0])]:
                        commands[c](d)
                        commandFound = True
                        break

                if args[0] == '1033':
                    moves += 1
                    if unlocked == True:
                        print("The door is unlocked.\n")
                    else:
                        unlocked = True
                        print("You unlock the door.")
                        print("You unlock the achievement: " + P + "Thinking outside the box." + W + "\n")
                        achievement.append('outside')
                        score += 10

                if args[0] == "take":
                    try:
                        if "item" in itens[currentRoom] and args[1] in itens[currentRoom]["item"]:
                            inventory.append(args[1])
                            moves += 1
                            print(args[1]+":" + " Taken.\n")
                            del itens[currentRoom]["item"]
                        else:
                            print("Can't get this.\n")

                    except:
                        print("Invalid.\n")

                if args[0] == "drop":
                    try:
                        if args[1] in inventory:
                            inventory.remove(args[1])
                            moves += 1
                            print(args[1]+":" + " Dropped.\n")

                        else:
                            print("Can't drop this.\n")

                    except:
                        print("Invalid.\n")

                if args[0] == "eat":
                      try:
                           if args[1] in inventory and args[1] in can_eat:
                                 global health, health_max
                                 if args[1] == can_eat[0]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 5 > health_max:
                                             inventory.remove('bread')
                                             health = 75
                                             print("You eat the bread.\n")
                                       else:
                                             inventory.remove('bread')
                                             health += 5
                                             print("You eat the bread.\n")

                                 elif args[1] == can_eat[1]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 5 > health_max:
                                             inventory.remove('apple')
                                             health = 75
                                             print("You eat the apple.\n")
                                       else:
                                             inventory.remove('apple')
                                             health += 5
                                             print("You eat the apple.\n")

                                 elif args[1] == can_eat[2]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 3 > health_max:
                                             inventory.remove('carrot')
                                             health = 75
                                             print("You eat the carrot.\n")
                                       else:
                                             inventory.remove('carrot')
                                             health += 3
                                             print("You eat the carrot.\n")

                                 elif args[1] == can_eat[3]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 4 > health_max:
                                             inventory.remove('tomato')
                                             health = 75
                                             print("You eat the tomato.\n")
                                       else:
                                             inventory.remove('tomato')
                                             health += 4
                                             print("You eat the tomato.\n")

                                 elif args[1] == can_eat[4]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 4 > health_max:
                                             inventory.remove('potato')
                                             health = 75
                                             print("You eat the potato.\n")
                                       else:
                                             inventory.remove('potato')
                                             health += 4
                                             print("You eat the potato.\n")

                                 elif args[1] == can_eat[5]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 2 > health_max:
                                             inventory.remove('onion')
                                             health = 75
                                             print("You eat the onion.\n")
                                       else:
                                             inventory.remove('onion')
                                             health += 2
                                             print("You eat the onion.\n")

                                 else:
                                     print("You can't eat this.\n")
                           else:
                               print("You don't have this.\n")
                      except:
                            print("Eat what?\n")

                if args[0] == "turn":
                    try:
                        if args[1] == 'lantern':
                            if 'lantern' in inventory:
                                if args[2] == 'on':
                                    moves += 1
                                    lantern_on = True
                                    print("The lantern is now on.\n")

                                elif args[2] == 'off':
                                    moves += 1
                                    lantern_on = False
                                    print("The lantern is now off.\n")
                            else:
                                print("You don't have a lantern.\n")
                    except:
                        print("Invalid.\n")

                if args[0] == "say":
                    try:
                        if args[1] != None:
                            moves += 1
                            print("You say:" + " " + args[1])
                            print("")
                        else:
                            pass
                    except:
                        print("Say what?\n")

                if args[0] == 'read':
                    try:
                        if args[1] == 'paper':
                            if 'paper' in inventory:
                                global paper
                                moves += 1
                                print(paper)
                            else:
                                pass

                        elif args[1] == 'note':
                            if 'note' in inventory:
                                global note
                                moves += 1
                                print(note)
                            else:
                                pass

                        elif args[1] == 'post-it':
                            if 'post-it' in inventory:
                                global post
                                moves += 1
                                print(post)
                            else:
                                pass

                        elif args[1] == 'poster':
                            if 'poster' in inventory:
                                global poster
                                moves += 1
                                print(poster)
                            else:
                                pass

                        else:
                            pass

                    except:
                        print("Read what?\n")

                if args[0] == 'look':
                    global key_desc
                    global sword_desc
                    global knife_desc
                    global ruby_desc
                    global amulet_desc
                    try:
                        if args[1] == 'at':
                            try:
                                if args[2] in inventory:
                                    if args[2] == 'key':
                                        print(key_desc)

                                    elif args[2] == 'sword':
                                        print(sword_desc)

                                    elif args[2] == 'knife':
                                        print(knife_desc)

                                    elif args[2] == 'ruby':
                                        print(ruby_desc)

                                    elif args[2] == 'amulet':
                                        print(amulet_desc)

                                    else:
                                        print("I see nothing special about this.\n")

                                else:
                                    print("You don't have this item.\n")

                            except:
                                print("Look at what?\n")

                    except:
                        print("Look at what?\n")

    def up(self):
        global moves
        moves += 1
        print("You can't go that way.\n")

    def down(self):
        global moves
        moves += 1
        print("You can't go that way.\n")

    def north(self):
        global moves
        moves += 1
        complete = True
        global unlocked
        if unlocked == True:
            d = Depository()
            d.inicio()
        else:
            print("The door is locked.\n")

    def south(self):
        global moves
        moves += 1
        complete = True
        t2 = Tunnel2()
        t2.inicio()

    def east(self):
        global moves
        moves += 1
        print("Nothing here.\n")

    def west(self):
        global moves
        moves += 1
        print("Nothing here.\n")

class Tunnel2:
    def __init__(self):
        self.state = 'tunnel2'

    def quit(self):
        c = character()
        c.quit()

    def ajuda(self):
        c = character()
        c.ajuda()

    def status(self):
        c = character()
        c.status()

    def restart(self):
        c = character()
        c.restart()

    def score(self):
        c = character()
        c.score()

    def save(self):
        save()

    def achievement(self):
        c = character()
        c.achievement()

    def inventory(self):
        if len(inventory) > 0:
            print("You have:")
            print inventory
            print("")
        else:
            print("Your inventory is empty.\n")

    def inicio(self):
        complete = False
        global moves, local
        global lantern_on
        local = 'Tunnel2'
        print("Tunnel")
        if lantern_on == False:
            print("You have moved into a dark place.\n")

        else:
            print("You are in a narrow tunnel.\n")

        itens = {
        1 : {}
        }
        currentRoom = 1

        commands = {
        'help': Tunnel2.ajuda,
        'quit': Tunnel2.quit,
        'save': Tunnel2.quit,
        'score': Tunnel2.score,
        'achievement': Tunnel2.achievement,
        'north': Tunnel2.north,
        'west': Tunnel2.west,
        'east': Tunnel2.east,
        'south': Tunnel2.south,
        'up': Tunnel2.up,
        'down': Tunnel2.down,
        'status': Tunnel2.status,
        'restart': Tunnel2.restart,
        'inventory': Tunnel2.inventory
        }

        t2 = Tunnel2()

        while complete == False:
            line = raw_input("> ")
            args = line.split()
            if len(args) == 0:
                print("What you want to do?\n")

            elif len(args) > 0:
                commandFound = False
                for c in commands.keys():
                    if args[0] == c[:len(args[0])]:
                        commands[c](t2)
                        commandFound = True
                        break

                if args[0] == "take":
                    try:
                        if "item" in itens[currentRoom] and args[1] in itens[currentRoom]["item"]:
                            inventory.append(args[1])
                            moves += 1
                            print(args[1]+":" + " Taken.\n")
                            del itens[currentRoom]["item"]
                        else:
                            print("Can't get this.\n")

                    except:
                        print("Invalid.\n")

                if args[0] == "drop":
                    try:
                        if args[1] in inventory:
                            inventory.remove(args[1])
                            moves += 1
                            print(args[1]+":" + " Dropped.\n")

                        else:
                            print("Can't drop this.\n")

                    except:
                        print("Invalid.\n")

                if args[0] == "eat":
                      try:
                           if args[1] in inventory and args[1] in can_eat:
                                 global health, health_max
                                 if args[1] == can_eat[0]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 5 > health_max:
                                             inventory.remove('bread')
                                             health = 75
                                             print("You eat the bread.\n")
                                       else:
                                             inventory.remove('bread')
                                             health += 5
                                             print("You eat the bread.\n")

                                 elif args[1] == can_eat[1]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 5 > health_max:
                                             inventory.remove('apple')
                                             health = 75
                                             print("You eat the apple.\n")
                                       else:
                                             inventory.remove('apple')
                                             health += 5
                                             print("You eat the apple.\n")

                                 elif args[1] == can_eat[2]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 3 > health_max:
                                             inventory.remove('carrot')
                                             health = 75
                                             print("You eat the carrot.\n")
                                       else:
                                             inventory.remove('carrot')
                                             health += 3
                                             print("You eat the carrot.\n")

                                 elif args[1] == can_eat[3]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 4 > health_max:
                                             inventory.remove('tomato')
                                             health = 75
                                             print("You eat the tomato.\n")
                                       else:
                                             inventory.remove('tomato')
                                             health += 4
                                             print("You eat the tomato.\n")

                                 elif args[1] == can_eat[4]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 4 > health_max:
                                             inventory.remove('potato')
                                             health = 75
                                             print("You eat the potato.\n")
                                       else:
                                             inventory.remove('potato')
                                             health += 4
                                             print("You eat the potato.\n")

                                 elif args[1] == can_eat[5]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 2 > health_max:
                                             inventory.remove('onion')
                                             health = 75
                                             print("You eat the onion.\n")
                                       else:
                                             inventory.remove('onion')
                                             health += 2
                                             print("You eat the onion.\n")

                                 else:
                                     print "You can't eat this.\n"
                           else:
                               print("You don't have this.\n")
                      except:
                            print("Eat what?\n")

                if args[0] == "turn":
                    try:
                        if args[1] == 'lantern':
                            if 'lantern' in inventory:
                                if args[2] == 'on':
                                    moves += 1
                                    lantern_on = True
                                    print("The lantern is now on.\n")

                                elif args[2] == 'off':
                                    moves += 1
                                    lantern_on = False
                                    print("The lantern is now off.\n")
                            else:
                                print("You don't have a lantern.\n")
                    except:
                        print("Invalid.\n")

                if args[0] == "say":
                    try:
                        if args[1] != None:
                            moves += 1
                            print("You say:" + " " + args[1])
                            print("")
                        else:
                            pass
                    except:
                        print("Say what?\n")

                if args[0] == 'read':
                    try:
                        if args[1] == 'paper':
                            if 'paper' in inventory:
                                global paper
                                moves += 1
                                print(paper)
                            else:
                                pass

                        elif args[1] == 'note':
                            if 'note' in inventory:
                                global note
                                moves += 1
                                print(note)
                            else:
                                pass

                        elif args[1] == 'post-it':
                            if 'post-it' in inventory:
                                global post
                                moves += 1
                                print(post)
                            else:
                                pass

                        elif args[1] == 'poster':
                            if 'poster' in inventory:
                                global poster
                                moves += 1
                                print(poster)
                            else:
                                pass

                        else:
                            pass

                    except:
                        print("Read what?\n")

                if args[0] == 'look':
                    global key_desc
                    global sword_desc
                    global knife_desc
                    global ruby_desc
                    global amulet_desc
                    try:
                        if args[1] == 'at':
                            try:
                                if args[2] in inventory:
                                    if args[2] == 'key':
                                        print(key_desc)

                                    elif args[2] == 'sword':
                                        print(sword_desc)

                                    elif args[2] == 'knife':
                                        print(knife_desc)

                                    elif args[2] == 'ruby':
                                        print(ruby_desc)

                                    elif args[2] == 'amulet':
                                        print(amulet_desc)

                                    else:
                                        print("I see nothing special about this.\n")

                                else:
                                    print("You don't have this item.\n")

                            except:
                                print("Look at what?\n")

                    except:
                        print("Look at what?\n")

    def up(self):
        global moves
        moves += 1
        print("You can't go that way.\n")

    def down(self):
        global moves
        moves += 1
        print("You can't go that way.\n")

    def north(self):
        global moves
        moves += 1
        d = Door()
        d.inicio()

    def south(self):
        global moves
        moves += 1
        complete = True
        wf = Waterfall()
        wf.inicio()

    def east(self):
        global moves
        moves += 1
        print("You can't go that way.\n")

    def west(self):
        global moves
        moves += 1
        print("You can't go that way.\n")

class Waterfall:
    def __init__(self):
        self.state = 'waterfall'

    def quit(self):
        c = character()
        c.quit()

    def ajuda(self):
        c = character()
        c.ajuda()

    def status(self):
        c = character()
        c.status()

    def restart(self):
        c = character()
        c.restart()

    def score(self):
        c = character()
        c.score()

    def save(self):
        save()

    def achievement(self):
        c = character()
        c.achievement()

    def inventory(self):
        if len(inventory) > 0:
            print("You have:")
            print inventory
            print("")
        else:
            print("Your inventory is empty.\n")

    def inicio(self):
        complete = False
        global moves, local
        local = 'Waterfall'
        if 'torch' in inventory:
            print("Waterfall")
            print("You are in front of the waterfall, you are so close to the waterfall")
            print("that your torch has gone out, but before that you could see a tunnel")
            print("behind the waterfall.\n")
            inventory.remove('torch')

        else:
            print("Waterfall")
            print("You are in front of the waterfall.\n")

        itens = {
        1 : {}
        }
        currentRoom = 1

        commands = {
        'help': Waterfall.ajuda,
        'quit': Waterfall.quit,
        'save': Waterfall.save,
        'score': Waterfall.score,
        'achievement': Waterfall.achievement,
        'north': Waterfall.north,
        'west': Waterfall.west,
        'east': Waterfall.east,
        'south': Waterfall.south,
        'up': Waterfall.up,
        'down': Waterfall.down,
        'status': Waterfall.status,
        'restart': Waterfall.restart,
        'inventory': Waterfall.inventory
        }

        wf = Waterfall()

        while complete == False:
            line = raw_input("> ")
            args = line.split()
            if len(args) == 0:
                print("What you want to do?\n")

            elif len(args) > 0:
                commandFound = False
                for c in commands.keys():
                    if args[0] == c[:len(args[0])]:
                        commands[c](wf)
                        commandFound = True
                        break

                if args[0] == "take":
                    try:
                        if "item" in itens[currentRoom] and args[1] in itens[currentRoom]["item"]:
                            inventory.append(args[1])
                            moves += 1
                            print(args[1]+":" + " Taken.\n")
                            del itens[currentRoom]["item"]
                        else:
                            print("Can't get this.\n")

                    except:
                        print("Invalid.\n")

                if args[0] == "drop":
                    try:
                        if args[1] in inventory:
                            inventory.remove(args[1])
                            moves += 1
                            print(args[1]+":" + " Dropped.\n")

                        else:
                            print("Can't drop this.\n")

                    except:
                        print("Invalid.\n")

                if args[0] == "eat":
                      try:
                           if args[1] in inventory and args[1] in can_eat:
                                 global health, health_max
                                 if args[1] == can_eat[0]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 5 > health_max:
                                             inventory.remove('bread')
                                             health = 75
                                             print("You eat the bread.\n")
                                       else:
                                             inventory.remove('bread')
                                             health += 5
                                             print("You eat the bread.\n")

                                 elif args[1] == can_eat[1]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 5 > health_max:
                                             inventory.remove('apple')
                                             health = 75
                                             print("You eat the apple.\n")
                                       else:
                                             inventory.remove('apple')
                                             health += 5
                                             print("You eat the apple.\n")

                                 elif args[1] == can_eat[2]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 3 > health_max:
                                             inventory.remove('carrot')
                                             health = 75
                                             print("You eat the carrot.\n")
                                       else:
                                             inventory.remove('carrot')
                                             health += 3
                                             print("You eat the carrot.\n")

                                 elif args[1] == can_eat[3]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 4 > health_max:
                                             inventory.remove('tomato')
                                             health = 75
                                             print("You eat the tomato.\n")
                                       else:
                                             inventory.remove('tomato')
                                             health += 4
                                             print("You eat the tomato.\n")

                                 elif args[1] == can_eat[4]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 4 > health_max:
                                             inventory.remove('potato')
                                             health = 75
                                             print("You eat the potato.\n")
                                       else:
                                             inventory.remove('potato')
                                             health += 4
                                             print("You eat the potato.\n")

                                 elif args[1] == can_eat[5]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 2 > health_max:
                                             inventory.remove('onion')
                                             health = 75
                                             print("You eat the onion.\n")
                                       else:
                                             inventory.remove('onion')
                                             health += 2
                                             print("You eat the onion.\n")

                                 else:
                                     print "You can't eat this.\n"
                           else:
                               print("You don't have this.\n")
                      except:
                            print("Eat what?\n")

                if args[0] == "turn":
                    try:
                        if args[1] == 'lantern':
                            global lantern_on
                            if 'lantern' in inventory:
                                if args[2] == 'on':
                                    moves += 1
                                    lantern_on = True
                                    print("The lantern is now on.\n")

                                elif args[2] == 'off':
                                    moves += 1
                                    lantern_on = False
                                    print("The lantern is now off.\n")
                            else:
                                print("You don't have a lantern.\n")
                    except:
                        print("Invalid.\n")

                if args[0] == "say":
                    try:
                        if args[1] != None:
                            print("You say:" + " " + args[1])
                            print("")
                            moves += 1
                        else:
                            pass
                    except:
                        print("Say what?\n")

                if args[0] == 'read':
                    try:
                        if args[1] == 'paper':
                            if 'paper' in inventory:
                                global paper
                                moves += 1
                                print(paper)
                            else:
                                pass

                        elif args[1] == 'note':
                            if 'note' in inventory:
                                global note
                                moves += 1
                                print(note)
                            else:
                                pass

                        elif args[1] == 'post-it':
                            if 'post-it' in inventory:
                                global post
                                moves += 1
                                print(post)
                            else:
                                pass

                        elif args[1] == 'poster':
                            if 'poster' in inventory:
                                global poster
                                moves += 1
                                print(poster)
                            else:
                                pass

                        else:
                            pass

                    except:
                        print("Read what?\n")

                if args[0] == 'look':
                    global key_desc
                    global sword_desc
                    global knife_desc
                    global ruby_desc
                    global amulet_desc
                    try:
                        if args[1] == 'at':
                            try:
                                if args[2] in inventory:
                                    if args[2] == 'key':
                                        print(key_desc)

                                    elif args[2] == 'sword':
                                        print(sword_desc)

                                    elif args[2] == 'knife':
                                        print(knife_desc)

                                    elif args[2] == 'ruby':
                                        print(ruby_desc)

                                    elif args[2] == 'amulet':
                                        print(amulet_desc)

                                    else:
                                        print("I see nothing special about this.\n")

                                else:
                                    print("You don't have this item.\n")

                            except:
                                print("Look at what?\n")

                    except:
                        print("Look at what?\n")

    def up(self):
        global moves
        moves += 1
        print("You can't go that way.\n")

    def down(self):
        global moves
        moves += 1
        print("You can't go that way.\n")

    def south(self):
        global moves
        moves += 1
        complete = True
        ot = Out()
        ot.inicio()

    def north(self):
        global moves
        moves += 1
        complete = True
        t2 = Tunnel2()
        t2.inicio()

    def east(self):
        global moves
        moves += 1
        print("There some bushes here.\n")

    def west(self):
        global moves
        moves += 1
        print("Some plants on the ground.\n")

class Out:
    def __init__(self):
        self.state = 'out'

    def quit(self):
        c = character()
        c.quit()

    def ajuda(self):
        c = character()
        c.ajuda()

    def status(self):
        c = character()
        c.status()

    def restart(self):
        c = character()
        c.restart()

    def score(self):
        c = character()
        c.score()

    def save(self):
        save()

    def achievement(self):
        c = character()
        c.achievement()

    def inventory(self):
        if len(inventory) > 0:
            print("You have:")
            print inventory
            print("")
        else:
            print("Your inventory is empty.\n")

    def inicio(self):
        complete = False
        global moves
        global printed, local
        local = 'Out'
        if printed == False:
            print("You left the cave.")
            print("There is giant rocky walls around you and have a beautiful")
            print("waterfall to north.\n")
            printed = True

        else:
            print("There is giant rocky walls around you and have a beautiful")
            print("waterfall to north.\n")

        itens = {
        1 : {}
        }
        currentRoom = 1

        commands = {
        'help': Out.ajuda,
        'quit': Out.quit,
        'score': Out.score,
        'save': Out.save,
        'achievement': Out.achievement,
        'north': Out.north,
        'west': Out.west,
        'east': Out.east,
        'south': Out.south,
        'up': Out.up,
        'down': Out.down,
        'status': Out.status,
        'restart': Out.restart,
        'inventory': Out.inventory
        }

        ot = Out()

        while complete == False:
            line = raw_input("> ")
            args = line.split()
            if len(args) == 0:
                print("What you want to do?\n")

            elif len(args) > 0:
                commandFound = False
                for c in commands.keys():
                    if args[0] == c[:len(args[0])]:
                        commands[c](ot)
                        commandFound = True
                        break

                if args[0] == "take":
                    try:
                        if "item" in itens[currentRoom] and args[1] in itens[currentRoom]["item"]:
                            inventory.append(args[1])
                            moves += 1
                            print(args[1]+":" + " Taken.\n")
                            del itens[currentRoom]["item"]
                        else:
                            print("Can't get this.\n")

                    except:
                        print("Invalid.\n")

                if args[0] == "drop":
                    try:
                        if args[1] in inventory:
                            inventory.remove(args[1])
                            moves += 1
                            print(args[1]+":" + " Dropped.\n")

                        else:
                            print("Can't drop this.\n")

                    except:
                        print("Invalid.\n")

                if args[0] == "eat":
                      try:
                           if args[1] in inventory and args[1] in can_eat:
                                 global health, health_max
                                 if args[1] == can_eat[0]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 5 > health_max:
                                             inventory.remove('bread')
                                             health = 75
                                             print("You eat the bread.\n")
                                       else:
                                             inventory.remove('bread')
                                             health += 5
                                             print("You eat the bread.\n")

                                 elif args[1] == can_eat[1]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 5 > health_max:
                                             inventory.remove('apple')
                                             health = 75
                                             print("You eat the apple.\n")
                                       else:
                                             inventory.remove('apple')
                                             health += 5
                                             print("You eat the apple.\n")

                                 elif args[1] == can_eat[2]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 3 > health_max:
                                             inventory.remove('carrot')
                                             health = 75
                                             print("You eat the carrot.\n")
                                       else:
                                             inventory.remove('carrot')
                                             health += 3
                                             print("You eat the carrot.\n")

                                 elif args[1] == can_eat[3]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 4 > health_max:
                                             inventory.remove('tomato')
                                             health = 75
                                             print("You eat the tomato.\n")
                                       else:
                                             inventory.remove('tomato')
                                             health += 4
                                             print("You eat the tomato.\n")

                                 elif args[1] == can_eat[4]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 4 > health_max:
                                             inventory.remove('potato')
                                             health = 75
                                             print("You eat the potato.\n")
                                       else:
                                             inventory.remove('potato')
                                             health += 4
                                             print("You eat the potato.\n")

                                 elif args[1] == can_eat[5]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 2 > health_max:
                                             inventory.remove('onion')
                                             health = 75
                                             print("You eat the onion.\n")
                                       else:
                                             inventory.remove('onion')
                                             health += 2
                                             print("You eat the onion.\n")

                                 else:
                                     print("You can't eat this.\n")
                           else:
                               print("You don't have this.\n")
                      except:
                            print("Eat what?\n")

                if args[0] == "turn":
                    try:
                        if args[1] == 'lantern':
                            global lantern_on
                            if 'lantern' in inventory:
                                if args[2] == 'on':
                                    moves += 1
                                    lantern_on = True
                                    print("The lantern is now on.\n")

                                elif args[2] == 'off':
                                    moves += 1
                                    lantern_on = False
                                    print("The lantern is now off.\n")
                            else:
                                print("You don't have a lantern.\n")
                    except:
                        print("Invalid.\n")

                if args[0] == "say":
                    try:
                        if args[1] != None:
                            print("You say:" + " " + args[1])
                            print("")
                            moves += 1
                        else:
                            pass
                    except:
                        print("Say what?\n")

                if args[0] == 'read':
                    try:
                        if args[1] == 'paper':
                            if 'paper' in inventory:
                                global paper
                                moves += 1
                                print(paper)
                            else:
                                pass

                        elif args[1] == 'note':
                            if 'note' in inventory:
                                global note
                                moves += 1
                                print(note)
                            else:
                                pass

                        elif args[1] == 'post-it':
                            if 'post-it' in inventory:
                                global post
                                moves += 1
                                print(post)
                            else:
                                pass

                        elif args[1] == 'poster':
                            if 'poster' in inventory:
                                global poster
                                moves += 1
                                print(poster)
                            else:
                                pass

                        else:
                            pass

                    except:
                        print("Read what?\n")

                if args[0] == 'look':
                    global key_desc
                    global sword_desc
                    global knife_desc
                    global ruby_desc
                    global amulet_desc
                    try:
                        if args[1] == 'at':
                            try:
                                if args[2] in inventory:
                                    if args[2] == 'key':
                                        print(key_desc)

                                    elif args[2] == 'sword':
                                        print(sword_desc)

                                    elif args[2] == 'knife':
                                        print(knife_desc)

                                    elif args[2] == 'ruby':
                                        print(ruby_desc)

                                    elif args[2] == 'amulet':
                                        print(amulet_desc)

                                    else:
                                        print("I see nothing special about this.\n")

                                else:
                                    print("You don't have this item.\n")

                            except:
                                print("Look at what?\n")

                    except:
                        print("Look at what?\n")

    def up(self):
        global moves
        moves += 1
        print("You can't go that way.\n")

    def down(self):
        global moves
        moves += 1
        complete = True
        sr2 = SmallRoom2()
        sr2.inicio()

    def north(self):
        global moves
        moves += 1
        complete = True
        wf = Waterfall()
        wf.inicio()

    def east(self):
        global moves
        moves += 1
        print("Some bushes here.\n")

    def west(self):
        global moves
        moves += 1
        print("Nothing here.\n")

    def south(self):
        global moves
        moves += 1
        print("Nothing here.\n")

class MineEntrance:
    def __init__(self):
        self.state = 'mine-entrance'

    def quit(self):
        c = character()
        c.quit()

    def ajuda(self):
        c = character()
        c.ajuda()

    def status(self):
        c = character()
        c.status()

    def restart(self):
        c = character()
        c.restart()

    def score(self):
        c = character()
        c.score()

    def save(self):
        save()

    def achievement(self):
        c = character()
        c.achievement()

    def inventory(self):
        if len(inventory) > 0:
            print("You have:")
            print inventory
            print("")
        else:
            print("Your inventory is empty.\n")

    def inicio(self):
        complete = False
        global moves, local
        local = 'MineEntrance'
        print("Mine Entrance")
        print("You are standing at the entrance of what might have been a coal mine.\n")

        itens = {
        1 : {}
        }
        currentRoom = 1

        commands = {
        'help': MineEntrance.ajuda,
        'quit': MineEntrance.quit,
        'score': MineEntrance.score,
        'save': MineEntrance.save,
        'achievement': MineEntrance.achievement,
        'north': MineEntrance.north,
        'west': MineEntrance.west,
        'east': MineEntrance.east,
        'south': MineEntrance.south,
        'up': MineEntrance.up,
        'down': MineEntrance.down,
        'status': MineEntrance.status,
        'restart': MineEntrance.restart,
        'inventory': MineEntrance.inventory
        }

        me = MineEntrance()

        while complete == False:
            line = raw_input("> ")
            args = line.split()
            if len(args) == 0:
                print("What you want to do?\n")

            elif len(args) > 0:
                commandFound = False
                for c in commands.keys():
                    if args[0] == c[:len(args[0])]:
                        commands[c](me)
                        commandFound = True
                        break

                if args[0] == "take":
                    try:
                        if "item" in itens[currentRoom] and args[1] in itens[currentRoom]["item"]:
                            inventory.append(args[1])
                            moves += 1
                            print(args[1]+":" + " Taken.\n")
                            del itens[currentRoom]["item"]
                        else:
                            print("Can't get this.\n")

                    except:
                        print("Invalid.\n")

                if args[0] == "drop":
                    try:
                        if args[1] in inventory:
                            inventory.remove(args[1])
                            moves += 1
                            print(args[1]+":" + " Dropped.\n")

                        else:
                            print("Can't drop this.\n")

                    except:
                        print("Invalid.\n")

                if args[0] == "eat":
                      try:
                           if args[1] in inventory and args[1] in can_eat:
                                 global health, health_max
                                 if args[1] == can_eat[0]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 5 > health_max:
                                             inventory.remove('bread')
                                             health = 75
                                             print("You eat the bread.\n")
                                       else:
                                             inventory.remove('bread')
                                             health += 5
                                             print("You eat the bread.\n")

                                 elif args[1] == can_eat[1]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 5 > health_max:
                                             inventory.remove('apple')
                                             health = 75
                                             print("You eat the apple.\n")
                                       else:
                                             inventory.remove('apple')
                                             health += 5
                                             print("You eat the apple.\n")

                                 elif args[1] == can_eat[2]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 3 > health_max:
                                             inventory.remove('carrot')
                                             health = 75
                                             print("You eat the carrot.\n")
                                       else:
                                             inventory.remove('carrot')
                                             health += 3
                                             print("You eat the carrot.\n")

                                 elif args[1] == can_eat[3]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 4 > health_max:
                                             inventory.remove('tomato')
                                             health = 75
                                             print("You eat the tomato.\n")
                                       else:
                                             inventory.remove('tomato')
                                             health += 4
                                             print("You eat the tomato.\n")

                                 elif args[1] == can_eat[4]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 4 > health_max:
                                             inventory.remove('potato')
                                             health = 75
                                             print("You eat the potato.\n")
                                       else:
                                             inventory.remove('potato')
                                             health += 4
                                             print("You eat the potato.\n")

                                 elif args[1] == can_eat[5]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 2 > health_max:
                                             inventory.remove('onion')
                                             health = 75
                                             print("You eat the onion.\n")
                                       else:
                                             inventory.remove('onion')
                                             health += 2
                                             print("You eat the onion.\n")

                                 else:
                                     print("You can't eat this.\n")
                           else:
                               print("You don't have this.\n")
                      except:
                            print("Eat what?\n")

                if args[0] == "turn":
                    try:
                        if args[1] == 'lantern':
                            global lantern_on
                            if 'lantern' in inventory:
                                if args[2] == 'on':
                                    lantern_on = True
                                    moves += 1
                                    print("The lantern is now on.\n")

                                elif args[2] == 'off':
                                    lantern_on = False
                                    moves += 1
                                    print("The lantern is now off.\n")
                            else:
                                print("You don't have a lantern.\n")
                    except:
                        print("Invalid.\n")

                if args[0] == "say":
                    try:
                        if args[1] != None:
                            print("You say:" + " " + args[1])
                            print("")
                            moves += 1
                        else:
                            pass
                    except:
                        print("Say what?\n")

                if args[0] == 'read':
                    try:
                        if args[1] == 'paper':
                            if 'paper' in inventory:
                                global paper
                                moves += 1
                                print(paper)
                            else:
                                pass

                        elif args[1] == 'note':
                            if 'note' in inventory:
                                global note
                                moves += 1
                                print(note)
                            else:
                                pass

                        elif args[1] == 'post-it':
                            if 'post-it' in inventory:
                                global post
                                moves += 1
                                print(post)
                            else:
                                pass

                        elif args[1] == 'poster':
                            if 'poster' in inventory:
                                global poster
                                moves += 1
                                print(poster)
                            else:
                                pass

                        else:
                            pass

                    except:
                        print("Read what?\n")

                if args[0] == 'look':
                    global key_desc
                    global sword_desc
                    global knife_desc
                    global ruby_desc
                    global amulet_desc
                    try:
                        if args[1] == 'at':
                            try:
                                if args[2] in inventory:
                                    if args[2] == 'key':
                                        print(key_desc)

                                    elif args[2] == 'sword':
                                        print(sword_desc)

                                    elif args[2] == 'knife':
                                        print(knife_desc)

                                    elif args[2] == 'ruby':
                                        print(ruby_desc)

                                    elif args[2] == 'amulet':
                                        print(amulet_desc)

                                    else:
                                        print("I see nothing special about this.\n")

                                else:
                                    print("You don't have this item.\n")

                            except:
                                print("Look at what?\n")

                    except:
                        print("Look at what?\n")

    def up(self):
        global moves
        moves += 1
        print("You can't go that way.\n")

    def down(self):
        global moves
        moves += 1
        print("You can't go that way.\n")

    def north(self):
        global moves
        moves += 1
        print("")

    def south(self):
        global moves
        moves += 1
        print("")

    def west(self):
        global moves
        moves += 1
        complete = True
        cm = CoalMine()
        cm.inicio()

    def east(self):
        global moves
        moves += 1
        complete = True
        pe = Passage()
        pe.inicio()

#I like that way
class SmallRoom2:
    def __init__(self):
        self.state = 'smallroom2'

    def quit(self):
        c = character()
        c.quit()

    def ajuda(self):
        c = character()
        c.ajuda()

    def status(self):
        c = character()
        c.status()

    def restart(self):
        c = character()
        c.restart()

    def score(self):
        c = character()
        c.score()

    def save(self):
        save()

    def achievement(self):
        c = character()
        c.achievement()

    def inventory(self):
        if len(inventory) > 0:
            print("You have:")
            print inventory
            print("")
        else:
            print("Your inventory is empty.\n")

    def up(self):
        global moves
        moves += 1
        ot = Out()
        ot.inicio()

    def down(self):
        global moves
        moves += 1
        print("You can't go that way.\n")

    def north(self):
        global moves
        moves += 1
        print("You can't go that way.\n")

    def east(self):
        global moves
        moves += 1
        print("You are in front of the stairs you can go up.\n")

    def south(self):
        global moves
        moves += 1
        print("You can't go that way.\n")

    def west(self):
        global moves
        moves += 1
        complete = True
        sr = SmallRoom()
        sr.inicio()

    def inicio(self):
        complete = False
        global moves, local
        local = 'SmallRoom2'
        print("Small Room")
        print("|-|")
        print("| |-----|")
        print("|  _  @E|")
        print("| |-----|")
        print("| |")
        print("You are in front of the stairs.")
        print("You can go west and go up.\n")

        itens = {
        1 : {}
        }
        currentRoom = 1

        commands = {
        'help': SmallRoom2.ajuda,
        'quit': SmallRoom2.quit,
        'save': SmallRoom2.save,
        'score': SmallRoom2.score,
        'achievement': SmallRoom2.achievement,
        'north': SmallRoom2.north,
        'west': SmallRoom2.west,
        'east': SmallRoom2.east,
        'south': SmallRoom2.south,
        'up': SmallRoom2.up,
        'down': SmallRoom2.down,
        'status': SmallRoom2.status,
        'restart': SmallRoom2.restart,
        'inventory': SmallRoom2.inventory
        }

        sr2 = SmallRoom2()

        while complete == False:
            line = raw_input("> ")
            args = line.split()
            if len(args) == 0:
                print("What you want to do?\n")

            elif len(args) > 0:
                commandFound = False
                for c in commands.keys():
                    if args[0] == c[:len(args[0])]:
                        commands[c](sr2)
                        commandFound = True
                        break

                if args[0] == "take":
                    try:
                        if "item" in itens[currentRoom] and args[1] in itens[currentRoom]["item"]:
                            inventory.append(args[1])
                            moves += 1
                            print(args[1]+":" + " Taken.\n")
                            del itens[currentRoom]["item"]
                        else:
                            print("Can't get this.\n")

                    except:
                        print("Invalid.\n")

                if args[0] == "drop":
                    try:
                        if args[1] in inventory:
                            inventory.remove(args[1])
                            moves += 1
                            print(args[1]+":" + " Dropped.\n")

                        else:
                            print("Can't drop this.\n")

                    except:
                        print("Invalid.\n")

                if args[0] == "eat":
                      try:
                           if args[1] in inventory and args[1] in can_eat:
                                 global health, health_max
                                 if args[1] == can_eat[0]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 5 > health_max:
                                             inventory.remove('bread')
                                             health = 75
                                             print("You eat the bread.\n")
                                       else:
                                             inventory.remove('bread')
                                             health += 5
                                             print("You eat the bread.\n")

                                 elif args[1] == can_eat[1]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 5 > health_max:
                                             inventory.remove('apple')
                                             health = 75
                                             print("You eat the apple.\n")
                                       else:
                                             inventory.remove('apple')
                                             health += 5
                                             print("You eat the apple.\n")

                                 elif args[1] == can_eat[2]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 3 > health_max:
                                             inventory.remove('carrot')
                                             health = 75
                                             print("You eat the carrot.\n")
                                       else:
                                             inventory.remove('carrot')
                                             health += 3
                                             print("You eat the carrot.\n")

                                 elif args[1] == can_eat[3]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 4 > health_max:
                                             inventory.remove('tomato')
                                             health = 75
                                             print("You eat the tomato.\n")
                                       else:
                                             inventory.remove('tomato')
                                             health += 4
                                             print("You eat the tomato.\n")

                                 elif args[1] == can_eat[4]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 4 > health_max:
                                             inventory.remove('potato')
                                             health = 75
                                             print("You eat the potato.\n")
                                       else:
                                             inventory.remove('potato')
                                             health += 4
                                             print("You eat the potato.\n")

                                 elif args[1] == can_eat[5]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 2 > health_max:
                                             inventory.remove('onion')
                                             health = 75
                                             print("You eat the onion.\n")
                                       else:
                                             inventory.remove('onion')
                                             health += 2
                                             print("You eat the onion.\n")

                                 else:
                                     print("You can't eat this.\n")
                           else:
                               print("You don't have this.\n")
                      except:
                            print("Eat what?\n")

                if args[0] == "turn":
                    try:
                        if args[1] == 'lantern':
                            global lantern_on
                            if 'lantern' in inventory:
                                if args[2] == 'on':
                                    lantern_on = True
                                    moves += 1
                                    print("The lantern is now on.\n")

                                elif args[2] == 'off':
                                    moves += 1
                                    lantern_on = False
                                    print("The lantern is now off.\n")
                            else:
                                print("You don't have a lantern.\n")
                    except:
                        print("Invalid.\n")

                if args[0] == "say":
                    try:
                        if args[1] != None:
                            print("You say:" + " " + args[1])
                            print("")
                            moves += 1
                        else:
                            pass
                    except:
                        print("Say what?\n")

                if args[0] == 'read':
                    try:
                        if args[1] == 'paper':
                            if 'paper' in inventory:
                                global paper
                                moves += 1
                                print(paper)
                            else:
                                pass

                        elif args[1] == 'note':
                            if 'note' in inventory:
                                global note
                                moves += 1
                                print(note)
                            else:
                                pass

                        elif args[1] == 'post-it':
                            if 'post-it' in inventory:
                                global post
                                moves += 1
                                print(post)
                            else:
                                pass

                        elif args[1] == 'poster':
                            if 'poster' in inventory:
                                global poster
                                moves += 1
                                print(poster)
                            else:
                                pass

                        else:
                            pass

                    except:
                        print("Read what?\n")

                if args[0] == 'look':
                    global key_desc
                    global sword_desc
                    global knife_desc
                    global ruby_desc
                    global amulet_desc
                    try:
                        if args[1] == 'at':
                            try:
                                if args[2] in inventory:
                                    if args[2] == 'key':
                                        print(key_desc)

                                    elif args[2] == 'sword':
                                        print(sword_desc)

                                    elif args[2] == 'knife':
                                        print(knife_desc)

                                    elif args[2] == 'ruby':
                                        print(ruby_desc)

                                    elif args[2] == 'amulet':
                                        print(amulet_desc)

                                    else:
                                        print("I see nothing special about this.\n")

                                else:
                                    print("You don't have this item.\n")

                            except:
                                print("Look at what?\n")

                    except:
                        print("Look at what?\n")

class SmallRoom:
    def __init__(self):
        self.state = 'smallroom'

    def quit(self):
        c = character()
        c.quit()

    def ajuda(self):
        c = character()
        c.ajuda()

    def status(self):
        c = character()
        c.status()

    def restart(self):
        c = character()
        c.restart()

    def score(self):
        c = character()
        c.score()

    def save(self):
        save()

    def achievement(self):
        c = character()
        c.achievement()

    def inventory(self):
        if len(inventory) > 0:
            print("You have:")
            print inventory
            print("")
        else:
            print("Your inventory is empty.\n")

    def up(self):
        global moves
        moves += 1
        print("You can't go that way.\n")

    def down(self):
        global moves
        moves += 1
        print("You can't go that way.\n")

    def north(self):
        global moves
        moves += 1
        print("You can't go that way.\n")

    def east(self):
        global moves
        moves += 1
        complete = True
        sr2 = SmallRoom2()
        sr2.inicio()

    def south(self):
        global moves
        moves += 1
        print("You can't go that way.\n")

    def west(self):
        global moves
        moves += 1
        complete = True
        r3 = Room3()
        r3.inicio()

    def inicio(self):
        complete = False
        global moves
        global passed
        global passed2, local
        local = 'SmallRoom'
        print("Small Room")
        print("|-|")
        print("| |-----|")
        print("|  _ @ E|")
        print("| |-----|")
        print("| |")
        passed2 = True
        if passed == True:
            print("There is stairs to east.")
            print("You can go west and east.\n")
        else:
            print("You open the door and enter in a small room.")
            print("There is stairs to east.")
            print("You can go west and east.\n")
            passed = True

        itens = {
        1 : {}
        }
        currentRoom = 1

        commands = {
        'help': SmallRoom.ajuda,
        'quit': SmallRoom.quit,
        'save': SmallRoom.save,
        'score': SmallRoom.score,
        'achievement': SmallRoom.achievement,
        'north': SmallRoom.north,
        'west': SmallRoom.west,
        'east': SmallRoom.east,
        'south': SmallRoom.south,
        'up': SmallRoom.up,
        'down': SmallRoom.down,
        'status': SmallRoom.status,
        'restart': SmallRoom.restart,
        'inventory': SmallRoom.inventory
        }

        sr = SmallRoom()

        while complete == False:
            line = raw_input("> ")
            args = line.split()
            if len(args) == 0:
                print("What you want to do?\n")

            elif len(args) > 0:
                commandFound = False
                for c in commands.keys():
                    if args[0] == c[:len(args[0])]:
                        commands[c](sr)
                        commandFound = True
                        break

                if args[0] == "take":
                    try:
                        if "item" in itens[currentRoom] and args[1] in itens[currentRoom]["item"]:
                            inventory.append(args[1])
                            moves += 1
                            print(args[1]+":" + " Taken.\n")
                            del itens[currentRoom]["item"]
                        else:
                            print("Can't get this.\n")

                    except:
                        print("Invalid.\n")

                if args[0] == "drop":
                    try:
                        if args[1] in inventory:
                            inventory.remove(args[1])
                            moves += 1
                            print(args[1]+":" + " Dropped.\n")

                        else:
                            print("Can't drop this.\n")

                    except:
                        print("Invalid.\n")

                if args[0] == "eat":
                      try:
                           if args[1] in inventory and args[1] in can_eat:
                                 global health, health_max
                                 if args[1] == can_eat[0]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 5 > health_max:
                                             inventory.remove('bread')
                                             health = 75
                                             print("You eat the bread.\n")
                                       else:
                                             inventory.remove('bread')
                                             health += 5
                                             print("You eat the bread.\n")

                                 elif args[1] == can_eat[1]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 5 > health_max:
                                             inventory.remove('apple')
                                             health = 75
                                             print("You eat the apple.\n")
                                       else:
                                             inventory.remove('apple')
                                             health += 5
                                             print("You eat the apple.\n")

                                 elif args[1] == can_eat[2]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 3 > health_max:
                                             inventory.remove('carrot')
                                             health = 75
                                             print("You eat the carrot.\n")
                                       else:
                                             inventory.remove('carrot')
                                             health += 3
                                             print("You eat the carrot.\n")

                                 elif args[1] == can_eat[3]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 4 > health_max:
                                             inventory.remove('tomato')
                                             health = 75
                                             print("You eat the tomato.\n")
                                       else:
                                             inventory.remove('tomato')
                                             health += 4
                                             print("You eat the tomato.\n")

                                 elif args[1] == can_eat[4]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 4 > health_max:
                                             inventory.remove('potato')
                                             health = 75
                                             print("You eat the potato.\n")
                                       else:
                                             inventory.remove('potato')
                                             health += 4
                                             print("You eat the potato.\n")

                                 elif args[1] == can_eat[5]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 2 > health_max:
                                             inventory.remove('onion')
                                             health = 75
                                             print("You eat the onion.\n")
                                       else:
                                             inventory.remove('onion')
                                             health += 2
                                             print("You eat the onion.\n")

                                 else:
                                     print("You can't eat this.\n")
                           else:
                               print("You don't have this.\n")
                      except:
                            print("Eat what?\n")

                if args[0] == "turn":
                    try:
                        if args[1] == 'lantern':
                            global lantern_on
                            if 'lantern' in inventory:
                                if args[2] == 'on':
                                    lantern_on = True
                                    moves += 1
                                    print("The lantern is now on.\n")

                                elif args[2] == 'off':
                                    lantern_on = False
                                    moves += 1
                                    print("The lantern is now off.\n")
                            else:
                                print("You don't have a lantern.\n")
                    except:
                        print("Invalid.\n")

                if args[0] == "say":
                    try:
                        if args[1] != None:
                            print("You say:" + " " + args[1])
                            print("")
                            moves += 1
                        else:
                            pass
                    except:
                        print("Say what?\n")

                if args[0] == 'read':
                    try:
                        if args[1] == 'paper':
                            if 'paper' in inventory:
                                global paper
                                moves += 1
                                print(paper)
                            else:
                                pass

                        elif args[1] == 'note':
                            if 'note' in inventory:
                                global note
                                moves += 1
                                print(note)
                            else:
                                pass

                        elif args[1] == 'post-it':
                            if 'post-it' in inventory:
                                global post
                                moves += 1
                                print(post)
                            else:
                                pass

                        elif args[1] == 'poster':
                            if 'poster' in inventory:
                                global poster
                                moves += 1
                                print(poster)
                            else:
                                pass

                        else:
                            pass

                    except:
                        print("Read what?\n")

                if args[0] == 'look':
                    global key_desc
                    global sword_desc
                    global knife_desc
                    global ruby_desc
                    global amulet_desc
                    try:
                        if args[1] == 'at':
                            try:
                                if args[2] in inventory:
                                    if args[2] == 'key':
                                        print(key_desc)

                                    elif args[2] == 'sword':
                                        print(sword_desc)

                                    elif args[2] == 'knife':
                                        print(knife_desc)

                                    elif args[2] == 'ruby':
                                        print(ruby_desc)

                                    elif args[2] == 'amulet':
                                        print(amulet_desc)

                                    else:
                                        print("I see nothing special about this.\n")

                                else:
                                    print("You don't have this item.\n")

                            except:
                                print("Look at what?\n")

                    except:
                        print("Look at what?\n")

class Room4:
    def __init__(self):
        self.state = 'room4'

    def quit(self):
        c = character()
        c.quit()

    def ajuda(self):
        c = character()
        c.ajuda()

    def status(self):
        c = character()
        c.status()

    def restart(self):
        c = character()
        c.restart()

    def score(self):
        c = character()
        c.score()

    def save(self):
        save()

    def achievement(self):
        c = character()
        c.achievement()

    def inventory(self):
        if len(inventory) > 0:
            print("You have:")
            print inventory
            print("")
        else:
            print("Your inventory is empty.\n")

    def up(self):
        global moves
        moves += 1
        print("You can't go that way.\n")

    def down(self):
        global moves
        moves += 1
        print("You can't go that way.\n")

    def north(self):
        global moves
        moves += 1
        print("You can't go that way.\n")

    def east(self):
        global moves
        moves += 1
        print("You can't go that way.\n")

    def south(self):
        global moves
        moves += 1
        complete = True
        r3 = Room3()
        r3.inicio()

    def west(self):
        global moves
        moves += 1
        print("You can't go that way.\n")

    def inicio(self):
        complete = False
        global moves, local
        local = 'Room4'
        print("Passage")
        print("|-|")
        print("|@|")
        print("| D")
        print("| |")
        print("| |")
        print("You can go north and south.\n")

        itens = {
        1 : {}
        }
        currentRoom = 1

        commands = {
        'help': Room4.ajuda,
        'quit': Room4.quit,
        'score': Room4.score,
        'save': Room4.save,
        'achievement': Room4.achievement,
        'north': Room4.north,
        'west': Room4.west,
        'east': Room4.east,
        'south': Room4.south,
        'up': Room4.up,
        'down': Room4.down,
        'status': Room4.status,
        'restart': Room4.restart,
        'inventory': Room4.inventory
        }

        r4 = Room4()

        while complete == False:
            line = raw_input("> ")
            args = line.split()
            if len(args) == 0:
                  print("What you want to do?\n")

            elif len(args) > 0:
                commandFound = False
                for c in commands.keys():
                    if args[0] == c[:len(args[0])]:
                        commands[c](r4)
                        commandFound = True
                        break

                if args[0] == "take":
                    try:
                        if "item" in itens[currentRoom] and args[1] in itens[currentRoom]["item"]:
                            inventory.append(args[1])
                            moves += 1
                            print(args[1]+":" + " Taken.\n")
                            del itens[currentRoom]["item"]
                        else:
                            print("Can't get this.\n")

                    except:
                        print("Invalid.\n")

                if args[0] == "drop":
                    try:
                        if args[1] in inventory:
                            inventory.remove(args[1])
                            moves += 1
                            print(args[1]+":" + " Dropped.\n")

                        else:
                            print("Can't drop this.\n")

                    except:
                        print("Invalid.\n")

                if args[0] == "eat":
                      try:
                           if args[1] in inventory and args[1] in can_eat:
                                 global health, health_max
                                 if args[1] == can_eat[0]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 5 > health_max:
                                             inventory.remove('bread')
                                             health = 75
                                             print("You eat the bread.\n")
                                       else:
                                             inventory.remove('bread')
                                             health += 5
                                             print("You eat the bread.\n")

                                 elif args[1] == can_eat[1]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 5 > health_max:
                                             inventory.remove('apple')
                                             health = 75
                                             print("You eat the apple.\n")
                                       else:
                                             inventory.remove('apple')
                                             health += 5
                                             print("You eat the apple.\n")

                                 elif args[1] == can_eat[2]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 3 > health_max:
                                             inventory.remove('carrot')
                                             health = 75
                                             print("You eat the carrot.\n")
                                       else:
                                             inventory.remove('carrot')
                                             health += 3
                                             print("You eat the carrot.\n")

                                 elif args[1] == can_eat[3]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 4 > health_max:
                                             inventory.remove('tomato')
                                             health = 75
                                             print("You eat the tomato.\n")
                                       else:
                                             inventory.remove('tomato')
                                             health += 4
                                             print("You eat the tomato.\n")

                                 elif args[1] == can_eat[4]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 4 > health_max:
                                             inventory.remove('potato')
                                             health = 75
                                             print("You eat the potato.\n")
                                       else:
                                             inventory.remove('potato')
                                             health += 4
                                             print("You eat the potato.\n")

                                 elif args[1] == can_eat[5]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 2 > health_max:
                                             inventory.remove('onion')
                                             health = 75
                                             print("You eat the onion.\n")
                                       else:
                                             inventory.remove('onion')
                                             health += 2
                                             print("You eat the onion.\n")

                                 else:
                                     print("You can't eat this.\n")
                           else:
                               print("You don't have this.\n")
                      except:
                            print("Eat what?\n")

                if args[0] == "turn":
                    try:
                        if args[1] == 'lantern':
                            global lantern_on
                            if 'lantern' in inventory:
                                if args[2] == 'on':
                                    lantern_on = True
                                    moves += 1
                                    print("The lantern is now on.\n")

                                elif args[2] == 'off':
                                    lantern_on = False
                                    moves += 1
                                    print("The lantern is now off.\n")
                            else:
                                print("You don't have a lantern.\n")
                    except:
                        print("Invalid.\n")

                if args[0] == "say":
                    try:
                        if args[1] != None:
                            print("You say:" + " " + args[1])
                            print("")
                            moves += 1
                        else:
                            pass
                    except:
                        print("Say what?\n")

                if args[0] == 'read':
                    try:
                        if args[1] == 'paper':
                            if 'paper' in inventory:
                                global paper
                                moves += 1
                                print(paper)
                            else:
                                pass

                        elif args[1] == 'note':
                            if 'note' in inventory:
                                global note
                                moves += 1
                                print(note)
                            else:
                                pass

                        elif args[1] == 'post-it':
                            if 'post-it' in inventory:
                                global post
                                moves += 1
                                print(post)
                            else:
                                pass

                        elif args[1] == 'poster':
                            if 'poster' in inventory:
                                global poster
                                moves += 1
                                print(poster)
                            else:
                                pass

                        else:
                            pass

                    except:
                        print("Read what?\n")

                if args[0] == 'look':
                    global key_desc
                    global sword_desc
                    global knife_desc
                    global ruby_desc
                    global amulet_desc
                    try:
                        if args[1] == 'at':
                            try:
                                if args[2] in inventory:
                                    if args[2] == 'key':
                                        print(key_desc)

                                    elif args[2] == 'sword':
                                        print(sword_desc)

                                    elif args[2] == 'knife':
                                        print(knife_desc)

                                    elif args[2] == 'ruby':
                                        print(ruby_desc)

                                    elif args[2] == 'amulet':
                                        print(amulet_desc)

                                    else:
                                        print("I see nothing special about this.\n")

                                else:
                                    print("You don't have this item.\n")

                            except:
                                print("Look at what?\n")

                    except:
                        print("Look at what?\n")

class Room3:
    def __init__(self):
        self.state = 'room3'

    def quit(self):
        c = character()
        c.quit()

    def ajuda(self):
        c = character()
        c.ajuda()

    def status(self):
        c = character()
        c.status()

    def restart(self):
        c = character()
        c.restart()

    def score(self):
        c = character()
        c.score()

    def save(self):
        save()

    def achievement(self):
        c = character()
        c.achievement()

    def inventory(self):
        if len(inventory) > 0:
            print("You have:")
            print inventory
            print("")
        else:
            print("Your inventory is empty.\n")

    def up(self):
        global moves
        moves += 1
        print("You can't go that way.\n")

    def down(self):
        global moves
        moves += 1
        print("You can't go that way.\n")

    def north(self):
        global moves
        moves += 1
        complete = True
        r4 = Room4()
        r4.inicio()

    def east(self):
        global moves
        moves += 1
        complete = True
        sr = SmallRoom()
        sr.inicio()

    def south(self):
        global moves
        moves += 1
        complete = True
        r2= Room2()
        r2.inicio()

    def west(self):
        global moves
        moves += 1
        print("You can't go that way.\n")

    def inicio(self):
        complete = False
        global moves, local
        global passed2
        local = 'Room3'
        print("Passage")
        print("|-|")
        print("| |")
        print("|@D")
        print("| |")
        print("| |")
        if passed2 == True:
            print("You can go north, south and east.\n")

        else:
            print("You see a wood door to the east.")
            print("You can go north, south and east.\n")

        itens = {
        1 : {}
        }
        currentRoom = 1

        commands = {
        'help': Room3.ajuda,
        'quit': Room3.quit,
        'score': Room3.score,
        'save': Room3.save,
        'achievement': Room3.achievement,
        'north': Room3.north,
        'west': Room3.west,
        'east': Room3.east,
        'south': Room3.south,
        'up': Room3.up,
        'down': Room3.down,
        'status': Room3.status,
        'restart': Room3.restart,
        'inventory': Room3.inventory
        }

        r3 = Room3()

        while complete == False:
            line = raw_input("> ")
            args = line.split()
            if len(args) == 0:
                  print("What you want to do?\n")

            elif len(args) > 0:
                commandFound = False
                for c in commands.keys():
                    if args[0] == c[:len(args[0])]:
                        commands[c](r3)
                        commandFound = True
                        break

                if args[0] == "take":
                    try:
                        if "item" in itens[currentRoom] and args[1] in itens[currentRoom]["item"]:
                            inventory.append(args[1])
                            moves += 1
                            print(args[1]+":" + " Taken.\n")
                            del itens[currentRoom]["item"]
                        else:
                            print("Can't get this.\n")

                    except:
                        print("Invalid.\n")

                if args[0] == "drop":
                    try:
                        if args[1] in inventory:
                            inventory.remove(args[1])
                            moves += 1
                            print(args[1]+":" + " Dropped.\n")

                        else:
                            print("Can't drop this.\n")

                    except:
                        print("Invalid.\n")

                if args[0] == "eat":
                      try:
                           if args[1] in inventory and args[1] in can_eat:
                                 global health, health_max
                                 if args[1] == can_eat[0]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 5 > health_max:
                                             inventory.remove('bread')
                                             health = 75
                                             print("You eat the bread.\n")
                                       else:
                                             inventory.remove('bread')
                                             health += 5
                                             print("You eat the bread.\n")

                                 elif args[1] == can_eat[1]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 5 > health_max:
                                             inventory.remove('apple')
                                             health = 75
                                             print("You eat the apple.\n")
                                       else:
                                             inventory.remove('apple')
                                             health += 5
                                             print("You eat the apple.\n")

                                 elif args[1] == can_eat[2]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 3 > health_max:
                                             inventory.remove('carrot')
                                             health = 75
                                             print("You eat the carrot.\n")
                                       else:
                                             inventory.remove('carrot')
                                             health += 3
                                             print("You eat the carrot.\n")

                                 elif args[1] == can_eat[3]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 4 > health_max:
                                             inventory.remove('tomato')
                                             health = 75
                                             print("You eat the tomato.\n")
                                       else:
                                             inventory.remove('tomato')
                                             health += 4
                                             print("You eat the tomato.\n")

                                 elif args[1] == can_eat[4]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 4 > health_max:
                                             inventory.remove('potato')
                                             health = 75
                                             print("You eat the potato.\n")
                                       else:
                                             inventory.remove('potato')
                                             health += 4
                                             print("You eat the potato.\n")

                                 elif args[1] == can_eat[5]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 2 > health_max:
                                             inventory.remove('onion')
                                             health = 75
                                             print("You eat the onion.\n")
                                       else:
                                             inventory.remove('onion')
                                             health += 2
                                             print("You eat the onion.\n")

                                 else:
                                     print("You can't eat this.\n")
                           else:
                               print("You don't have this.\n")
                      except:
                            print("Eat what?\n")

                if args[0] == "turn":
                    try:
                        if args[1] == 'lantern':
                            global lantern_on
                            if 'lantern' in inventory:
                                if args[2] == 'on':
                                    lantern_on = True
                                    moves += 1
                                    print("The lantern is now on.\n")

                                elif args[2] == 'off':
                                    lantern_on = False
                                    moves += 1
                                    print("The lantern is now off.\n")
                            else:
                                print("You don't have a lantern.\n")
                    except:
                        print("Invalid.\n")

                if args[0] == "say":
                    try:
                        if args[1] != None:
                            moves += 1
                            print("You say:" + " " + args[1])
                            print("")
                        else:
                            pass
                    except:
                        print("Say what?\n")

                if args[0] == 'read':
                    try:
                        if args[1] == 'paper':
                            if 'paper' in inventory:
                                global paper
                                moves += 1
                                print(paper)
                            else:
                                pass

                        elif args[1] == 'note':
                            if 'note' in inventory:
                                global note
                                moves += 1
                                print(note)
                            else:
                                pass

                        elif args[1] == 'post-it':
                            if 'post-it' in inventory:
                                global post
                                moves += 1
                                print(post)
                            else:
                                pass

                        elif args[1] == 'poster':
                            if 'poster' in inventory:
                                global poster
                                moves += 1
                                print(poster)
                            else:
                                pass

                        else:
                            pass

                    except:
                        print("Read what?\n")

                if args[0] == 'look':
                    global key_desc
                    global sword_desc
                    global knife_desc
                    global ruby_desc
                    global amulet_desc
                    try:
                        if args[1] == 'at':
                            try:
                                if args[2] in inventory:
                                    if args[2] == 'key':
                                        print(key_desc)

                                    elif args[2] == 'sword':
                                        print(sword_desc)

                                    elif args[2] == 'knife':
                                        print(knife_desc)

                                    elif args[2] == 'ruby':
                                        print(ruby_desc)

                                    elif args[2] == 'amulet':
                                        print(amulet_desc)

                                    else:
                                        print("I see nothing special about this.\n")

                                else:
                                    print("You don't have this item.\n")

                            except:
                                print("Look at what?\n")

                    except:
                        print("Look at what?\n")

class Room2:
    def __init__(self):
        self.state = 'room2'

    def quit(self):
        c = character()
        c.quit()

    def ajuda(self):
        c = character()
        c.ajuda()

    def status(self):
        c = character()
        c.status()

    def restart(self):
        c = character()
        c.restart()

    def score(self):
        c = character()
        c.score()

    def save(self):
        save()

    def achievement(self):
        c = character()
        c.achievement()

    def inventory(self):
        if len(inventory) > 0:
            print("You have:")
            print inventory
            print("")
        else:
            print("Your inventory is empty.\n")

    def up(self):
        global moves
        moves += 1
        print("You can't go that way.\n")

    def down(self):
        global moves
        moves += 1
        print("You can't go that way.\n")

    def north(self):
        global moves
        moves += 1
        complete = True
        r3 = Room3()
        r3.inicio()

    def east(self):
        global moves
        moves += 1
        print("You can't go that way.\n")

    def south(self):
        global moves
        moves += 1
        complete = True
        r = Room()
        r.inicio()

    def west(self):
        global moves
        moves += 1
        print("You can't go that way.\n")

    def inicio(self):
        complete = False
        global moves, local
        local = 'Room2'
        print("Passage")
        print("|-|")
        print("| |")
        print("| D")
        print("|@|")
        print("| |")
        print("You can go north and south.\n")

        itens = {
        1 : {}
        }
        currentRoom = 1

        commands = {
        'help': Room2.ajuda,
        'quit': Room2.quit,
        'save': Room2.save,
        'score': Room2.score,
        'achievement': Room2.achievement,
        'north': Room2.north,
        'west': Room2.west,
        'east': Room2.east,
        'south': Room2.south,
        'up': Room2.up,
        'down': Room2.down,
        'status': Room2.status,
        'restart': Room2.restart,
        'inventory': Room2.inventory
        }

        r2 = Room2()

        while complete == False:
            line = raw_input("> ")
            args = line.split()
            if len(args) == 0:
                  print("What you want to do?\n")

            elif len(args) > 0:
                commandFound = False
                for c in commands.keys():
                    if args[0] == c[:len(args[0])]:
                        commands[c](r2)
                        commandFound = True
                        break

                if args[0] == "take":
                    try:
                        if "item" in itens[currentRoom] and args[1] in itens[currentRoom]["item"]:
                            inventory.append(args[1])
                            moves += 1
                            print(args[1]+":" + " Taken.\n")
                            del itens[currentRoom]["item"]
                        else:
                            print("Can't get this.\n")

                    except:
                        print("Invalid.\n")

                if args[0] == "drop":
                    try:
                        if args[1] in inventory:
                            inventory.remove(args[1])
                            moves += 1
                            print(args[1]+":" + " Dropped.\n")

                        else:
                            print("Can't drop this.\n")

                    except:
                        print("Invalid.\n")

                if args[0] == "eat":
                      try:
                           if args[1] in inventory and args[1] in can_eat:
                                 global health, health_max
                                 if args[1] == can_eat[0]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 5 > health_max:
                                             inventory.remove('bread')
                                             health = 75
                                             print("You eat the bread.\n")
                                       else:
                                             inventory.remove('bread')
                                             health += 5
                                             print("You eat the bread.\n")

                                 elif args[1] == can_eat[1]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 5 > health_max:
                                             inventory.remove('apple')
                                             health = 75
                                             print("You eat the apple.\n")
                                       else:
                                             inventory.remove('apple')
                                             health += 5
                                             print("You eat the apple.\n")

                                 elif args[1] == can_eat[2]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 3 > health_max:
                                             inventory.remove('carrot')
                                             health = 75
                                             print("You eat the carrot.\n")
                                       else:
                                             inventory.remove('carrot')
                                             health += 3
                                             print("You eat the carrot.\n")

                                 elif args[1] == can_eat[3]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 4 > health_max:
                                             inventory.remove('tomato')
                                             health = 75
                                             print("You eat the tomato.\n")
                                       else:
                                             inventory.remove('tomato')
                                             health += 4
                                             print("You eat the tomato.\n")

                                 elif args[1] == can_eat[4]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 4 > health_max:
                                             inventory.remove('potato')
                                             health = 75
                                             print("You eat the potato.\n")
                                       else:
                                             inventory.remove('potato')
                                             health += 4
                                             print("You eat the potato.\n")

                                 elif args[1] == can_eat[5]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 2 > health_max:
                                             inventory.remove('onion')
                                             health = 75
                                             print("You eat the onion.\n")
                                       else:
                                             inventory.remove('onion')
                                             health += 2
                                             print("You eat the onion.\n")

                                 else:
                                     print("You can't eat this.\n")
                           else:
                               print("You don't have this.\n")
                      except:
                            print("Eat what?\n")

                if args[0] == "turn":
                    try:
                        if args[1] == 'lantern':
                            global lantern_on
                            if 'lantern' in inventory:
                                if args[2] == 'on':
                                    lantern_on = True
                                    moves += 1
                                    print("The lantern is now on.\n")

                                elif args[2] == 'off':
                                    lantern_on = False
                                    moves += 1
                                    print("The lantern is now off.\n")
                            else:
                                print("You don't have a lantern.\n")
                    except:
                        print("Invalid.\n")

                if args[0] == "say":
                    try:
                        if args[1] != None:
                            moves += 1
                            print("You say:" + " " + args[1])
                            print("")
                        else:
                            pass
                    except:
                        print("Say what?\n")

                if args[0] == 'read':
                    try:
                        if args[1] == 'paper':
                            if 'paper' in inventory:
                                global paper
                                moves += 1
                                print(paper)
                            else:
                                pass

                        elif args[1] == 'note':
                            if 'note' in inventory:
                                global note
                                moves += 1
                                print(note)
                            else:
                                pass

                        elif args[1] == 'post-it':
                            if 'post-it' in inventory:
                                global post
                                moves += 1
                                print(post)
                            else:
                                pass

                        elif args[1] == 'poster':
                            if 'poster' in inventory:
                                global poster
                                moves += 1
                                print(poster)
                            else:
                                pass

                        else:
                            pass

                    except:
                        print("Read what?\n")

                if args[0] == 'look':
                    global key_desc
                    global sword_desc
                    global knife_desc
                    global ruby_desc
                    global amulet_desc
                    try:
                        if args[1] == 'at':
                            try:
                                if args[2] in inventory:
                                    if args[2] == 'key':
                                        print(key_desc)

                                    elif args[2] == 'sword':
                                        print(sword_desc)

                                    elif args[2] == 'knife':
                                        print(knife_desc)

                                    elif args[2] == 'ruby':
                                        print(ruby_desc)

                                    elif args[2] == 'amulet':
                                        print(amulet_desc)

                                    else:
                                        print("I see nothing special about this.\n")

                                else:
                                    print("You don't have this item.\n")

                            except:
                                print("Look at what?\n")

                    except:
                        print("Look at what?\n")

class Room:
    def __init__(self):
        self.state = 'room'

    def quit(self):
        c = character()
        c.quit()

    def ajuda(self):
        c = character()
        c.ajuda()

    def status(self):
        c = character()
        c.status()

    def restart(self):
        c = character()
        c.restart()

    def score(self):
        c = character()
        c.score()

    def save(self):
        save()

    def achievement(self):
        c = character()
        c.achievement()

    def inventory(self):
        if len(inventory) > 0:
            print("You have:")
            print inventory
            print("")
        else:
            print("Your inventory is empty.\n")

    def up(self):
        global moves
        moves += 1
        print("You can't go that way.\n")

    def down(self):
        global moves
        moves += 1
        print("You can't go that way.\n")

    def north(self):
        global moves
        moves += 1
        complete = True
        r2 = Room2()
        r2.inicio()

    def east(self):
        global moves
        moves += 1
        print("You can't go that way.\n")

    def south(self):
        global moves
        moves += 1
        complete = True
        pr = PreRoom()
        pr.inicio()

    def west(self):
        global moves
        moves += 1
        print("You can't go that way.\n")

    def inicio(self):
        complete = False
        global moves, local
        local = 'Room'
        print("Passage")
        print("|-|")
        print("| |")
        print("| D")
        print("| |")
        print("|@|")
        print("You can go north and south.\n")

        itens = {
        1 : {}
        }
        currentRoom = 1

        commands = {
        'help': Room.ajuda,
        'quit': Room.quit,
        'save': Room.save,
        'score': Room.score,
        'achievement': Room.achievement,
        'north': Room.north,
        'west': Room.west,
        'east': Room.east,
        'south': Room.south,
        'up': Room.up,
        'down': Room.down,
        'status': Room.status,
        'restart': Room.restart,
        'inventory': Room.inventory
        }

        r = Room()

        while complete == False:
            line = raw_input("> ")
            args = line.split()
            if len(args) == 0:
                  print("What you want to do?\n")

            elif len(args) > 0:
                commandFound = False
                for c in commands.keys():
                    if args[0] == c[:len(args[0])]:
                        commands[c](r)
                        commandFound = True
                        break

                if args[0] == "take":
                    try:
                        if "item" in itens[currentRoom] and args[1] in itens[currentRoom]["item"]:
                            inventory.append(args[1])
                            moves += 1
                            print(args[1]+":" + " Taken.\n")
                            del itens[currentRoom]["item"]
                        else:
                            print("Can't get this.\n")

                    except:
                        print("Invalid.\n")

                if args[0] == "drop":
                    try:
                        if args[1] in inventory:
                            inventory.remove(args[1])
                            moves += 1
                            print(args[1]+":" + " Dropped.\n")

                        else:
                            print("Can't drop this.\n")

                    except:
                        print("Invalid.\n")

                if args[0] == "eat":
                      try:
                           if args[1] in inventory and args[1] in can_eat:
                                 global health, health_max
                                 if args[1] == can_eat[0]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 5 > health_max:
                                             inventory.remove('bread')
                                             health = 75
                                             print("You eat the bread.\n")
                                       else:
                                             inventory.remove('bread')
                                             health += 5
                                             print("You eat the bread.\n")

                                 elif args[1] == can_eat[1]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 5 > health_max:
                                             inventory.remove('apple')
                                             health = 75
                                             print("You eat the apple.\n")
                                       else:
                                             inventory.remove('apple')
                                             health += 5
                                             print("You eat the apple.\n")

                                 elif args[1] == can_eat[2]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 3 > health_max:
                                             inventory.remove('carrot')
                                             health = 75
                                             print("You eat the carrot.\n")
                                       else:
                                             inventory.remove('carrot')
                                             health += 3
                                             print("You eat the carrot.\n")

                                 elif args[1] == can_eat[3]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 4 > health_max:
                                             inventory.remove('tomato')
                                             health = 75
                                             print("You eat the tomato.\n")
                                       else:
                                             inventory.remove('tomato')
                                             health += 4
                                             print("You eat the tomato.\n")

                                 elif args[1] == can_eat[4]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 4 > health_max:
                                             inventory.remove('potato')
                                             health = 75
                                             print("You eat the potato.\n")
                                       else:
                                             inventory.remove('potato')
                                             health += 4
                                             print("You eat the potato.\n")

                                 elif args[1] == can_eat[5]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 2 > health_max:
                                             inventory.remove('onion')
                                             health = 75
                                             print("You eat the onion.\n")
                                       else:
                                             inventory.remove('onion')
                                             health += 2
                                             print("You eat the onion.\n")

                                 else:
                                     print("You can't eat this.\n")
                           else:
                               print("You don't have this.\n")
                      except:
                            print("Eat what?\n")

                if args[0] == "turn":
                    try:
                        if args[1] == 'lantern':
                            global lantern_on
                            if 'lantern' in inventory:
                                if args[2] == 'on':
                                    lantern_on = True
                                    moves += 1
                                    print("The lantern is now on.\n")

                                elif args[2] == 'off':
                                    lantern_on = False
                                    moves += 1
                                    print("The lantern is now off.\n")
                            else:
                                print("You don't have a lantern.\n")
                    except:
                        print("Invalid.\n")

                if args[0] == "say":
                    try:
                        if args[1] != None:
                            moves += 1
                            print("You say:" + " " + args[1])
                            print("")
                        else:
                            pass
                    except:
                        print("Say what?\n")

                if args[0] == 'read':
                    try:
                        if args[1] == 'paper':
                            if 'paper' in inventory:
                                global paper
                                moves += 1
                                print(paper)
                            else:
                                pass

                        elif args[1] == 'note':
                            if 'note' in inventory:
                                global note
                                moves += 1
                                print(note)
                            else:
                                pass

                        elif args[1] == 'post-it':
                            if 'post-it' in inventory:
                                global post
                                moves += 1
                                print(post)
                            else:
                                pass

                        elif args[1] == 'poster':
                            if 'poster' in inventory:
                                global poster
                                moves += 1
                                print(poster)
                            else:
                                pass

                        else:
                            pass

                    except:
                        print("Read what?\n")

                if args[0] == 'look':
                    global key_desc
                    global sword_desc
                    global knife_desc
                    global ruby_desc
                    global amulet_desc
                    try:
                        if args[1] == 'at':
                            try:
                                if args[2] in inventory:
                                    if args[2] == 'key':
                                        print(key_desc)

                                    elif args[2] == 'sword':
                                        print(sword_desc)

                                    elif args[2] == 'knife':
                                        print(knife_desc)

                                    elif args[2] == 'ruby':
                                        print(ruby_desc)

                                    elif args[2] == 'amulet':
                                        print(amulet_desc)

                                    else:
                                        print("I see nothing special about this.\n")

                                else:
                                    print("You don't have this item.\n")

                            except:
                                print("Look at what?\n")

                    except:
                        print("Look at what?\n")

class PreRoom:
    def __init__(self):
        self.state = 'preroom'

    def quit(self):
        c = character()
        c.quit()

    def ajuda(self):
        c = character()
        c.ajuda()

    def status(self):
        c = character()
        c.status()

    def restart(self):
        c = character()
        c.restart()

    def score(self):
        c = character()
        c.score()

    def save(self):
        save()

    def achievement(self):
        c = character()
        c.achievement()

    def inventory(self):
        if len(inventory) > 0:
            print("You have:")
            print inventory
            print("")
        else:
            print("Your inventory is empty.\n")

    def up(self):
        global moves
        moves += 1
        print("You can't go that way.\n")

    def down(self):
        global moves
        moves += 1
        print("You can't go that way.\n")

    def north(self):
        global moves
        moves += 1
        complete = True
        r = Room()
        r.inicio()

    def east(self):
        global moves
        moves += 1
        print("You can't go that way.\n")

    def south(self):
        global moves
        moves += 1
        complete = True
        a = Altar()
        a.inicio()

    def west(self):
        global moves
        moves += 1
        print("You can't go that way.\n")

    def inicio(self):
        complete = False
        global moves, local
        local = 'PreRoom'
        print("Passage")
        print("- -")
        print("|@|")
        print("- -")
        print("You are in a narrow passage.")
        print("You can go north and south.\n")

        itens = {
        1 : {}
        }
        currentRoom = 1

        commands = {
        'help': PreRoom.ajuda,
        'quit': PreRoom.quit,
        'score': PreRoom.score,
        'achievement': PreRoom.achievement,
        'north': PreRoom.north,
        'west': PreRoom.west,
        'east': PreRoom.east,
        'south': PreRoom.south,
        'up': PreRoom.up,
        'down': PreRoom.down,
        'status': PreRoom.status,
        'restart': PreRoom.restart,
        'inventory': PreRoom.inventory
        }

        pr = PreRoom()

        while complete == False:
            line = raw_input("> ")
            args = line.split()
            if len(args) == 0:
                  print("What you want to do?\n")

            elif len(args) > 0:
                commandFound = False
                for c in commands.keys():
                    if args[0] == c[:len(args[0])]:
                        commands[c](pr)
                        commandFound = True
                        break

                if args[0] == "take":
                    try:
                        if "item" in itens[currentRoom] and args[1] in itens[currentRoom]["item"]:
                            inventory.append(args[1])
                            moves += 1
                            print(args[1]+":" + " Taken.\n")
                            del itens[currentRoom]["item"]
                        else:
                            print("Can't get this.\n")

                    except:
                        print("Invalid.\n")

                if args[0] == "drop":
                    try:
                        if args[1] in inventory:
                            inventory.remove(args[1])
                            moves += 1
                            print(args[1]+":" + " Dropped.\n")

                        else:
                            print("Can't drop this.\n")

                    except:
                        print("Invalid.\n")

                if args[0] == "eat":
                      try:
                           if args[1] in inventory and args[1] in can_eat:
                                 global health, health_max
                                 if args[1] == can_eat[0]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 5 > health_max:
                                             inventory.remove('bread')
                                             health = 75
                                             print("You eat the bread.\n")
                                       else:
                                             inventory.remove('bread')
                                             health += 5
                                             print("You eat the bread.\n")

                                 elif args[1] == can_eat[1]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 5 > health_max:
                                             inventory.remove('apple')
                                             health = 75
                                             print("You eat the apple.\n")
                                       else:
                                             inventory.remove('apple')
                                             health += 5
                                             print("You eat the apple.\n")

                                 elif args[1] == can_eat[2]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 3 > health_max:
                                             inventory.remove('carrot')
                                             health = 75
                                             print("You eat the carrot.\n")
                                       else:
                                             inventory.remove('carrot')
                                             health += 3
                                             print("You eat the carrot.\n")

                                 elif args[1] == can_eat[3]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 4 > health_max:
                                             inventory.remove('tomato')
                                             health = 75
                                             print("You eat the tomato.\n")
                                       else:
                                             inventory.remove('tomato')
                                             health += 4
                                             print("You eat the tomato.\n")

                                 elif args[1] == can_eat[4]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 4 > health_max:
                                             inventory.remove('potato')
                                             health = 75
                                             print("You eat the potato.\n")
                                       else:
                                             inventory.remove('potato')
                                             health += 4
                                             print("You eat the potato.\n")

                                 elif args[1] == can_eat[5]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 2 > health_max:
                                             inventory.remove('onion')
                                             health = 75
                                             print("You eat the onion.\n")
                                       else:
                                             inventory.remove('onion')
                                             health += 2
                                             print("You eat the onion.\n")

                                 else:
                                     print("You can't eat this.\n")
                           else:
                               print("You don't have this.\n")
                      except:
                            print("Eat what?\n")

                if args[0] == "turn":
                    try:
                        if args[1] == 'lantern':
                            global lantern_on
                            if 'lantern' in inventory:
                                if args[2] == 'on':
                                    lantern_on = True
                                    moves += 1
                                    print("The lantern is now on.\n")

                                elif args[2] == 'off':
                                    lantern_on = False
                                    moves += 1
                                    print("The lantern is now off.\n")
                            else:
                                print("You don't have a lantern.\n")
                    except:
                        print("Invalid.\n")

                if args[0] == "say":
                    try:
                        if args[1] != None:
                            moves += 1
                            print("You say:" + " " + args[1])
                            print("")
                        else:
                            pass
                    except:
                        print("Say what?\n")

                if args[0] == 'read':
                    try:
                        if args[1] == 'paper':
                            if 'paper' in inventory:
                                global paper
                                moves += 1
                                print(paper)
                            else:
                                pass

                        elif args[1] == 'note':
                            if 'note' in inventory:
                                global note
                                moves += 1
                                print(note)
                            else:
                                pass

                        elif args[1] == 'post-it':
                            if 'post-it' in inventory:
                                global post
                                moves += 1
                                print(post)
                            else:
                                pass

                        elif args[1] == 'poster':
                            if 'poster' in inventory:
                                global poster
                                moves += 1
                                print(poster)
                            else:
                                pass

                        else:
                            pass

                    except:
                        print("Read what?\n")

                if args[0] == 'look':
                    global key_desc
                    global sword_desc
                    global knife_desc
                    global ruby_desc
                    global amulet_desc
                    try:
                        if args[1] == 'at':
                            try:
                                if args[2] in inventory:
                                    if args[2] == 'key':
                                        print(key_desc)

                                    elif args[2] == 'sword':
                                        print(sword_desc)

                                    elif args[2] == 'knife':
                                        print(knife_desc)

                                    elif args[2] == 'ruby':
                                        print(ruby_desc)

                                    elif args[2] == 'amulet':
                                        print(amulet_desc)

                                    else:
                                        print("I see nothing special about this.\n")

                                else:
                                    print("You don't have this item.\n")

                            except:
                                print("Look at what?\n")

                    except:
                        print("Look at what?\n")

class Altar:
    def __init__(self):
        self.state = 'altar'

    def quit(self):
        c = character()
        c.quit()

    def ajuda(self):
        c = character()
        c.ajuda()

    def status(self):
        c = character()
        c.status()

    def restart(self):
        c = character()
        c.restart()

    def score(self):
        c = character()
        c.score()

    def save(self):
        save()

    def achievement(self):
        c = character()
        c.achievement()

    def inventory(self):
        if len(inventory) > 0:
            print("You have:")
            print inventory
            print("")
        else:
            print("Your inventory is empty.\n")

    def up(self):
        global moves
        moves += 1
        print("You can't go that way.\n")

    def down(self):
        global moves
        moves += 1
        print("You can't go that way.\n")

    def north(self):
        global moves
        moves += 1
        if killed == False:
            print("There is a Troll blocking your passage.\n")
        else:
            pr = PreRoom()
            pr.inicio()

    def east(self):
        global moves
        moves += 1
        print("Nothing here.\n")

    def south(self):
        global moves
        moves += 1
        complete = True
        pa = PreAltar()
        pa.inicio()

    def west(self):
        global moves
        moves += 1
        print("Nothing here.\n")

    def inicio(self):
        global moves
        global killed
        global reward
        global local
        global troll_life
        local = 'Altar'
        enemy = ['Troll']
        complete = False

        print("Altar")
        if killed == False:
            print("You are in a small room with a Troll blocking your passage.\n")
        else:
            print("")

        itens = {
        1 : {}
        }
        currentRoom = 1

        commands = {
        'help': Altar.ajuda,
        'quit': Altar.quit,
        'save': Altar.save,
        'score': Altar.score,
        'achievement': Altar.achievement,
        'north': Altar.north,
        'west': Altar.west,
        'east': Altar.east,
        'south': Altar.south,
        'up': Altar.up,
        'down': Altar.down,
        'status': Altar.status,
        'restart': Altar.restart,
        'inventory': Altar.inventory
        }

        a = Altar()

        while complete == False:
            line = raw_input("> ")
            args = line.split()
            if len(args) == 0:
                  print("What you want to do?\n")

            elif len(args) > 0:
                commandFound = False
                for c in commands.keys():
                    if args[0] == c[:len(args[0])]:
                        commands[c](a)
                        commandFound = True
                        break

                if args[0] == "take":
                    try:
                        if "item" in itens[currentRoom] and args[1] in itens[currentRoom]["item"]:
                            inventory.append(args[1])
                            moves += 1
                            print(args[1]+":" + " Taken.\n")
                            del itens[currentRoom]["item"]
                        else:
                            print("Can't get this.\n")

                    except:
                        print("Invalid.\n")

                if args[0] == "drop":
                    try:
                        if args[1] in inventory:
                            inventory.remove(args[1])
                            moves += 1
                            print(args[1]+":" + " Dropped.\n")

                        else:
                            print("Can't drop this.\n")

                    except:
                        print("Invalid.\n")

                if args[0] == "eat":
                      try:
                           if args[1] in inventory and args[1] in can_eat:
                                 global health, health_max
                                 if args[1] == can_eat[0]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 5 > health_max:
                                             inventory.remove('bread')
                                             health = 75
                                             print("You eat the bread.\n")
                                       else:
                                             inventory.remove('bread')
                                             health += 5
                                             print("You eat the bread.\n")

                                 elif args[1] == can_eat[1]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 5 > health_max:
                                             inventory.remove('apple')
                                             health = 75
                                             print("You eat the apple.\n")
                                       else:
                                             inventory.remove('apple')
                                             health += 5
                                             print("You eat the apple.\n")

                                 elif args[1] == can_eat[2]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 3 > health_max:
                                             inventory.remove('carrot')
                                             health = 75
                                             print("You eat the carrot.\n")
                                       else:
                                             inventory.remove('carrot')
                                             health += 3
                                             print("You eat the carrot.\n")

                                 elif args[1] == can_eat[3]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 4 > health_max:
                                             inventory.remove('tomato')
                                             health = 75
                                             print("You eat the tomato.\n")
                                       else:
                                             inventory.remove('tomato')
                                             health += 4
                                             print("You eat the tomato.\n")

                                 elif args[1] == can_eat[4]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 4 > health_max:
                                             inventory.remove('potato')
                                             health = 75
                                             print("You eat the potato.\n")
                                       else:
                                             inventory.remove('potato')
                                             health += 4
                                             print("You eat the potato.\n")

                                 elif args[1] == can_eat[5]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 2 > health_max:
                                             inventory.remove('onion')
                                             health = 75
                                             print("You eat the onion.\n")
                                       else:
                                             inventory.remove('onion')
                                             health += 2
                                             print("You eat the onion.\n")

                                 else:
                                     print("You can't eat this.\n")
                           else:
                               print("You don't have this.\n")
                      except:
                            print("Eat what?\n")

                if args[0] == "turn":
                    try:
                        if args[1] == 'lantern':
                            global lantern_on
                            if 'lantern' in inventory:
                                if args[2] == 'on':
                                    lantern_on = True
                                    moves += 1
                                    print("The lantern is now on.\n")

                                elif args[2] == 'off':
                                    lantern_on = False
                                    moves += 1
                                    print("The lantern is now off.\n")
                            else:
                                print("You don't have a lantern.\n")
                    except:
                        print("Invalid.\n")

                if args[0] == "say":
                    try:
                        if args[1] != None:
                            print("You say:" + " " + args[1])
                            print("")
                            moves += 1
                        else:
                            pass
                    except:
                        print("Say what?\n")

                if args[0] == 'read':
                    try:
                        if args[1] == 'paper':
                            if 'paper' in inventory:
                                global paper
                                moves += 1
                                print(paper)
                            else:
                                pass

                        elif args[1] == 'note':
                            if 'note' in inventory:
                                global note
                                moves += 1
                                print(note)
                            else:
                                pass

                        elif args[1] == 'post-it':
                            if 'post-it' in inventory:
                                global post
                                moves += 1
                                print(post)
                            else:
                                pass

                        elif args[1] == 'poster':
                            if 'poster' in inventory:
                                global poster
                                moves += 1
                                print(poster)
                            else:
                                pass

                        else:
                            pass

                    except:
                        print("Read what?\n")

                if args[0] == 'look':
                    global key_desc
                    global sword_desc
                    global knife_desc
                    global ruby_desc
                    global amulet_desc
                    try:
                        if args[1] == 'at':
                            try:
                                if args[2] in inventory:
                                    if args[2] == 'key':
                                        print(key_desc)

                                    elif args[2] == 'sword':
                                        print(sword_desc)

                                    elif args[2] == 'knife':
                                        print(knife_desc)

                                    elif args[2] == 'ruby':
                                        print(ruby_desc)

                                    elif args[2] == 'amulet':
                                        print(amulet_desc)

                                    else:
                                        print("I see nothing special about this.\n")

                                else:
                                    print("You don't have this item.\n")

                            except:
                                print("Look at what?\n")

                    except:
                        print("Look at what?\n")

                if args[0] == "hit":
                    try:
                        if args[1] in enemy:
                            try:
                                if args[2] == 'with':
                                    global coins
                                    if args[3] == 'sword':
                                        if args[3] in inventory:
                                            global bonus
                                            bonus = 5

                                            if 'Troll' in enemy:
                                                if troll_life > 0:
                                                    troll_life -= attack + bonus + random.randint(1,10)
                                                    print("You hit the Troll with the sword.")
                                                    moves += 1
                                                    if troll_life > 0:
                                                        print("[Troll life]: %d")% troll_life
                                                        troll_attack = random.randint(1,10)
                                                        health -= troll_attack
                                                        print("The Troll is angry and hit you with the axe.")
                                                        print("[Your health]: %d\n")% health

                                                    else:
                                                        reward = True
                                                        killed = True
                                                        print("You made the Troll feel the sadness.")
                                                        achievement.append('sadness')
                                                        print("You unlock the achievement: " + R + "Just Sadness." + W + "\n" )

                                                else:
                                                    moves += 1
                                                    reward = True
                                                    killed = True
                                                    enemy.remove('Troll')
                                                    print("The Troll is crying because he is sad.\n")

                                        else:
                                            print("You don't have this item.\n")

                                    elif args[3] == 'knife':
                                        if args[3] in inventory:
                                            bonus = 3

                                            if 'Troll' in enemy:
                                                if troll_life > 0:
                                                    troll_life -= attack + bonus + random.randint(1,10)
                                                    print("You hit the Troll with the knife.")
                                                    moves += 1
                                                    if troll_life > 0:
                                                        print("[Troll life]: %d")% troll_life
                                                        troll_attack = random.randint(1,10)
                                                        health -= troll_attack
                                                        print("The Troll is angry and hit you with the axe.")
                                                        print("[Your health]: %d\n")% health

                                                    else:
                                                        reward = True
                                                        killed = True
                                                        print("You made the Troll feel the sadness.")
                                                        achievement.append('sadness')
                                                        print("You unlock the achievement: " + R + "Just Sadness." + W + "\n" )

                                                else:
                                                    moves += 1
                                                    reward = True
                                                    killed = True
                                                    enemy.remove('Troll')
                                                    print("The Troll is crying because he is sad.\n")

                                    elif args[3] == 'sadness':
                                        if args[3] in skill:
                                            bonus = 6

                                            if 'Troll' in enemy:
                                                if troll_life > 0:
                                                    troll_life -= attack + bonus + random.randint(1,10)
                                                    print("You hit the Troll with the Sad Attack.")
                                                    moves += 1
                                                    if troll_life > 0:
                                                        print("[Troll life]: %d")% troll_life
                                                        print("the troll is sad and cannot attack you.\n")

                                                    else:
                                                        reward = True
                                                        killed = True
                                                        print("You made the Troll feel the sadness.")
                                                        achievement.append('sadness')
                                                        print("You unlock the achievement: " + R + "Just Sadness." + W + "\n")

                                                else:
                                                    moves += 1
                                                    reward = True
                                                    killed = True
                                                    print("You made the Troll feel the sadness.\n")

                                            else:
                                                moves += 1
                                                print("The Troll is crying because he is sad.\n")

                                        else:
                                            print("You don't have this skill.\n")
                                    else:
                                        print("You can't use this.\n")
                                else:
                                    pass

                            except:
                                print("With what?\n")

                        else:
                            print("Who?\n")

                    except:
                        print("Who?\n")

class PreAltar:
    def __init__(self):
        self.state = 'pre-altar'

    def quit(self):
        c = character()
        c.quit()

    def ajuda(self):
        c = character()
        c.ajuda()

    def status(self):
        c = character()
        c.status()

    def restart(self):
        c = character()
        c.restart()

    def score(self):
        c = character()
        c.score()

    def save(self):
        save()

    def achievement(self):
        c = character()
        c.achievement()

    def inventory(self):
        if len(inventory) > 0:
            print("You have:")
            print inventory
            print("")
        else:
            print("Your inventory is empty.\n")

    def inicio(self):
        complete = False
        print("Cave")
        global moves, local
        local = 'PreAltar'
        global killed
        if killed == True:
            print("")
        else:
            print("Do you hear a strange sound from the north.\n")

        itens = {
        1 : {}
        }

        currentRoom = 1

        commands = {
        'help': PreAltar.ajuda,
        'quit': PreAltar.quit,
        'save': PreAltar.save,
        'score': PreAltar.score,
        'achievement': PreAltar.achievement,
        'north': PreAltar.north,
        'west': PreAltar.west,
        'east': PreAltar.east,
        'south': PreAltar.south,
        'up': PreAltar.up,
        'down': PreAltar.down,
        'status': PreAltar.status,
        'restart': PreAltar.restart,
        'inventory': PreAltar.inventory
        }

        pa = PreAltar()

        while complete == False:
            line = raw_input("> ")
            args = line.split()
            if len(args) == 0:
                  print("What you want to do?\n")

            elif len(args) > 0:
                commandFound = False
                for c in commands.keys():
                    if args[0] == c[:len(args[0])]:
                        commands[c](pa)
                        commandFound = True
                        break

                if args[0] == "take":
                    try:
                        if "item" in itens[currentRoom] and args[1] in itens[currentRoom]["item"]:
                            inventory.append(args[1])
                            moves += 1
                            print(args[1]+":" + " Taken.\n")
                            del itens[currentRoom]["item"]
                        else:
                            print("Can't get this.\n")

                    except:
                        print("Invalid.\n")

                if args[0] == "drop":
                    try:
                        if args[1] in inventory:
                            inventory.remove(args[1])
                            moves += 1
                            print(args[1]+":" + " Dropped.\n")

                        else:
                            print("Can't drop this.\n")

                    except:
                      print("Invalid.\n")

                if args[0] == "eat":
                      try:
                           if args[1] in inventory and args[1] in can_eat:
                                 global health, health_max
                                 if args[1] == can_eat[0]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 5 > health_max:
                                             inventory.remove('bread')
                                             health = 75
                                             print("You eat the bread.\n")
                                       else:
                                             inventory.remove('bread')
                                             health += 5
                                             print("You eat the bread.\n")

                                 elif args[1] == can_eat[1]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 5 > health_max:
                                             inventory.remove('apple')
                                             health = 75
                                             print("You eat the apple.\n")
                                       else:
                                             inventory.remove('apple')
                                             health += 5
                                             print("You eat the apple.\n")

                                 elif args[1] == can_eat[2]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 3 > health_max:
                                             inventory.remove('carrot')
                                             health = 75
                                             print("You eat the carrot.\n")
                                       else:
                                             inventory.remove('carrot')
                                             health += 3
                                             print("You eat the carrot.\n")

                                 elif args[1] == can_eat[3]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 4 > health_max:
                                             inventory.remove('tomato')
                                             health = 75
                                             print("You eat the tomato.\n")
                                       else:
                                             inventory.remove('tomato')
                                             health += 4
                                             print("You eat the tomato.\n")

                                 elif args[1] == can_eat[4]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 4 > health_max:
                                             inventory.remove('potato')
                                             health = 75
                                             print("You eat the potato.\n")
                                       else:
                                             inventory.remove('potato')
                                             health += 4
                                             print("You eat the potato.\n")

                                 elif args[1] == can_eat[5]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 2 > health_max:
                                             inventory.remove('onion')
                                             health = 75
                                             print("You eat the onion.\n")
                                       else:
                                             inventory.remove('onion')
                                             health += 2
                                             print("You eat the onion.\n")

                                 else:
                                     print("You can't eat this.\n")
                           else:
                               print("You don't have this.\n")
                      except:
                            print("Eat what?\n")

                if args[0] == "turn":
                    try:
                        if args[1] == 'lantern':
                            global lantern_on
                            if 'lantern' in inventory:
                                if args[2] == 'on':
                                    lantern_on = True
                                    moves += 1
                                    print("The lantern is now on.\n")

                                elif args[2] == 'off':
                                    lantern_on = False
                                    moves += 1
                                    print("The lantern is now off.\n")
                            else:
                                print("You don't have a lantern.\n")
                    except:
                        print("Invalid.\n")

                if args[0] == "say":
                    try:
                        if args[1] != None:
                            moves += 1
                            print("You say:" + " " + args[1])
                            print("")
                        else:
                            pass
                    except:
                        print("Say what?\n")

                if args[0] == 'read':
                    try:
                        if args[1] == 'paper':
                            if 'paper' in inventory:
                                global paper
                                moves += 1
                                print(paper)
                            else:
                                pass

                        elif args[1] == 'note':
                            if 'note' in inventory:
                                global note
                                moves += 1
                                print(note)
                            else:
                                pass

                        elif args[1] == 'post-it':
                            if 'post-it' in inventory:
                                global post
                                moves += 1
                                print(post)
                            else:
                                pass

                        elif args[1] == 'poster':
                            if 'poster' in inventory:
                                global poster
                                moves += 1
                                print(poster)
                            else:
                                pass

                        else:
                            pass

                    except:
                        print("Read what?\n")

                if args[0] == 'look':
                    global key_desc
                    global sword_desc
                    global knife_desc
                    global ruby_desc
                    global amulet_desc
                    try:
                        if args[1] == 'at':
                            try:
                                if args[2] in inventory:
                                    if args[2] == 'key':
                                        print(key_desc)

                                    elif args[2] == 'sword':
                                        print(sword_desc)

                                    elif args[2] == 'knife':
                                        print(knife_desc)

                                    elif args[2] == 'ruby':
                                        print(ruby_desc)

                                    elif args[2] == 'amulet':
                                        print(amulet_desc)

                                    else:
                                        print("I see nothing special about this.\n")

                                else:
                                    print("You don't have this item.\n")

                            except:
                                print("Look at what?\n")

                    except:
                        print("Look at what?\n")

    def up(self):
        global moves
        moves += 1
        print("You can't go that way.\n")

    def down(self):
        global moves
        moves += 1
        print("You can't go that way.\n")

    def north(self):
        global moves
        moves += 1
        a = Altar()
        a.inicio()

    def east(self):
        global moves
        moves += 1
        print("Nothing here.\n")

    def south(self):
        global moves
        moves += 1
        c3 = Cave3()
        c3.inicio()

    def west(self):
        global moves
        moves += 1
        print("Nothing here.\n")

class Cave3:
    def __init__(self):
        self.state = 'cave3'

    def quit(self):
        c = character()
        c.quit()

    def ajuda(self):
        c = character()
        c.ajuda()

    def status(self):
        c = character()
        c.status()

    def restart(self):
        c = character()
        c.restart()

    def score(self):
        c = character()
        c.score()

    def save(self):
        save()

    def achievement(self):
        c = character()
        c.achievement()

    def inventory(self):
        if len(inventory) > 0:
            print("You have:")
            print inventory
            print("")
        else:
            print("Your inventory is empty.\n")

    def inicio(self):
        complete = False
        global moves, local
        global lantern_on
        local = 'Cave3'
        print("Cave")
        if 'torch' in inventory:
            print("The only thing lighting the place it's your torch.")
            print("There is a sword on the ground.\n")
            itens = {
            1 : {"item": 'sword'}
            }
            currentRoom = 1

        elif 'lantern' in inventory and lantern_on == True:
            print("Your lantern is on, but it's still too dark to see.\n")
            itens = {
            1 : {}
            }

            currentRoom = 1

        elif 'torch' not in inventory:
            print("It's too dark to see. You need a torch.\n")
            itens = {
            1 : {}
            }

            currentRoom = 1

        commands = {
        'help': Cave3.ajuda,
        'quit': Cave3.quit,
        'save': Cave3.save,
        'score': Cave3.score,
        'save': Cave3.save,
        'achievement': Cave3.achievement,
        'north': Cave3.north,
        'west': Cave3.west,
        'east': Cave3.east,
        'south': Cave3.south,
        'up': Cave3.up,
        'down': Cave3.down,
        'status': Cave3.status,
        'restart': Cave3.restart,
        'inventory': Cave3.inventory
        }

        c3 = Cave3()

        while complete == False:
            line = raw_input("> ")
            args = line.split()
            if len(args) == 0:
                  print("What you want to do?\n")

            elif len(args) > 0:
                commandFound = False
                for c in commands.keys():
                    if args[0] == c[:len(args[0])]:
                        commands[c](c3)
                        commandFound = True
                        break

                if args[0] == "take":
                    try:
                        if "item" in itens[currentRoom] and args[1] in itens[currentRoom]["item"]:
                            inventory.append(args[1])
                            moves += 1
                            print(args[1]+":" + " A legendary blade.\n")
                            del itens[currentRoom]["item"]
                        else:
                            print("Can't get this.\n")

                    except:
                        print("Invalid.\n")

                if args[0] == "drop":
                    try:
                        if args[1] in inventory:
                            inventory.remove(args[1])
                            moves += 1
                            print(args[1]+":" + " Dropped.\n")

                        else:
                            print("Can't drop this.\n")

                    except:
                      print("Invalid.\n")

                if args[0] == "eat":
                      try:
                           if args[1] in inventory and args[1] in can_eat:
                                 global health, health_max
                                 if args[1] == can_eat[0]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 5 > health_max:
                                             inventory.remove('bread')
                                             health = 75
                                             print("You eat the bread.\n")
                                       else:
                                             inventory.remove('bread')
                                             health += 5
                                             print("You eat the bread.\n")

                                 elif args[1] == can_eat[1]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 5 > health_max:
                                             inventory.remove('apple')
                                             health = 75
                                             print("You eat the apple.\n")
                                       else:
                                             inventory.remove('apple')
                                             health += 5
                                             print("You eat the apple.\n")

                                 elif args[1] == can_eat[2]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 3 > health_max:
                                             inventory.remove('carrot')
                                             health = 75
                                             print("You eat the carrot.\n")
                                       else:
                                             inventory.remove('carrot')
                                             health += 3
                                             print("You eat the carrot.\n")

                                 elif args[1] == can_eat[3]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 4 > health_max:
                                             inventory.remove('tomato')
                                             health = 75
                                             print("You eat the tomato.\n")
                                       else:
                                             inventory.remove('tomato')
                                             health += 4
                                             print("You eat the tomato.\n")

                                 elif args[1] == can_eat[4]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 4 > health_max:
                                             inventory.remove('potato')
                                             health = 75
                                             print("You eat the potato.\n")
                                       else:
                                             inventory.remove('potato')
                                             health += 4
                                             print("You eat the potato.\n")

                                 elif args[1] == can_eat[5]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 2 > health_max:
                                             inventory.remove('onion')
                                             health = 75
                                             print("You eat the onion.\n")
                                       else:
                                             inventory.remove('onion')
                                             health += 2
                                             print("You eat the onion.\n")

                                 else:
                                     print("You can't eat this.\n")
                           else:
                               print("You don't have this.\n")
                      except:
                            print("Eat what?\n")

                if args[0] == "turn":
                    try:
                        if args[1] == 'lantern':
                            if 'lantern' in inventory:
                                if args[2] == 'on':
                                    lantern_on = True
                                    moves += 1
                                    print("The lantern is now on.\n")

                                elif args[2] == 'off':
                                    lantern_on = False
                                    moves += 1
                                    print("The lantern is now off.\n")
                            else:
                                print("You don't have a lantern.\n")
                    except:
                        print("Invalid.\n")

                if args[0] == "say":
                    try:
                        if args[1] != None:
                            moves += 1
                            print("You say:" + " " + args[1])
                            print("")
                        else:
                            pass
                    except:
                        print("Say what?\n")

                if args[0] == 'read':
                    try:
                        if args[1] == 'paper':
                            if 'paper' in inventory:
                                global paper
                                moves += 1
                                print(paper)
                            else:
                                pass

                        elif args[1] == 'note':
                            if 'note' in inventory:
                                global note
                                moves += 1
                                print(note)
                            else:
                                pass

                        elif args[1] == 'post-it':
                            if 'post-it' in inventory:
                                global post
                                moves += 1
                                print(post)
                            else:
                                pass

                        elif args[1] == 'poster':
                            if 'poster' in inventory:
                                global poster
                                moves += 1
                                print(poster)
                            else:
                                pass

                        else:
                            pass

                    except:
                        print("Read what?\n")

                if args[0] == 'look':
                    global key_desc
                    global sword_desc
                    global knife_desc
                    global ruby_desc
                    global amulet_desc
                    try:
                        if args[1] == 'at':
                            try:
                                if args[2] in inventory:
                                    if args[2] == 'key':
                                        print(key_desc)

                                    elif args[2] == 'sword':
                                        print(sword_desc)

                                    elif args[2] == 'knife':
                                        print(knife_desc)

                                    elif args[2] == 'ruby':
                                        print(ruby_desc)

                                    elif args[2] == 'amulet':
                                        print(amulet_desc)

                                    else:
                                        print("I see nothing special about this.\n")

                                else:
                                    print("You don't have this item.\n")

                            except:
                                print("Look at what?\n")

                    except:
                        print("Look at what?\n")

    def up(self):
        global moves
        moves += 1
        complete = True
        c2 = Cave2()
        c2.inicio()

    def down(self):
        global moves
        moves += 1
        print("You can't go that way.\n")

    def north(self):
        global moves
        moves += 1
        if 'torch' in inventory:
            complete = True
            pa = PreAltar()
            pa.inicio()

        elif 'lantern' in inventory and lantern_on == True:
            complete = True
            pa = PreAltar()
            pa.inicio()

        else:
            print("It's too dark to see.\n")

    def east(self):
        if 'torch' in inventory:
            print("")
        else:
            print("It's too dark to see.\n")

    def south(self):
        if 'torch' in inventory:
            print("There is stairs here, you can go up.\n")
        else:
            print("It's too dark to see.\n")

    def west(self):
        if 'torch' in inventory:
            print("")
        else:
            print("It's too dark to see.\n")

class House3:
    def __init__(self):
        self.state = 'house3'

    def quit(self):
        c = character()
        c.quit()

    def ajuda(self):
        c = character()
        c.ajuda()

    def status(self):
        c = character()
        c.status()

    def restart(self):
        c = character()
        c.restart()

    def score(self):
        c = character()
        c.score()

    def save(self):
        save()

    def achievement(self):
        c = character()
        c.achievement()

    def inventory(self):
        if len(inventory) > 0:
            print("You have:")
            print inventory
            print("")
        else:
            print("Your inventory is empty.\n")

    def inicio(self):
        complete = False
        global moves, local
        local = 'House3'
        print("House")
        print("You are in the house. There is a man here, he sells emeralds.")
        print("Emerald [10 Coins]\n")

        itens = {
        1: {"item": 'emerald'}
        }

        currentRoom = 1

        commands = {
        'help': House3.ajuda,
        'quit': House3.quit,
        'save': House3.save,
        'score': House3.score,
        'achievement': House3.achievement,
        'north': House3.north,
        'west': House3.west,
        'east': House3.east,
        'south': House3.south,
        'up': House3.up,
        'down': House3.down,
        'status': House3.status,
        'restart': House3.restart,
        'inventory': House3.inventory
        }

        h3 = House3()

        while complete == False:
            line = raw_input("> ")
            args = line.split()
            if len(args) == 0:
                  print("What you want to do?\n")

            elif len(args) > 0:
                commandFound = False
                for c in commands.keys():
                    if args[0] == c[:len(args[0])]:
                        commands[c](h3)
                        commandFound = True
                        break

                if args[0] == "buy":
                    try:
                        moves += 1
                        if "item" in itens[currentRoom] and args[1] in itens[currentRoom]["item"]:
                            global coins
                            if coins >= 10:
                                coins -= 10
                                inventory.append(args[1])
                                print(args[1]+":" + " Taken.")
                                if coins > 0:
                                    print("You say: All this money don't make me sad though.\n")
                                else:
                                    print("")

                            else:
                                print("You don't have enough money.\n")
                        else:
                            print("Can't buy this.\n")

                    except:
                        print("Invalid.\n")

                if args[0] == "take":
                    try:
                        if "item" in itens[currentRoom] and args[1] in itens[currentRoom]["item"]:
                            moves += 1
                            print("Can't get this.\n")

                        else:
                            print("Can't get this.\n")

                    except:
                        print("Invalid.\n")

                if args[0] == "drop":
                    try:
                        if args[1] in inventory:
                            inventory.remove(args[1])
                            moves += 1
                            print(args[1]+":" + " Dropped.\n")

                        else:
                            print("Can't drop this.\n")

                    except:
                      print("Invalid.\n")

                if args[0] == "eat":
                      try:
                           if args[1] in inventory and args[1] in can_eat:
                                 global health, health_max
                                 if args[1] == can_eat[0]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 5 > health_max:
                                             inventory.remove('bread')
                                             health = 75
                                             print("You eat the bread.\n")
                                       else:
                                             inventory.remove('bread')
                                             health += 5
                                             print("You eat the bread.\n")

                                 elif args[1] == can_eat[1]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 5 > health_max:
                                             inventory.remove('apple')
                                             health = 75
                                             print("You eat the apple.\n")
                                       else:
                                             inventory.remove('apple')
                                             health += 5
                                             print("You eat the apple.\n")

                                 elif args[1] == can_eat[2]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 3 > health_max:
                                             inventory.remove('carrot')
                                             health = 75
                                             print("You eat the carrot.\n")
                                       else:
                                             inventory.remove('carrot')
                                             health += 3
                                             print("You eat the carrot.\n")

                                 elif args[1] == can_eat[3]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 4 > health_max:
                                             inventory.remove('tomato')
                                             health = 75
                                             print("You eat the tomato.\n")
                                       else:
                                             inventory.remove('tomato')
                                             health += 4
                                             print("You eat the tomato.\n")

                                 elif args[1] == can_eat[4]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 4 > health_max:
                                             inventory.remove('potato')
                                             health = 75
                                             print("You eat the potato.\n")
                                       else:
                                             inventory.remove('potato')
                                             health += 4
                                             print("You eat the potato.\n")

                                 elif args[1] == can_eat[5]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 2 > health_max:
                                             inventory.remove('onion')
                                             health = 75
                                             print("You eat the onion.\n")
                                       else:
                                             inventory.remove('onion')
                                             health += 2
                                             print("You eat the onion.\n")

                                 else:
                                     print("You can't eat this.\n")
                           else:
                               print("You don't have this.\n")
                      except:
                            print("Eat what?\n")

                if args[0] == "turn":
                    try:
                        if args[1] == 'lantern':
                            global lantern_on
                            if 'lantern' in inventory:
                                if args[2] == 'on':
                                    lantern_on = True
                                    moves += 1
                                    print("The lantern is now on.\n")

                                elif args[2] == 'off':
                                    lantern_on = False
                                    moves += 1
                                    print("The lantern is now off.\n")
                            else:
                                print("You don't have a lantern.\n")
                    except:
                        print("Invalid.\n")

                if args[0] == "say":
                    try:
                        if args[1] != None:
                            moves += 1
                            print("You say:" + " " + args[1])
                            print("")
                        else:
                            pass
                    except:
                        print("Say what?\n")

                if args[0] == 'read':
                    try:
                        if args[1] == 'paper':
                            if 'paper' in inventory:
                                global paper
                                moves += 1
                                print(paper)
                            else:
                                pass

                        elif args[1] == 'note':
                            if 'note' in inventory:
                                global note
                                moves += 1
                                print(note)
                            else:
                                pass

                        elif args[1] == 'post-it':
                            if 'post-it' in inventory:
                                global post
                                moves += 1
                                print(post)
                            else:
                                pass

                        elif args[1] == 'poster':
                            if 'poster' in inventory:
                                global poster
                                moves += 1
                                print(poster)
                            else:
                                pass

                        else:
                            pass

                    except:
                        print("Read what?\n")

                if args[0] == 'look':
                    global key_desc
                    global sword_desc
                    global knife_desc
                    global ruby_desc
                    global amulet_desc
                    try:
                        if args[1] == 'at':
                            try:
                                if args[2] in inventory:
                                    if args[2] == 'key':
                                        print(key_desc)

                                    elif args[2] == 'sword':
                                        print(sword_desc)

                                    elif args[2] == 'knife':
                                        print(knife_desc)

                                    elif args[2] == 'ruby':
                                        print(ruby_desc)

                                    elif args[2] == 'amulet':
                                        print(amulet_desc)

                                    else:
                                        print("I see nothing special about this.\n")

                                else:
                                    print("You don't have this item.\n")

                            except:
                                print("Look at what?\n")

                    except:
                        print("Look at what?\n")

    def up(self):
        global moves
        moves += 1
        print("You can't go that way.\n")

    def down(self):
        global moves
        moves += 1
        print("You can't go that way.\n")

    def north(self):
        global moves
        moves += 1
        print("Nothing here.\n")

    def east(self):
        global moves
        moves += 1
        print("You can't go that way.\n")

    def south(self):
        global moves
        moves += 1
        p = Plains()
        p.inicio()

    def west(self):
        global moves
        moves += 1
        print("You can't go that way.\n")

class Passage:
    def __init__(self):
        self.state = 'passage'

    def quit(self):
        c = character()
        c.quit()

    def ajuda(self):
        c = character()
        c.ajuda()

    def status(self):
        c = character()
        c.status()

    def restart(self):
        c = character()
        c.restart()

    def score(self):
        c = character()
        c.score()

    def achievement(self):
        c = character()
        c.achievement()

    def inventory(self):
        if len(inventory) > 0:
            print("You have:")
            print inventory
            print("")
        else:
            print("Your inventory is empty.\n")

    def inicio(self):
        complete = False
        global moves
        print("Passage")
        print("This path extends to west.\n")
        itens = {
        1: {}
        }

        currentRoom = 1

        commands = {
        'help': Passage.ajuda,
        'quit': Passage.quit,
        'score': Passage.score,
        'achievement': Passage.achievement,
        'north': Passage.north,
        'west': Passage.west,
        'east': Passage.east,
        'south': Passage.south,
        'up': Passage.up,
        'down': Passage.down,
        'status': Passage.status,
        'restart': Passage.restart,
        'inventory': Passage.inventory
        }

        pe = Passage()

        while complete == False:
            line = raw_input("> ")
            args = line.split()
            if len(args) == 0:
                  print("What you want to do?\n")

            elif len(args) > 0:
                commandFound = False
                for c in commands.keys():
                    if args[0] == c[:len(args[0])]:
                        commands[c](pe)
                        commandFound = True
                        break

                if args[0] == "take":
                    try:
                        if "item" in itens[currentRoom] and args[1] in itens[currentRoom]["item"]:
                            inventory.append(args[1])
                            moves += 1
                            print(args[1]+":" + " Taken.\n")
                            del itens[currentRoom]["item"]
                        else:
                            print("Can't get this.\n")

                    except:
                        print("Invalid.\n")

                if args[0] == "drop":
                    try:
                        if args[1] in inventory:
                            inventory.remove(args[1])
                            moves += 1
                            print(args[1]+":" + " Dropped.\n")

                        else:
                            print("Can't drop this.\n")

                    except:
                      print("Invalid.\n")

                if args[0] == "eat":
                      try:
                           if args[1] in inventory and args[1] in can_eat:
                                 global health, health_max
                                 if args[1] == can_eat[0]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 5 > health_max:
                                             inventory.remove('bread')
                                             health = 75
                                             print("You eat the bread.\n")
                                       else:
                                             inventory.remove('bread')
                                             health += 5
                                             print("You eat the bread.\n")

                                 elif args[1] == can_eat[1]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 5 > health_max:
                                             inventory.remove('apple')
                                             health = 75
                                             print("You eat the apple.\n")
                                       else:
                                             inventory.remove('apple')
                                             health += 5
                                             print("You eat the apple.\n")

                                 elif args[1] == can_eat[2]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 3 > health_max:
                                             inventory.remove('carrot')
                                             health = 75
                                             print("You eat the carrot.\n")
                                       else:
                                             inventory.remove('carrot')
                                             health += 3
                                             print("You eat the carrot.\n")

                                 elif args[1] == can_eat[3]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 4 > health_max:
                                             inventory.remove('tomato')
                                             health = 75
                                             print("You eat the tomato.\n")
                                       else:
                                             inventory.remove('tomato')
                                             health += 4
                                             print("You eat the tomato.\n")

                                 elif args[1] == can_eat[4]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 4 > health_max:
                                             inventory.remove('potato')
                                             health = 75
                                             print("You eat the potato.\n")
                                       else:
                                             inventory.remove('potato')
                                             health += 4
                                             print("You eat the potato.\n")

                                 elif args[1] == can_eat[5]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 2 > health_max:
                                             inventory.remove('onion')
                                             health = 75
                                             print("You eat the onion.\n")
                                       else:
                                             inventory.remove('onion')
                                             health += 2
                                             print("You eat the onion.\n")

                                 else:
                                     print("You can't eat this.\n")
                           else:
                               print("You don't have this.\n")
                      except:
                            print("Eat what?\n")

                if args[0] == "turn":
                    try:
                        if args[1] == 'lantern':
                            global lantern_on
                            if 'lantern' in inventory:
                                if args[2] == 'on':
                                    lantern_on = True
                                    moves += 1
                                    print("The lantern is now on.\n")

                                elif args[2] == 'off':
                                    lantern_on = False
                                    moves += 1
                                    print("The lantern is now off.\n")
                            else:
                                print("You don't have a lantern.\n")
                    except:
                        print("Invalid.\n")

                if args[0] == "say":
                    try:
                        if args[1] != None:
                            moves += 1
                            print("You say:" + " " + args[1])
                            print("")
                        else:
                            pass
                    except:
                        print("Say what?\n")

                if args[0] == 'read':
                    try:
                        if args[1] == 'paper':
                            if 'paper' in inventory:
                                global paper
                                moves += 1
                                print(paper)
                            else:
                                pass

                        elif args[1] == 'note':
                            if 'note' in inventory:
                                global note
                                moves += 1
                                print(note)
                            else:
                                pass

                        elif args[1] == 'post-it':
                            if 'post-it' in inventory:
                                global post
                                moves += 1
                                print(post)
                            else:
                                pass

                        elif args[1] == 'poster':
                            if 'poster' in inventory:
                                global poster
                                moves += 1
                                print(poster)
                            else:
                                pass

                        else:
                            pass

                    except:
                        print("Read what?\n")

                if args[0] == 'look':
                    global key_desc
                    global sword_desc
                    global knife_desc
                    global ruby_desc
                    global amulet_desc
                    try:
                        if args[1] == 'at':
                            try:
                                if args[2] in inventory:
                                    if args[2] == 'key':
                                        print(key_desc)

                                    elif args[2] == 'sword':
                                        print(sword_desc)

                                    elif args[2] == 'knife':
                                        print(knife_desc)

                                    elif args[2] == 'ruby':
                                        print(ruby_desc)

                                    elif args[2] == 'amulet':
                                        print(amulet_desc)

                                    else:
                                        print("I see nothing special about this.\n")

                                else:
                                    print("You don't have this item.\n")

                            except:
                                print("Look at what?\n")

                    except:
                        print("Look at what?\n")

    def up(self):
        global moves
        moves += 1
        print("You can't go that way.\n")

    def down(self):
        global moves
        moves += 1
        print("You can't go that way.\n")

    def north(self):
        global moves
        moves += 1
        print("There is some coal on the ground.\n")

    def east(self):
        global moves
        moves += 1
        complete = True
        c2 = Cave2()
        c2.inicio()

    def south(self):
        global moves
        moves += 1
        print("Nothing here.\n")

    def west(self):
        global moves
        moves += 1
        me = MineEntrance()
        me.inicio()

class Cave2:
    def __init__(self):
        self.state = 'cave2'

    def quit(self):
        c = character()
        c.quit()

    def ajuda(self):
        c = character()
        c.ajuda()

    def status(self):
        c = character()
        c.status()

    def restart(self):
        c = character()
        c.restart()

    def score(self):
        c = character()
        c.score()

    def save(self):
        save()

    def achievement(self):
        c = character()
        c.achievement()

    def inventory(self):
        if len(inventory) > 0:
            print("You have:")
            print inventory
            print("")
        else:
            print("Your inventory is empty.\n")

    def inicio(self):
        complete = False
        global moves, local
        local = 'Cave2'
        print("Cave")
        print("There is some lactites on top of the cave.")
        print("Has torches illuminating the cave and has stairs here.\n")
        #https://www.youtube.com/watch?v=iX1a3JngmpI

        itens = {
        1: {"item": 'torch'}
        }
        currentRoom = 1

        commands = {
        'help': Cave2.ajuda,
        'quit': Cave2.quit,
        'save': Cave2.save,
        'score': Cave2.score,
        'achievement': Cave2.achievement,
        'north': Cave2.north,
        'west': Cave2.west,
        'east': Cave2.east,
        'south': Cave2.south,
        'up': Cave2.up,
        'down': Cave2.down,
        'status': Cave2.status,
        'restart': Cave2.restart,
        'inventory': Cave2.inventory
        }

        c2 = Cave2()

        while complete == False:
            line = raw_input("> ")
            args = line.split()
            if len(args) == 0:
                  print("What you want to do?\n")

            elif len(args) > 0:
                commandFound = False
                for c in commands.keys():
                    if args[0] == c[:len(args[0])]:
                        commands[c](c2)
                        commandFound = True
                        break

                if args[0] == "take":
                    try:
                        if "item" in itens[currentRoom] and args[1] in itens[currentRoom]["item"]:
                            inventory.append(args[1])
                            moves += 1
                            print(args[1]+":" + " Taken.\n")
                            del itens[currentRoom]["item"]
                        else:
                            print("Can't get this.\n")

                    except:
                        print("Invalid.\n")

                if args[0] == "drop":
                    try:
                        if args[1] in inventory:
                            inventory.remove(args[1])
                            moves += 1
                            print(args[1]+":" + " Dropped.\n")

                        else:
                            print("Can't drop this.\n")

                    except:
                      print("Invalid.\n")

                if args[0] == "eat":
                      try:
                           if args[1] in inventory and args[1] in can_eat:
                                 global health, health_max
                                 if args[1] == can_eat[0]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 5 > health_max:
                                             inventory.remove('bread')
                                             health = 75
                                             print("You eat the bread.\n")
                                       else:
                                             inventory.remove('bread')
                                             health += 5
                                             print("You eat the bread.\n")

                                 elif args[1] == can_eat[1]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 5 > health_max:
                                             inventory.remove('apple')
                                             health = 75
                                             print("You eat the apple.\n")
                                       else:
                                             inventory.remove('apple')
                                             health += 5
                                             print("You eat the apple.\n")

                                 elif args[1] == can_eat[2]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 3 > health_max:
                                             inventory.remove('carrot')
                                             health = 75
                                             print("You eat the carrot.\n")
                                       else:
                                             inventory.remove('carrot')
                                             health += 3
                                             print("You eat the carrot.\n")

                                 elif args[1] == can_eat[3]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 4 > health_max:
                                             inventory.remove('tomato')
                                             health = 75
                                             print("You eat the tomato.\n")
                                       else:
                                             inventory.remove('tomato')
                                             health += 4
                                             print("You eat the tomato.\n")

                                 elif args[1] == can_eat[4]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 4 > health_max:
                                             inventory.remove('potato')
                                             health = 75
                                             print("You eat the potato.\n")
                                       else:
                                             inventory.remove('potato')
                                             health += 4
                                             print("You eat the potato.\n")

                                 elif args[1] == can_eat[5]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 2 > health_max:
                                             inventory.remove('onion')
                                             health = 75
                                             print("You eat the onion.\n")
                                       else:
                                             inventory.remove('onion')
                                             health += 2
                                             print("You eat the onion.\n")

                                 else:
                                     print("You can't eat this.\n")
                           else:
                               print("You don't have this.\n")
                      except:
                            print("Eat what?\n")

                if args[0] == "turn":
                    try:
                        if args[1] == 'lantern':
                            global lantern_on
                            if 'lantern' in inventory:
                                if args[2] == 'on':
                                    lantern_on = True
                                    moves += 1
                                    print("The lantern is now on.\n")

                                elif args[2] == 'off':
                                    lantern_on = False
                                    moves += 1
                                    print("The lantern is now off.\n")
                            else:
                                print("You don't have a lantern.\n")
                    except:
                        print("Invalid.\n")

                if args[0] == "say":
                    try:
                        if args[1] != None:
                            moves += 1
                            print("You say:" + " " + args[1])
                            print("")
                        else:
                            pass
                    except:
                        print("Say what?\n")

                if args[0] == 'read':
                    try:
                        if args[1] == 'paper':
                            if 'paper' in inventory:
                                global paper
                                moves += 1
                                print(paper)
                            else:
                                pass

                        elif args[1] == 'note':
                            if 'note' in inventory:
                                global note
                                moves += 1
                                print(note)
                            else:
                                pass

                        elif args[1] == 'post-it':
                            if 'post-it' in inventory:
                                global post
                                moves += 1
                                print(post)
                            else:
                                pass

                        elif args[1] == 'poster':
                            if 'poster' in inventory:
                                global poster
                                moves += 1
                                print(poster)
                            else:
                                pass

                        else:
                            pass

                    except:
                        print("Read what?\n")

                if args[0] == 'look':
                    global key_desc
                    global sword_desc
                    global knife_desc
                    global ruby_desc
                    global amulet_desc
                    try:
                        if args[1] == 'at':
                            try:
                                if args[2] in inventory:
                                    if args[2] == 'key':
                                        print(key_desc)

                                    elif args[2] == 'sword':
                                        print(sword_desc)

                                    elif args[2] == 'knife':
                                        print(knife_desc)

                                    elif args[2] == 'ruby':
                                        print(ruby_desc)

                                    elif args[2] == 'amulet':
                                        print(amulet_desc)

                                    else:
                                        print("I see nothing special about this.\n")

                                else:
                                    print("You don't have this item.\n")

                            except:
                                print("Look at what?\n")

                    except:
                        print("Look at what?\n")

    def up(self):
        global moves
        moves += 1
        print("You can't go that way.\n")

    def down(self):
        global moves
        moves += 1
        complete = True
        c3 = Cave3()
        c3.inicio()

    def north(self):
        global moves
        moves += 1
        print("Nothing here.\n")

    def east(self):
        global moves
        moves += 1
        global coins
        if coins == 5 or coins > 0:
            print("Nothing here.\n")
        else:
            print("You found 10 coins.\n")
            coins += 10

    def south(self):
        global moves
        moves += 1
        complete = True
        cv = Cave()
        cv.inicio()

    def west(self):
        global moves
        moves += 1
        complete = True
        pe = Passage()
        pe.inicio()

class Cave:
    def __init__(self):
        self.state = 'cave'

    def quit(self):
        c = character()
        c.quit()

    def ajuda(self):
        c = character()
        c.ajuda()

    def status(self):
        c = character()
        c.status()

    def restart(self):
        c = character()
        c.restart()

    def score(self):
        c = character()
        c.score()

    def save(self):
        save()

    def achievement(self):
        c = character()
        c.achievement()

    def inventory(self):
        if len(inventory) > 0:
            print("You have:")
            print inventory
            print("")
        else:
            print("Your inventory is empty.\n")

    def inicio(self):
        complete = False
        print("Cave")
        global moves, local
        global lantern_on
        local = 'Cave'
        if 'torch' in inventory:
            print("")

        elif lantern_on == True:
            print("")

        else:
            print("You have moved into a dark place.\n")

        itens = {
        1: {}
        }

        currentRoom = 1

        commands = {
        'help': Cave.ajuda,
        'quit': Cave.quit,
        'save': Cave.save,
        'score': Cave.score,
        'achievement': Cave.achievement,
        'north': Cave.north,
        'west': Cave.west,
        'east': Cave.east,
        'south': Cave.south,
        'up': Cave.up,
        'down': Cave.down,
        'status': Cave.status,
        'restart': Cave.restart,
        'inventory': Cave.inventory
        }

        cv = Cave()

        while complete == False:
            line = raw_input("> ")
            args = line.split()
            if len(args) == 0:
                  print("What you want to do?\n")

            elif len(args) > 0:
                commandFound = False
                for c in commands.keys():
                    if args[0] == c[:len(args[0])]:
                        commands[c](cv)
                        commandFound = True
                        break

                if args[0] == "take":
                    try:
                        if "item" in itens[currentRoom] and args[1] in itens[currentRoom]["item"]:
                            inventory.append(args[1])
                            moves += 1
                            print(args[1]+":" + " Taken.\n")
                            del itens[currentRoom]["item"]
                        else:
                            print("Can't get this.\n")

                    except:
                        print("Invalid.\n")

                if args[0] == "drop":
                    try:
                        if args[1] in inventory:
                            inventory.remove(args[1])
                            moves += 1
                            print(args[1]+":" + " Dropped.\n")

                        else:
                            print("Can't drop this.\n")

                    except:
                      print("Invalid.\n")

                if args[0] == "eat":
                      try:
                           if args[1] in inventory and args[1] in can_eat:
                                 global health, health_max
                                 if args[1] == can_eat[0]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 5 > health_max:
                                             inventory.remove('bread')
                                             health = 75
                                             print("You eat the bread.\n")
                                       else:
                                             inventory.remove('bread')
                                             health += 5
                                             print("You eat the bread.\n")

                                 elif args[1] == can_eat[1]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 5 > health_max:
                                             inventory.remove('apple')
                                             health = 75
                                             print("You eat the apple.\n")
                                       else:
                                             inventory.remove('apple')
                                             health += 5
                                             print("You eat the apple.\n")

                                 elif args[1] == can_eat[2]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 3 > health_max:
                                             inventory.remove('carrot')
                                             health = 75
                                             print("You eat the carrot.\n")
                                       else:
                                             inventory.remove('carrot')
                                             health += 3
                                             print("You eat the carrot.\n")

                                 elif args[1] == can_eat[3]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 4 > health_max:
                                             inventory.remove('tomato')
                                             health = 75
                                             print("You eat the tomato.\n")
                                       else:
                                             inventory.remove('tomato')
                                             health += 4
                                             print("You eat the tomato.\n")

                                 elif args[1] == can_eat[4]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 4 > health_max:
                                             inventory.remove('potato')
                                             health = 75
                                             print("You eat the potato.\n")
                                       else:
                                             inventory.remove('potato')
                                             health += 4
                                             print("You eat the potato.\n")

                                 elif args[1] == can_eat[5]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 2 > health_max:
                                             inventory.remove('onion')
                                             health = 75
                                             print("You eat the onion.\n")
                                       else:
                                             inventory.remove('onion')
                                             health += 2
                                             print("You eat the onion.\n")

                                 else:
                                     print("You can't eat this.\n")
                           else:
                               print("You don't have this.\n")
                      except:
                            print("Eat what?\n")

                if args[0] == "turn":
                    try:
                        if args[1] == 'lantern':
                            if 'lantern' in inventory:
                                if args[2] == 'on':
                                    lantern_on = True
                                    moves += 1
                                    print("The lantern is now on.\n")

                                elif args[2] == 'off':
                                    lantern_on = False
                                    moves += 1
                                    print("The lantern is now off.\n")
                            else:
                                print("You don't have a lantern.\n")
                    except:
                        print("Invalid.\n")

                if args[0] == "say":
                    try:
                        if args[1] != None:
                            moves += 1
                            print("You say:" + " " + args[1])
                            print("")
                        else:
                            pass
                    except:
                        print("Say what?\n")

                if args[0] == 'read':
                    try:
                        if args[1] == 'paper':
                            if 'paper' in inventory:
                                global paper
                                moves += 1
                                print(paper)
                            else:
                                pass

                        elif args[1] == 'note':
                            if 'note' in inventory:
                                global note
                                moves += 1
                                print(note)
                            else:
                                pass

                        elif args[1] == 'post-it':
                            if 'post-it' in inventory:
                                global post
                                moves += 1
                                print(post)
                            else:
                                pass

                        elif args[1] == 'poster':
                            if 'poster' in inventory:
                                global poster
                                moves += 1
                                print(poster)
                            else:
                                pass

                        else:
                            pass

                    except:
                        print("Read what?\n")

                if args[0] == 'look':
                    global key_desc
                    global sword_desc
                    global knife_desc
                    global ruby_desc
                    global amulet_desc
                    try:
                        if args[1] == 'at':
                            try:
                                if args[2] in inventory:
                                    if args[2] == 'key':
                                        print(key_desc)

                                    elif args[2] == 'sword':
                                        print(sword_desc)

                                    elif args[2] == 'knife':
                                        print(knife_desc)

                                    elif args[2] == 'ruby':
                                        print(ruby_desc)

                                    elif args[2] == 'amulet':
                                        print(amulet_desc)

                                    else:
                                        print("I see nothing special about this.\n")

                                else:
                                    print("You don't have this item.\n")

                            except:
                                print("Look at what?\n")

                    except:
                        print("Look at what?\n")

    def up(self):
        global moves
        moves += 1
        print("You can't go that way.\n")

    def down(self):
        global moves
        moves += 1
        print("You can't go that way.\n")

    def north(self):
        global moves
        moves += 1
        complete = True
        c2 = Cave2()
        c2.inicio()

    def east(self):
        global moves
        moves += 1
        print("Darkness.\n")

    def south(self):
        global moves
        moves += 1
        complete = True
        m = Mountain()
        m.inicio()

    def west(self):
        global moves
        moves += 1
        print("Darkness.\n")

class Plains:
    def __init__(self):
        self.state = 'plains'

    def quit(self):
        c = character()
        c.quit()

    def ajuda(self):
        c = character()
        c.ajuda()

    def status(self):
        c = character()
        c.status()

    def restart(self):
        c = character()
        c.restart()

    def score(self):
        c = character()
        c.score()

    def achievement(self):
        c = character()
        c.achievement()

    def inventory(self):
        if len(inventory) > 0:
            print("You have:")
            print inventory
            print("")
        else:
            print("Your inventory is empty.\n")

    def inicio(self):
        complete = False
        global moves
        print("Plains")
        if 'amulet' in inventory:
            print("You are in the plains. It's windy here.")
            print("Has a market to north.\n")
        else:
            print("This place is too scary. It's windy here.\n")

        itens = {
        1: {}
        }

        currentRoom = 1

        commands = {
        'help': Plains.ajuda,
        'quit': Plains.quit,
        'score': Plains.score,
        'achievement': Plains.achievement,
        'north': Plains.north,
        'west': Plains.west,
        'east': Plains.east,
        'south': Plains.south,
        'up': Plains.up,
        'down': Plains.down,
        'status': Plains.status,
        'restart': Plains.restart,
        'inventory': Plains.inventory
        }

        p = Plains()

        while complete == False:
            line = raw_input("> ")
            args = line.split()
            if len(args) == 0:
                  print("What you want to do?\n")

            elif len(args) == 0:
                print("What you want to do?\n")

            elif len(args) > 0:
                commandFound = False
                for c in commands.keys():
                    if args[0] == c[:len(args[0])]:
                        commands[c](p)
                        commandFound = True
                        break

                if args[0] == "take":
                    try:
                        if "item" in itens[currentRoom] and args[1] in itens[currentRoom]["item"]:
                            inventory.append(args[1])
                            moves += 1
                            print(args[1]+":" + " Taken.\n")
                            del itens[currentRoom]["item"]
                        else:
                            print("Can't get this.\n")

                    except:
                        print("Invalid.\n")

                if args[0] == "drop":
                    try:
                        if args[1] in inventory:
                            inventory.remove(args[1])
                            moves += 1
                            print(args[1]+":" + " Dropped.\n")

                        else:
                            print("Can't drop this.\n")

                    except:
                      print("Invalid.\n")

                if args[0] == "eat":
                      try:
                           if args[1] in inventory and args[1] in can_eat:
                                 global health, health_max
                                 if args[1] == can_eat[0]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 5 > health_max:
                                             inventory.remove('bread')
                                             health = 75
                                             print("You eat the bread.\n")
                                       else:
                                             inventory.remove('bread')
                                             health += 5
                                             print("You eat the bread.\n")

                                 elif args[1] == can_eat[1]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 5 > health_max:
                                             inventory.remove('apple')
                                             health = 75
                                             print("You eat the apple.\n")
                                       else:
                                             inventory.remove('apple')
                                             health += 5
                                             print("You eat the apple.\n")

                                 elif args[1] == can_eat[2]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 3 > health_max:
                                             inventory.remove('carrot')
                                             health = 75
                                             print("You eat the carrot.\n")
                                       else:
                                             inventory.remove('carrot')
                                             health += 3
                                             print("You eat the carrot.\n")

                                 elif args[1] == can_eat[3]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 4 > health_max:
                                             inventory.remove('tomato')
                                             health = 75
                                             print("You eat the tomato.\n")
                                       else:
                                             inventory.remove('tomato')
                                             health += 4
                                             print("You eat the tomato.\n")

                                 elif args[1] == can_eat[4]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 4 > health_max:
                                             inventory.remove('potato')
                                             health = 75
                                             print("You eat the potato.\n")
                                       else:
                                             inventory.remove('potato')
                                             health += 4
                                             print("You eat the potato.\n")

                                 elif args[1] == can_eat[5]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 2 > health_max:
                                             inventory.remove('onion')
                                             health = 75
                                             print("You eat the onion.\n")
                                       else:
                                             inventory.remove('onion')
                                             health += 2
                                             print("You eat the onion.\n")

                                 else:
                                     print("You can't eat this.\n")
                           else:
                               print("You don't have this.\n")
                      except:
                            print("Eat what?\n")

                if args[0] == "turn":
                    try:
                        if args[1] == 'lantern':
                            if 'lantern' in inventory:
                                global lantern_on
                                if args[2] == 'on':
                                    lantern_on = True
                                    moves += 1
                                    print("The lantern is now on.\n")

                                elif args[2] == 'off':
                                    lantern_on = False
                                    moves += 1
                                    print("The lantern is now off.\n")
                            else:
                                print("You don't have a lantern.\n")
                    except:
                        print("Invalid.\n")

                if args[0] == "say":
                    try:
                        if args[1] != None:
                            moves += 1
                            print("You say:" + " " + args[1])
                            print("")
                        else:
                            pass
                    except:
                        print("Say what?\n")

                if args[0] == 'read':
                    try:
                        if args[1] == 'paper':
                            if 'paper' in inventory:
                                global paper
                                moves += 1
                                print(paper)
                            else:
                                pass

                        elif args[1] == 'note':
                            if 'note' in inventory:
                                global note
                                moves += 1
                                print(note)
                            else:
                                pass

                        elif args[1] == 'post-it':
                            if 'post-it' in inventory:
                                global post
                                moves += 1
                                print(post)
                            else:
                                pass

                        elif args[1] == 'poster':
                            if 'poster' in inventory:
                                global poster
                                moves += 1
                                print(poster)
                            else:
                                pass

                        else:
                            pass

                    except:
                        print("Read what?\n")

                if args[0] == 'look':
                    global key_desc
                    global sword_desc
                    global knife_desc
                    global ruby_desc
                    global amulet_desc
                    try:
                        if args[1] == 'at':
                            try:
                                if args[2] in inventory:
                                    if args[2] == 'key':
                                        print(key_desc)

                                    elif args[2] == 'sword':
                                        print(sword_desc)

                                    elif args[2] == 'knife':
                                        print(knife_desc)

                                    elif args[2] == 'ruby':
                                        print(ruby_desc)

                                    elif args[2] == 'amulet':
                                        print(amulet_desc)

                                    else:
                                        print("I see nothing special about this.\n")

                                else:
                                    print("You don't have this item.\n")

                            except:
                                print("Look at what?\n")

                    except:
                        print("Look at what?\n")

    def up(self):
        global moves
        moves += 1
        if 'amulet' in inventory:
            print("You can't go that way.\n")

        else:
            print("Sadboy is too scared to move.\n")

    def down(self):
        global moves
        moves += 1
        if 'amulet' in inventory:
            print("You can't go that way.\n")

        else:
            print("Sadboy is too scared to move.\n")

    def north(self):
        global moves
        moves += 1
        if 'amulet' in inventory:
            complete = True
            h3 = House3()
            h3.inicio()

        else:
            print("Sadboy is too scared to move.\n")

    def east(self):
        global moves
        moves += 1
        if 'amulet' in inventory:
            complete = True
            be = Bridge()
            be.inicio()

        else:
            print("Sadboy is too scared to move.\n")

    def south(self):
        global moves
        moves += 1
        if 'amulet' in inventory:
            pass

        else:
            print("Sadboy is too scared to move.\n")

    def west(self):
        global moves
        moves += 1
        if 'amulet' in inventory:
            pass

        else:
            print("Sadboy is too scared to move.\n")

class Bridge:
    def __init__(self):
        self.state = 'brigde'

    def quit(self):
        c = character()
        c.quit()

    def ajuda(self):
        c = character()
        c.ajuda()

    def status(self):
        c = character()
        c.status()

    def restart(self):
        c = character()
        c.restart()

    def score(self):
        c = character()
        c.score()

    def save(self):
        save()

    def achievement(self):
        c = character()
        c.achievement()

    def inventory(self):
        if len(inventory) > 0:
            print("You have:")
            print inventory
            print("")
        else:
            print("Your inventory is empty.\n")

    def inicio(self):
        complete = False
        global moves, local
        local = 'Bridge'
        print("Bridge")
        print("There is a small stream below the bridge.")
        print("You can go to west and east.\n")

        itens = {
        1: {}
        }

        currentRoom = 1

        commands = {
        'help': Bridge.ajuda,
        'quit': Bridge.quit,
        'save': Bridge.save,
        'score': Bridge.score,
        'achievement': Bridge.achievement,
        'north': Bridge.north,
        'west': Bridge.west,
        'east': Bridge.east,
        'south': Bridge.south,
        'up': Bridge.up,
        'down': Bridge.down,
        'status': Bridge.status,
        'restart': Bridge.restart,
        'inventory': Bridge.inventory
        }

        b = Bridge()

        while complete == False:
            line = raw_input("> ")
            args = line.split()
            if len(args) == 0:
                print("What you want to do?\n")

            elif len(args) > 0:
                commandFound = False
                for c in commands.keys():
                    if args[0] == c[:len(args[0])]:
                        commands[c](b)
                        commandFound = True
                        break

                if args[0] == "take":
                    try:
                        if "item" in itens[currentRoom] and args[1] in itens[currentRoom]["item"]:
                            inventory.append(args[1])
                            moves += 1
                            print(args[1]+":" + " Taken.\n")
                            del itens[currentRoom]["item"]
                        else:
                            print("Can't get this.\n")

                    except:
                        print("Invalid.\n")

                if args[0] == "drop":
                    try:
                        if args[1] in inventory:
                            inventory.remove(args[1])
                            moves += 1
                            print(args[1]+":" + " Dropped.\n")

                        else:
                            print("Can't drop this.\n")

                    except:
                      print("Invalid.\n")

                if args[0] == "eat":
                      try:
                           if args[1] in inventory and args[1] in can_eat:
                                 global health, health_max
                                 if args[1] == can_eat[0]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 5 > health_max:
                                             inventory.remove('bread')
                                             health = 75
                                             print("You eat the bread.\n")
                                       else:
                                             inventory.remove('bread')
                                             health += 5
                                             print("You eat the bread.\n")

                                 elif args[1] == can_eat[1]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 5 > health_max:
                                             inventory.remove('apple')
                                             health = 75
                                             print("You eat the apple.\n")
                                       else:
                                             inventory.remove('apple')
                                             health += 5
                                             print("You eat the apple.\n")

                                 elif args[1] == can_eat[2]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 3 > health_max:
                                             inventory.remove('carrot')
                                             health = 75
                                             print("You eat the carrot.\n")
                                       else:
                                             inventory.remove('carrot')
                                             health += 3
                                             print("You eat the carrot.\n")

                                 elif args[1] == can_eat[3]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 4 > health_max:
                                             inventory.remove('tomato')
                                             health = 75
                                             print("You eat the tomato.\n")
                                       else:
                                             inventory.remove('tomato')
                                             health += 4
                                             print("You eat the tomato.\n")

                                 elif args[1] == can_eat[4]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 4 > health_max:
                                             inventory.remove('potato')
                                             health = 75
                                             print("You eat the potato.\n")
                                       else:
                                             inventory.remove('potato')
                                             health += 4
                                             print("You eat the potato.\n")

                                 elif args[1] == can_eat[5]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 2 > health_max:
                                             inventory.remove('onion')
                                             health = 75
                                             print("You eat the onion.\n")
                                       else:
                                             inventory.remove('onion')
                                             health += 2
                                             print("You eat the onion.\n")

                                 else:
                                     print("You can't eat this.\n")
                           else:
                               print("You don't have this.\n")
                      except:
                            print("Eat what?\n")

                if args[0] == "turn":
                    try:
                        if args[1] == 'lantern':
                            if 'lantern' in inventory:
                                global lantern_on
                                if args[2] == 'on':
                                    lantern_on = True
                                    moves += 1
                                    print("The lantern is now on.\n")

                                elif args[2] == 'off':
                                    lantern_on = False
                                    moves += 1
                                    print("The lantern is now off.\n")
                            else:
                                print("You don't have a lantern.\n")
                    except:
                        print("Invalid.\n")

                if args[0] == "say":
                    try:
                        if args[1] != None:
                            moves += 1
                            print("You say:" + " " + args[1])
                            print("")
                        else:
                            pass
                    except:
                        print("Say what?\n")

                if args[0] == 'read':
                    try:
                        if args[1] == 'paper':
                            if 'paper' in inventory:
                                global paper
                                moves += 1
                                print(paper)
                            else:
                                pass

                        elif args[1] == 'note':
                            if 'note' in inventory:
                                global note
                                moves += 1
                                print(note)
                            else:
                                pass

                        elif args[1] == 'post-it':
                            if 'post-it' in inventory:
                                global post
                                moves += 1
                                print(post)
                            else:
                                pass

                        elif args[1] == 'poster':
                            if 'poster' in inventory:
                                global poster
                                moves += 1
                                print(poster)
                            else:
                                pass

                        else:
                            pass

                    except:
                        print("Read what?\n")

                if args[0] == 'look':
                    global key_desc
                    global sword_desc
                    global knife_desc
                    global ruby_desc
                    global amulet_desc
                    try:
                        if args[1] == 'at':
                            try:
                                if args[2] in inventory:
                                    if args[2] == 'key':
                                        print(key_desc)

                                    elif args[2] == 'sword':
                                        print(sword_desc)

                                    elif args[2] == 'knife':
                                        print(knife_desc)

                                    elif args[2] == 'ruby':
                                        print(ruby_desc)

                                    elif args[2] == 'amulet':
                                        print(amulet_desc)

                                    else:
                                        print("I see nothing special about this.\n")

                                else:
                                    print("You don't have this item.\n")

                            except:
                                print("Look at what?\n")

                    except:
                        print("Look at what?\n")

    def up(self):
        global moves
        moves += 1
        print("You can't go that way.\n")

    def down(self):
        global moves
        moves += 1
        print("You can't go that way.\n")

    def north(self):
        global moves
        moves += 1
        print("You can't go that way.\n")

    def east(self):
        global moves
        moves += 1
        complete = True
        fp = ForestPath()
        fp.inicio()

    def south(self):
        global moves
        moves += 1
        print("You can't go that way.\n")

    def west(self):
        global moves
        moves += 1
        if 'amulet' in inventory:
            p = Plains()
            p.inicio()

        else:
            print("Are you sure you want to cross the bridge? [y/n]\n")
            check = raw_input("> ")
            if check == 'y':
                complete = True
                p = Plains()
                p.inicio()

            if check == 'n':
                b = Bridge()
                b.inicio()

            elif check != 'y' or 'n':
                check = raw_input("> ")

class Attic2:
    def __init__(self):
        self.state = 'clearing'

    def quit(self):
        c = character()
        c.quit()

    def ajuda(self):
        c = character()
        c.ajuda()

    def status(self):
        c = character()
        c.status()

    def restart(self):
        c = character()
        c.restart()

    def score(self):
        c = character()
        c.score()

    def achievement(self):
        c = character()
        c.achievement()

    def inventory(self):
        if len(inventory) > 0:
            print("You have:")
            print inventory
            print("")
        else:
            print("Your inventory is empty.\n")

    def inicio(self):
        complete = False
        global moves
        print("Attic")

        if 'amulet' in inventory:
            print("")

            itens = {
            1: {}
            }

            currentRoom = 1

        else:
            if 'ruby' in inventory:
                print("There's an old man sitting in an armchair, he asks if you have a ruby.")
                print("And you have a ruby, you give the ruby ​​to him and he gives you an amulet.\n")
                inventory.remove('ruby')
                inventory.append('amulet')

            else:
                print("There's an old man sitting in an armchair, he asks if you have a ruby.")
                print("But you don't have a ruby.\n")


            itens = {
            1: {}
            }

            currentRoom = 1

        commands = {
        'help': Attic2.ajuda,
        'quit': Attic2.quit,
        'score': Attic2.score,
        'achievement': Attic2.achievement,
        'north': Attic2.north,
        'west': Attic2.west,
        'east': Attic2.east,
        'south': Attic2.south,
        'up': Attic2.up,
        'down': Attic2.down,
        'status': Attic2.status,
        'restart': Attic2.restart,
        'inventory': Attic2.inventory
        }

        a2 = Attic2()

        while complete == False:
            line = raw_input("> ")
            args = line.split()
            if len(args) == 0:
                print("What you want to do?\n")

            elif len(args) > 0:
                commandFound = False
                for c in commands.keys():
                    if args[0] == c[:len(args[0])]:
                        commands[c](a2)
                        commandFound = True
                        break

                if args[0] == "take":
                    try:
                        if "item" in itens[currentRoom] and args[1] in itens[currentRoom]["item"]:
                            inventory.append(args[1])
                            moves += 1
                            print(args[1]+":" + " Taken.\n")
                            del itens[currentRoom]["item"]
                        else:
                            print("Can't get this.\n")

                    except:
                        print("Invalid.\n")

                if args[0] == "drop":
                    try:
                        if args[1] in inventory:
                            inventory.remove(args[1])
                            moves += 1
                            print(args[1]+":" + " Dropped.\n")

                        else:
                            print("Can't drop this.\n")

                    except:
                      print("Invalid.\n")

                if args[0] == "eat":
                      try:
                           if args[1] in inventory and args[1] in can_eat:
                                 global health, health_max
                                 if args[1] == can_eat[0]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 5 > health_max:
                                             inventory.remove('bread')
                                             health = 75
                                             print("You eat the bread.\n")
                                       else:
                                             inventory.remove('bread')
                                             health += 5
                                             print("You eat the bread.\n")

                                 elif args[1] == can_eat[1]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 5 > health_max:
                                             inventory.remove('apple')
                                             health = 75
                                             print("You eat the apple.\n")
                                       else:
                                             inventory.remove('apple')
                                             health += 5
                                             print("You eat the apple.\n")

                                 elif args[1] == can_eat[2]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 3 > health_max:
                                             inventory.remove('carrot')
                                             health = 75
                                             print("You eat the carrot.\n")
                                       else:
                                             inventory.remove('carrot')
                                             health += 3
                                             print("You eat the carrot.\n")

                                 elif args[1] == can_eat[3]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 4 > health_max:
                                             inventory.remove('tomato')
                                             health = 75
                                             print("You eat the tomato.\n")
                                       else:
                                             inventory.remove('tomato')
                                             health += 4
                                             print("You eat the tomato.\n")

                                 elif args[1] == can_eat[4]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 4 > health_max:
                                             inventory.remove('potato')
                                             health = 75
                                             print("You eat the potato.\n")
                                       else:
                                             inventory.remove('potato')
                                             health += 4
                                             print("You eat the potato.\n")

                                 elif args[1] == can_eat[5]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 2 > health_max:
                                             inventory.remove('onion')
                                             health = 75
                                             print("You eat the onion.\n")
                                       else:
                                             inventory.remove('onion')
                                             health += 2
                                             print("You eat the onion.\n")

                                 else:
                                     print("You can't eat this.\n")
                           else:
                               print("You don't have this.\n")
                      except:
                            print("Eat what?\n")

                if args[0] == "turn":
                    try:
                        if args[1] == 'lantern':
                            if 'lantern' in inventory:
                                global lantern_on
                                if args[2] == 'on':
                                    lantern_on = True
                                    moves += 1
                                    print("The lantern is now on.\n")

                                elif args[2] == 'off':
                                    lantern_on = False
                                    moves += 1
                                    print("The lantern is now off.\n")
                            else:
                                print("You don't have a lantern.\n")
                    except:
                        print("Invalid.\n")

                if args[0] == "say":
                    try:
                        if args[1] != None:
                            moves += 1
                            print("You say:" + " " + args[1])
                            print("")
                        else:
                            pass
                    except:
                        print("Say what?\n")

                if args[0] == 'read':
                    try:
                        if args[1] == 'paper':
                            if 'paper' in inventory:
                                global paper
                                moves += 1
                                print(paper)
                            else:
                                pass

                        elif args[1] == 'note':
                            if 'note' in inventory:
                                global note
                                moves += 1
                                print(note)
                            else:
                                pass

                        elif args[1] == 'post-it':
                            if 'post-it' in inventory:
                                global post
                                moves += 1
                                print(post)
                            else:
                                pass

                        elif args[1] == 'poster':
                            if 'poster' in inventory:
                                global poster
                                moves += 1
                                print(poster)
                            else:
                                pass

                        else:
                            pass

                    except:
                        print("Read what?\n")

                if args[0] == 'look':
                    global key_desc
                    global sword_desc
                    global knife_desc
                    global ruby_desc
                    global amulet_desc
                    try:
                        if args[1] == 'at':
                            try:
                                if args[2] in inventory:
                                    if args[2] == 'key':
                                        print(key_desc)

                                    elif args[2] == 'sword':
                                        print(sword_desc)

                                    elif args[2] == 'knife':
                                        print(knife_desc)

                                    elif args[2] == 'ruby':
                                        print(ruby_desc)

                                    elif args[2] == 'amulet':
                                        print(amulet_desc)

                                    else:
                                        print("I see nothing special about this.\n")

                                else:
                                    print("You don't have this item.\n")

                            except:
                                print("Look at what?\n")

                    except:
                        print("Look at what?\n")

    def up(self):
        global moves
        moves += 1
        print("You can't go that way.\n")

    def down(self):
        global moves
        moves += 1
        complete = True
        h2 = House2()
        h2.inicio()

    def north(self):
        global moves
        moves += 1
        print("Nothing here.\n")

    def east(self):
        global moves
        moves += 1
        print("Nothing here.\n")

    def south(self):
        global moves
        moves += 1
        print("Nothing here.\n")

    def west(self):
        global moves
        moves += 1
        print("Nothing here.\n")

class Clearing:
    def __init__(self):
        self.state = 'clearing'

    def quit(self):
        c = character()
        c.quit()

    def ajuda(self):
        c = character()
        c.ajuda()

    def status(self):
        c = character()
        c.status()

    def restart(self):
        c = character()
        c.restart()

    def score(self):
        c = character()
        c.score()

    def save(self):
        save()

    def achievement(self):
        c = character()
        c.achievement()

    def inventory(self):
        if len(inventory) > 0:
            print("You have:")
            print inventory
            print("")
        else:
            print("Your inventory is empty.\n")

    def inicio(self):
        complete = False
        global moves, local
        local = 'Clearing'
        print("Clearing")
        print("You are in a clearing, with a forest surrounding you.\n")

        itens = {
        1: {}
        }

        currentRoom = 1

        commands = {
        'help': Clearing.ajuda,
        'quit': Clearing.quit,
        'save': Clearing.save,
        'score': Clearing.score,
        'achievement': Clearing.achievement,
        'north': Clearing.north,
        'west': Clearing.west,
        'east': Clearing.east,
        'south': Clearing.south,
        'up': Clearing.up,
        'down': Clearing.down,
        'status': Clearing.status,
        'restart': Clearing.restart,
        'inventory': Clearing.inventory
        }

        cr = Clearing()

        while complete == False:
            line = raw_input("> ")
            args = line.split()
            if len(args) == 0:
                print("What you want to do?\n")

            elif len(args) > 0:
                commandFound = False
                for c in commands.keys():
                    if args[0] == c[:len(args[0])]:
                        commands[c](cr)
                        commandFound = True
                        break

                if args[0] == "take":
                    try:
                        if "item" in itens[currentRoom] and args[1] in itens[currentRoom]["item"]:
                            inventory.append(args[1])
                            moves += 1
                            print(args[1]+":" + " Taken.\n")
                            del itens[currentRoom]["item"]
                        else:
                            print("Can't get this.\n")

                    except:
                        print("Invalid.\n")

                if args[0] == "drop":
                    try:
                        if args[1] in inventory:
                            inventory.remove(args[1])
                            moves += 1
                            print(args[1]+":" + " Dropped.\n")

                        else:
                            print("Can't drop this.\n")

                    except:
                      print("Invalid.\n")

                if args[0] == "eat":
                      try:
                           if args[1] in inventory and args[1] in can_eat:
                                 global health, health_max
                                 if args[1] == can_eat[0]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 5 > health_max:
                                             inventory.remove('bread')
                                             health = 75
                                             print("You eat the bread.\n")
                                       else:
                                             inventory.remove('bread')
                                             health += 5
                                             print("You eat the bread.\n")

                                 elif args[1] == can_eat[1]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 5 > health_max:
                                             inventory.remove('apple')
                                             health = 75
                                             print("You eat the apple.\n")
                                       else:
                                             inventory.remove('apple')
                                             health += 5
                                             print("You eat the apple.\n")

                                 elif args[1] == can_eat[2]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 3 > health_max:
                                             inventory.remove('carrot')
                                             health = 75
                                             print("You eat the carrot.\n")
                                       else:
                                             inventory.remove('carrot')
                                             health += 3
                                             print("You eat the carrot.\n")

                                 elif args[1] == can_eat[3]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 4 > health_max:
                                             inventory.remove('tomato')
                                             health = 75
                                             print("You eat the tomato.\n")
                                       else:
                                             inventory.remove('tomato')
                                             health += 4
                                             print("You eat the tomato.\n")

                                 elif args[1] == can_eat[4]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 4 > health_max:
                                             inventory.remove('potato')
                                             health = 75
                                             print("You eat the potato.\n")
                                       else:
                                             inventory.remove('potato')
                                             health += 4
                                             print("You eat the potato.\n")

                                 elif args[1] == can_eat[5]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 2 > health_max:
                                             inventory.remove('onion')
                                             health = 75
                                             print("You eat the onion.\n")
                                       else:
                                             inventory.remove('onion')
                                             health += 2
                                             print("You eat the onion.\n")

                                 else:
                                     print("You can't eat this.\n")
                           else:
                               print("You don't have this.\n")
                      except:
                            print("Eat what?\n")

                if args[0] == "turn":
                    try:
                        if args[1] == 'lantern':
                            if 'lantern' in inventory:
                                global lantern_on
                                if args[2] == 'on':
                                    lantern_on = True
                                    moves += 1
                                    print("The lantern is now on.\n")

                                elif args[2] == 'off':
                                    lantern_on = False
                                    moves += 1
                                    print("The lantern is now off.\n")
                            else:
                                print("You don't have a lantern.\n")
                    except:
                        print("Invalid.\n")

                if args[0] == "say":
                    try:
                        if args[1] != None:
                            moves += 1
                            print("You say:" + " " + args[1])
                            print("")
                        else:
                            pass
                    except:
                        print("Say what?\n")

                if args[0] == 'read':
                    try:
                        if args[1] == 'paper':
                            if 'paper' in inventory:
                                global paper
                                moves += 1
                                print(paper)
                            else:
                                pass

                        elif args[1] == 'note':
                            if 'note' in inventory:
                                global note
                                moves += 1
                                print(note)
                            else:
                                pass

                        elif args[1] == 'post-it':
                            if 'post-it' in inventory:
                                global post
                                moves += 1
                                print(post)
                            else:
                                pass

                        elif args[1] == 'poster':
                            if 'poster' in inventory:
                                global poster
                                moves += 1
                                print(poster)
                            else:
                                pass

                        else:
                            pass

                    except:
                        print("Read what?\n")

                if args[0] == 'look':
                    global key_desc
                    global sword_desc
                    global knife_desc
                    global ruby_desc
                    global amulet_desc
                    try:
                        if args[1] == 'at':
                            try:
                                if args[2] in inventory:
                                    if args[2] == 'key':
                                        print(key_desc)

                                    elif args[2] == 'sword':
                                        print(sword_desc)

                                    elif args[2] == 'knife':
                                        print(knife_desc)

                                    elif args[2] == 'ruby':
                                        print(ruby_desc)

                                    elif args[2] == 'amulet':
                                        print(amulet_desc)

                                    else:
                                        print("I see nothing special about this.\n")

                                else:
                                    print("You don't have this item.\n")

                            except:
                                print("Look at what?\n")

                    except:
                        print("Look at what?\n")

    def up(self):
        global moves
        moves += 1
        print("You can't go that way.\n")

    def down(self):
        global moves
        moves += 1
        print("You can't go that way.\n")

    def north(self):
        global moves
        moves += 1
        if 'amulet' in inventory:
            pass
        else:
            print("Sadboy is too scared to go north. You need a amulet.\n")

    def east(self):
        global moves
        moves += 1
        print("Nothing here.\n")

    def south(self):
        global moves
        moves += 1
        complete = True
        f = Forest()
        f.inicio()

    def west(self):
        global moves
        moves += 1
        complete = True
        m = Mountain()
        m.inicio()

#Trip through memory lane
class Mountain:
    def __init__(self):
        self.state = 'mountain'

    def quit(self):
        c = character()
        c.quit()

    def ajuda(self):
        c = character()
        c.ajuda()

    def status(self):
        c = character()
        c.status()

    def restart(self):
        c = character()
        c.restart()

    def score(self):
        c = character()
        c.score()

    def save(self):
        save()

    def achievement(self):
        c = character()
        c.achievement()

    def inventory(self):
        if len(inventory) > 0:
            print("You have:")
            print inventory
            print("")
        else:
            print("Your inventory is empty.\n")

    def inicio(self):
        complete = False
        global moves, local
        local = 'Mountain'
        print("Mountain")
        print("A mystery mountain, there is a entrance to north.\n")

        itens = {
        1: {}
        }

        currentRoom = 1

        commands = {
        'help': Mountain.ajuda,
        'quit': Mountain.quit,
        'save': Mountain.save,
        'score': Mountain.score,
        'achievement': Mountain.achievement,
        'north': Mountain.north,
        'west': Mountain.west,
        'east': Mountain.east,
        'south': Mountain.south,
        'up': Mountain.up,
        'down': Mountain.down,
        'status': Mountain.status,
        'restart': Mountain.restart,
        'inventory': Mountain.inventory
        }

        m = Mountain()

        while complete == False:
            line = raw_input("> ")
            args = line.split()
            if len(args) == 0:
                print("What you want to do?\n")

            elif len(args) > 0:
                commandFound = False
                for c in commands.keys():
                    if args[0] == c[:len(args[0])]:
                        commands[c](m)
                        commandFound = True
                        break

                if args[0] == "take":
                    try:
                        if "item" in itens[currentRoom] and args[1] in itens[currentRoom]["item"]:
                            inventory.append(args[1])
                            moves += 1
                            print(args[1]+":" + " Taken.\n")
                            del itens[currentRoom]["item"]
                        else:
                            print("Can't get this.\n")

                    except:
                        print("Invalid.\n")

                if args[0] == "drop":
                    try:
                        if args[1] in inventory:
                            inventory.remove(args[1])
                            moves += 1
                            print(args[1]+":" + " Dropped.\n")

                        else:
                            print("Can't drop this.\n")

                    except:
                      print("Invalid.\n")

                if args[0] == "eat":
                      try:
                           if args[1] in inventory and args[1] in can_eat:
                                 global health, health_max
                                 if args[1] == can_eat[0]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 5 > health_max:
                                             inventory.remove('bread')
                                             health = 75
                                             print("You eat the bread.\n")
                                       else:
                                             inventory.remove('bread')
                                             health += 5
                                             print("You eat the bread.\n")

                                 elif args[1] == can_eat[1]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 5 > health_max:
                                             inventory.remove('apple')
                                             health = 75
                                             print("You eat the apple.\n")
                                       else:
                                             inventory.remove('apple')
                                             health += 5
                                             print("You eat the apple.\n")

                                 elif args[1] == can_eat[2]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 3 > health_max:
                                             inventory.remove('carrot')
                                             health = 75
                                             print("You eat the carrot.\n")
                                       else:
                                             inventory.remove('carrot')
                                             health += 3
                                             print("You eat the carrot.\n")

                                 elif args[1] == can_eat[3]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 4 > health_max:
                                             inventory.remove('tomato')
                                             health = 75
                                             print("You eat the tomato.\n")
                                       else:
                                             inventory.remove('tomato')
                                             health += 4
                                             print("You eat the tomato.\n")

                                 elif args[1] == can_eat[4]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 4 > health_max:
                                             inventory.remove('potato')
                                             health = 75
                                             print("You eat the potato.\n")
                                       else:
                                             inventory.remove('potato')
                                             health += 4
                                             print("You eat the potato.\n")

                                 elif args[1] == can_eat[5]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 2 > health_max:
                                             inventory.remove('onion')
                                             health = 75
                                             print("You eat the onion.\n")
                                       else:
                                             inventory.remove('onion')
                                             health += 2
                                             print("You eat the onion.\n")

                                 else:
                                     print("You can't eat this.\n")
                           else:
                               print("You don't have this.\n")
                      except:
                            print("Eat what?\n")

                if args[0] == "turn":
                    try:
                        if args[1] == 'lantern':
                            if 'lantern' in inventory:
                                global lantern_on
                                if args[2] == 'on':
                                    lantern_on = True
                                    moves += 1
                                    print("The lantern is now on.\n")

                                elif args[2] == 'off':
                                    lantern_on = False
                                    moves += 1
                                    print("The lantern is now off.\n")
                            else:
                                print("You don't have a lantern.\n")
                    except:
                        print("Invalid.\n")

                if args[0] == "say":
                    try:
                        if args[1] != None:
                            moves += 1
                            print("You say:" + " " + args[1])
                            print("")
                        else:
                            pass
                    except:
                        print("Say what?\n")

                if args[0] == 'read':
                    try:
                        if args[1] == 'paper':
                            if 'paper' in inventory:
                                global paper
                                moves += 1
                                print(paper)
                            else:
                                pass

                        elif args[1] == 'note':
                            if 'note' in inventory:
                                global note
                                moves += 1
                                print(note)
                            else:
                                pass

                        elif args[1] == 'post-it':
                            if 'post-it' in inventory:
                                global post
                                moves += 1
                                print(post)
                            else:
                                pass

                        elif args[1] == 'poster':
                            if 'poster' in inventory:
                                global poster
                                moves += 1
                                print(poster)
                            else:
                                pass

                        else:
                            pass

                    except:
                        print("Read what?\n")

                if args[0] == 'look':
                    global key_desc
                    global sword_desc
                    global knife_desc
                    global ruby_desc
                    global amulet_desc
                    try:
                        if args[1] == 'at':
                            try:
                                if args[2] in inventory:
                                    if args[2] == 'key':
                                        print(key_desc)

                                    elif args[2] == 'sword':
                                        print(sword_desc)

                                    elif args[2] == 'knife':
                                        print(knife_desc)

                                    elif args[2] == 'ruby':
                                        print(ruby_desc)

                                    elif args[2] == 'amulet':
                                        print(amulet_desc)

                                    else:
                                        print("I see nothing special about this.\n")

                                else:
                                    print("You don't have this item.\n")

                            except:
                                print("Look at what?\n")

                    except:
                        print("Look at what?\n")

    def up(self):
        global moves
        moves += 1
        print("You can't go that way.\n")

    def down(self):
        global moves
        moves += 1
        print("You can't go that way.\n")

    def north(self):
        global moves
        moves += 1
        cv = Cave()
        cv.inicio()

    def east(self):
        global moves
        moves += 1
        complete = True
        c = Clearing()
        c.inicio()

    def south(self):
        global moves
        moves += 1
        complete = True
        f = Forest()
        f.inicio()

    def west(self):
        global moves
        moves += 1
        print("Nothing here.\n")

class OutTemple:
    def __init__(self):
        self.state = 'outtemple'

    def quit(self):
        c = character()
        c.quit()

    def ajuda(self):
        c = character()
        c.ajuda()

    def status(self):
        c = character()
        c.status()

    def restart(self):
        c = character()
        c.restart()

    def score(self):
        c = character()
        c.score()

    def achievement(self):
        c = character()
        c.achievement()

    def inventory(self):
        if len(inventory) > 0:
            print("You have:")
            print inventory
            print("")
        else:
            print("Your inventory is empty.\n")

    def inicio(self):
        complete = False
        global moves
        global lantern_on
        print("Valley")
        print("There some trees around you.")

        if lantern_on == True:
            print("With the light of your flashlight you see a ring on the floor")
            print("emitting a strange blue light.\n")
            itens = {
            1 : {"item": "ring"}
            }
            currentRoom = 1

        else:
            print("")
            itens = {
            1 : {}
            }
            currentRoom = 1

        commands = {
        'help': OutTemple.ajuda,
        'quit': OutTemple.quit,
        'score': OutTemple.score,
        'achievement': OutTemple.achievement,
        'north': OutTemple.north,
        'west': OutTemple.west,
        'east': OutTemple.east,
        'south': OutTemple.south,
        'up': OutTemple.up,
        'down': OutTemple.down,
        'status': OutTemple.status,
        'restart': OutTemple.restart,
        'inventory': OutTemple.inventory
        }

        ot = OutTemple()

        while complete == False:
            line = raw_input("> ")
            args = line.split()
            if len(args) == 0:
                print("What you want to do?\n")

            elif len(args) > 0:
                commandFound = False
                for c in commands.keys():
                    if args[0] == c[:len(args[0])]:
                        commands[c](ot)
                        commandFound = True
                        break

                if args[0] == "take":
                    try:
                        if "item" in itens[currentRoom] and args[1] in itens[currentRoom]["item"]:
                            inventory.append(args[1])
                            moves += 1
                            print(args[1]+":" + " Taken.\n")
                            del itens[currentRoom]["item"]
                        else:
                            print("Can't get this.\n")

                    except:
                        print("Invalid.\n")

                if args[0] == "drop":
                    try:
                        if args[1] in inventory:
                            inventory.remove(args[1])
                            moves += 1
                            print(args[1]+":" + " Dropped.\n")

                        else:
                            print("Can't drop this.\n")

                    except:
                      print("Invalid.\n")

                if args[0] == "eat":
                      try:
                           if args[1] in inventory and args[1] in can_eat:
                                 global health, health_max
                                 if args[1] == can_eat[0]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 5 > health_max:
                                             inventory.remove('bread')
                                             health = 75
                                             print("You eat the bread.\n")
                                       else:
                                             inventory.remove('bread')
                                             health += 5
                                             print("You eat the bread.\n")

                                 elif args[1] == can_eat[1]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 5 > health_max:
                                             inventory.remove('apple')
                                             health = 75
                                             print("You eat the apple.\n")
                                       else:
                                             inventory.remove('apple')
                                             health += 5
                                             print("You eat the apple.\n")

                                 elif args[1] == can_eat[2]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 3 > health_max:
                                             inventory.remove('carrot')
                                             health = 75
                                             print("You eat the carrot.\n")
                                       else:
                                             inventory.remove('carrot')
                                             health += 3
                                             print("You eat the carrot.\n")

                                 elif args[1] == can_eat[3]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 4 > health_max:
                                             inventory.remove('tomato')
                                             health = 75
                                             print("You eat the tomato.\n")
                                       else:
                                             inventory.remove('tomato')
                                             health += 4
                                             print("You eat the tomato.\n")

                                 elif args[1] == can_eat[4]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 4 > health_max:
                                             inventory.remove('potato')
                                             health = 75
                                             print("You eat the potato.\n")
                                       else:
                                             inventory.remove('potato')
                                             health += 4
                                             print("You eat the potato.\n")

                                 elif args[1] == can_eat[5]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 2 > health_max:
                                             inventory.remove('onion')
                                             health = 75
                                             print("You eat the onion.\n")
                                       else:
                                             inventory.remove('onion')
                                             health += 2
                                             print("You eat the onion.\n")

                                 else:
                                     print("You can't eat this.\n")
                           else:
                               print("You don't have this.\n")
                      except:
                            print("Eat what?\n")

                if args[0] == "turn":
                    try:
                        if args[1] == 'lantern':
                            if 'lantern' in inventory:
                                if args[2] == 'on':
                                    lantern_on = True
                                    moves += 1
                                    print("The lantern is now on.\n")

                                elif args[2] == 'off':
                                    lantern_on = False
                                    moves += 1
                                    print("The lantern is now off.\n")
                            else:
                                print("You don't have a lantern.\n")
                    except:
                        print("Invalid.\n")

                if args[0] == "say":
                    try:
                        if args[1] != None:
                            moves += 1
                            print("You say:" + " " + args[1])
                            print("")
                        else:
                            pass
                    except:
                        print("Say what?\n")

                if args[0] == 'read':
                    try:
                        if args[1] == 'paper':
                            if 'paper' in inventory:
                                global paper
                                moves += 1
                                print(paper)
                            else:
                                pass

                        elif args[1] == 'note':
                            if 'note' in inventory:
                                global note
                                moves += 1
                                print(note)
                            else:
                                pass

                        elif args[1] == 'post-it':
                            if 'post-it' in inventory:
                                global post
                                moves += 1
                                print(post)
                            else:
                                pass

                        elif args[1] == 'poster':
                            if 'poster' in inventory:
                                global poster
                                moves += 1
                                print(poster)
                            else:
                                pass

                        else:
                            pass

                    except:
                        print("Read what?\n")

                if args[0] == 'look':
                    global key_desc
                    global sword_desc
                    global knife_desc
                    global ruby_desc
                    global amulet_desc
                    try:
                        if args[1] == 'at':
                            try:
                                if args[2] in inventory:
                                    if args[2] == 'key':
                                        print(key_desc)

                                    elif args[2] == 'sword':
                                        print(sword_desc)

                                    elif args[2] == 'knife':
                                        print(knife_desc)

                                    elif args[2] == 'ruby':
                                        print(ruby_desc)

                                    elif args[2] == 'amulet':
                                        print(amulet_desc)

                                    else:
                                        print("I see nothing special about this.\n")

                                else:
                                    print("You don't have this item.\n")

                            except:
                                print("Look at what?\n")

                    except:
                        print("Look at what?\n")

    def up(self):
        global moves
        moves += 1
        print("You can't go that way.\n")

    def down(self):
        global moves
        moves += 1
        print("You can't go that way.\n")

    def north(self):
        global moves
        moves += 1
        print("You are near a house.\n")
        complete = True
        oh = OutHouse()
        oh.inicio()

    def east(self):
        global moves
        moves += 1
        pass

    def south(self):
        global moves
        moves += 1
        pass

    def west(self):
        global moves
        moves += 1
        complete = True
        fp = ForestPath()
        fp.inicio()

class Kitchen:
    def __init__(self):
        self.state = 'kitchen'

    def quit(self):
        c = character()
        c.quit()

    def ajuda(self):
        c = character()
        c.ajuda()

    def status(self):
        c = character()
        c.status()

    def restart(self):
        c = character()
        c.restart()

    def score(self):
        c = character()
        c.score()

    def achievement(self):
        c = character()
        c.achievement()

    def inventory(self):
        if len(inventory) > 0:
            print("You have:")
            print inventory
            print("")
        else:
            print("Your inventory is empty.\n")

    def inicio(self):
        complete = False
        print("Kitchen")
        global moves
        global taken2
        if taken2 == True:
            print("You are in the kitchen.\n")
            itens = {
            1 : {}
            }
            currentRoom = 1
        else:
            print("You are in the kitchen, there is a bread on the table.\n")
            itens = {
            1 : {"item": 'bread'}
            }
            currentRoom = 1

        commands = {
        'help': Kitchen.ajuda,
        'quit': Kitchen.quit,
        'score': Kitchen.score,
        'achievement': Kitchen.achievement,
        'north': Kitchen.north,
        'west': Kitchen.west,
        'east': Kitchen.east,
        'south': Kitchen.south,
        'up': Kitchen.up,
        'down': Kitchen.down,
        'status': Kitchen.status,
        'restart': Kitchen.restart,
        'inventory': Kitchen.inventory
        }

        k = Kitchen()

        while complete == False:
            line = raw_input("> ")
            args = line.split()
            if len(args) == 0:
                print("What you want to do?\n")

            elif len(args) > 0:
                commandFound = False
                for c in commands.keys():
                    if args[0] == c[:len(args[0])]:
                        commands[c](k)
                        commandFound = True
                        break

                if args[0] == "take":
                    try:
                        if "item" in itens[currentRoom] and args[1] in itens[currentRoom]["item"]:
                            inventory.append(args[1])
                            moves += 1
                            print(args[1]+":" + " Taken.\n")
                            del itens[currentRoom]["item"]
                            taken2 = True
                        else:
                            print("Can't get this.\n")

                    except:
                        print("Invalid.\n")

                if args[0] == "drop":
                    try:
                        if args[1] in inventory:
                            inventory.remove(args[1])
                            moves += 1
                            print(args[1]+":" + " Dropped.\n")

                        else:
                            print("Can't drop this.\n")

                    except:
                      print("Invalid.\n")

                if args[0] == "eat":
                      try:
                           if args[1] in inventory and args[1] in can_eat:
                                 global health, health_max
                                 if args[1] == can_eat[0]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 5 > health_max:
                                             inventory.remove('bread')
                                             health = 75
                                             print("You eat the bread.\n")
                                       else:
                                             inventory.remove('bread')
                                             health += 5
                                             print("You eat the bread.\n")

                                 elif args[1] == can_eat[1]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 5 > health_max:
                                             inventory.remove('apple')
                                             health = 75
                                             print("You eat the apple.\n")
                                       else:
                                             inventory.remove('apple')
                                             health += 5
                                             print("You eat the apple.\n")

                                 elif args[1] == can_eat[2]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 3 > health_max:
                                             inventory.remove('carrot')
                                             health = 75
                                             print("You eat the carrot.\n")
                                       else:
                                             inventory.remove('carrot')
                                             health += 3
                                             print("You eat the carrot.\n")

                                 elif args[1] == can_eat[3]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 4 > health_max:
                                             inventory.remove('tomato')
                                             health = 75
                                             print("You eat the tomato.\n")
                                       else:
                                             inventory.remove('tomato')
                                             health += 4
                                             print("You eat the tomato.\n")

                                 elif args[1] == can_eat[4]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 4 > health_max:
                                             inventory.remove('potato')
                                             health = 75
                                             print("You eat the potato.\n")
                                       else:
                                             inventory.remove('potato')
                                             health += 4
                                             print("You eat the potato.\n")

                                 elif args[1] == can_eat[5]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 2 > health_max:
                                             inventory.remove('onion')
                                             health = 75
                                             print("You eat the onion.\n")
                                       else:
                                             inventory.remove('onion')
                                             health += 2
                                             print("You eat the onion.\n")

                                 else:
                                     print("You can't eat this.\n")
                           else:
                               print("You don't have this.\n")
                      except:
                            print("Eat what?\n")

                if args[0] == "turn":
                    try:
                        if args[1] == 'lantern':
                            if 'lantern' in inventory:
                                global lantern_on
                                if args[2] == 'on':
                                    lantern_on = True
                                    moves += 1
                                    print("The lantern is now on.\n")

                                elif args[2] == 'off':
                                    lantern_on = False
                                    moves += 1
                                    print("The lantern is now off.\n")
                            else:
                                print("You don't have a lantern.\n")
                    except:
                        print("Invalid.\n")

                if args[0] == "say":
                    try:
                        if args[1] != None:
                            moves += 1
                            print("You say:" + " " + args[1])
                            print("")
                        else:
                            pass
                    except:
                        print("Say what?\n")

                if args[0] == 'read':
                    try:
                        if args[1] == 'paper':
                            if 'paper' in inventory:
                                global paper
                                moves += 1
                                print(paper)
                            else:
                                pass

                        elif args[1] == 'note':
                            if 'note' in inventory:
                                global note
                                moves += 1
                                print(note)
                            else:
                                pass

                        elif args[1] == 'post-it':
                            if 'post-it' in inventory:
                                global post
                                moves += 1
                                print(post)
                            else:
                                pass

                        elif args[1] == 'poster':
                            if 'poster' in inventory:
                                global poster
                                moves += 1
                                print(poster)
                            else:
                                pass

                        else:
                            pass

                    except:
                        print("Read what?\n")

                if args[0] == 'look':
                    global key_desc
                    global sword_desc
                    global knife_desc
                    global ruby_desc
                    global amulet_desc
                    try:
                        if args[1] == 'at':
                            try:
                                if args[2] in inventory:
                                    if args[2] == 'key':
                                        print(key_desc)

                                    elif args[2] == 'sword':
                                        print(sword_desc)

                                    elif args[2] == 'knife':
                                        print(knife_desc)

                                    elif args[2] == 'ruby':
                                        print(ruby_desc)

                                    elif args[2] == 'amulet':
                                        print(amulet_desc)

                                    else:
                                        print("I see nothing special about this.\n")

                                else:
                                    print("You don't have this item.\n")

                            except:
                                print("Look at what?\n")

                    except:
                        print("Look at what?\n")

                if args[0] == 'open':
                        print("Nothing to open here.\n")

                if args[0] == 'close':
                        print("Nothing to close here.\n")

    def up(self):
        global moves
        moves += 1
        complete = True
        print("You can't go that way.\n")

    def down(self):
        global moves
        moves += 1
        print("You can't go that way.\n")

    def north(self):
        global moves
        moves += 1
        print("You can't go that way.\n")

    def east(self):
        global moves
        moves += 1
        print("You can't go that way.\n")

    def south(self):
        global moves
        moves += 1
        print("You can't go that way.\n")

    def west(self):
        global moves
        moves += 1
        complete = True
        h2 = House2()
        h2.inicio()

class House2:
    def __init__(self):
        self.state = 'house2'

    def quit(self):
        c = character()
        c.quit()

    def ajuda(self):
        c = character()
        c.ajuda()

    def status(self):
        c = character()
        c.status()

    def restart(self):
        c = character()
        c.restart()

    def score(self):
        c = character()
        c.score()

    def save(self):
        save()

    def achievement(self):
        c = character()
        c.achievement()

    def inventory(self):
        if len(inventory) > 0:
            print("You have:")
            print inventory
            print("")
        else:
            print("Your inventory is empty.\n")

    def inicio(self):
        complete = False
        print("House")
        global moves
        global trapdoor_open
        global trapdoor_close
        global local
        local = 'House2'
        if 'amulet' in inventory:
            print("")
            if 'poster' in inventory:
                itens = {
                1 : {}
                }
                currentRoom = 1
            else:
                itens = {
                1 : {"item": 'poster'}
                }
                currentRoom = 1

        else:
            print("You are in the house. There is a poster in the wall and there is")
            print("a trapdoor here. You hear a strange noise, there's someone in the attic.\n")

            if 'poster' in inventory:
                itens = {
                1 : {}
                }
                currentRoom = 1
            else:
                itens = {
                1 : {"item": 'poster'}
                }
                currentRoom = 1

        commands = {
        'help': House2.ajuda,
        'quit': House2.quit,
        'save': House2.save,
        'score': House2.score,
        'achievement': House2.achievement,
        'north': House2.north,
        'west': House2.west,
        'east': House2.east,
        'south': House2.south,
        'up': House2.up,
        'down': House2.down,
        'status': House2.status,
        'restart': House2.restart,
        'inventory': House2.inventory
        }

        h2 = House2()

        while complete == False:
            line = raw_input("> ")
            args = line.split()
            if len(args) == 0:
                print("What you want to do?\n")

            elif len(args) > 0:
                commandFound = False
                for c in commands.keys():
                    if args[0] == c[:len(args[0])]:
                        commands[c](h2)
                        commandFound = True
                        break

                if args[0] == "take":
                    try:
                        if "item" in itens[currentRoom] and args[1] in itens[currentRoom]["item"]:
                            inventory.append(args[1])
                            moves += 1
                            print(args[1]+":" + " Taken.\n")
                            del itens[currentRoom]["item"]
                        else:
                            print("Can't get this.\n")

                    except:
                        print("Invalid.\n")

                if args[0] == "drop":
                    try:
                        if args[1] in inventory:
                            inventory.remove(args[1])
                            moves += 1
                            print(args[1]+":" + " Dropped.\n")

                        else:
                            print("Can't drop this.\n")

                    except:
                      print("Invalid.\n")

                if args[0] == "eat":
                      try:
                           if args[1] in inventory and args[1] in can_eat:
                                 global health, health_max
                                 if args[1] == can_eat[0]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 5 > health_max:
                                             inventory.remove('bread')
                                             health = 75
                                             print("You eat the bread.\n")
                                       else:
                                             inventory.remove('bread')
                                             health += 5
                                             print("You eat the bread.\n")

                                 elif args[1] == can_eat[1]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 5 > health_max:
                                             inventory.remove('apple')
                                             health = 75
                                             print("You eat the apple.\n")
                                       else:
                                             inventory.remove('apple')
                                             health += 5
                                             print("You eat the apple.\n")

                                 elif args[1] == can_eat[2]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 3 > health_max:
                                             inventory.remove('carrot')
                                             health = 75
                                             print("You eat the carrot.\n")
                                       else:
                                             inventory.remove('carrot')
                                             health += 3
                                             print("You eat the carrot.\n")

                                 elif args[1] == can_eat[3]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 4 > health_max:
                                             inventory.remove('tomato')
                                             health = 75
                                             print("You eat the tomato.\n")
                                       else:
                                             inventory.remove('tomato')
                                             health += 4
                                             print("You eat the tomato.\n")

                                 elif args[1] == can_eat[4]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 4 > health_max:
                                             inventory.remove('potato')
                                             health = 75
                                             print("You eat the potato.\n")
                                       else:
                                             inventory.remove('potato')
                                             health += 4
                                             print("You eat the potato.\n")

                                 elif args[1] == can_eat[5]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 2 > health_max:
                                             inventory.remove('onion')
                                             health = 75
                                             print("You eat the onion.\n")
                                       else:
                                             inventory.remove('onion')
                                             health += 2
                                             print("You eat the onion.\n")

                                 else:
                                     print("You can't eat this.\n")
                           else:
                               print("You don't have this.\n")
                      except:
                            print("Eat what?\n")

                if args[0] == "turn":
                    try:
                        if args[1] == 'lantern':
                            if 'lantern' in inventory:
                                global lantern_on
                                if args[2] == 'on':
                                    lantern_on = True
                                    moves += 1
                                    print("The lantern is now on.\n")

                                elif args[2] == 'off':
                                    lantern_on = False
                                    moves += 1
                                    print("The lantern is now off.\n")
                            else:
                                print("You don't have a lantern.\n")
                    except:
                        print("Invalid.\n")

                if args[0] == "say":
                    try:
                        if args[1] != None:
                            moves += 1
                            print("You say:" + " " + args[1])
                            print("")
                        else:
                            pass
                    except:
                        print("Say what?\n")

                if args[0] == 'read':
                    try:
                        if args[1] == 'paper':
                            if 'paper' in inventory:
                                global paper
                                moves += 1
                                print(paper)
                            else:
                                pass

                        elif args[1] == 'note':
                            if 'note' in inventory:
                                global note
                                moves += 1
                                print(note)
                            else:
                                pass

                        elif args[1] == 'post-it':
                            if 'post-it' in inventory:
                                global post
                                moves += 1
                                print(post)
                            else:
                                pass

                        elif args[1] == 'poster':
                            if 'poster' in inventory:
                                global poster
                                moves += 1
                                print(poster)
                            else:
                                pass

                        else:
                            pass

                    except:
                        print("Read what?\n")

                if args[0] == 'look':
                    global key_desc
                    global sword_desc
                    global knife_desc
                    global ruby_desc
                    global amulet_desc
                    try:
                        if args[1] == 'at':
                            try:
                                if args[2] in inventory:
                                    if args[2] == 'key':
                                        print(key_desc)

                                    elif args[2] == 'sword':
                                        print(sword_desc)

                                    elif args[2] == 'knife':
                                        print(knife_desc)

                                    elif args[2] == 'ruby':
                                        print(ruby_desc)

                                    elif args[2] == 'amulet':
                                        print(amulet_desc)

                                    else:
                                        print("I see nothing special about this.\n")

                                else:
                                    print("You don't have this item.\n")

                            except:
                                print("Look at what?\n")

                    except:
                        print("Look at what?\n")

                if args[0] == 'open':
                    try:
                        if args[1] == 'trapdoor':
                            trapdoor_open = True
                            trapdoor_close = False
                            print("You open the trapdoor.\n")

                        else:
                            print("Open what?\n")

                    except:
                        print("Open what?\n")

                if args[0] == 'close':
                    try:
                        if args[1] == 'trapdoor':
                            trapdoor_open = False
                            trapdoor_close = True
                            print("You close the trapdoor.\n")

                        else:
                            print("Close what?\n")

                    except:
                        print("Close what?\n")

    def up(self):
        global moves
        moves += 1
        complete = True
        a2 = Attic2()
        a2.inicio()

    def down(self):
        global moves
        moves += 1
        if trapdoor_open == True and trapdoor_close == False:
            complete = True
            td2 = TrapDoor2()
            td2.inicio()

        else:
            print("There is a trapdoor here, but you need to open it.\n")

    def north(self):
        global moves
        moves += 1
        pass

    def east(self):
        global moves
        moves += 1
        complete = True
        k = Kitchen()
        k.inicio()

    def south(self):
        global moves
        moves += 1
        complete = True
        ss = SmallStream()
        ss.inicio()

    def west(self):
        global moves
        moves += 1
        pass

class SmallStream:
    def __init__(self):
        self.state = 'stream'

    def quit(self):
        c = character()
        c.quit()

    def status(self):
        c = character()
        c.status()

    def ajuda(self):
        c = character()
        c.ajuda()

    def restart(self):
        c = character()
        c.restart()

    def score(self):
        c = character()
        c.score()

    def achievement(self):
        c = character()
        c.achievement()

    def inventory(self):
        if len(inventory) > 0:
            print("You have:")
            print inventory
            print("")
        else:
            print("Your inventory is empty.\n")

    def inicio(self):
        complete = False
        global moves
        print("Small stream")
        if 'ring' in inventory:
            print("There is a small stream here, the water of the stream is crystal clear.")
            print("Have a house in the west.\n")

            itens = {
            1 : {}
            }

            currentRoom = 1

        else:
            print("There is a small stream here, the water of the stream is crystal clear")
            print("you can see a knife in the stream. Have a house in the west.\n")

            itens = {
            1 : {"item": 'knife'}
            }

            currentRoom = 1

        commands = {
        'help': SmallStream.ajuda,
        'quit': SmallStream.quit,
        'score': SmallStream.score,
        'achievement': SmallStream.achievement,
        'north': SmallStream.north,
        'west': SmallStream.west,
        'east': SmallStream.east,
        'south': SmallStream.south,
        'up': SmallStream.up,
        'down': SmallStream.down,
        'status': SmallStream.status,
        'restart': SmallStream.restart,
        'inventory': SmallStream.inventory
        }

        st = SmallStream()

        while complete == False:
            line = raw_input("> ")
            args = line.split()
            if len(args) == 0:
                print("What you want to do?\n")

            elif len(args) > 0:
                commandFound = False
                for c in commands.keys():
                    if args[0] == c[:len(args[0])]:
                        commands[c](st)
                        commandFound = True
                        break

                if args[0] == "take":
                    try:
                        if "item" in itens[currentRoom] and args[1] in itens[currentRoom]["item"]:
                            inventory.append(args[1])
                            moves += 1
                            print(args[1]+":" + " Taken.\n")
                            del itens[currentRoom]["item"]
                        else:
                            print("Can't get this.\n")

                    except:
                        print("Invalid.\n")

                if args[0] == "drop":
                    try:
                        if args[1] in inventory:
                            inventory.remove(args[1])
                            moves += 1
                            print(args[1]+":" + " Dropped.\n")

                        else:
                            print("Can't drop this.\n")

                    except:
                      print("Invalid.\n")

                if args[0] == "eat":
                      try:
                           if args[1] in inventory and args[1] in can_eat:
                                 global health, health_max
                                 if args[1] == can_eat[0]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 5 > health_max:
                                             inventory.remove('bread')
                                             health = 75
                                             print("You eat the bread.\n")
                                       else:
                                             inventory.remove('bread')
                                             health += 5
                                             print("You eat the bread.\n")

                                 elif args[1] == can_eat[1]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 5 > health_max:
                                             inventory.remove('apple')
                                             health = 75
                                             print("You eat the apple.\n")
                                       else:
                                             inventory.remove('apple')
                                             health += 5
                                             print("You eat the apple.\n")

                                 elif args[1] == can_eat[2]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 3 > health_max:
                                             inventory.remove('carrot')
                                             health = 75
                                             print("You eat the carrot.\n")
                                       else:
                                             inventory.remove('carrot')
                                             health += 3
                                             print("You eat the carrot.\n")

                                 elif args[1] == can_eat[3]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 4 > health_max:
                                             inventory.remove('tomato')
                                             health = 75
                                             print("You eat the tomato.\n")
                                       else:
                                             inventory.remove('tomato')
                                             health += 4
                                             print("You eat the tomato.\n")

                                 elif args[1] == can_eat[4]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 4 > health_max:
                                             inventory.remove('potato')
                                             health = 75
                                             print("You eat the potato.\n")
                                       else:
                                             inventory.remove('potato')
                                             health += 4
                                             print("You eat the potato.\n")

                                 elif args[1] == can_eat[5]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 2 > health_max:
                                             inventory.remove('onion')
                                             health = 75
                                             print("You eat the onion.\n")
                                       else:
                                             inventory.remove('onion')
                                             health += 2
                                             print("You eat the onion.\n")

                                 else:
                                     print("You can't eat this.\n")
                           else:
                               print("You don't have this.\n")
                      except:
                            print("Eat what?\n")

                if args[0] == "turn":
                    try:
                        if args[1] == 'lantern':
                            if 'lantern' in inventory:
                                global lantern_on
                                if args[2] == 'on':
                                    lantern_on = True
                                    moves += 1
                                    print("The lantern is now on.\n")

                                elif args[2] == 'off':
                                    lantern_on = False
                                    moves += 1
                                    print("The lantern is now off.\n")
                            else:
                                print("You don't have a lantern.\n")
                    except:
                        print("Invalid.\n")

                if args[0] == "say":
                    try:
                        if args[1] != None:
                            moves += 1
                            print("You say:" + " " + args[1])
                            print("")
                        else:
                            pass
                    except:
                        print("Say what?\n")

                if args[0] == 'read':
                    try:
                        if args[1] == 'paper':
                            if 'paper' in inventory:
                                global paper
                                moves += 1
                                print(paper)
                            else:
                                pass

                        elif args[1] == 'note':
                            if 'note' in inventory:
                                global note
                                moves += 1
                                print(note)
                            else:
                                pass

                        elif args[1] == 'post-it':
                            if 'post-it' in inventory:
                                global post
                                moves += 1
                                print(post)
                            else:
                                pass

                        elif args[1] == 'poster':
                            if 'poster' in inventory:
                                global poster
                                moves += 1
                                print(poster)
                            else:
                                pass

                        else:
                            pass

                    except:
                        print("Read what?\n")

                if args[0] == 'look':
                    global key_desc
                    global sword_desc
                    global knife_desc
                    global ruby_desc
                    global amulet_desc
                    try:
                        if args[1] == 'at':
                            try:
                                if args[2] in inventory:
                                    if args[2] == 'key':
                                        print(key_desc)

                                    elif args[2] == 'sword':
                                        print(sword_desc)

                                    elif args[2] == 'knife':
                                        print(knife_desc)

                                    elif args[2] == 'ruby':
                                        print(ruby_desc)

                                    elif args[2] == 'amulet':
                                        print(amulet_desc)

                                    else:
                                        print("I see nothing special about this.\n")

                                else:
                                    print("You don't have this item.\n")

                            except:
                                print("Look at what?\n")

                    except:
                        print("Look at what?\n")

    def up(self):
        global moves
        moves += 1
        print("You can't go that way.\n")

    def down(self):
        global moves
        moves += 1
        print("You can't go that way.\n")

    def north(self):
        global moves
        moves += 1
        print("Stream water.\n")

    def east(self):
        global moves
        moves += 1
        print("Stream water.\n")

    def south(self):
        global moves
        moves += 1
        cb = CanyonBottom()
        cb.inicio()

    def west(self):
        global moves
        moves += 1
        complete = True
        h2 = House2()
        h2.inicio()

class Attic:
    def __init__(self):
        self.state = 'attic'

    def quit(self):
        c = character()
        c.quit()

    def status(self):
        c = character()
        c.status()

    def ajuda(self):
        c = character()
        c.ajuda()

    def restart(self):
        c = character()
        c.restart()

    def score(self):
        c = character()
        c.score()

    def achievement(self):
        c = character()
        c.achievement()

    def inventory(self):
        if len(inventory) > 0:
            print("You have:")
            print inventory
            print("")
        else:
            print("Your inventory is empty.\n")

    def inicio(self):
        complete = False
        global moves
        print("Attic")
        if 'key' in inventory:
            print("This is the attic. The only exit is a stairway leading down.")
            print("There lamps illuminating the place.\n")

            itens = {
            1 : {}
            }

            currentRoom = 1

        else:
            print("This is the attic. The only exit is a stairway leading down.")
            print("There lamps illuminating the place. There is a key and a sphere here.\n")

            itens = {
            1 : {"item": 'key', "item2": 'sphere'}
            }

            currentRoom = 1

        commands = {
        'help': Attic.ajuda,
        'quit': Attic.quit,
        'score': Attic.score,
        'achievement': Attic.achievement,
        'north': Attic.north,
        'west': Attic.west,
        'east': Attic.east,
        'south': Attic.south,
        'up': Attic.up,
        'down': Attic.down,
        'status': Attic.status,
        'restart': Attic.restart,
        'inventory': Attic.inventory
        }

        a = Attic()

        while complete == False:
            line = raw_input("> ")
            args = line.split()
            if len(args) == 0:
                print("What you want to do?\n")

            elif len(args) > 0:
                commandFound = False
                for c in commands.keys():
                    if args[0] == c[:len(args[0])]:
                        commands[c](a)
                        commandFound = True
                        break

                if args[0] == "take":
                    try:
                        if "item" in itens[currentRoom] and args[1] in itens[currentRoom]["item"]:
                            inventory.append(args[1])
                            moves += 1
                            print(args[1]+":" + " Taken.\n")
                            del itens[currentRoom]["item"]

                        elif "item2" in itens[currentRoom] and args[1] in itens[currentRoom]["item2"]:
                            inventory.append(args[1])
                            moves += 1
                            print(args[1]+":" + " Taken.\n")
                            del itens[currentRoom]["item2"]

                        else:
                            print("Can't get this.\n")

                    except:
                        print("Invalid.\n")

                if args[0] == "drop":
                    try:
                        if args[1] in inventory:
                            inventory.remove(args[1])
                            moves += 1
                            print(args[1]+":" + " Dropped.\n")

                        else:
                            print("Can't drop this.\n")

                    except:
                      print("Invalid.\n")

                if args[0] == "turn":
                    try:
                        if args[1] == 'lantern':
                            if 'lantern' in inventory:
                                global lantern_on
                                if args[2] == 'on':
                                    lantern_on = True
                                    moves += 1
                                    print("The lantern is now on.\n")

                                elif args[2] == 'off':
                                    lantern_on = False
                                    moves += 1
                                    print("The lantern is now off.\n")
                            else:
                                print("You don't have a lantern.\n")
                    except:
                        print("Invalid.\n")

                if args[0] == "say":
                    try:
                        if args[1] != None:
                            moves += 1
                            print("You say:" + " " + args[1])
                            print("")
                        else:
                            pass
                    except:
                        print("Say what?\n")

                if args[0] == 'read':
                    try:
                        if args[1] == 'paper':
                            if 'paper' in inventory:
                                global paper
                                moves += 1
                                print(paper)
                            else:
                                pass

                        elif args[1] == 'note':
                            if 'note' in inventory:
                                global note
                                moves += 1
                                print(note)
                            else:
                                pass

                        elif args[1] == 'post-it':
                            if 'post-it' in inventory:
                                global post
                                moves += 1
                                print(post)
                            else:
                                pass

                        elif args[1] == 'poster':
                            if 'poster' in inventory:
                                global poster
                                moves += 1
                                print(poster)
                            else:
                                pass

                        else:
                            pass

                    except:
                        print("Read what?\n")

                if args[0] == 'look':
                    global key_desc
                    global sword_desc
                    global knife_desc
                    global ruby_desc
                    global amulet_desc
                    try:
                        if args[1] == 'at':
                            try:
                                if args[2] in inventory:
                                    if args[2] == 'key':
                                        print(key_desc)

                                    elif args[2] == 'sword':
                                        print(sword_desc)

                                    elif args[2] == 'knife':
                                        print(knife_desc)

                                    elif args[2] == 'ruby':
                                        print(ruby_desc)

                                    elif args[2] == 'amulet':
                                        print(amulet_desc)

                                    else:
                                        print("I see nothing special about this.\n")

                                else:
                                    print("You don't have this item.\n")

                            except:
                                print("Look at what?\n")

                    except:
                        print("Look at what?\n")

    def up(self):
        global moves
        moves += 1
        print("You can't go that way.\n")

    def down(self):
        global moves
        moves += 1
        complete = True
        h = House()
        h.inicio()

    def north(self):
        global moves
        moves += 1
        print("Have a window here.")
        print("You see the Forest Path through the window.\n")

    def east(self):
        global moves
        moves += 1
        print("Some boxes.\n")

    def south(self):
        global moves
        moves += 1
        print("Have a window here.")
        print("You see a crescent moon in the sky through the window.\n")

    def west(self):
        global moves
        moves += 1
        print("A bed, a mirror and a clock.\n")

class CanyonBottom:
    def __init__(self):
        self.state = 'canyonbottom'

    def quit(self):
        c = character()
        c.quit()

    def status(self):
        c = character()
        c.status()

    def ajuda(self):
        c = character()
        c.ajuda()

    def restart(self):
        c = character()
        c.restart()

    def score(self):
        c = character()
        c.score()

    def save(self):
        save()

    def achievement(self):
        c = character()
        c.achievement()

    def inventory(self):
        if len(inventory) > 0:
            print("You have:")
            print inventory
            print("")
        else:
            print("Your inventory is empty.\n")

    def inicio(self):
        complete = False
        global moves, local
        local = 'CanyonBottom'
        print("Canyon Bottom")
        print("You are beneath the walls of the river canyon.\n")

        itens = {
        1: {}
        }

        currentRoom = 1

        commands = {
        'help': CanyonBottom.ajuda,
        'quit': CanyonBottom.quit,
        'save': CanyonBottom.save,
        'score': CanyonBottom.score,
        'achievement': CanyonBottom.achievement,
        'north': CanyonBottom.north,
        'west': CanyonBottom.west,
        'east': CanyonBottom.east,
        'south': CanyonBottom.south,
        'up': CanyonBottom.up,
        'down': CanyonBottom.down,
        'status': CanyonBottom.status,
        'restart': CanyonBottom.restart,
        'inventory': CanyonBottom.inventory
        }

        cb = CanyonBottom()

        while complete == False:
            line = raw_input("> ")
            args = line.split()
            if len(args) == 0:
                print("What you want to do?\n")

            elif len(args) > 0:
                commandFound = False
                for c in commands.keys():
                    if args[0] == c[:len(args[0])]:
                        commands[c](cb)
                        commandFound = True
                        break

                if args[0] == "take":
                    try:
                        if "item" in itens[currentRoom] and args[1] in itens[currentRoom]["item"]:
                            inventory.append(args[1])
                            moves += 1
                            print(args[1]+":" + " Taken.\n")
                            del itens[currentRoom]["item"]
                        else:
                            print("Can't get this.\n")

                    except:
                        print("Invalid.\n")

                if args[0] == "drop":
                    try:
                        if args[1] in inventory:
                            inventory.remove(args[1])
                            moves += 1
                            print(args[1]+":" + " Dropped.\n")

                        else:
                            print("Can't drop this.\n")

                    except:
                      print("Invalid.\n")

                if args[0] == "eat":
                      try:
                           if args[1] in inventory and args[1] in can_eat:
                                 global health, health_max
                                 if args[1] == can_eat[0]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 5 > health_max:
                                             inventory.remove('bread')
                                             health = 75
                                             print("You eat the bread.\n")
                                       else:
                                             inventory.remove('bread')
                                             health += 5
                                             print("You eat the bread.\n")

                                 elif args[1] == can_eat[1]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 5 > health_max:
                                             inventory.remove('apple')
                                             health = 75
                                             print("You eat the apple.\n")
                                       else:
                                             inventory.remove('apple')
                                             health += 5
                                             print("You eat the apple.\n")

                                 elif args[1] == can_eat[2]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 3 > health_max:
                                             inventory.remove('carrot')
                                             health = 75
                                             print("You eat the carrot.\n")
                                       else:
                                             inventory.remove('carrot')
                                             health += 3
                                             print("You eat the carrot.\n")

                                 elif args[1] == can_eat[3]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 4 > health_max:
                                             inventory.remove('tomato')
                                             health = 75
                                             print("You eat the tomato.\n")
                                       else:
                                             inventory.remove('tomato')
                                             health += 4
                                             print("You eat the tomato.\n")

                                 elif args[1] == can_eat[4]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 4 > health_max:
                                             inventory.remove('potato')
                                             health = 75
                                             print("You eat the potato.\n")
                                       else:
                                             inventory.remove('potato')
                                             health += 4
                                             print("You eat the potato.\n")

                                 elif args[1] == can_eat[5]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 2 > health_max:
                                             inventory.remove('onion')
                                             health = 75
                                             print("You eat the onion.\n")
                                       else:
                                             inventory.remove('onion')
                                             health += 2
                                             print("You eat the onion.\n")

                                 else:
                                     print("You can't eat this.\n")
                           else:
                               print("You don't have this.\n")
                      except:
                            print("Eat what?\n")

                if args[0] == "turn":
                    try:
                        if args[1] == 'lantern':
                            if 'lantern' in inventory:
                                global lantern_on
                                if args[2] == 'on':
                                    lantern_on = True
                                    moves += 1
                                    print("The lantern is now on.\n")

                                elif args[2] == 'off':
                                    lantern_on = False
                                    moves += 1
                                    print("The lantern is now off.\n")
                            else:
                                print("You don't have a lantern.\n")
                    except:
                        print("Invalid.\n")

                if args[0] == "say":
                    try:
                        if args[1] != None:
                            moves += 1
                            print("You say:" + " " + args[1])
                            print("")
                        else:
                            pass
                    except:
                        print("Say what?\n")

                if args[0] == 'read':
                    try:
                        if args[1] == 'paper':
                            if 'paper' in inventory:
                                global paper
                                moves += 1
                                print(paper)
                            else:
                                pass

                        elif args[1] == 'note':
                            if 'note' in inventory:
                                global note
                                moves += 1
                                print(note)
                            else:
                                pass

                        elif args[1] == 'post-it':
                            if 'post-it' in inventory:
                                global post
                                moves += 1
                                print(post)
                            else:
                                pass

                        elif args[1] == 'poster':
                            if 'poster' in inventory:
                                global poster
                                moves += 1
                                print(poster)
                            else:
                                pass

                        else:
                            pass

                    except:
                        print("Read what?\n")

                if args[0] == 'look':
                    global key_desc
                    global sword_desc
                    global knife_desc
                    global ruby_desc
                    global amulet_desc
                    try:
                        if args[1] == 'at':
                            try:
                                if args[2] in inventory:
                                    if args[2] == 'key':
                                        print(key_desc)

                                    elif args[2] == 'sword':
                                        print(sword_desc)

                                    elif args[2] == 'knife':
                                        print(knife_desc)

                                    elif args[2] == 'ruby':
                                        print(ruby_desc)

                                    elif args[2] == 'amulet':
                                        print(amulet_desc)

                                    else:
                                        print("I see nothing special about this.\n")

                                else:
                                    print("You don't have this item.\n")

                            except:
                                print("Look at what?\n")

                    except:
                        print("Look at what?\n")

    def up(self):
        global moves
        moves += 1
        complete = True
        rl = RockyLedge()
        rl.inicio()

    def down(self):
        global moves
        moves += 1
        print("You can't go that way.\n")

    def north(self):
        global moves
        moves += 1
        print("Sand and stones.\n")

    def east(self):
        global moves
        moves += 1
        print("Some stones here.\n")

    def south(self):
        global moves
        moves += 1
        print("Some stones here.\n")

    def west(self):
        global moves
        moves += 1
        complete = True
        st = SmallStream()
        st.inicio()

class RockyLedge:
    def __init__(self):
        self.state = 'rockyledge'

    def quit(self):
        c = character()
        c.quit()

    def status(self):
        c = character()
        c.status()

    def ajuda(self):
        c = character()
        c.ajuda()

    def restart(self):
        c = character()
        c.restart()

    def score(self):
        c = character()
        c.score()

    def save(self):
        save()

    def achievement(self):
        c = character()
        c.achievement()

    def inventory(self):
        if len(inventory) > 0:
            print("You have:")
            print inventory
            print("")
        else:
            print("Your inventory is empty.\n")

    def inicio(self):
        complete = False
        global moves, local
        local = 'RockyLedge'
        print("Rocky Ledge")
        print("You are 15 feet above the ground. You are on a ledge about halfway up")
        print("the wall of the river canyon, from here you can see a house to west.\n")

        itens = {
        1: {}
        }
        currentRoom = 1

        commands = {
        'help': RockyLedge.ajuda,
        'quit': RockyLedge.quit,
        'save': RockyLedge.save,
        'score': RockyLedge.score,
        'achievement': RockyLedge.achievement,
        'north': RockyLedge.north,
        'west': RockyLedge.west,
        'east': RockyLedge.east,
        'south': RockyLedge.south,
        'up': RockyLedge.up,
        'down': RockyLedge.down,
        'status': RockyLedge.status,
        'restart': RockyLedge.restart,
        'inventory': RockyLedge.inventory
        }

        rl = RockyLedge()

        while complete == False:
            line = raw_input("> ")
            args = line.split()
            if len(args) == 0:
                print("What you want to do?\n")

            elif len(args) > 0:
                commandFound = False
                for c in commands.keys():
                    if args[0] == c[:len(args[0])]:
                        commands[c](rl)
                        commandFound = True
                        break

                if args[0] == "take":
                    try:
                        if "item" in itens[currentRoom] and args[1] in itens[currentRoom]["item"]:
                            inventory.append(args[1])
                            moves += 1
                            print(args[1]+":" + " Taken.\n")
                            del itens[currentRoom]["item"]
                        else:
                            print("Can't get this.\n")

                    except:
                        print("Invalid.\n")

                if args[0] == "drop":
                    try:
                        if args[1] in inventory:
                            inventory.remove(args[1])
                            moves += 1
                            print(args[1]+":" + " Dropped.\n")

                        else:
                            print("Can't drop this.\n")

                    except:
                      print("Invalid.\n")

                if args[0] == "eat":
                      try:
                           if args[1] in inventory and args[1] in can_eat:
                                 global health, health_max
                                 if args[1] == can_eat[0]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 5 > health_max:
                                             inventory.remove('bread')
                                             health = 75
                                             print("You eat the bread.\n")
                                       else:
                                             inventory.remove('bread')
                                             health += 5
                                             print("You eat the bread.\n")

                                 elif args[1] == can_eat[1]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 5 > health_max:
                                             inventory.remove('apple')
                                             health = 75
                                             print("You eat the apple.\n")
                                       else:
                                             inventory.remove('apple')
                                             health += 5
                                             print("You eat the apple.\n")

                                 elif args[1] == can_eat[2]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 3 > health_max:
                                             inventory.remove('carrot')
                                             health = 75
                                             print("You eat the carrot.\n")
                                       else:
                                             inventory.remove('carrot')
                                             health += 3
                                             print("You eat the carrot.\n")

                                 elif args[1] == can_eat[3]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 4 > health_max:
                                             inventory.remove('tomato')
                                             health = 75
                                             print("You eat the tomato.\n")
                                       else:
                                             inventory.remove('tomato')
                                             health += 4
                                             print("You eat the tomato.\n")

                                 elif args[1] == can_eat[4]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 4 > health_max:
                                             inventory.remove('potato')
                                             health = 75
                                             print("You eat the potato.\n")
                                       else:
                                             inventory.remove('potato')
                                             health += 4
                                             print("You eat the potato.\n")

                                 elif args[1] == can_eat[5]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 2 > health_max:
                                             inventory.remove('onion')
                                             health = 75
                                             print("You eat the onion.\n")
                                       else:
                                             inventory.remove('onion')
                                             health += 2
                                             print("You eat the onion.\n")

                                 else:
                                     print("You can't eat this.\n")
                           else:
                               print("You don't have this.\n")
                      except:
                            print("Eat what?\n")

                if args[0] == "turn":
                    try:
                        if args[1] == 'lantern':
                            if 'lantern' in inventory:
                                global lantern_on
                                if args[2] == 'on':
                                    lantern_on = True
                                    moves += 1
                                    print("The lantern is now on.\n")

                                elif args[2] == 'off':
                                    lantern_on = False
                                    moves += 1
                                    print("The lantern is now off.\n")
                            else:
                                print("You don't have a lantern.\n")
                    except:
                        print("Invalid.\n")

                if args[0] == "say":
                    try:
                        if args[1] != None:
                            moves += 1
                            print("You say:" + " " + args[1])
                            print("")
                        else:
                            pass
                    except:
                        print("Say what?\n")

                if args[0] == 'read':
                    try:
                        if args[1] == 'paper':
                            if 'paper' in inventory:
                                global paper
                                moves += 1
                                print(paper)
                            else:
                                pass

                        elif args[1] == 'note':
                            if 'note' in inventory:
                                global note
                                moves += 1
                                print(note)
                            else:
                                pass

                        elif args[1] == 'post-it':
                            if 'post-it' in inventory:
                                global post
                                moves += 1
                                print(post)
                            else:
                                pass

                        elif args[1] == 'poster':
                            if 'poster' in inventory:
                                global poster
                                moves += 1
                                print(poster)
                            else:
                                pass

                        else:
                            pass

                    except:
                        print("Read what?\n")

                if args[0] == 'look':
                    global key_desc
                    global sword_desc
                    global knife_desc
                    global ruby_desc
                    global amulet_desc
                    try:
                        if args[1] == 'at':
                            try:
                                if args[2] in inventory:
                                    if args[2] == 'key':
                                        print(key_desc)

                                    elif args[2] == 'sword':
                                        print(sword_desc)

                                    elif args[2] == 'knife':
                                        print(knife_desc)

                                    elif args[2] == 'ruby':
                                        print(ruby_desc)

                                    elif args[2] == 'amulet':
                                        print(amulet_desc)

                                    else:
                                        print("I see nothing special about this.\n")

                                else:
                                    print("You don't have this item.\n")

                            except:
                                print("Look at what?\n")

                    except:
                        print("Look at what?\n")

    def up(self):
        global moves
        moves += 1
        complete = True
        canyon = Canyon()
        canyon.inicio()

    def down(self):
        global moves
        moves += 1
        complete = True
        cb = CanyonBottom()
        cb.inicio()

    def north(self):
        global moves
        moves += 1
        pass

    def east(self):
        global moves
        moves += 1
        pass

    def south(self):
        global moves
        moves += 1
        pass

    def west(self):
        global moves
        moves += 1
        pass

class Canyon:
    def __init__(self):
        self.state = 'canyon'

    def quit(self):
        c = character()
        c.quit()

    def status(self):
        c = character()
        c.status()

    def ajuda(self):
        c = character()
        c.ajuda()

    def restart(self):
        c = character()
        c.restart()

    def score(self):
        c = character()
        c.score()

    def save(self):
        save()

    def achievement(self):
        c = character()
        c.achievement()

    def inventory(self):
        if len(inventory) > 0:
            print("You have:")
            print inventory
            print("")
        else:
            print("Your inventory is empty.\n")

    def inicio(self):
        complete = False
        global moves, local
        local == 'CanyonView'
        print("Canyon View")
        print("You are at the top of great canyon. From here there is")
        print("a awesome view of the canyon. It is possible to climb down")
        print("into the canyon from here.\n")

        itens = {
        1: {}
        }
        currentRoom = 1

        commands = {
        'help': Canyon.ajuda,
        'quit': Canyon.quit,
        'save': Canyon.save,
        'score': Canyon.score,
        'achievement': Canyon.achievement,
        'north': Canyon.north,
        'west': Canyon.west,
        'east': Canyon.east,
        'south': Canyon.south,
        'up': Canyon.up,
        'down': Canyon.down,
        'status': Canyon.status,
        'restart': Canyon.restart,
        'inventory': Canyon.inventory
        }

        canyon = Canyon()

        while complete == False:
            line = raw_input("> ")
            args = line.split()
            if len(args) == 0:
                print("What you want to do?\n")

            elif len(args) > 0:
                commandFound = False
                for c in commands.keys():
                    if args[0] == c[:len(args[0])]:
                        commands[c](canyon)
                        commandFound = True
                        break

                if args[0] == "take":
                    try:
                        if "item" in itens[currentRoom] and args[1] in itens[currentRoom]["item"]:
                            inventory.append(args[1])
                            moves += 1
                            print(args[1]+":" + " Taken.\n")
                            del itens[currentRoom]["item"]
                        else:
                            print("Can't get this.\n")

                    except:
                        print("Invalid.\n")

                if args[0] == "drop":
                    try:
                        if args[1] in inventory:
                            inventory.remove(args[1])
                            moves += 1
                            print(args[1]+":" + " Dropped.\n")

                        else:
                            print("Can't drop this.\n")
                    except:
                        print("Invalid.\n")

                if args[0] == "eat":
                      try:
                           if args[1] in inventory and args[1] in can_eat:
                                 global health, health_max
                                 if args[1] == can_eat[0]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 5 > health_max:
                                             inventory.remove('bread')
                                             health = 75
                                             print("You eat the bread.\n")
                                       else:
                                             inventory.remove('bread')
                                             health += 5
                                             print("You eat the bread.\n")

                                 elif args[1] == can_eat[1]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 5 > health_max:
                                             inventory.remove('apple')
                                             health = 75
                                             print("You eat the apple.\n")
                                       else:
                                             inventory.remove('apple')
                                             health += 5
                                             print("You eat the apple.\n")

                                 elif args[1] == can_eat[2]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 3 > health_max:
                                             inventory.remove('carrot')
                                             health = 75
                                             print("You eat the carrot.\n")
                                       else:
                                             inventory.remove('carrot')
                                             health += 3
                                             print("You eat the carrot.\n")

                                 elif args[1] == can_eat[3]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 4 > health_max:
                                             inventory.remove('tomato')
                                             health = 75
                                             print("You eat the tomato.\n")
                                       else:
                                             inventory.remove('tomato')
                                             health += 4
                                             print("You eat the tomato.\n")

                                 elif args[1] == can_eat[4]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 4 > health_max:
                                             inventory.remove('potato')
                                             health = 75
                                             print("You eat the potato.\n")
                                       else:
                                             inventory.remove('potato')
                                             health += 4
                                             print("You eat the potato.\n")

                                 elif args[1] == can_eat[5]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 2 > health_max:
                                             inventory.remove('onion')
                                             health = 75
                                             print("You eat the onion.\n")
                                       else:
                                             inventory.remove('onion')
                                             health += 2
                                             print("You eat the onion.\n")

                                 else:
                                     print("You can't eat this.\n")
                           else:
                               print("You don't have this.\n")
                      except:
                            print("Eat what?\n")

                if args[0] == "turn":
                    try:
                        if args[1] == 'lantern':
                            if 'lantern' in inventory:
                                global lantern_on
                                if args[2] == 'on':
                                    lantern_on = True
                                    moves += 1
                                    print("The lantern is now on.\n")

                                elif args[2] == 'off':
                                    lantern_on = False
                                    moves += 1
                                    print("The lantern is now off.\n")
                            else:
                                print("You don't have a lantern.\n")
                    except:
                        print("Invalid.\n")

                if args[0] == "say":
                    try:
                        if args[1] != None:
                            moves += 1
                            print("You say:" + " " + args[1])
                            print("")
                        else:
                            pass
                    except:
                        print("Say what?\n")

                if args[0] == 'read':
                    try:
                        if args[1] == 'paper':
                            if 'paper' in inventory:
                                global paper
                                moves += 1
                                print(paper)
                            else:
                                pass

                        elif args[1] == 'note':
                            if 'note' in inventory:
                                global note
                                moves += 1
                                print(note)
                            else:
                                pass

                        elif args[1] == 'post-it':
                            if 'post-it' in inventory:
                                global post
                                moves += 1
                                print(post)
                            else:
                                pass

                        elif args[1] == 'poster':
                            if 'poster' in inventory:
                                global poster
                                moves += 1
                                print(poster)
                            else:
                                pass

                        else:
                            pass

                    except:
                        print("Read what?\n")

                if args[0] == 'look':
                    global key_desc
                    global sword_desc
                    global knife_desc
                    global ruby_desc
                    global amulet_desc
                    try:
                        if args[1] == 'at':
                            try:
                                if args[2] in inventory:
                                    if args[2] == 'key':
                                        print(key_desc)

                                    elif args[2] == 'sword':
                                        print(sword_desc)

                                    elif args[2] == 'knife':
                                        print(knife_desc)

                                    elif args[2] == 'ruby':
                                        print(ruby_desc)

                                    elif args[2] == 'amulet':
                                        print(amulet_desc)

                                    else:
                                        print("I see nothing special about this.\n")

                                else:
                                    print("You don't have this item.\n")

                            except:
                                print("Look at what?\n")

                    except:
                        print("Look at what?\n")

    def up(self):
        global moves
        moves += 1
        print("You can't go that way.\n")

    def down(self):
        global moves
        moves += 1
        complete = True
        rl = RockyLedge()
        rl.inicio()

    def north(self):
        global moves
        moves += 1
        print("Nothing interesting here.\n")

    def east(self):
        global moves
        moves += 1
        print("Has a rocky ledge down.\n")

    def south(self):
        global moves
        moves += 1
        oh = OutHouse()
        oh.inicio()

    def west(self):
        global moves
        moves += 1
        print("Nothing interesting here.\n")

class Temple:
    def __init__(self):
        self.state = 'temple'

    def quit(self):
        c = character()
        c.quit()

    def status(self):
        c = character()
        c.status()

    def ajuda(self):
        c = character()
        c.ajuda()

    def restart(self):
        c = character()
        c.restart()

    def score(self):
        c = character()
        c.score()

    def save(self):
        save()

    def achievement(self):
        c = character()
        c.achievement()

    def inventory(self):
        if len(inventory) > 0:
            print("You have:")
            print inventory
            print("")
        else:
            print("Your inventory is empty.\n")

    def inicio(self):
        complete = False
        print("Temple")
        global moves, local
        global chest_open
        local = 'Temple'
        if chest_open == True and 'rope' in inventory:
            print("")

        elif chest_open == True and 'rope' not in inventory:
            print("Has a rope on the ground.\n")
            itens = {
            1: {"item": 'rope'}
            }
            currentRoom = 1

        elif chest_open == False and 'rope' in inventory:
            print("Has a chest here.\n")

        elif chest_open == False and 'rope' not in inventory:
            print("Has a chest here and has a rope on the ground.\n")
            itens = {
            1: {"item": 'rope'}
            }
            currentRoom = 1

        commands = {
        'help': Temple.ajuda,
        'quit': Temple.quit,
        'score': Temple.score,
        'save': Temple.save,
        'achievement': Temple.achievement,
        'north': Temple.north,
        'west': Temple.west,
        'east': Temple.east,
        'south': Temple.south,
        'up': Temple.up,
        'down': Temple.down,
        'status': Temple.status,
        'restart': Temple.restart,
        'inventory': Temple.inventory
        }

        te = Temple()

        while complete == False:
            line = raw_input("> ")
            args = line.split()
            if len(args) == 0:
                print("What you want to do?\n")

            elif len(args) > 0:
                commandFound = False
                for c in commands.keys():
                    if args[0] == c[:len(args[0])]:
                        commands[c](te)
                        commandFound = True
                        break

                if args[0] == "take":
                    try:
                        if "item" in itens[currentRoom] and args[1] in itens[currentRoom]["item"]:
                            inventory.append(args[1])
                            moves += 1
                            print(args[1]+":" + " Taken.\n")
                            del itens[currentRoom]["item"]
                        elif args[1] == 'chest':
                            print("Really?\n")
                        else:
                            print("Can't get this.\n")

                    except:
                        print("Invalid.\n")

                if args[0] == "drop":
                    try:
                        if args[1] in inventory:
                            inventory.remove(args[1])
                            moves += 1
                            print(args[1]+":" + " Dropped.\n")

                        else:
                            print("Can't drop this.\n")
                    except:
                        print("Invalid.\n")

                if args[0] == "eat":
                      try:
                           if args[1] in inventory and args[1] in can_eat:
                                 global health, health_max
                                 if args[1] == can_eat[0]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 5 > health_max:
                                             inventory.remove('bread')
                                             health = 75
                                             print("You eat the bread.\n")
                                       else:
                                             inventory.remove('bread')
                                             health += 5
                                             print("You eat the bread.\n")

                                 elif args[1] == can_eat[1]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 5 > health_max:
                                             inventory.remove('apple')
                                             health = 75
                                             print("You eat the apple.\n")
                                       else:
                                             inventory.remove('apple')
                                             health += 5
                                             print("You eat the apple.\n")

                                 elif args[1] == can_eat[2]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 3 > health_max:
                                             inventory.remove('carrot')
                                             health = 75
                                             print("You eat the carrot.\n")
                                       else:
                                             inventory.remove('carrot')
                                             health += 3
                                             print("You eat the carrot.\n")

                                 elif args[1] == can_eat[3]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 4 > health_max:
                                             inventory.remove('tomato')
                                             health = 75
                                             print("You eat the tomato.\n")
                                       else:
                                             inventory.remove('tomato')
                                             health += 4
                                             print("You eat the tomato.\n")

                                 elif args[1] == can_eat[4]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 4 > health_max:
                                             inventory.remove('potato')
                                             health = 75
                                             print("You eat the potato.\n")
                                       else:
                                             inventory.remove('potato')
                                             health += 4
                                             print("You eat the potato.\n")

                                 elif args[1] == can_eat[5]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 2 > health_max:
                                             inventory.remove('onion')
                                             health = 75
                                             print("You eat the onion.\n")
                                       else:
                                             inventory.remove('onion')
                                             health += 2
                                             print("You eat the onion.\n")

                                 else:
                                     print("You can't eat this.\n")
                           else:
                               print("You don't have this.\n")
                      except:
                            print("Eat what?\n")

                if args[0] == "turn":
                    try:
                        if args[1] == 'lantern':
                            if 'lantern' in inventory:
                                global lantern_on
                                if args[2] == 'on':
                                    lantern_on = True
                                    moves += 1
                                    print("The lantern is now on.\n")

                                elif args[2] == 'off':
                                    lantern_on = False
                                    moves += 1
                                    print("The lantern is now off.\n")
                            else:
                                print("You don't have a lantern.\n")
                    except:
                        print("Invalid.\n")

                if args[0] == "say":
                    try:
                        if args[1] != None:
                            moves += 1
                            print("You say:" + " " + args[1])
                            print("")
                        else:
                            pass
                    except:
                        print("Say what?\n")

                if args[0] == 'read':
                    try:
                        if args[1] == 'paper':
                            if 'paper' in inventory:
                                global paper
                                moves += 1
                                print(paper)
                            else:
                                pass

                        elif args[1] == 'note':
                            if 'note' in inventory:
                                global note
                                moves += 1
                                print(note)
                            else:
                                pass

                        elif args[1] == 'post-it':
                            if 'post-it' in inventory:
                                global post
                                moves += 1
                                print(post)
                            else:
                                pass

                        elif args[1] == 'poster':
                            if 'poster' in inventory:
                                global poster
                                moves += 1
                                print(poster)
                            else:
                                pass

                        else:
                            pass

                    except:
                        print("Read what?\n")

                if args[0] == 'open':
                    try:
                        if args[1] == 'chest':
                            if chest_open == True:
                                moves += 1
                                print("The chest is open.\n")

                            else:
                                print("You open the chest.")
                                chest_open = True
                                moves += 1
                                print("You found 5 coins inside the chest.\n")
                                global coins
                                coins += 5

                        else:
                            print("You can't open this.\n")

                    except:
                        print("Open what?\n")

                if args[0] == 'look':
                    global key_desc
                    global sword_desc
                    global knife_desc
                    global ruby_desc
                    global amulet_desc
                    try:
                        if args[1] == 'at':
                            try:
                                if args[2] in inventory:
                                    if args[2] == 'key':
                                        print(key_desc)

                                    elif args[2] == 'sword':
                                        print(sword_desc)

                                    elif args[2] == 'knife':
                                        print(knife_desc)

                                    elif args[2] == 'ruby':
                                        print(ruby_desc)

                                    elif args[2] == 'amulet':
                                        print(amulet_desc)

                                    else:
                                        print("I see nothing special about this.\n")

                                else:
                                    print("You don't have this item.\n")

                            except:
                                print("Look at what?\n")

                    except:
                        print("Look at what?\n")

    def up(self):
        global moves
        moves += 1
        if 'rope' in inventory:
            print("You use your rope to go up.\n")
            ot = OutTemple()
            ot.inicio()

        else:
            print("You can't go that way.\n")

    def down(self):
        global moves
        moves += 1
        print("You can't go that way.\n")

    def north(self):
        global moves
        moves += 1
        print("Pillars and ruins.\n")

    def east(self):
        global moves
        moves += 1
        print("Pillars and ruins.\n")

    def west(self):
        global moves
        moves += 1
        t = Tunnel()
        t.inicio()

    def south(self):
        global moves
        moves += 1
        print("Pillars and ruins.\n")

class Tunnel:
    def __init__(self):
        self.state = 'tunnel'

    def quit(self):
        c = character()
        c.quit()

    def status(self):
        c = character()
        c.status()

    def ajuda(self):
        c = character()
        c.ajuda()

    def restart(self):
        c = character()
        c.restart()

    def score(self):
        c = character()
        c.score()

    def save(self):
        save()

    def achievement(self):
        c = character()
        c.achievement()

    def inventory(self):
        if len(inventory) > 0:
            print("You have:")
            print inventory
            print("")
        else:
            print("Your inventory is empty.\n")

    def inicio(self):
        complete = False
        print("Tunnel")
        global moves, local
        global lantern_on
        local = 'Tunnel'
        if lantern_on == True:
            global lock
            if lock == False:
                lock = True
                global coins
                print("You found 5 coins.\n")
                coins += 5
            else:
                print("")
        else:
            print("")

        itens = {
        1: {}
        }

        currentRoom = 1

        commands = {
        'help': Tunnel.ajuda,
        'quit': Tunnel.quit,
        'save': Tunnel.save,
        'score': Tunnel.score,
        'achievement': Tunnel.achievement,
        'north': Tunnel.north,
        'west': Tunnel.west,
        'east': Tunnel.east,
        'south': Tunnel.south,
        'up': Tunnel.up,
        'down': Tunnel.down,
        'status': Tunnel.status,
        'restart': Tunnel.restart,
        'inventory': Tunnel.inventory
        }

        t = Tunnel()

        while complete == False:
            line = raw_input("> ")
            args = line.split()
            if len(args) == 0:
                print("What you want to do?\n")

            elif len(args) > 0:
                commandFound = False
                for c in commands.keys():
                    if args[0] == c[:len(args[0])]:
                        commands[c](t)
                        commandFound = True
                        break

                if args[0] == "take":
                    try:
                        if "item" in itens[currentRoom] and args[1] in itens[currentRoom]["item"]:
                            inventory.append(args[1])
                            moves += 1
                            print(args[1]+":" + " Taken.\n")
                            del itens[currentRoom]["item"]
                        else:
                            print("Can't get this.\n")

                    except:
                        print("Invalid.\n")

                if args[0] == "drop":
                    try:
                        if args[1] in inventory:
                            inventory.remove(args[1])
                            moves += 1
                            print(args[1]+":" + " Dropped.\n")

                        else:
                            print("Can't drop this.\n")
                    except:
                        print("Invalid.\n")

                if args[0] == "open":
                      moves += 1
                      print("Nothing to open here.\n")

                if args[0] == "close":
                      moves += 1
                      print("Nothing to close here.\n")

                if args[0] == "eat":
                      try:
                           if args[1] in inventory and args[1] in can_eat:
                                 global health, health_max
                                 if args[1] == can_eat[0]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 5 > health_max:
                                             inventory.remove('bread')
                                             health = 75
                                             print("You eat the bread.\n")
                                       else:
                                             inventory.remove('bread')
                                             health += 5
                                             print("You eat the bread.\n")

                                 elif args[1] == can_eat[1]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 5 > health_max:
                                             inventory.remove('apple')
                                             health = 75
                                             print("You eat the apple.\n")
                                       else:
                                             inventory.remove('apple')
                                             health += 5
                                             print("You eat the apple.\n")

                                 elif args[1] == can_eat[2]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 3 > health_max:
                                             inventory.remove('carrot')
                                             health = 75
                                             print("You eat the carrot.\n")
                                       else:
                                             inventory.remove('carrot')
                                             health += 3
                                             print("You eat the carrot.\n")

                                 elif args[1] == can_eat[3]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 4 > health_max:
                                             inventory.remove('tomato')
                                             health = 75
                                             print("You eat the tomato.\n")
                                       else:
                                             inventory.remove('tomato')
                                             health += 4
                                             print("You eat the tomato.\n")

                                 elif args[1] == can_eat[4]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 4 > health_max:
                                             inventory.remove('potato')
                                             health = 75
                                             print("You eat the potato.\n")
                                       else:
                                             inventory.remove('potato')
                                             health += 4
                                             print("You eat the potato.\n")

                                 elif args[1] == can_eat[5]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 2 > health_max:
                                             inventory.remove('onion')
                                             health = 75
                                             print("You eat the onion.\n")
                                       else:
                                             inventory.remove('onion')
                                             health += 2
                                             print("You eat the onion.\n")

                                 else:
                                     print("You can't eat this.\n")
                           else:
                               print("You don't have this.\n")
                      except:
                            print("Eat what?\n")

                if args[0] == "turn":
                    try:
                        if args[1] == 'lantern':
                            if 'lantern' in inventory:
                                if args[2] == 'on':
                                    lantern_on = True
                                    moves += 1
                                    print("The lantern is now on.\n")

                                elif args[2] == 'off':
                                    lantern_on = False
                                    moves += 1
                                    print("The lantern is now off.\n")
                            else:
                                print("You don't have a lantern.\n")
                    except:
                        print("Invalid.\n")

                if args[0] == "say":
                    try:
                        if args[1] != None:
                            moves += 1
                            print("You say:" + " " + args[1])
                            print("")
                        else:
                            pass
                    except:
                        print("Say what?\n")

                if args[0] == 'read':
                    try:
                        if args[1] == 'paper':
                            if 'paper' in inventory:
                                global paper
                                moves += 1
                                print(paper)
                            else:
                                pass

                        elif args[1] == 'note':
                            if 'note' in inventory:
                                global note
                                moves += 1
                                print(note)
                            else:
                                pass

                        elif args[1] == 'post-it':
                            if 'post-it' in inventory:
                                global post
                                moves += 1
                                print(post)
                            else:
                                pass

                        elif args[1] == 'poster':
                            if 'poster' in inventory:
                                global poster
                                moves += 1
                                print(poster)
                            else:
                                pass

                        else:
                            pass

                    except:
                        print("Read what?\n")

                if args[0] == 'look':
                    global key_desc
                    global sword_desc
                    global knife_desc
                    global ruby_desc
                    global amulet_desc
                    try:
                        if args[1] == 'at':
                            try:
                                if args[2] in inventory:
                                    if args[2] == 'key':
                                        print(key_desc)

                                    elif args[2] == 'sword':
                                        print(sword_desc)

                                    elif args[2] == 'knife':
                                        print(knife_desc)

                                    elif args[2] == 'ruby':
                                        print(ruby_desc)

                                    elif args[2] == 'amulet':
                                        print(amulet_desc)

                                    else:
                                        print("I see nothing special about this.\n")

                                else:
                                    print("You don't have this item.\n")

                            except:
                                print("Look at what?\n")

                    except:
                        print("Look at what?\n")

    def north(self):
        global moves
        moves += 1
        print("Nothing here.\n")

    def east(self):
        global moves
        moves += 1
        complete = True
        te = Temple()
        te.inicio()

    def south(self):
        global moves
        moves += 1
        print("Nothing here.\n")

    def west(self):
        global moves
        moves += 1
        tp = TrapDoor()
        tp.inicio()

    def up(self):
        global moves
        moves += 1
        print("You can't go that way.\n")

    def down(self):
        global moves
        moves += 1
        print("You can't go that way.\n")

class OutHouse:
    def __init__(self):
        self.state = 'outhouse'

    def quit(self):
        c = character()
        c.quit()

    def status(self):
        c = character()
        c.status()

    def ajuda(self):
        c = character()
        c.ajuda()

    def restart(self):
        c = character()
        c.restart()

    def score(self):
        c = character()
        c.score()

    def save(self):
        save()

    def achievement(self):
        c = character()
        c.achievement()

    def inventory(self):
        if len(inventory) > 0:
            print("You have:")
            print inventory
            print("")
        else:
            print("Your inventory is empty.\n")

    def inicio(self):
        complete = False
        global moves, local
        local = 'OutHouse'
        print("Outside")
        print("Now you're outside the house.")
        if 'amulet' in inventory:
            print("")
            itens = {
            1 : {}
            }
            currentRoom = 1

        elif 'ruby' in inventory:
            print("")
            itens = {
            1 : {}
            }
            currentRoom = 1

        else:
            print("There's something shining on the ground, there's a ruby ​​here.\n")
            itens = {
            1 : {"item": 'ruby'}
            }
            currentRoom = 1

        commands = {
        'help': OutHouse.ajuda,
        'quit': OutHouse.quit,
        'save': OutHouse.save,
        'score': OutHouse.score,
        'achievement': OutHouse.achievement,
        'north': OutHouse.north,
        'west': OutHouse.west,
        'east': OutHouse.east,
        'south': OutHouse.south,
        'up': OutHouse.up,
        'down': OutHouse.down,
        'status': OutHouse.status,
        'restart': OutHouse.restart,
        'inventory': OutHouse.inventory
        }

        itens = {
        1 : {"item": 'ruby'}
        }
        currentRoom = 1

        oh = OutHouse()

        while complete == False:
            line = raw_input("> ")
            args = line.split()
            if len(args) == 0:
                print("What you want to do?\n")

            elif len(args) > 0:
                commandFound = False
                for c in commands.keys():
                    if args[0] == c[:len(args[0])]:
                        commands[c](oh)
                        commandFound = True
                        break

                if args[0] == "take":
                    try:
                        if "item" in itens[currentRoom] and args[1] in itens[currentRoom]["item"]:
                            inventory.append(args[1])
                            moves += 1
                            print(args[1]+":" + " Taken.\n")
                            del itens[currentRoom]["item"]
                        else:
                            print("Can't get this.\n")

                    except:
                        print("Invalid.\n")

                if args[0] == "drop":
                    try:
                        if args[1] in inventory:
                            inventory.remove(args[1])
                            moves += 1
                            print(args[1]+":" + " Dropped.\n")

                        else:
                            print("Can't drop this.\n")
                    except:
                        print("Invalid.\n")

                if args[0] == "eat":
                      try:
                           if args[1] in inventory and args[1] in can_eat:
                                 global health, health_max
                                 if args[1] == can_eat[0]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 5 > health_max:
                                             inventory.remove('bread')
                                             health = 75
                                             print("You eat the bread.\n")
                                       else:
                                             inventory.remove('bread')
                                             health += 5
                                             print("You eat the bread.\n")

                                 elif args[1] == can_eat[1]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 5 > health_max:
                                             inventory.remove('apple')
                                             health = 75
                                             print("You eat the apple.\n")
                                       else:
                                             inventory.remove('apple')
                                             health += 5
                                             print("You eat the apple.\n")

                                 elif args[1] == can_eat[2]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 3 > health_max:
                                             inventory.remove('carrot')
                                             health = 75
                                             print("You eat the carrot.\n")
                                       else:
                                             inventory.remove('carrot')
                                             health += 3
                                             print("You eat the carrot.\n")

                                 elif args[1] == can_eat[3]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 4 > health_max:
                                             inventory.remove('tomato')
                                             health = 75
                                             print("You eat the tomato.\n")
                                       else:
                                             inventory.remove('tomato')
                                             health += 4
                                             print("You eat the tomato.\n")

                                 elif args[1] == can_eat[4]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 4 > health_max:
                                             inventory.remove('potato')
                                             health = 75
                                             print("You eat the potato.\n")
                                       else:
                                             inventory.remove('potato')
                                             health += 4
                                             print("You eat the potato.\n")

                                 elif args[1] == can_eat[5]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 2 > health_max:
                                             inventory.remove('onion')
                                             health = 75
                                             print("You eat the onion.\n")
                                       else:
                                             inventory.remove('onion')
                                             health += 2
                                             print("You eat the onion.\n")

                                 else:
                                     print("You can't eat this.\n")
                           else:
                               print("You don't have this.\n")
                      except:
                            print("Eat what?\n")

                if args[0] == "turn":
                    try:
                        if args[1] == 'lantern':
                            if 'lantern' in inventory:
                                global lantern_on
                                if args[2] == 'on':
                                    lantern_on = True
                                    moves += 1
                                    print("The lantern is now on.\n")

                                elif args[2] == 'off':
                                    lantern_on = False
                                    moves += 1
                                    print("The lantern is now off.\n")
                            else:
                                print("You don't have a lantern.\n")
                    except:
                        print("Invalid.\n")

                if args[0] == "say":
                    try:
                        if args[1] != None:
                            moves += 1
                            print("You say:" + " " + args[1])
                            print("")
                        else:
                            pass
                    except:
                        print("Say what?\n")

                if args[0] == 'read':
                    try:
                        if args[1] == 'paper':
                            if 'paper' in inventory:
                                global paper
                                moves += 1
                                print(paper)
                            else:
                                pass

                        elif args[1] == 'note':
                            if 'note' in inventory:
                                global note
                                moves += 1
                                print(note)
                            else:
                                pass

                        elif args[1] == 'post-it':
                            if 'post-it' in inventory:
                                global post
                                moves += 1
                                print(post)
                            else:
                                pass

                        elif args[1] == 'poster':
                            if 'poster' in inventory:
                                global poster
                                moves += 1
                                print(poster)
                            else:
                                pass

                        else:
                            pass

                    except:
                        print("Read what?\n")

                if args[0] == 'look':
                    global key_desc
                    global sword_desc
                    global knife_desc
                    global ruby_desc
                    global amulet_desc
                    try:
                        if args[1] == 'at':
                            try:
                                if args[2] in inventory:
                                    if args[2] == 'key':
                                        print(key_desc)

                                    elif args[2] == 'sword':
                                        print(sword_desc)

                                    elif args[2] == 'knife':
                                        print(knife_desc)

                                    elif args[2] == 'ruby':
                                        print(ruby_desc)

                                    elif args[2] == 'amulet':
                                        print(amulet_desc)

                                    else:
                                        print("I see nothing special about this.\n")

                                else:
                                    print("You don't have this item.\n")

                            except:
                                print("Look at what?\n")

                    except:
                        print("Look at what?\n")

    def down(self):
        global moves
        moves += 1
        print("You can't go that way.\n")

    def up(self):
        global moves
        moves += 1
        print("You can't go that way.\n")

    def north(self):
        global moves
        moves += 1
        complete = True
        canyon = Canyon()
        canyon.inicio()

    def east(self):
        global moves
        moves += 1
        print("Nothing here.\n")

    def west(self):
        global moves
        moves += 1
        complete = True
        wh = WhiteHouse()
        wh.inicio()

    def south(self):
        global moves
        moves += 1
        ot = OutTemple()
        ot.inicio()

class SecondFloor:
    def __init__(self):
        self.state = 'secondfloor'

    def quit(self):
        c = character()
        c.quit()

    def status(self):
        c = character()
        c.status()

    def ajuda(self):
        c = character()
        c.ajuda()

    def restart(self):
        c = character()
        c.restart()

    def score(self):
        c = character()
        c.score()

    def save(self):
        save()

    def achievement(self):
        c = character()
        c.achievement()

    def inventory(self):
        if len(inventory) > 0:
            print("You have:")
            print inventory
            print("")
        else:
            print("Your inventory is empty.\n")

    def inicio(self):
        complete = False
        global moves, local
        local = 'SecondFloor'
        print("Second floor")
        if 'note' in inventory:
            print("")
            itens = {
            1: {}
            }
            currentRoom = 1
        else:
            print("There is a note here.\n")
            itens = {
            1: {"item": 'note'}
            }
            currentRoom = 1

        commands = {
        'help': SecondFloor.ajuda,
        'quit': SecondFloor.quit,
        'save': SecondFloor.save,
        'score': SecondFloor.score,
        'achievement': SecondFloor.achievement,
        'north': SecondFloor.north,
        'west': SecondFloor.west,
        'east': SecondFloor.east,
        'south': SecondFloor.south,
        'up': SecondFloor.up,
        'down': SecondFloor.down,
        'status': SecondFloor.status,
        'restart': SecondFloor.restart,
        'inventory': SecondFloor.inventory
        }

        sf = SecondFloor()

        while complete == False:
            line = raw_input("> ")
            args = line.split()
            if len(args) == 0:
                print("What you want to do?\n")

            elif len(args) > 0:
                commandFound = False
                for c in commands.keys():
                    if args[0] == c[:len(args[0])]:
                        commands[c](sf)
                        commandFound = True
                        break

                if args[0] == "take":
                    try:
                        if "item" in itens[currentRoom] and args[1] in itens[currentRoom]["item"]:
                            inventory.append(args[1])
                            moves += 1
                            print(args[1]+":" + " Taken.\n")
                            del itens[currentRoom]["item"]
                        else:
                            print("Can't get this.\n")

                    except:
                        print("Invalid.\n")

                if args[0] == "drop":
                    try:
                        if args[1] in inventory:
                            inventory.remove(args[1])
                            moves += 1
                            print(args[1]+":" + " Dropped.\n")

                        else:
                            print("Can't drop this.\n")
                    except:
                        print("Invalid.\n")

                if args[0] == "eat":
                      try:
                           if args[1] in inventory and args[1] in can_eat:
                                 global health, health_max
                                 if args[1] == can_eat[0]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 5 > health_max:
                                             inventory.remove('bread')
                                             health = 75
                                             print("You eat the bread.\n")
                                       else:
                                             inventory.remove('bread')
                                             health += 5
                                             print("You eat the bread.\n")

                                 elif args[1] == can_eat[1]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 5 > health_max:
                                             inventory.remove('apple')
                                             health = 75
                                             print("You eat the apple.\n")
                                       else:
                                             inventory.remove('apple')
                                             health += 5
                                             print("You eat the apple.\n")

                                 elif args[1] == can_eat[2]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 3 > health_max:
                                             inventory.remove('carrot')
                                             health = 75
                                             print("You eat the carrot.\n")
                                       else:
                                             inventory.remove('carrot')
                                             health += 3
                                             print("You eat the carrot.\n")

                                 elif args[1] == can_eat[3]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 4 > health_max:
                                             inventory.remove('tomato')
                                             health = 75
                                             print("You eat the tomato.\n")
                                       else:
                                             inventory.remove('tomato')
                                             health += 4
                                             print("You eat the tomato.\n")

                                 elif args[1] == can_eat[4]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 4 > health_max:
                                             inventory.remove('potato')
                                             health = 75
                                             print("You eat the potato.\n")
                                       else:
                                             inventory.remove('potato')
                                             health += 4
                                             print("You eat the potato.\n")

                                 elif args[1] == can_eat[5]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 2 > health_max:
                                             inventory.remove('onion')
                                             health = 75
                                             print("You eat the onion.\n")
                                       else:
                                             inventory.remove('onion')
                                             health += 2
                                             print("You eat the onion.\n")

                                 else:
                                     print("You can't eat this.\n")
                           else:
                               print("You don't have this.\n")
                      except:
                            print("Eat what?\n")

                if args[0] == "turn":
                    try:
                        if args[1] == 'lantern':
                            if 'lantern' in inventory:
                                global lantern_on
                                if args[2] == 'on':
                                    moves += 1
                                    lantern_on = True
                                    print("The lantern is now on.\n")

                                elif args[2] == 'off':
                                    moves += 1
                                    lantern_on = False
                                    print("The lantern is now off.\n")
                            else:
                                print("You don't have a lantern.\n")
                    except:
                        print("Invalid.\n")

                if args[0] == "say":
                    try:
                        if args[1] != None:
                            moves += 1
                            print("You say:" + " " + args[1])
                            print("")
                        else:
                            pass
                    except:
                        print("Say what?\n")

                if args[0] == 'read':
                    try:
                        if args[1] == 'paper':
                            if 'paper' in inventory:
                                global paper
                                moves += 1
                                print(paper)
                            else:
                                pass

                        elif args[1] == 'note':
                            if 'note' in inventory:
                                global note
                                moves += 1
                                print(note)
                            else:
                                pass

                        elif args[1] == 'post-it':
                            if 'post-it' in inventory:
                                global post
                                moves += 1
                                print(post)
                            else:
                                pass

                        elif args[1] == 'poster':
                            if 'poster' in inventory:
                                global poster
                                moves += 1
                                print(poster)
                            else:
                                pass

                        else:
                            pass

                    except:
                        print("Read what?\n")

                if args[0] == 'look':
                    global key_desc
                    global sword_desc
                    global knife_desc
                    global ruby_desc
                    global amulet_desc
                    try:
                        if args[1] == 'at':
                            try:
                                if args[2] in inventory:
                                    if args[2] == 'key':
                                        print(key_desc)

                                    elif args[2] == 'sword':
                                        print(sword_desc)

                                    elif args[2] == 'knife':
                                        print(knife_desc)

                                    elif args[2] == 'ruby':
                                        print(ruby_desc)

                                    elif args[2] == 'amulet':
                                        print(amulet_desc)

                                    else:
                                        print("I see nothing special about this.\n")

                                else:
                                    print("You don't have this item.\n")

                            except:
                                print("Look at what?\n")

                    except:
                        print("Look at what?\n")

    def up(self):
        global moves
        moves += 1
        print("You can't go that way.\n")

    def down(self):
        global moves
        moves += 1
        print("You down the stairs.\n")
        wh = WhiteHouse()
        wh.inicio()

    def north(self):
        global moves
        moves += 1
        print("Balcony")
        print("A beautiful sight, a vase of flowers on your left")
        print("a balcony table on your right with glasses and dishes")
        print("you look up and see a crescent moon.\n")

    def west(self):
        global moves
        moves += 1
        if 'key' in inventory:
            ir = InRoom()
            ir.inicio()
        else:
            print("Have a door here but is locked.\n")

    def east(self):
        global moves
        moves += 1
        print("Bathroom")
        print("A shower, a toilet and sink and a mirror.\n")

    def south(self):
        global moves
        moves += 1
        print("Nothing interesting here.\n")

class InRoom:
    def __init__(self):
        self.state = 'inroom'

    def quit(self):
        c = character()
        c.quit()

    def status(self):
        c = character()
        c.status()

    def ajuda(self):
        c = character()
        c.ajuda()

    def restart(self):
        c = character()
        c.restart()

    def score(self):
        c = character()
        c.score()

    def save(self):
        save()

    def achievement(self):
        c = character()
        c.achievement()

    def inventory(self):
        if len(inventory) > 0:
            print("You have:")
            print inventory
            print("")
        else:
            print("Your inventory is empty.\n")

    def inicio(self):
        complete = False
        global moves, local
        local = 'InRoom'
        print("Bedroom")
        if 'post-it' in inventory:
            print("You enter in the room.\n")
            itens = {
            1 : {}
            }
            currentRoom = 1

        else:
            print("You enter in the room. There is a post-it in the wall.\n")
            itens = {
            1 : {"item": 'post-it'}
            }
            currentRoom = 1

        commands = {
        'help': InRoom.ajuda,
        'quit': InRoom.quit,
        'save': InRoom.save,
        'north': InRoom.north,
        'score': InRoom.score,
        'achievement': InRoom.achievement,
        'west': InRoom.west,
        'east': InRoom.east,
        'south': InRoom.south,
        'up': InRoom.up,
        'down': InRoom.down,
        'status': InRoom.status,
        'restart': InRoom.inventory,
        'inventory': InRoom.inventory
        }

        ir = InRoom()

        while complete == False:
            line = raw_input("> ")
            args = line.split()
            if len(args) == 0:
                print("What you want to do?\n")

            elif len(args) > 0:
                commandFound = False
                for c in commands.keys():
                    if args[0] == c[:len(args[0])]:
                        commands[c](ir)
                        commandFound = True
                        break

                if args[0] == "take":
                    try:
                        if "item" in itens[currentRoom] and args[1] in itens[currentRoom]["item"]:
                            inventory.append(args[1])
                            moves += 1
                            print(args[1]+":" + " Taken.\n")
                            del itens[currentRoom]["item"]
                        else:
                            print("Can't get this.\n")

                    except:
                        print("Invalid.\n")

                if args[0] == "drop":
                    try:
                        if args[1] in inventory:
                            inventory.remove(args[1])
                            moves += 1
                            print(args[1]+":" + " Dropped.\n")

                        else:
                            print("Can't drop this.\n")
                    except:
                        print("Invalid.\n")

                if args[0] == "eat":
                      try:
                           if args[1] in inventory and args[1] in can_eat:
                                 global health, health_max
                                 if args[1] == can_eat[0]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 5 > health_max:
                                             inventory.remove('bread')
                                             health = 75
                                             print("You eat the bread.\n")
                                       else:
                                             inventory.remove('bread')
                                             health += 5
                                             print("You eat the bread.\n")

                                 elif args[1] == can_eat[1]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 5 > health_max:
                                             inventory.remove('apple')
                                             health = 75
                                             print("You eat the apple.\n")
                                       else:
                                             inventory.remove('apple')
                                             health += 5
                                             print("You eat the apple.\n")

                                 elif args[1] == can_eat[2]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 3 > health_max:
                                             inventory.remove('carrot')
                                             health = 75
                                             print("You eat the carrot.\n")
                                       else:
                                             inventory.remove('carrot')
                                             health += 3
                                             print("You eat the carrot.\n")

                                 elif args[1] == can_eat[3]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 4 > health_max:
                                             inventory.remove('tomato')
                                             health = 75
                                             print("You eat the tomato.\n")
                                       else:
                                             inventory.remove('tomato')
                                             health += 4
                                             print("You eat the tomato.\n")

                                 elif args[1] == can_eat[4]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 4 > health_max:
                                             inventory.remove('potato')
                                             health = 75
                                             print("You eat the potato.\n")
                                       else:
                                             inventory.remove('potato')
                                             health += 4
                                             print("You eat the potato.\n")

                                 elif args[1] == can_eat[5]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 2 > health_max:
                                             inventory.remove('onion')
                                             health = 75
                                             print("You eat the onion.\n")
                                       else:
                                             inventory.remove('onion')
                                             health += 2
                                             print("You eat the onion.\n")

                                 else:
                                     print("You can't eat this.\n")
                           else:
                               print("You don't have this.\n")
                      except:
                            print("Eat what?\n")

                if args[0] == "turn":
                    try:
                        if args[1] == 'lantern':
                            if 'lantern' in inventory:
                                global lantern_on
                                if args[2] == 'on':
                                    moves += 1
                                    lantern_on = True
                                    print("The lantern is now on.\n")

                                elif args[2] == 'off':
                                    moves += 1
                                    lantern_on = False
                                    print("The lantern is now off.\n")
                            else:
                                print("You don't have a lantern.\n")
                    except:
                        print("Invalid.\n")

                if args[0] == "say":
                    try:
                        if args[1] != None:
                            moves += 1
                            print("You say:" + " " + args[1])
                            print("")
                        else:
                            pass
                    except:
                        print("Say what?\n")

                if args[0] == 'read':
                    try:
                        if args[1] == 'paper':
                            if 'paper' in inventory:
                                global paper
                                moves += 1
                                print(paper)
                            else:
                                pass

                        elif args[1] == 'note':
                            if 'note' in inventory:
                                global note
                                moves += 1
                                print(note)
                            else:
                                pass

                        elif args[1] == 'post-it':
                            if 'post-it' in inventory:
                                global post
                                moves += 1
                                print(post)
                            else:
                                pass

                        elif args[1] == 'poster':
                            if 'poster' in inventory:
                                global poster
                                moves += 1
                                print(poster)
                            else:
                                pass

                        else:
                            pass

                    except:
                        print("Read what?\n")

                if args[0] == 'look':
                    global key_desc
                    global sword_desc
                    global knife_desc
                    global ruby_desc
                    global amulet_desc
                    try:
                        if args[1] == 'at':
                            try:
                                if args[2] in inventory:
                                    if args[2] == 'key':
                                        print(key_desc)

                                    elif args[2] == 'sword':
                                        print(sword_desc)

                                    elif args[2] == 'knife':
                                        print(knife_desc)

                                    elif args[2] == 'ruby':
                                        print(ruby_desc)

                                    elif args[2] == 'amulet':
                                        print(amulet_desc)

                                    else:
                                        print("I see nothing special about this.\n")

                                else:
                                    print("You don't have this item.\n")

                            except:
                                print("Look at what?\n")

                    except:
                        print("Look at what?\n")

    def up(self):
        global moves
        moves += 1
        print("You can't go that way.\n")

    def down(self):
        global moves
        moves += 1
        print("You can't go that way.\n")

    def north(self):
        global moves
        moves += 1
        print("You find a window, you look across it.")
        print("And you see a crescent moon.\n")

    def west(self):
        global moves
        moves += 1
        print("A bedroom, a tv and a video game.\n")

    def east(self):
        global moves
        moves += 1
        complete = True
        sf = SecondFloor()
        sf.inicio()

    def south(self):
        global moves
        moves += 1
        print("Posters in the wall.\n")

class WhiteHouse:
    def __init__(self):
        self.state = 'whiteouse'

    def quit(self):
        c = character()
        c.quit()

    def status(self):
        c = character()
        c.status()

    def ajuda(self):
        c = character()
        c.ajuda()

    def restart(self):
        c = character()
        c.restart()

    def score(self):
        c = character()
        c.score()

    def save(self):
        save()

    def achievement(self):
        c = character()
        c.achievement()

    def inventory(self):
        if len(inventory) > 0:
            print("You have:")
            print inventory
            print("")
        else:
            print("Your inventory is empty.\n")

    def inicio(self):
        up_ok = True
        down_ok = False
        complete = False
        global moves, local
        local = 'WhiteHouse'
        print("White House")
        print("The door is open and you enter in the white house.")
        print("Have stairs here.\n")

        commands = {
        'help': WhiteHouse.ajuda,
        'quit': WhiteHouse.quit,
        'save': WhiteHouse.save,
        'north': WhiteHouse.north,
        'score': WhiteHouse.score,
        'achievement': WhiteHouse.achievement,
        'west': WhiteHouse.west,
        'east': WhiteHouse.east,
        'south': WhiteHouse.south,
        'up': WhiteHouse.up,
        'down': WhiteHouse.down,
        'status': WhiteHouse.status,
        'restart': WhiteHouse.restart,
        'inventory': WhiteHouse.inventory
        }

        itens = {
        1: {}
        }
        currentRoom = 1

        wh = WhiteHouse()

        while complete == False:
            line = raw_input("> ")
            args = line.split()
            if len(args) == 0:
                print("What you want to do?\n")

            elif len(args) > 0:
                commandFound = False
                for c in commands.keys():
                    if args[0] == c[:len(args[0])]:
                        commands[c](wh)
                        commandFound = True
                        break

                if args[0] == "take":
                    try:
                        if "item" in itens[currentRoom] and args[1] in itens[currentRoom]["item"]:
                            inventory.append(args[1])
                            moves += 1
                            print(args[1]+":" + " Taken.\n")
                            del itens[currentRoom]["item"]
                        else:
                            print("Can't get this.\n")

                    except:
                        print("Invalid.\n")

                if args[0] == "drop":
                    try:
                        if args[1] in inventory:
                            inventory.remove(args[1])
                            moves += 1
                            print(args[1]+":" + " Dropped.\n")

                        else:
                            print("Can't drop this.\n")
                    except:
                        print("Invalid.\n")

                if args[0] == "eat":
                      try:
                           if args[1] in inventory and args[1] in can_eat:
                                 global health, health_max
                                 if args[1] == can_eat[0]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 5 > health_max:
                                             inventory.remove('bread')
                                             health = 75
                                             print("You eat the bread.\n")
                                       else:
                                             inventory.remove('bread')
                                             health += 5
                                             print("You eat the bread.\n")

                                 elif args[1] == can_eat[1]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 5 > health_max:
                                             inventory.remove('apple')
                                             health = 75
                                             print("You eat the apple.\n")
                                       else:
                                             inventory.remove('apple')
                                             health += 5
                                             print("You eat the apple.\n")

                                 elif args[1] == can_eat[2]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 3 > health_max:
                                             inventory.remove('carrot')
                                             health = 75
                                             print("You eat the carrot.\n")
                                       else:
                                             inventory.remove('carrot')
                                             health += 3
                                             print("You eat the carrot.\n")

                                 elif args[1] == can_eat[3]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 4 > health_max:
                                             inventory.remove('tomato')
                                             health = 75
                                             print("You eat the tomato.\n")
                                       else:
                                             inventory.remove('tomato')
                                             health += 4
                                             print("You eat the tomato.\n")

                                 elif args[1] == can_eat[4]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 4 > health_max:
                                             inventory.remove('potato')
                                             health = 75
                                             print("You eat the potato.\n")
                                       else:
                                             inventory.remove('potato')
                                             health += 4
                                             print("You eat the potato.\n")

                                 elif args[1] == can_eat[5]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 2 > health_max:
                                             inventory.remove('onion')
                                             health = 75
                                             print("You eat the onion.\n")
                                       else:
                                             inventory.remove('onion')
                                             health += 2
                                             print("You eat the onion.\n")

                                 else:
                                     print("You can't eat this.\n")
                           else:
                               print("You don't have this.\n")
                      except:
                            print("Eat what?\n")

                if args[0] == "turn":
                    try:
                        if args[1] == 'lantern':
                            if 'lantern' in inventory:
                                global lantern_on
                                if args[2] == 'on':
                                    moves += 1
                                    lantern_on = True
                                    print("The lantern is now on.\n")

                                elif args[2] == 'off':
                                    moves += 1
                                    lantern_on = False
                                    print("The lantern is now off.\n")
                            else:
                                print("You don't have a lantern.\n")
                    except:
                        print("Invalid.\n")

                if args[0] == "say":
                    try:
                        if args[1] != None:
                            moves += 1
                            print("You say:" + " " + args[1])
                            print("")
                        else:
                            pass
                    except:
                        print("Say what?\n")

                if args[0] == 'read':
                    try:
                        if args[1] == 'paper':
                            if 'paper' in inventory:
                                global paper
                                moves += 1
                                print(paper)
                            else:
                                pass

                        elif args[1] == 'note':
                            if 'note' in inventory:
                                global note
                                moves += 1
                                print(note)
                            else:
                                pass

                        elif args[1] == 'post-it':
                            if 'post-it' in inventory:
                                global post
                                moves += 1
                                print(post)
                            else:
                                pass

                        elif args[1] == 'poster':
                            if 'poster' in inventory:
                                global poster
                                moves += 1
                                print(poster)
                            else:
                                pass

                        else:
                            pass

                    except:
                        print("Read what?\n")

                if args[0] == 'look':
                    global key_desc
                    global sword_desc
                    global knife_desc
                    global ruby_desc
                    global amulet_desc
                    try:
                        if args[1] == 'at':
                            try:
                                if args[2] in inventory:
                                    if args[2] == 'key':
                                        print(key_desc)

                                    elif args[2] == 'sword':
                                        print(sword_desc)

                                    elif args[2] == 'knife':
                                        print(knife_desc)

                                    elif args[2] == 'ruby':
                                        print(ruby_desc)

                                    elif args[2] == 'amulet':
                                        print(amulet_desc)

                                    else:
                                        print("I see nothing special about this.\n")

                                else:
                                    print("You don't have this item.\n")

                            except:
                                print("Look at what?\n")

                    except:
                        print("Look at what?\n")

    def up(self):
        global moves
        moves += 1
        global up_ok
        global down_ok
        up_ok = False
        down_ok = True
        sf = SecondFloor()
        sf.inicio()

    def down(self):
        global moves
        moves += 1
        print("You can't go that way.\n")

    def north(self):
        global moves
        moves += 1
        print("Kitchen Room")
        print("Table, chairs, stove, cupboard, dishes and a sink.\n")

    def east(self):
        global moves
        moves += 1
        complete = True
        oh = OutHouse()
        oh.inicio()

    def west(self):
        global moves
        moves += 1
        complete = True
        f = Forest()
        f.inicio()

    def south(self):
        global moves
        moves += 1
        print("Living room")
        print("You are in the living room, white walls, white curtains,")
        print("a broken old tv here, a sofa, a armchair, a coffee table")
        print("and a plant on the coffee table.\n")

class Forest:
    def __init__(self):
        self.state = 'forest'

    def quit(self):
        c = character()
        c.quit()

    def status(self):
        c = character()
        c.status()

    def ajuda(self):
        c = character()
        c.ajuda()

    def restart(self):
        c = character()
        c.restart()

    def score(self):
        c = character()
        c.score()

    def save(self):
        save()

    def achievement(self):
        c = character()
        c.achievement()

    def inventory(self):
        if len(inventory) > 0:
            print("You have:")
            print inventory
            print("")
        else:
            print("Your inventory is empty.\n")

    def inicio(self):
        complete = False
        global moves
        global local
        local = 'Forest'
        print("Forest")
        print("You are in the forest, there are a lot trees around you.")
        print("Have some birds here, you look at the sky and see the stars.\n")

        commands = {
        'help': Forest.ajuda,
        'quit': Forest.quit,
        'save': Forest.save,
        'score': Forest.score,
        'achievement': Forest.achievement,
        'north': Forest.north,
        'west': Forest.west,
        'east': Forest.east,
        'south': Forest.south,
        'up': Forest.up,
        'down': Forest.down,
        'status': Forest.status,
        'restart': Forest.restart,
        'inventory': Forest.inventory
        }

        ft = Forest()

        itens = {
        1: {}
        }
        currentRoom = 1

        while complete == False:
            line = raw_input("> ")
            args = line.split()
            if len(args) == 0:
                print("What you want to do?\n")

            elif len(args) > 0:
                commandFound = False
                for c in commands.keys():
                    if args[0] == c[:len(args[0])]:
                        commands[c](ft)
                        commandFound = True
                        break

                if args[0] == "take":
                    try:
                        if "item" in itens[currentRoom] and args[1] in itens[currentRoom]["item"]:
                            inventory.append(args[1])
                            moves += 1
                            print(args[1]+":" + " Taken.\n")
                            del itens[currentRoom]["item"]
                        else:
                            print("Can't get this.\n")

                    except:
                        print("Invalid.\n")

                if args[0] == "drop":
                    try:
                        if args[1] in inventory:
                            inventory.remove(args[1])
                            moves += 1
                            print(args[1]+":" + " Dropped.\n")

                        else:
                            print("Can't drop this.\n")
                    except:
                        print("Invalid.\n")

                if args[0] == "eat":
                      try:
                           if args[1] in inventory and args[1] in can_eat:
                                 global health, health_max
                                 if args[1] == can_eat[0]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 5 > health_max:
                                             inventory.remove('bread')
                                             health = 75
                                             print("You eat the bread.\n")
                                       else:
                                             inventory.remove('bread')
                                             health += 5
                                             print("You eat the bread.\n")

                                 elif args[1] == can_eat[1]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 5 > health_max:
                                             inventory.remove('apple')
                                             health = 75
                                             print("You eat the apple.\n")
                                       else:
                                             inventory.remove('apple')
                                             health += 5
                                             print("You eat the apple.\n")

                                 elif args[1] == can_eat[2]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 3 > health_max:
                                             inventory.remove('carrot')
                                             health = 75
                                             print("You eat the carrot.\n")
                                       else:
                                             inventory.remove('carrot')
                                             health += 3
                                             print("You eat the carrot.\n")

                                 elif args[1] == can_eat[3]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 4 > health_max:
                                             inventory.remove('tomato')
                                             health = 75
                                             print("You eat the tomato.\n")
                                       else:
                                             inventory.remove('tomato')
                                             health += 4
                                             print("You eat the tomato.\n")

                                 elif args[1] == can_eat[4]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 4 > health_max:
                                             inventory.remove('potato')
                                             health = 75
                                             print("You eat the potato.\n")
                                       else:
                                             inventory.remove('potato')
                                             health += 4
                                             print("You eat the potato.\n")

                                 elif args[1] == can_eat[5]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 2 > health_max:
                                             inventory.remove('onion')
                                             health = 75
                                             print("You eat the onion.\n")
                                       else:
                                             inventory.remove('onion')
                                             health += 2
                                             print("You eat the onion.\n")

                                 else:
                                     print("You can't eat this.\n")
                           else:
                               print("You don't have this.\n")
                      except:
                            print("Eat what?\n")

                if args[0] == "turn":
                    try:
                        if args[1] == 'lantern':
                            if 'lantern' in inventory:
                                global lantern_on
                                if args[2] == 'on':
                                    lantern_on = True
                                    moves += 1
                                    print("The lantern is now on.\n")

                                elif args[2] == 'off':
                                    lantern_on = False
                                    moves += 1
                                    print("The lantern is now off.\n")
                            else:
                                print("You don't have a lantern.\n")
                    except:
                        print("Invalid.\n")

                if args[0] == "say":
                    try:
                        if args[1] != None:
                            moves += 1
                            print("You say:" + " " + args[1])
                            print("")

                        else:
                            pass
                    except:
                        print("Say what?\n")

                if args[0] == 'read':
                    try:
                        if args[1] == 'paper':
                            if 'paper' in inventory:
                                global paper
                                moves += 1
                                print(paper)
                            else:
                                pass

                        elif args[1] == 'note':
                            if 'note' in inventory:
                                global note
                                moves += 1
                                print(note)
                            else:
                                pass

                        elif args[1] == 'post-it':
                            if 'post-it' in inventory:
                                global post
                                moves += 1
                                print(post)
                            else:
                                pass

                        elif args[1] == 'poster':
                            if 'poster' in inventory:
                                global poster
                                moves += 1
                                print(poster)
                            else:
                                pass

                        else:
                            pass

                    except:
                        print("Read what?\n")

                if args[0] == 'look':
                    global key_desc
                    global sword_desc
                    global knife_desc
                    global ruby_desc
                    global amulet_desc
                    try:
                        if args[1] == 'at':
                            try:
                                if args[2] in inventory:
                                    if args[2] == 'key':
                                        print(key_desc)

                                    elif args[2] == 'sword':
                                        print(sword_desc)

                                    elif args[2] == 'knife':
                                        print(knife_desc)

                                    elif args[2] == 'ruby':
                                        print(ruby_desc)

                                    elif args[2] == 'amulet':
                                        print(amulet_desc)

                                    else:
                                        print("I see nothing special about this.\n")

                                else:
                                    print("You don't have this item.\n")

                            except:
                                print("Look at what?\n")

                    except:
                        print("Look at what?\n")

    def up(self):
        global moves
        moves += 1
        print("You can't go that way.\n")

    def down(self):
        global moves
        moves += 1
        print("You can't go that way.\n")

    def north(self):
        global moves
        moves += 1
        complete = True
        c = Clearing()
        c.inicio()

    def east(self):
        global moves
        moves += 1
        complete = True
        wh = WhiteHouse()
        wh.inicio()

    def south(self):
        global moves
        moves += 1
        print("You look to south and see the Forest Path.\n")
        complete = True
        fp = ForestPath()
        fp.inicio()

    def west(self):
        global moves
        moves += 1
        m = Mountain()
        m.inicio()

class ForestPath:
    def __init__(self):
        self.state = 'forestpath'

    def status(self):
        c = character()
        c.status()

    def quit(self):
        c = character()
        c.quit()

    def ajuda(self):
        c = character()
        c.ajuda()

    def restart(self):
        c = character()
        c.restart()

    def save(self):
        save()

    def score(self):
        c = character()
        c.score()

    def achievement(self):
        c = character()
        c.achievement()

    def inventory(self):
        if len(inventory) > 0:
            print("You have:")
            print inventory
            print("")
        else:
            print("Your inventory is empty.\n")

    def inicio(self):
        global local
        local = 'ForestPath'
        complete = False
        global moves
        global score
        global taken
        print("Forest Path")
        if 'paper' in inventory:
            print("Now you are on a forest path.")
            print("A lot of trees, some bushes and a little stream.")
            print("You hear the sound of the birds, it's amazing sound.\n")

            itens = {
            1: {}
            }
            currentRoom = 1

        else:
            print("Now you are on a forest path.")
            print("A lot of trees, some bushes and a little stream.")
            print("You hear the sound of the birds, it's amazing sound.")
            print("There is a paper here.\n")

            itens = {
            1: {"item": 'paper'}
            }
            currentRoom = 1

        commands = {
        'help': ForestPath.ajuda,
        'quit': ForestPath.quit,
        'save': ForestPath.save,
        'score': ForestPath.score,
        'achievement': ForestPath.achievement,
        'north': ForestPath.north,
        'west': ForestPath.west,
        'east': ForestPath.east,
        'south': ForestPath.south,
        'up': ForestPath.up,
        'down': ForestPath.down,
        'status': ForestPath.status,
        'restart': ForestPath.restart,
        'inventory': ForestPath.inventory
        }

        fp = ForestPath()

        while complete == False:
            line = raw_input("> ")
            args = line.split()
            if len(args) == 0:
                print("What you want to do?\n")

            elif len(args) > 0:
                commandFound = False
                for c in commands.keys():
                    if args[0] == c[:len(args[0])]:
                        commands[c](fp)
                        commandFound = True
                        break

                if args[0] == "take":
                    try:
                        if "item" in itens[currentRoom] and args[1] in itens[currentRoom]["item"]:
                            global moves
                            moves += 1
                            inventory.append(args[1])
                            print(args[1]+":" + " Taken.\n")
                            if taken == True:
                                pass
                            else:
                                taken = True
                                score += 5

                            del itens[currentRoom]["item"]
                        else:
                            print("Can't get this.\n")

                    except:
                        print("Invalid.\n")

                if args[0] == "drop":
                    try:
                        if args[1] in inventory:
                            moves += 1
                            inventory.remove(args[1])
                            print(args[1]+":" + " Dropped.\n")
                        else:
                            print("Can't drop this.\n")
                    except:
                        print("Invalid.\n")

                if args[0] == "eat":
                      try:
                           if args[1] in inventory and args[1] in can_eat:
                                 global health, health_max
                                 if args[1] == can_eat[0]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 5 > health_max:
                                             inventory.remove('bread')
                                             health = 75
                                             print("You eat the bread.\n")
                                       else:
                                             inventory.remove('bread')
                                             health += 5
                                             print("You eat the bread.\n")

                                 elif args[1] == can_eat[1]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 5 > health_max:
                                             inventory.remove('apple')
                                             health = 75
                                             print("You eat the apple.\n")
                                       else:
                                             inventory.remove('apple')
                                             health += 5
                                             print("You eat the apple.\n")

                                 elif args[1] == can_eat[2]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 3 > health_max:
                                             inventory.remove('carrot')
                                             health = 75
                                             print("You eat the carrot.\n")
                                       else:
                                             inventory.remove('carrot')
                                             health += 3
                                             print("You eat the carrot.\n")

                                 elif args[1] == can_eat[3]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 4 > health_max:
                                             inventory.remove('tomato')
                                             health = 75
                                             print("You eat the tomato.\n")
                                       else:
                                             inventory.remove('tomato')
                                             health += 4
                                             print("You eat the tomato.\n")

                                 elif args[1] == can_eat[4]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 4 > health_max:
                                             inventory.remove('potato')
                                             health = 75
                                             print("You eat the potato.\n")
                                       else:
                                             inventory.remove('potato')
                                             health += 4
                                             print("You eat the potato.\n")

                                 elif args[1] == can_eat[5]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 2 > health_max:
                                             inventory.remove('onion')
                                             health = 75
                                             print("You eat the onion.\n")
                                       else:
                                             inventory.remove('onion')
                                             health += 2
                                             print("You eat the onion.\n")

                                 else:
                                     print("You can't eat this.\n")
                           else:
                               print("You don't have this.\n")
                      except:
                            print("Eat what?\n")

                if args[0] == "turn":
                    try:
                        if args[1] == 'lantern':
                            if 'lantern' in inventory:
                                global lantern_on
                                if args[2] == 'on':
                                    lantern_on = True
                                    moves += 1
                                    print("The lantern is now on.\n")

                                elif args[2] == 'off':
                                    lantern_on = False
                                    moves += 1
                                    print("The lantern is now off.\n")

                            else:
                                print("You don't have a lantern.\n")
                    except:
                        print("Invalid.\n")

                if args[0] == "say":
                    try:
                        if args[1] != None:
                            moves += 1
                            print("You say:" + " " + args[1])
                            print("")

                        else:
                            pass
                    except:
                        print("Say what?\n")

                if args[0] == 'read':
                    try:
                        if args[1] == 'paper':
                            if 'paper' in inventory:
                                global paper
                                moves += 1
                                print(paper)
                            else:
                                pass

                        elif args[1] == 'note':
                            if 'note' in inventory:
                                global note
                                moves += 1
                                print(note)
                            else:
                                pass

                        elif args[1] == 'post-it':
                            if 'post-it' in inventory:
                                global post
                                moves += 1
                                print(post)
                            else:
                                pass

                        elif args[1] == 'poster':
                            if 'poster' in inventory:
                                global poster
                                moves += 1
                                print(poster)
                            else:
                                pass

                        else:
                            pass
                    except:
                        print("Read what?\n")

                if args[0] == 'look':
                    global key_desc
                    global sword_desc
                    global knife_desc
                    global ruby_desc
                    global amulet_desc
                    try:
                        if args[1] == 'at':
                            try:
                                if args[2] in inventory:
                                    if args[2] == 'key':
                                        print(key_desc)

                                    elif args[2] == 'sword':
                                        print(sword_desc)

                                    elif args[2] == 'knife':
                                        print(knife_desc)

                                    elif args[2] == 'ruby':
                                        print(ruby_desc)

                                    elif args[2] == 'amulet':
                                        print(amulet_desc)

                                    else:
                                        print("I see nothing special about this.\n")

                                else:
                                    print("You don't have this item.\n")

                            except:
                                print("Look at what?\n")

                    except:
                        print("Look at what?\n")

    def up(self):
        global moves
        moves += 1
        print("You can't go that way.\n")

    def down(self):
        global moves
        moves += 1
        print("You can't go that way.\n")

    def south(self):
        global moves
        moves += 1
        complete = True
        h = House()
        h.inicio()

    def west(self):
        global moves
        moves += 1
        complete = True
        b = Bridge()
        b.inicio()

    def north(self):
        global moves
        moves += 1
        complete = True
        ft = Forest()
        ft.inicio()

    def east(self):
        global moves
        moves += 1
        complete = True
        ot = OutTemple()
        ot.inicio()

class TrapDoor:
    def __init__(self):
        self.state = 'trapdoor'

    def quit(self):
        c = character()
        c.quit()

    def ajuda(self):
        c = character()
        c.ajuda()

    def status(self):
        c = character()
        c.status()

    def restart(self):
        c = character()
        c.restart()

    def score(self):
        c = character()
        c.score()

    def save(self):
        save()

    def inventory(self):
        if len(inventory) > 0:
            print("You have:")
            print inventory
            print("")
        else:
            print("Your inventory is empty.\n")

    def inicio(self):
        complete = False
        global moves
        global trapdoor1_open
        global trapdoor1_close
        global lantern_on
        global local
        local = 'TrapDoor'
        print("Tunnel")
        if lantern_on == True and 'lantern' in inventory:
            print("You are in a narrow tunnel, this path extends to east.\n")
            itens = {
            1 : {}
            }
            currentRoom = 1

        elif 'torch' in inventory and 'lantern' not in inventory:
            print("You are in a narrow tunnel, this path extends to east.\n")
            itens = {
            1 : {"item": 'lantern'}
            }
            currentRoom = 1

        elif 'torch' in inventory and 'lantern' in inventory:
            print("You are in a narrow tunnel, this path extends to east.\n")
            itens = {
            1 : {"item": 'lantern'}
            }
            currentRoom = 1

        elif 'lantern' in inventory:
            print("You have moved into a dark place, this path extends to east.\n")
            itens = {
            1 : {}
            }
            currentRoom = 1

        else:
            print("You have moved into a dark place.")
            print("This path extends to east.")
            print("There is a lantern here(battery-powered).\n")
            itens = {
            1 : {"item": 'lantern'}
            }
            currentRoom = 1

        Commands = {
        'help': TrapDoor.ajuda,
        'quit': TrapDoor.quit,
        'save': TrapDoor.save,
        'score': TrapDoor.score,
        'north': TrapDoor.north,
        'west': TrapDoor.west,
        'east': TrapDoor.east,
        'south': TrapDoor.south,
        'up': TrapDoor.up,
        'down': TrapDoor.down,
        'status': TrapDoor.status,
        'restart': TrapDoor.restart,
        'inventory': TrapDoor.inventory
        }

        tp = TrapDoor()

        while complete == False:
            line = raw_input("> ")
            args = line.split()
            if len(args) == 0:
                print("What you want to do?\n")

            elif len(args) > 0:
                commandFound = False
                for c in Commands.keys():
                    if args[0] == c[:len(args[0])]:
                        Commands[c](tp)
                        commandFound = True
                        break

                if args[0] == "take":
                    try:
                        if "item" in itens[currentRoom] and args[1] in itens[currentRoom]["item"]:
                            inventory.append(args[1])
                            moves += 1
                            print(args[1]+":" + " Taken.\n")
                            del itens[currentRoom]["item"]
                        else:
                            print("Can't get this.\n")

                    except:
                        print("Invalid.\n")

                if args[0] == "drop":
                    try:
                        if args[1] in inventory:
                            inventory.remove(args[1])
                            moves += 1
                            print(args[1]+":" + " Dropped.\n")
                        else:
                            print("Can't drop this.\n")
                    except:
                        print("Invalid.\n")

                if args[0] == "eat":
                      try:
                           if args[1] in inventory and args[1] in can_eat:
                                 global health, health_max
                                 if args[1] == can_eat[0]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 5 > health_max:
                                             inventory.remove('bread')
                                             health = 75
                                             print("You eat the bread.\n")
                                       else:
                                             inventory.remove('bread')
                                             health += 5
                                             print("You eat the bread.\n")

                                 elif args[1] == can_eat[1]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 5 > health_max:
                                             inventory.remove('apple')
                                             health = 75
                                             print("You eat the apple.\n")
                                       else:
                                             inventory.remove('apple')
                                             health += 5
                                             print("You eat the apple.\n")

                                 elif args[1] == can_eat[2]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 3 > health_max:
                                             inventory.remove('carrot')
                                             health = 75
                                             print("You eat the carrot.\n")
                                       else:
                                             inventory.remove('carrot')
                                             health += 3
                                             print("You eat the carrot.\n")

                                 elif args[1] == can_eat[3]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 4 > health_max:
                                             inventory.remove('tomato')
                                             health = 75
                                             print("You eat the tomato.\n")
                                       else:
                                             inventory.remove('tomato')
                                             health += 4
                                             print("You eat the tomato.\n")

                                 elif args[1] == can_eat[4]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 4 > health_max:
                                             inventory.remove('potato')
                                             health = 75
                                             print("You eat the potato.\n")
                                       else:
                                             inventory.remove('potato')
                                             health += 4
                                             print("You eat the potato.\n")

                                 elif args[1] == can_eat[5]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 2 > health_max:
                                             inventory.remove('onion')
                                             health = 75
                                             print("You eat the onion.\n")
                                       else:
                                             inventory.remove('onion')
                                             health += 2
                                             print("You eat the onion.\n")

                                 else:
                                     print("You can't eat this.\n")
                           else:
                               print("You don't have this.\n")
                      except:
                            print("Eat what?\n")

                if args[0] == "turn":
                    try:
                        if args[1] == 'lantern':
                            if 'lantern' in inventory:
                                if args[2] == 'on':
                                    lantern_on = True
                                    moves += 1
                                    print("The lantern is now on.\n")

                                elif args[2] == 'off':
                                    lantern_on = False
                                    moves += 1
                                    print("The lantern is now off.\n")

                            else:
                                print("You don't have a lantern.\n")
                    except:
                        print("Invalid.\n")

                if args[0] == "say":
                    try:
                        if args[1] != None:
                            moves += 1
                            print("You say:" + " " + args[1])
                            print("")
                        else:
                            pass
                    except:
                        print("Say what?\n")

                if args[0] == 'read':
                    try:
                        if args[1] == 'paper':
                            if 'paper' in inventory:
                                global paper
                                moves += 1
                                print(paper)
                            else:
                                pass

                        elif args[1] == 'note':
                            if 'note' in inventory:
                                global note
                                moves += 1
                                print(note)
                            else:
                                pass

                        elif args[1] == 'post-it':
                            if 'post-it' in inventory:
                                global post
                                moves += 1
                                print(post)
                            else:
                                pass

                        elif args[1] == 'poster':
                            if 'poster' in inventory:
                                global poster
                                moves += 1
                                print(poster)
                            else:
                                pass

                        else:
                            pass

                    except:
                        print("Read what?\n")

                if args[0] == 'open':
                    try:
                        if args[1] == 'trapdoor':
                            moves += 1
                            trapdoor1_open = True
                            trapdoor1_close = False
                            print("You open the trapdoor.\n")

                        else:
                            print("Open what?\n")

                    except:
                        print("Open what?\n")

                if args[0] == 'close':
                    try:
                        if args[1] == 'trapdoor':
                            moves += 1
                            trapdoor1_open = False
                            trapdoor1_close = True
                            print("You close the trapdoor.\n")

                        else:
                            print("Close what?\n")

                    except:
                        print("Close what?\n")

                if args[0] == 'look':
                    global key_desc
                    global sword_desc
                    global knife_desc
                    global ruby_desc
                    global amulet_desc
                    try:
                        if args[1] == 'at':
                            try:
                                if args[2] in inventory:
                                    if args[2] == 'key':
                                        print(key_desc)

                                    elif args[2] == 'sword':
                                        print(sword_desc)

                                    elif args[2] == 'knife':
                                        print(knife_desc)

                                    elif args[2] == 'ruby':
                                        print(ruby_desc)

                                    elif args[2] == 'amulet':
                                        print(amulet_desc)

                                    else:
                                        print("I see nothing special about this.\n")

                                else:
                                    print("You don't have this item.\n")

                            except:
                                print("Look at what?\n")

                    except:
                        print("Look at what?\n")

    def up(self):
        global moves
        moves += 1
        if trapdoor1_open == True and trapdoor1_close == False:
            complete = True
            h = House()
            h.inicio()

        else:
            print("The trapdoor is closed.\n")

    def down(self):
        global moves
        moves += 1
        print("You can't go that way.\n")

    def north(self):
        global moves
        moves += 1
        print("Some bricks on the ground.\n")

    def east(self):
        global moves
        moves += 1
        complete = True
        t = Tunnel()
        t.inicio()

    def west(self):
        global moves
        moves += 1
        print("Nothing here.\n")

    def south(self):
        global moves
        moves += 1
        print("Nothing here just sadness.\n")

class House:
    def __init__(self):
        self.state = 'house'

    def quit(self):
        c = character()
        c.quit()

    def save(self):
        save()

    def status(self):
        c = character()
        c.status()

    def ajuda(self):
        c = character()
        c.ajuda()

    def restart(self):
        c = character()
        c.restart()

    def score(self):
        c = character()
        c.score()

    def inventory(self):
        if len(inventory) > 0:
            print("You have:")
            print inventory
            print("")
        else:
            print("Your inventory is empty.\n")

    def achievement(self):
        c = character()
        c.achievement()

    def inicio(self):
        global local
        local = 'House'
        complete = False
        global moves
        global trapdoor1_open
        global trapdoor1_close

        commands = {
        'help': House.ajuda,
        'quit': House.quit,
        'save': House.save,
        'score': House.score,
        'achievement': House.achievement,
        'north': House.north,
        'west': House.west,
        'east': House.east,
        'south': House.south,
        'up': House.up,
        'down': House.down,
        'status': House.status,
        'inventory': House.inventory,
        'restart': House.restart
        }

        itens = {
        1 : {}

        }
        currentRoom = 1

        h = House()

        print("House")
        print("You are stading in a open field of a house, there is a door here.")
        print("Have a trapdoor here. You can go to the attic here.\n")

        while complete == False:
            line = raw_input("> ")
            args = line.split()
            if len(args) == 0:
                print("What you want to do?\n")

            elif len(args) > 0:
                commandFound = False
                for c in commands.keys():
                    if args[0] == c[:len(args[0])]:
                        commands[c](h)
                        commandFound = True
                        break

                if args[0] == "take":
                    try:
                        if "item" in itens[currentRoom] and args[1] in itens[currentRoom]["item"]:
                            moves += 1
                            inventory.append(args[1])
                            print(args[1]+":" + " Taken.\n")
                            del itens[currentRoom]["item"]

                        else:
                            print("Can't get this.\n")

                    except:
                        print("Invalid.\n")

                if args[0] == "drop":
                    try:
                        if args[1] in inventory:
                            moves += 1
                            inventory.remove(args[1])
                            print(args[1]+":" + " Dropped.\n")

                        else:
                            print("Can't drop this.\n")
                    except:
                        print("Invalid.\n")

                if args[0] == "eat":
                      try:
                           if args[1] in inventory and args[1] in can_eat:
                                 global health, health_max
                                 if args[1] == can_eat[0]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 5 > health_max:
                                             inventory.remove('bread')
                                             health = 75
                                             print("You eat the bread.\n")
                                       else:
                                             inventory.remove('bread')
                                             health += 5
                                             print("You eat the bread.\n")

                                 elif args[1] == can_eat[1]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 5 > health_max:
                                             inventory.remove('apple')
                                             health = 75
                                             print("You eat the apple.\n")
                                       else:
                                             inventory.remove('apple')
                                             health += 5
                                             print("You eat the apple.\n")

                                 elif args[1] == can_eat[2]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 3 > health_max:
                                             inventory.remove('carrot')
                                             health = 75
                                             print("You eat the carrot.\n")
                                       else:
                                             inventory.remove('carrot')
                                             health += 3
                                             print("You eat the carrot.\n")

                                 elif args[1] == can_eat[3]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 4 > health_max:
                                             inventory.remove('tomato')
                                             health = 75
                                             print("You eat the tomato.\n")
                                       else:
                                             inventory.remove('tomato')
                                             health += 4
                                             print("You eat the tomato.\n")

                                 elif args[1] == can_eat[4]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 4 > health_max:
                                             inventory.remove('potato')
                                             health = 75
                                             print("You eat the potato.\n")
                                       else:
                                             inventory.remove('potato')
                                             health += 4
                                             print("You eat the potato.\n")

                                 elif args[1] == can_eat[5]:
                                       if health == health_max:
                                             print("Your health is full.\n")

                                       elif health + 2 > health_max:
                                             inventory.remove('onion')
                                             health = 75
                                             print("You eat the onion.\n")
                                       else:
                                             inventory.remove('onion')
                                             health += 2
                                             print("You eat the onion.\n")

                                 else:
                                     print("You can't eat this.\n")
                           else:
                               print("You don't have this.\n")
                      except:
                            print("Eat what?\n")

                if args[0] == "turn":
                    try:
                        if args[1] == 'lantern':
                            if 'lantern' in inventory:
                                global lantern_on
                                if args[2] == 'on':
                                    lantern_on = True
                                    moves += 1
                                    print("The lantern is now on.\n")

                                elif args[2] == 'off':
                                    lantern_on = False
                                    moves += 1
                                    print("The lantern is now off.\n")
                            else:
                                print("You don't have a lantern.\n")
                    except:
                        print("Invalid.\n")

                if args[0] == "say":
                    try:
                        if args[1] != None:
                            moves += 1
                            print("You say:" + " " + args[1])
                            print("")

                        else:
                            pass
                    except:
                        print("Say what?\n")

                if args[0] == 'read':
                    try:
                        if args[1] == 'paper':
                            if 'paper' in inventory:
                                global paper
                                moves += 1
                                print(paper)
                            else:
                                pass

                        elif args[1] == 'note':
                            if 'note' in inventory:
                                global note
                                moves += 1
                                print(note)
                            else:
                                pass

                        elif args[1] == 'post-it':
                            if 'post-it' in inventory:
                                global post
                                moves += 1
                                print(post)
                            else:
                                pass

                        elif args[1] == 'poster':
                            if 'poster' in inventory:
                                global poster
                                moves += 1
                                print(poster)
                            else:
                                pass

                        else:
                            pass

                    except:
                        print("Read what?\n")

                if args[0] == 'open':
                    try:
                        if args[1] == 'trapdoor':
                            moves += 1
                            trapdoor1_close = False
                            trapdoor1_open = True
                            print("You open the trapdoor.\n")

                        else:
                            print("Open what?\n")

                    except:
                        print("Open what?\n")

                if args[0] == 'close':
                    try:
                        if args[1] == 'trapdoor':
                            moves += 1
                            trapdoor1_close = True
                            trapdoor1_open = False
                            print("You close the trapdoor.\n")

                        else:
                            print("Close what?\n")

                    except:
                        print("Close what?\n")

                if args[0] == 'look':
                    global key_desc
                    global sword_desc
                    global knife_desc
                    global ruby_desc
                    global amulet_desc
                    try:
                        if args[1] == 'at':
                            try:
                                if args[2] in inventory:
                                    if args[2] == 'key':
                                        print(key_desc)

                                    elif args[2] == 'sword':
                                        print(sword_desc)

                                    elif args[2] == 'knife':
                                        print(knife_desc)

                                    elif args[2] == 'ruby':
                                        print(ruby_desc)

                                    elif args[2] == 'amulet':
                                        print(amulet_desc)

                                    else:
                                        print("I see nothing special about this.\n")

                                else:
                                    print("You don't have this item.\n")

                            except:
                                print("Look at what?\n")

                    except:
                        print("Look at what?\n")

    def down(self):
        global moves
        moves += 1
        if trapdoor1_open == True and trapdoor1_close == False:
            complete = True
            tp = TrapDoor()
            tp.inicio()
        else:
            print("There is a trapdoor here, but you need to open it.\n")

    def up(self):
        global moves
        moves += 1
        complete = True
        a = Attic()
        a.inicio()

    def north(self):
        global moves
        moves += 1
        complete = True
        f = ForestPath()
        f.inicio()

    def west(self):
        global moves
        moves += 1
        print "West of House"
        print "You find a window, and look through it."
        print "You look at the sky and see a crescent moon."
        print "This is beautiful.\n"

    def east(self):
        global moves
        moves += 1
        print("Living Room")
        print("Table, chairs, a beige sofa, a broken old tv")
        print("and a old vinyl record player.\n")

    def south(self):
        global moves
        moves += 1
        print("Behind the House")
        print("Some shrubs and flowers, A table and two chairs.")
        print("And fence around the back of the house.\n")

banner = """\n\n\n\n

              _____                         _   _____
             |     |___ ___ ___ ___ ___ ___| |_|     |___ ___ ___
             |   --|  _| -_|_ -|  _| -_|   |  _| | | | . | . |   |
             |_____|_| |___|___|___|___|_|_|_| |_|_|_|___|___|_|_|

          ===========================================================
          [Author]: Immunity [Version]: %s | CrescentMoon Sad
          ===========================================================

\t\t\t    Press ENTER to continue
"""% version

def credits():
    os.system("clear")
    print("\n\n              Programmer: Immunity")
    print("             Beta Tester: Guilherme\n")
    print R + ("    I'm a lonely cloud with my windows down\n")
    print W +("                      京都\n")

    cont = raw_input("")
    if cont != None:
        options()
    else:
        pass

def options():
    os.system("clear")
    try:
        save = open("savefile", "r")
        print """
    New Game
    Continue Game
    Credits
    Exit
        \n"""

    except IOError:
        print """
    New Game
    Credits
    Exit
        \n"""

    except ValueError:
        print """
    New Game
    Credits
    Exit
        \n"""

    option = raw_input("")

    if option == 'New Game':
        os.system("clear")
        print("(type help to get a list of actions)")
        print("CrescentMoon: The Sad Text Adventure")
        print("Copyright (c) 2016, 2017 By Immunity. All rights reserved.")
        print("Version: %s / Serial Number: %s\n")%(version, serial)
        h = House()
        h.inicio()
    elif option == 'Continue Game':
        continue_game()
    elif option == 'Credits':
        credits()
    elif option == 'credits':
        credits()
    elif option == 'Exit':
        os.system("clear")
        sys.exit()
    elif option == 'exit':
        os.system("clear")
        sys.exit()
    else:
        options()

def start():
    try:
        os.system("clear")
        print(banner)
        s = raw_input("")
        if s != None:
            options()
    except KeyboardInterrupt, ex:
        sys.exit()

if __name__ == "__main__":
    start()
