from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass


class Sword(Weapon):
    def attack(self):
        print("Боец наносит удар мечом.")
        return True

class Bow(Weapon):
    def attack(self):
        print("Боец стреляет из лука.")


class Fighter:
    def __init__(self, weapon=None):
        self.weapon = weapon

    def change_weapon(self, weapon):
        self.weapon = weapon

    def fight(self, monster):
        if self.weapon.attack():
            print(f"Монстр {monster.name} побежден!")
        else:
            print(f"Монстр {monster.name} победил!")


class Monster:
    def __init__(self, name):
        self.name = name

fighter = Fighter(Bow())

monster = Monster("Гигантский паук")

fighter.change_weapon(Sword())

fighter.fight(monster)
