import random
from typing import Final


class WeaponTypes:
    BOW: Final[int] = 1
    SWORD: Final[int] = 2
    AXE: Final[int] = 3
    SPEAR: Final[int] = 4


class Weapon:

    def __init__(self):
        self.durability = 0
        self.damage = 0

    def active_description(self):
        return ""

    def name(self):
        return "A Weapon"

    def enhance_durability(self, amount_of_enhancement):
        self.durability = self.durability + amount_of_enhancement

    def damaged(self, amount_of_damage):
        self.durability = self.durability - amount_of_damage

    def enhance_damage(self, amount_of_enhancement):
        self.damage = self.damage + amount_of_enhancement


class Bow(Weapon):
    def __init__(self):
        self.durability = random.randint(2, 4)
        self.damage = 6

    def active_description(self):
        return "bow gripped tight in your hand"

    def name(self):
        return "bow"


class Sword(Weapon):
    def __init__(self):
        self.durability = random.randint(7, 9)
        self.damage = 4

    def active_description(self):
        return "your trusty blade held tight"

    def name(self):
        return "sword"


class Axe(Weapon):
    def __init__(self):
        self.durability = random.randint(4, 6)
        self.damage = 5

    def active_description(self):
        return "gripping the handle of your axe"

    def name(self):
        return "axe"


class Unarmed(Weapon):
    def __init__(self):
        self.durability = 0
        self.damage = 1

    def active_description(self):
        return "shaking as you walk unarmed"

    def name(self):
        return "bare hands"


class Spear(Weapon):
    def __init__(self):
        self.durability = random.randint(6, 10)
        self.damage = 4

    def active_description(self):
        return "with your spear at the ready"

    def name(self):
        return "spear"
