import random
import time
import json

json_dict = json.load(open('story.json'))
encounters = json_dict["encounters"]

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


def play_encounter(encounter, curr_scene = 0):
    if curr_scene == -1:
        return

    answer = input("[y/n]").lower()

    for scenario in encounter["scenarios"]:
        if curr_scene not in scenario["prev_scenes"]:
            continue

        scenario_modifiers = scenario["modifiers"]
        if not all(elem in modifiers for elem in scenario_modifiers):
            continue

        if answer != scenario["answer"]:
            continue

        curr_scene = scenario["next_scene"]

        play_encounter(encounter, curr_scene)


compassion = 50
foolhardy = 50
greed = 50
courage = 50
honor = 50
deaths = 0

modifiers = []

num_encounters = len(encounters)
completed_encounters = []

game = True

while game:
    encounter_index = random.randint(0, num_encounters - 1)
    completed_encounters.append(encounter_index)

    encounter = encounters[encounter_index]

    for line in encounter["intro"]:
        print(line)
        time.sleep(1)

    play_encounter(encounter)
