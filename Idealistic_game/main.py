import random
import time

compassion = 50
foolhardy = 50
greed = 50
courage = 50
honor = 50
deaths = 0

print(" _____ _____  ______          _      _____  _____ _______ _____ _____  ")
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
    ["You spot a valiant warrior.", "He carries a long sword and rides on a horse." "'I challenge you to a duel!', he says", "Do you wish to fight him?"]

]

wolf = False
day = 1
numbersPicked = []

while True:
    print()
    print("DAY " + str(day))
    print()

    if len(numbersPicked) == len(encounters):
        exit()

    randomNumber = 0
    while randomNumber in numbersPicked:
        randomNumber = random.randint(0, len(encounters)-1)
    numbersPicked.append(randomNumber)

    for event in encounters[randomNumber]:
        time.sleep(1)
        print(event)

    time.sleep(1)
    yn = input("[y/n]")

    if randomNumber == 0:
        if yn == 'y':
            print("You approach her to give her water but she leaps and grabs you by the throat")
            time.sleep(1)
            print("She smiles and suffocates you to death")
            time.sleep(1)
            print("Right before you die, you see her turn into a disgusting monster and then you hear the sickening crunch of your bones")

            deaths += 1
            foolhardy += 15
            compassion += 5

        if yn == 'n':
            print("You feel suspicious of the woman, and for good reason. Moments later, the woman dies and her body morphs into a disgusting creature")

            compassion -= 10
            foolhardy -= 15


    if randomNumber == 1:
        if yn == 'y':
            print("You approach the gold, but the man punches you.")
            time.sleep(1)
            print("You both lock eyes and throw punches at one another.")
            time.sleep(1)
            print("Just as you are about to knock him out, his eyes turn into beady red eyes and the man turns into an overgrown bat. He swallows you whole. You die.")

            deaths += 1
            compassion -= 10
            honor -= 15
            greed += 15
            
        if yn == 'n':
            print("You nod at the man.")
            time.sleep(1)
            print("The man's entire body glows and he rises above the ground.")
            time.sleep(1)
            print("You are a honorable man, here take this pot of gold.")
            time.sleep(1)
            print("The man dissapears, and you take the gold you were rewarded.")

            compassion += 5
            honor += 10
            greed -= 5

    if randomNumber == 2:
        if yn == 'y':
            print("You walk towards the mouth, and the cave swallows you.")
            time.sleep(1)
            print("Immediately, the cave opens up into a large cavern.")
            time.sleep(1)
            print("At the center you spot a chest, however it is guarded by two skeletal creatures.")
            time.sleep(1)
            print("They walk towards you, one makes a lousy attempt to claw you, but you are easily able to take them down.")
            time.sleep(1)
            print("You open the chest to find it full of precious gems.")

            courage += 15
            foolhardy -= 5
            greed += 10

        if yn == 'n':
            print("Afraid of what may lie in the cave you walk past it continuing your journey in the forest.")
            courage -= 15
            foolhardy += 5
            greed -= 5

    if randomNumber == 3:
        if yn == 'y':
            print("Congratulations! You now have a pet wolf, it will eventually grow to be a loyal and fearsome beast.")
            time.sleep(1)
            wolfName = input("What do you wish to name your companion?")
            wolf = True
            time.sleep(1)
            print(wolfName + " it is!")

            courage += 5
            honor += 5

        if yn == "n":
            print("You decline the wolf and leave it to suffer")
            wolf = False
            time.sleep(1)
            print("Frustrated, it bites you and mauls you. The wolf is much fiercer than you expected but you are able to fight it off, but not without sustaining major injuries.")

            courage -= 5
            honor += 5

    if randomNumber == 4:
        if yn == 'y':
            print("You choose to fight the beast!")
            if wolf == False:
                chanceOfWinning = 2

            else:
                chanceOfWinning = 1

            success = random.randint(0,chanceOfWinning)
            if success == 1:
                time.sleep(1)
                if wolf == True:
                    print("You and " + wolfName + " circle the ogre, " + wolfName + " attacks first, he leaps and lashes at the ogres eye.")
                    time.sleep(1)
                    print("While " + wolfName + " distracts the ogre you go behind and stab your blade into the ogre's back. The ogre falls to his death.")

                else:
                    print("You stare at the ogre and jump as high as you can. You land on the branch of a tree.")
                    time.sleep(1)
                    print("The ogre's eyes look for you, as you stealthily jump from one branch to another. Eventually you are behind the ogre.")
                    time.sleep(1)
                    print("You plunge your sword into the back of the ogre's head. The ogre dies.")

            else:
                time.sleep(1)
                if wolf == True:
                    print("You and " + wolfName + " circle the ogre." + "The ogre makes the first move, but also the last, as he throws you into the distant woods with his powerful arm. You die.")
                    deaths \
                        += 1

                else:
                    print("You look at the ogre and with adrenaline pulsing through you, you run at him.")
                    time.sleep(1)
                    print("The ogre smiles and kicks you into the distance. You fall with a thud breaking all of your bones. You die")
                    deaths += 1

            courage += 15
            foolhardy += 10

        if yn == 'n':
            print("You decide to avoid the ogre, and blend into the landscape.")
            time.sleep(1)
            print("The ogre looks for you but doesn't spot you behind the bush.")
            time.sleep(1)
            print("The ogre passes you.")

            courage -= 10
            foolhardy -= 10

    if randomNumber == 5:
        if yn == 'y':
            if wolf == True:
                print("You charge, you command your wolf to bite at the horse, in hopes you could make the warrior fall")
                time.sleep(1.5)
                print(wolfName + "Bites at the horse but the horse doesn't fall. The warrior charges at you and beheads you with his mighty sword.")

            else:
                print("You charge at the warrior, your sword drawn. A mighty sword fight ensues but it ends with the warrior chopping of your head.")

            honor += 15
            foolhardy += 10
            courage += 10

        if yn == 'n':
            print("You walk away knowing that this was a fight you could never win.")

            honor -= 10
            foolhardy -= 15
            courage -= 5

    time.sleep(1)
    print("Your Compassion " + str(compassion))
    time.sleep(1)
    print("Your Foolishness " + str(foolhardy))
    time.sleep(1)
    print("Your Greed " + str(greed))
    time.sleep(1)
    print("Your Courage " + str(courage))
    time.sleep(1)
    print("Your Honor " + str(honor))
    time.sleep(1)
    print("Your Deaths " + str(deaths))
    time.sleep(1)

    day += 1