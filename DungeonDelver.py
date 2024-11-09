import random
from typing import Final

monster_hp = 0
ran_loot = 0
rock_has = 0
encounter = 0
spare_food = 0
monster_dm = 0

BOW: Final[int] = 1
SWORD: Final[int] = 2
AXE: Final[int] = 3

def kick_down_door():
    # IF SPAM GO!
    global encounter, monster_name, monster_hp, monster_dm, rock_has, spare_food
    if encounter == 1:
        print("COMBAT!")
        monster_name = "the giant spider"
        monster_hp = 4
        monster_dm = 2
        monster_attack()
        looting()
    elif encounter == 2:
        print("COMBAT!")
        monster_name = "the giant rat"
        monster_hp = 8
        monster_dm = 1
        monster_attack()
        looting()
    elif encounter == 3:
        print("COMBAT!")
        monster_name = "the fat goblin"
        monster_hp = 10
        monster_dm = 1
        monster_attack()
        looting()
    elif encounter == 4:
        print("COMBAT!")
        monster_name = "the cave bear"
        monster_hp = 15
        monster_dm = 3
        monster_attack()
        looting()
    elif encounter == 5:
        print("COMBAT!")
        monster_name = "the crystal beast"
        monster_hp = 20
        monster_dm = 2
        monster_attack()
        looting()
    elif encounter == 6:
        print("COMBAT!")
        monster_name = "the berserk goblin"
        monster_hp = 12
        monster_dm = 4
        monster_attack()
        looting()
    elif encounter == 7:
        print("A wolf pack attacks you!")
        for p in range(3):
            monster_name = "a wolf"
            monster_hp = 7
            monster_dm = 2
            monster_attack()
            if health <= 0:
                print("you are eaten by the wolf pack")
                break
        looting()
    elif encounter == 8:
        print("You encounter a strange man on a bridge")
        str(input("What is your name"))
        str(input("what is your quest"))
        str(input("what is your favorite colour"))
        print("Right, off you go")
    elif encounter == 9:
        print("COMBAT!")
        monster_name = "the giant golem"
        if rock_has == 1:
            print("A giant golem blocks your way, but it crumbles after seeing the enchanted stone")
        else:
            monster_hp = 30
            monster_dm = 4
            monster_attack()
        looting()
    elif encounter == 10:
        print("COMBAT!")
        monster_name = "the uncomfortably large mole"
        monster_hp = 16
        monster_dm = 5
        monster_attack()
        looting()
    elif encounter == 11:
        print("you enter a huge hall of goblins,")
        if spare_food == 1:
            print("You give the goblin king your spare food. He chuckles and challenges you to a fight")
        else:
            monster_hp = 5
            monster_dm = 1
            monster_name = "the very skinny goblin"
            monster_attack()
            monster_hp = 7
            monster_dm = 3
            monster_name = "the tall lanky goblin who knows karate"
            monster_attack()
        monster_hp = 50
        monster_dm = 1
        monster_name = "the goblin king"
        monster_attack()
        looting()
        looting()
    elif encounter == 12:
        print("COMBAT!")
        monster_hp = 25
        monster_dm = 4
        monster_name = "the red dragon"
        monster_attack()
        print("The dragon releases out a thunderous roar")
        monster_hp = 30
        monster_dm = 5
        monster_attack()
        looting()
        looting()
    else:
        print("you find goku?")
        monster_name = "goku"
        if rock_has == 1 and spare_food == 1:
            print("The magic rock seems to sap much of gokus power, and you give him some of your spare food.")
            monster_hp = 45
            monster_dm = 8
        elif rock_has == 1:
            print("The magic rock seems to sap much of gokus power, can you win?")
            monster_hp = 60
            monster_dm = 10
        elif spare_food == 1:
            print("You give goku some of your spare food, it still looks quite bleak though")
            monster_hp = 85
            monster_dm = 12
        else:
            monster_hp = 100
            monster_dm = 15
        monster_attack()
        if health >= 0:
            print("did you just kill goku? Uh you win I guess, nice job!")
        else:
            return()
        exit()


