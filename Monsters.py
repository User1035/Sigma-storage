from typing import Final


class Monster:

    def __init__(self):
        self.monster_hp = 0
        self.monster_dm = 0

    def damaged(self, amount_of_damage):
        self.monster_hp = self.monster_hp - amount_of_damage


class GiantSpider(Monster):
    def __init__(self):
        self.monster_hp = 4
        self.monster_dm = 3
        self.name = "the giant spider"


class Rat(Monster):
    def __init__(self):
        self.monster_hp = 8
        self.monster_dm = 1
        self.name = "the giant rat"


class FatGoblin(Monster):
    def __init__(self):
        self.monster_hp = 8
        self.monster_dm = 1
        self.name = "the fat goblin"


class CaveBear(Monster):
    def __init__(self):
        self.monster_hp = 15
        self.monster_dm = 4
        self.name = "the cave bear"


class CrystalBeast(Monster):
    def __init__(self):
        self.monster_hp = 20
        self.monster_dm = 5
        self.name = "the Crystal beast"


class BerserkGoblin(Monster):
    def __init__(self):
        self.monster_hp = 12
        self.monster_dm = 6
        self.name = "the berserk goblin"


class Wolf(Monster):
    def __init__(self):
        self.monster_hp = 7
        self.monster_dm = 3
        self.name = "the wolf"


class GiantGolem(Monster):
    def __init__(self):
        self.monster_hp = 30
        self.monster_dm = 5
        self.name = "the giant golem"


class LargeMole(Monster):
    def __init__(self):
        self.monster_hp = 20
        self.monster_dm = 6
        self.name = "the uncomfortably large mole"


class GoblinKing(Monster):
    def __init__(self):
        self.monster_hp = 50
        self.monster_dm = 2
        self.name = "the goblin king"


class RedDragon(Monster):
    def __init__(self):
        self.monster_hp = 25
        self.monster_dm = 5
        self.name = "the red dragon"


class Lich(Monster):
    def __init__(self):
        self.monster_hp = 25
        self.monster_dm = 4
        self.name = "the lich"


class Zombie(Monster):
    def __init__(self):
        self.monster_hp = 20
        self.monster_dm = 2
        self.name = "the zombie"
