import random
import time
import json

json_dict = json.load(open("story.json"))
encounters = json_dict["encounters"]


def slow_print(text_arr):
    for line in text_arr:
        print(line)
        time.sleep(1)


def game_intro():
    global name

    idealistic_title = [
        "  _____ _____  ______          _      _____  _____ _______ _____ _____ ",
        " |_   _|  __ \|  ____|   /\   | |    |_   _|/ ____|__   __|_   _/ ____|",
        "   | | | |  | | |__     /  \  | |      | | | (___    | |    | || |     ",
        "   | | | |  | |  __|   / /\ \ | |      | |  \___ \   | |    | || |     ",
        "  _| |_| |__| | |____ / ____ \| |____ _| |_ ____) |  | |   _| || |____ ",
        " |_____|_____/|______/_/    \_\______|_____|_____/   |_|  |_____\_____|",
    ]

    [print(line) for line in idealistic_title]

    time.sleep(2)
    print()
    print()
    print("Welcome, stranger, to the The Forest Of Lost Souls")
    time.sleep(1)
    name = input("What is your name, lost one? ")
    time.sleep(1)
    if name == "crrystalz" or "rrishi":
        print(
            "What a beauitiful name!",
            "Well, "
            + name
            + ", now that you have entered The Forest Of The Lost Souls you are trapped here unless you are the Idealistic One from The Great Prophecy",
        )
    else:
        print(
            "What a peculiar name... Anyhow, "
            + name
            + ", now that you have entered The Forest Of The Lost Souls you are trapped here unless you are the Idealistic One from The Great Prophecy"
        )
    time.sleep(2)
    print("I wish you good luck while you strive to survive in the forest")
    time.sleep(1.5)
    print()
    print("...The spirit who welcomed you, leaves you to survive in the forest")
    time.sleep(1)

    return


def play_encounter(encounter, curr_scene_index=-1):
    global answer

    global compassion
    global foolhardy
    global greed
    global courage
    global honor
    global deaths

    if curr_scene_index == -1:
        answer = ""

    for scenario in encounter["scenarios"]:
        if curr_scene_index not in scenario["prev_scenes"]:
            continue

        scenario_modifiers = scenario["modifiers"]
        if not all(elem in modifiers for elem in scenario_modifiers):
            continue

        if answer != scenario["answer"]:
            continue

        curr_scene_index = scenario["next_scene"]

        if curr_scene_index != -2:
            curr_scene = encounter["scenes"][curr_scene_index]
            slow_print(curr_scene["text"])

            if encounter["scenes"][curr_scene_index]["interactive"] == "T":
                answer = input("[y/n] ").lower()
            else:
                answer = ""

            # scene result format - [compassion, foolhardy, greed, courage, honor, deaths]
            scene_result = curr_scene["result"]

            compassion += scene_result[0]
            foolhardy += scene_result[1]
            greed += scene_result[2]
            courage += scene_result[3]
            honor += scene_result[4]
            deaths += scene_result[5]

            play_encounter(encounter, curr_scene)

        else:
            return


game_intro()

compassion = 50
foolhardy = 50
greed = 50
courage = 50
honor = 50
deaths = 0

modifiers = []

num_encounters = len(encounters)
completed_encounters = []
num_completed_encounters = 0
encounter_index = -1

day = 1

game = True

while game:
    while encounter_index in completed_encounters:
        encounter_index = random.randint(0, num_encounters - 1)
    completed_encounters.append(encounter_index)

    encounter = encounters[encounter_index]

    slow_print(
        [
            "",
            "DAY " + str(day),
            "",
        ]
    )

    play_encounter(encounter)

    slow_print(
        [
            "",
            "Your compassion: " + str(compassion),
            "Your foolhardy: " + str(foolhardy),
            "Your greed: " + str(greed),
            "Your courage: " + str(courage),
            "Your honor: " + str(honor),
            "Your deaths: " + str(deaths),
            "",
        ]
    )

    num_completed_encounters += 1

    day += 1

    if num_completed_encounters == num_encounters:
        game = False

slow_print(
    [
        "",
        "You descended into the underworld... without completing The Great Prophecy",
        "Cause: Old Age",
    ]
)

game_over = [
    " _____   ___  ___  ___ _____   _____  _   _ ___________ ",
    "|  __ \ / _ \ |  \/  ||  ___| |  _  || | | |  ___| ___ \\",
    "| |  \// /_\ \| .  . || |__   | | | || | | | |__ | |_/ /",
    "| | __ |  _  || |\/| ||  __|  | | | || | | |  __||    / ",
    "| |_\ \| | | || |  | || |___  \ \_/ /\ \_/ / |___| |\ \ ",
    " \____/\_| |_/\_|  |_/\____/   \___/  \___/\____/\_| \_|"
]

[print(line) for line in game_over]