from typing import Final


class Monster:

    def __init__(self):
        self.monster_hp = 0
        self.monster_dm = 0

    def name(self):
        return "Monster"

    def damaged(self, amount_of_damage):
        self.monster_hp = self.monster_hp - amount_of_damage

class Rat(Monster):
    def __init__(self):
        self.monster_hp = 8
        self.monster_dm = 1
    def name(self):
        return "The giant rat"

class Fatgoblin(Monster):
    def __init__(self):
        self.monster_hp = 8
        self.monster_dm = 1
    def name(self):
        return "The fat goblin"
