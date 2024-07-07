from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass


class Sword(Weapon):
    def attack(self):
        print("Боец наносит удар мечом.")
        # return True

class Bow(Weapon):
    def attack(self):
        print("Боец стреляет из лука.")


class Molot(Weapon):
    def attack(self):
        print("Боец бьет молотом.")


class Fighter:
    def __init__(self, weapon=None):
        self.weapon = weapon

    def change_weapon(self, weapon):
        self.weapon = weapon
        print("Боец сменил оружие.")

    def fight(self):
       self.weapon.attack()
       print(f"Монстр {monster.name} побежден! \n")



class Monster:
    def __init__(self, name):
        self.name = name


sword1 = Sword()
bow1 = Bow()
molot1 = Molot()
monster = Monster("Вася")
fighter = Fighter(bow1)

fighter.fight()

monster = Monster("Петя")
fighter.change_weapon(sword1)
fighter.fight()

monster = Monster("Толя")
fighter.change_weapon(molot1)
fighter.fight()