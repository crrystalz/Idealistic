import random
import time
import json

json_dict = json.load(open('sdf.json'))

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

compassion = 50
foolhardy = 50
greed = 50
courage = 50
honor = 50
deaths = 0

modifiers = []
encounter = -1
prev_scene = -1
curr_scene = -1

completed_encounters = []

game = True

while game:
    for scenario in json_dict["scenarios"]:
        