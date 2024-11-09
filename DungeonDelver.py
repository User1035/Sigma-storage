import random, Weapons, Character

monster_hp = 0
ran_loot = 0
rock_has = 0
encounter = 0
spare_food = 0
monster_dm = 0


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
            if character.health <= 0:
                print("you are eaten by the wolf pack")
                break
        looting()
    elif encounter == 8:
        print("You encounter a strange man on a bridge")
        str(input("What is your name"))
        str(input("what is your quest"))
        str(input("what is your favorite colour"))
        print("Right, off you go")
        looting()
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
            if character.is_dead():
                print("the skinny goblin smiles with glee")
                return()
            monster_hp = 7
            monster_dm = 3
            monster_name = "the tall lanky goblin who knows karate"
            monster_attack()
            if character.is_dead():
                print("the lanky goblin shadowboxes on your corpse")
                return()
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
        if character.is_dead():
            return ()
        print("The dragon releases out a thunderous roar")
        monster_hp = 30
        monster_dm = 5
        monster_attack()
        looting()
        looting()
    elif encounter == 13:
        print("COMBAT!")
        monster_hp = 30
        monster_dm = 3
        monster_name = "the lich"
        monster_attack()
        if character.is_dead():
            print("The lich revives you as an undead servant")
            return ()
        print("the lich backs away, sending his undead minions instead")
        monster_hp = 20
        monster_dm = 1
        monster_name = "the zombie"
        if character.is_dead():
            print("The lich revives you as an undead servant")
            return ()
        monster_attack()
        monster_hp = 8
        monster_dm = 3
        monster_name = "the sceleton"
        if character.is_dead():
            print("The lich revives you as an undead servant")
            return ()
        print("the lich returns to the battle, though he is still injured from earlier")
        monster_hp = 20
        monster_dm = 5
        monster_name = "the wounded lich"
        monster_attack()
        looting()
        looting()
    else:
        print("you find goku?")
        monster_name = "goku"
        if rock_has == 1 and spare_food == 1:
            print("The magic rock seems to sap much of goku's power, and you give him some of your spare food.")
            monster_hp = 60
            monster_dm = 7
        elif rock_has == 1:
            print("The magic rock seems to sap much of goku's power, can you win?")
            monster_hp = 60
            monster_dm = 10
        elif spare_food == 1:
            print("You give goku some of your spare food, it still looks quite bleak though")
            monster_hp = 100
            monster_dm = 12
        else:
            monster_hp = 100
            monster_dm = 15
        monster_attack()
        if character.is_alive():
            print("did you just kill goku? Uh you win I guess, nice job!")
        else:
            return()
        exit()


