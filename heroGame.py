
#TEXT BASED GAME

import random, sys, time

class human(object):
    def __init__(self, name, age, gender, eyeColor, hairColor, health, attack):
        self.name = name
        self.age = age
        self.gender = gender
        self.eyeColor = eyeColor
        self.hairColor = hairColor
        self.health = health
        self.attack = attack
        self.inventory = {"healingPotion":1, "inferiorEyeUses":1} #sets up a dictionary - you may want to pull out a key

    def health_loss(self, damage):
        print (self.name + " takes " + str(damage) + " damage.")
        self.health = self.health - damage
        print (self.name + " has " + str(self.health) + " remaining health.")
        time.sleep(1)

    def healing_potion(self):
        if self.inventory.get("healingPotion") > 0:
            print (self.name + " drinks a healing potion.")
            self.health = self.health + 30
            print (self.name + " has " + str(self.health) + " health.")
            time.sleep(1)
            self.inventory["healingPotion"] = self.inventory.get("healingPotion") -1
        else:
            print ("Out of healing potions.")
            time.sleep(1)

    def att(self):
        print (self.name + " attacks!!!")
        time.sleep(1)
        return self.attack



class hero(human):
    def __init__(self, name, age, gender, eyeColor, hairColor, health, attack):
        human.__init__(self, name, age, gender, eyeColor, hairColor, health, attack)

    def pantsless_crit(self):
        print (self.name + " takes off his pants and dances around madly!!! Critical Pantsless hit!!!")
        self.health = self.health -5
        return 40

    def inferior_eyecolor_attack(self, humans):
        if self.inventory.get("inferiorEyeUses") > 0:
            for hum in humans:
                if hum.eyeColor != self.eyeColor:
                    print(self.name + " makes you feel guilty for not having the superior " + self.eyeColor + " eye color.")
                    hum.healthloss(25)
                else:
                    print("Open your eyes, " + hum.name + " has the same eye color!")
            self.inventory["inferiorEyeUses"] = self.inventory.get("inferiorEyeUses") -1
        else:
            print("I am way too out of shape for that!")


def hero_creation():
    print("Hero, WWT summons you to defeat a clan of unkempt engineers!!!")
    print("Please describe yourself: ")
    name = input("What is your name? ")
    gender = input("What is your gender? ")
    age = input("How old are you? ")
    eyeColor = input("What are the color of your eyes? ")
    hairColor = input("What is the color of your hair? ")

    health = random.randint(90, 130)
    attack = random.randint(5, 12)

    print("Your health is: " + str(health))
    print("Your attack is: " + str(attack))

    return(hero(name, age, gender, eyeColor, hairColor, health, attack))



def Main():
    mainHero = hero_creation()
    if mainHero == "quit":
        return

    jake = human("Jake", 35, "Male", "Blue", "Blonde", 80, 9)
    keith = human("Keith", 36, "Male", "Blue", "Blonde", 110, 2)
    logan = human("Logan", 23, "Male", "Blue", "Brown", 100, 7)

    villians = [jake, keith, logan] #when health hits 0, remove from list
    print("Sentinels ATTACKS!!!")

    while mainHero.health > 0:
        for villian in villians:
            if mainHero.health > 0 and villian.health > 0:
                mainHero.health_loss(villian.att())
            elif mainHero.health > 0 and villian.health <= 0:
                print(villian.name + " ran to mama!")
                #villians.remove(villian)
        if villians[0].health == 0 and villians[1] == 0 and villians[2] == 0:
            print("Great job Neo!")
        if mainHero.health > 0:
            hero_decision(mainHero, villians)


        if mainHero.health == 0:
            print("\n You have died!")
            print("""           ______
        .-"      "-.
       /            \
      |              |
      |,  .-.  .-.  ,|
      | )(__/  \__)( |
      |/     /\     \|
      (_     ^^     _)
       \__|IIIIII|__/
        | \IIIIII/ |
        \          /
         `--------""")


        if mainHero.health < 0:
            print("KO")
            print("""           ______
        .-"      "-.
       /            \
      |              |
      |,  .-.  .-.  ,|
      | )(__/  \__)( |
      |/     /\     \|
      (_     ^^     _)
       \__|IIIIII|__/
        | \IIIIII/ |
        \          /
         `--------""")


def hero_decision(mainHero, villians):
    print("1. Attack Jake ")
    print("2. Attack Keith ")
    print("3. Attack Logan ")
    print("4. Chance to instant kill Logan ")
    print("5. Attempt to kill all humans with insta ability strike ")
    print("6. Drink a potion ")
    print("7. Attack humans that have inferior eye color to yours ")
    print()

    choiceOfAttack = 0

    while choiceOfAttack not in range(1, 8):
        while True:
            try:
                choiceOfAttack = int(input("Select your move, warrior!")) #puts number in as an int vs string
                break
            except:
                print("Incorrect Input.")

    while 1:
        try:
            choiceOfAttack = int(input("Select your next move, warrior!")) #converts number to int vs string
            break
        except:
            print("Incorrect Input \n Select your next move, warrior!")

    while choiceOfAttack not in range(1,8): #fix this
        choiceOfAttack = (input("That is an invalid selection. \n Select your next move!"))


    if choiceOfAttack == 1:
        crit = random.randint(1, 10) #10 percent chance for critical
        if crit == 1 or crit == 2:
            villians[0].health_loss(mainHero.pantsless_crit())
        else:
            villians[0].health_loss(mainHero.att())

    if choiceOfAttack == 2:
        crit = random.randint(1, 10)
        if crit == 1 or crit == 2:
            villians[1].health_loss(mainHero.pantsless_crit())
        else:
            villians[1].health_loss(mainHero.att())

    if choiceOfAttack == 3:
        crit = random.randint(1, 10)
        if crit == 1 or crit == 2:
            villians[2].health_loss(mainHero.pantsless_crit())
        else:
            villians[2].health_loss(mainHero.att())

    if choiceOfAttack == 4:
        crit = random.randint(1, 10)
        if crit == 1:
            villians[2].health = 0
        else:
            print("You face plant and lose 1 health.")
            mainHero.health -= 1

    if choiceOfAttack == 5:
        crit = random.randint(1, 10)
        print("You attempt to kill all humans, cool story bro!")
        if crit == 1 or crit == 2 or crit == 3:
            villians[0].health = 0
            villians[1].health = 0
            villians[2].health = 0
            print("You are the chosen one!")
        else:
            mainHero.health = mainHero.health // 2
            print("Fail!")
            print(mainHero.name + "Health: " + str(mainHero.health))

    if choiceOfAttack == 6:
        mainHero.healing_potion()

    if choiceOfAttack == 7:
        mainHero.inferior_eyecolor_attack(villians)

Main()
