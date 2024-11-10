import Weapons


class Character:

    def __init__(self):
        self.health = 30
        self.weapon = Weapons.Unarmed()

    def injure(self, amount_of_damage):
        self.health = self.health - amount_of_damage
        print("you have", self.health, "health remaining")

    def heal(self, amount_of_healing):
        self.health = self.health + amount_of_healing

    def is_alive(self):
        return self.health > 0

    def is_dead(self):
        return self.health <= 0
