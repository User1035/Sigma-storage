from typing import Final


class Monster:

    def __init__(self):
        self.monster_hp = 0
        self.monster_dm = 0

    def damaged(self, amount_of_damage):
        self.monster_hp = self.monster_hp - amount_of_damage


class GiantSpider(Monster):
    def __init__(self):
        self.hp = 4
        self.dm = 3
        self.name = "the giant spider"


class Rat(Monster):
    def __init__(self):
        self.hp = 8
        self.dm = 1
        self.name = "the giant rat"


class FatGoblin(Monster):
    def __init__(self):
        self.hp = 8
        self.dm = 1
        self.name = "the fat goblin"


class CaveBear(Monster):
    def __init__(self):
        self.hp = 15
        self.dm = 4
        self.name = "the cave bear"


class CrystalBeast(Monster):
    def __init__(self):
        self.hp = 20
        self.dm = 5
        self.name = "the Crystal beast"


class BerserkGoblin(Monster):
    def __init__(self):
        self.hp = 12
        self.dm = 6
        self.name = "the berserk goblin"


class Wolf(Monster):
    def __init__(self):
        self.hp = 7
        self.dm = 3
        self.name = "the wolf"


class GiantGolem(Monster):
    def __init__(self):
        self.hp = 30
        self.dm = 5
        self.name = "the giant golem"


class LargeMole(Monster):
    def __init__(self):
        self.hp = 20
        self.dm = 6
        self.name = "the uncomfortably large mole"


class GoblinKing(Monster):
    def __init__(self):
        self.hp = 50
        self.dm = 2
        self.name = "the goblin king"


class RedDragon(Monster):
    def __init__(self):
        self.hp = 25
        self.dm = 5
        self.name = "the red dragon"


class Lich(Monster):
    def __init__(self):
        self.hp = 25
        self.dm = 4
        self.name = "the lich"


class Zombie(Monster):
    def __init__(self):
        self.hp = 20
        self.dm = 2
        self.name = "the zombie"