def looting():
    global ran_loot, health, weapon_dur, rock_has, spare_food, weapon_dam
    if health >= 0:
        print("You search the room")
    else:
        return()
    ran_loot = encounter + random.randint(1, 3)
    # give me liberty, give me fire, give me if statements, or I retire
    if ran_loot == 2:
        print("you find a moldy piece of bread, you attempt to cut of the mold and heal 1 health")
        health = health + 1
    elif ran_loot == 3:
        print("you find some rats, you cook them and eat them healing 3 health.")
        health = health + 3
    elif ran_loot == 4:
        print("you find a health potion, it heals you 8 health")
        health = health + 8
    elif ran_loot == 5:
        print("you find a rusty buckler, that can take a parry instead of your weapon twice")
        weapon_dur = weapon_dur + 2
        y = random.randint(0, 2)
        if y == 1:
            print("you also find a boiled egg that heals you 3 health")
            health = health + 3
        elif y == 2:
            print("you also find a moldy piece of bread, you attempt to cut of the mold and heal 1 health")
            health = health + 1
    elif ran_loot == 6:
        print("you find a general potion, it heals you 5 health and repairs your weapon slightly")
        health = health + 5
        weapon_dur = weapon_dur + 2
    elif ran_loot == 7:
        print("you find a greater healing potion, it heals you 10 health")
        health = health + 10
    elif ran_loot == 8:
        print("you find an iron buckler, it can parry instead of your weapon 4 times")
        weapon_dur = weapon_dur + 4
        y = random.randint(0, 2)
        if y == 1:
            print("you also find a piece of bread that heals you 4 health")
            health = health + 4
        elif y == 2:
            print("you also find a steak that heals you 6 health")
            health = health + 6
    elif ran_loot == 9 or ran_loot == 10:
        if rock_has == 0:
            print("you find an enchanted rock, could come in handy")
            rock_has = 1
        print("your rock glows, you heal 12")
        health = health + 12
    elif ran_loot == 11:
        print("you find a goblin feast, you heal 15 and gain some spare food")
        health = health + 15
        spare_food = 1
    elif ran_loot == 12:
        print("you find an armoury, and take a side dagger boosting your damage")
        weapon_dam = weapon_dam + 2
        weapon_dur = weapon_dur + 2
    elif ran_loot == 13:
        print("you find a divine potion, healing you 20 and restoring your weapon massively")
        health = health + 20
        weapon_dur = weapon_dur + 4
    elif ran_loot == 14:
        if rock_has == 0:
            print("you find an enchanted rock, could come in handy")
            rock_has = 1
        print("your rock glows, your damage increases and you heal 5")
        weapon_dam = weapon_dam + 2
        health = health + 5
    elif ran_loot == 15:
        print("you find a pantry containing fresh food, you heal 20 and gain some spare food")
        health = health + 20
        spare_food = 1
    else:
        print("you find nothing")


def monster_attack():
    global monster_hp, health, weapon_dam, weapon_dur
    print("you encounter", monster_name)
    while monster_hp > 0 and health > 0:
        incoming = random.randint(-2, 4) + monster_dm
        if incoming < 0:
            incoming = 0
        print(incoming, "damage incoming!")
        fight_act = input("1 for dodge, 2 for strike, 3 for parry")
        if fight_act == "1":
            print("you do a dodge roll reducing the damage by 3")
            incoming = incoming-3
            if incoming < 0:
                incoming = 0
            health = health - incoming
            print("you have", health, "health remaining")
        elif fight_act == "2":
            print("you go to strike the enemy")
            print("your damage is", weapon_dam)
            monster_hp = monster_hp-weapon_dam
            health = health - incoming
            print("you have", health, "health remaining")
        elif fight_act == "3":
            weapon_dur = weapon_dur-1
            if weapon_dur <= 0 and weapon_dam == 1:
                weapon_dur = 0
                health = health - incoming
                print("you try and parry with your fists, It has no effect")
                print("you have", health, "health remaining")
            elif weapon_dur <= 0:
                weapon_dur = 0
                print("you parry but your weapon shatters!")
                weapon_dam = 1
            else:
                print("you parry but your weapon is damaged")
                print("your weapon is", weapon_dur, "hits away from being destroyed")
        else:
            print("you miss your opportunity to act")
            health = health - incoming
            print("you have", health, "health remaining")
    if health > 0:
        print("You win!")
    else:
        print("Your dead")
        return()


running = 1
while running == 1:
    monster_hp = 0
    ran_loot = 0
    rock_has = 0
    encounter = 0
    spare_food = 0
    monster_dm = 0
    health = 30
    monster_name = 0
    weapon = int(input("please select your starting weapon, 1 for a bow, 2 for a sword, 3 for an axe"))
# selects starting weapon, and is stored as an integer
    if weapon == AXE:
        weapon_dur = random.randint(4, 6)
        weapon_dam = 5
    elif weapon == SWORD:
        weapon_dur = random.randint(7, 9)
        weapon_dam = 4
    elif weapon == BOW:
        weapon_dur = random.randint(2, 4)
        weapon_dam = 6
    else:   # what kind of weapon is this???
        weapon_dur = 0
        weapon_dam = 1
# basic code that assigns base characteristics based on the weapon
    if weapon == BOW:
        print("You enter the dungeon with 30 health and walk into the first room, bow gripped tight in your hand")
    elif weapon == SWORD:
        print("You enter the dungeon with 30 health and walk into the first room, your trusty blade held tight")
    elif weapon == AXE:
        print("You enter the dungeon with 30 health and walk into the first room, gripping the handle of your axe")
    else:
        print("You enter the dungeon and with 30 health walk into the first room, shaking as you walk unarmed")
# changing starting message to show what weapon you have picked
    for x in range(5):
        encounter = encounter + random.randint(1, 3)
        kick_down_door()
        if health <= 0:
            break
    if health <= 0:
        running = int(input("continue? 1 for yes 2 for no"))
    else:
        encounter = 100
        kick_down_door()
