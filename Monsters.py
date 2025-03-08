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
        self.name = "The giant spider"



class Rat(Monster):
    def __init__(self):
        self.monster_hp = 8
        self.monster_dm = 1
        self.name = "The giant rat"


class FatGoblin(Monster):
    def __init__(self):
        self.monster_hp = 8
        self.monster_dm = 1
        self.name = "The fat goblin"
