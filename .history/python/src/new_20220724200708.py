import random
import time
import json

print("  _____ _____  ______          _      _____  _____ _______ _____ _____ ")
print(" |_   _|  __ \|  ____|   /\   | |    |_   _|/ ____|__   __|_   _/ ____|")
print("   | | | |  | | |__     /  \  | |      | | | (___    | |    | || |     ")
print("   | | | |  | |  __|   / /\ \ | |      | |  \___ \   | |    | || |     ")
print("  _| |_| |__| | |____ / ____ \| |____ _| |_ ____) |  | |   _| || |____ ")
print(" |_____|_____/|______/_/    \_\______|_____|_____/   |_|  |_____\_____|")
time.sleep(2)
print()
print()
print("Welcome, stranger, to the The Forest Of Lost Souls")
time.sleep(1)
name = input("What is your name, lost one?")
time.sleep(1)
print("What a peculiar name... Anyhow, " + name + ", now that you have entered The Forest Of The Lost Souls you are trapped here unless you are the Idealistic One from The Great Prophecy")
time.sleep(2)
print("I wish you good luck while you strive to survive in the forest")
time.sleep(1.5)
print()
print("...The spirit who welcomed you, leaves you to survive in the forest")
time.sleep(1)

encounters = [
    ["You see a old lady approach you.", "'Help!', she cries. 'I am in need of water.. please!'", "How can I trust you, you ask.", "'I'm just an old lady, will you help me?!', she says."],
    ["You approach a lake to collect water when you spot a pot of gold next to a tree.", "You look closer and notice a man in ragged clothes next to the pot", "'Please don't take my gold', the man begs, 'it's all I have'", "You look at the man, you could easily fight him and steal the gold if you wished.", "Will you steal his gold?"],
    ["You spot a cave, it has a gloomy and eerie feel to it.", "You stare at the mouth of the cave, it calls you in, and you wonder what may be inside", "Do you wish to enter the cave?"],
    ["A young wolf approaches you.", "It appears to be an orphan.", "If you help it it may help in upcoming fights, but it will force you to feed it.", "Do you wish to adopt the wolf?"],
    ["An ogre thunders toward you, he measured up to 8 feet in size and board a massive club.", "Do you fight or run? [fight = y / run = n]"],
    ["You spot a valiant warrior.", "He carries a long sword and rides on an impressive black steed.", "'I challenge you to a duel!', he says", "Do you wish to fight him?"],
    ["You find a chest plate made of a strong metal.", "Do you wish to put it on?", "[Chest plate - Increases your defense stats!]"],
    ["You find a sharp sword made of a strong metal.", "Do you wish to equip it?", "[Sharp Sword - Increases your attack stats!]"]
]

compassion = 50
foolhardy = 50
greed = 50
courage = 50
honor = 50
deaths = 0

modifiers = []

json_dict = json.load(open('sdf.json'))

for scenario in json_dict["scenarios"]:
    