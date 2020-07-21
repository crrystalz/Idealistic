import random
import time

compassion = 50
foolhardy = 50
greed = 50
courage = 50
honor = 50
deaths = 0

print("IDEALSTIC")
time.sleep(1.5)
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

day = 1
print("DAY " + str(day))
print()

encounters = [
    ["You see a old lady approach you.", "'Help!', she cries. 'I am in need of water.. please!'", "How can I trust you, you ask", "'I'm just an old lady, will you help me?!', she says."],
    ["You approach a lake to collect water when you spot a pot of gold next to a tree.", "You look closer and notice a man in ragged clothes next to the pot", "'Please don't take my gold', the man begs, 'it's all I have'", "You look at the man, you could easily fight him and steal the gold if you wished.", "Will you steal his gold?"],
    ["You spot a cave, it has a gloomy and eerie feel to it.", "You stare at the mouth of the cave, it calls you in, and you wonder what may be inside", "Do you wish to enter the cave?"]
]

numbersPicked = []
while True:

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

        if yn == 'n':
            print("Afraid of what may lie in the cave you walk past it continuing your journey in the forest.")
            courage -= 15
            foolhardy += 5

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