def looting():
    global ran_loot, rock_has, spare_food
    if character.is_alive():
        print("You search the room")
    else:
        return()
    ran_loot = encounter + random.randint(1, 3)
    # give me liberty, give me fire, give me if statements, or I retire
    if ran_loot == 2:
        print("you find a moldy piece of bread, you attempt to cut of the mold and heal 1 health")
        character.heal(1)
    elif ran_loot == 3:
        print("you find some rats, you cook them and eat them healing 3 health.")
        character.heal(3)
    elif ran_loot == 4:
        print("you find a health potion, it heals you 8 health")
        character.heal(8)
    elif ran_loot == 5:
        print("you find a rusty buckler, that can take a parry instead of your weapon twice")
        character.weapon.enhance_durability(2)
        y = random.randint(0, 2)
        if y == 1:
            print("you also find a boiled egg that heals you 3 health")
            character.heal(3)
        elif y == 2:
            print("you also find a moldy piece of bread, you attempt to cut of the mold and heal 1 health")
            character.heal(1)
    elif ran_loot == 6:
        print("you find a general potion, it heals you 5 health and repairs your weapon slightly")
        character.heal(5)
        character.weapon.enhance_durability(2)
    elif ran_loot == 7:
        print("you find a greater healing potion, it heals you 10 health")
        character.heal(10)
    elif ran_loot == 8:
        print("you find an iron buckler, it can parry instead of your weapon 4 times")
        character.weapon.enhance_durability(4)
        y = random.randint(0, 2)
        if y == 1:
            print("you also find a piece of bread that heals you 4 health")
            character.heal(4)
        elif y == 2:
            print("you also find a steak that heals you 6 health")
            character.heal(6)
    elif ran_loot == 9 or ran_loot == 10:
        if rock_has == 0:
            print("you find an enchanted rock, could come in handy")
            rock_has = 1
        print("your rock glows, you heal 12")
        character.heal(12)
    elif ran_loot == 11:
        print("you find a goblin feast, you heal 15 and gain some spare food")
        character.heal(15)
        spare_food = 1
    elif ran_loot == 12:
        print("you find an armoury, and take a side dagger boosting your damage")
        character.weapon.enhance_damage(2)
        character.weapon.enhance_durability(2)
    elif ran_loot == 13:
        print("you find a divine potion, healing you 20 and restoring your weapon massively")
        character.heal(20)
        character.weapon.enhance_durability(4)
    elif ran_loot == 14:
        if rock_has == 0:
            print("you find an enchanted rock, could come in handy")
            rock_has = 1
        print("your rock glows, your damage increases and you heal 5")
        character.weapon.enhance_damage(2)
        character.heal(5)
    elif ran_loot == 15:
        print("you find a pantry containing fresh food, you heal 20 and gain some spare food")
        character.heal(20)
        spare_food = 1
    else:
        print("you find nothing")


def monster_attack():
    global monster_hp
    print("you encounter", monster_name)
    while monster_hp > 0 and character.is_alive():
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
            character.injure(incoming)
        elif fight_act == "2":
            print("you go to strike the enemy")
            print("your damage is", character.weapon.damage)
            monster_hp = monster_hp - character.weapon.damage
            character.injure(incoming)
        elif fight_act == "3":
            print("You try to parry with your", character.weapon.name())

            if isinstance(character.weapon, Weapons.Unarmed):
                print("you try and parry with your fists, It has no effect")
                character.injure(incoming)
            else:
                character.weapon.damaged(1)
                if character.weapon.durability <= 0:
                    print("you parry but your " + character.weapon.name() + " shatters!")
                    character.weapon = Weapons.Unarmed()
                else:
                    print("you parry but your " + character.weapon.name() + " is damaged")
                    print("your weapon is", character.weapon.durability, "hits away from being destroyed")
        else:
            print("you miss your opportunity to act")
            character.injure(incoming)
    if character.is_alive():
        print("You win!")
    else:
        print("Your dead")
        return()

running = 1
while running == 1:

    character = Character.Character()
    monster_hp = 0
    ran_loot = 0
    rock_has = 0
    encounter = 0
    spare_food = 0
    monster_dm = 0
    monster_name = 0

    weaponChoice = int(input("please select your starting weapon,"
                             " 1 for a bow, 2 for a sword, 3 for an axe, 4 for a spear"))
    match weaponChoice:
        case Weapons.WeaponTypes.AXE:
            character.weapon = Weapons.Axe()
        case Weapons.WeaponTypes.SWORD:
            character.weapon = Weapons.Sword()
        case Weapons.WeaponTypes.BOW:
            character.weapon = Weapons.Bow()
        case Weapons.WeaponTypes.SPEAR:
            character.weapon = Weapons.Spear()

    # Welcome to the dungeon message
    print("You enter the dungeon with " + format(character.health) +
          " health and walk into the first room, " + character.weapon.active_description())

    # changing starting message to show what weapon you have picked
    for x in range(5):
        encounter = encounter + random.randint(1, 3)
        kick_down_door()
        if character.is_dead():
            break
    if character.is_dead():
        running = int(input("continue? 1 for yes 2 for no"))
    else:
        encounter = 100
        kick_down_door()
    running = int(input("continue? 1 for yes 2 for no"))