class Weapon:
    def shoot(self):
        pass
class Pistol(Weapon):
    def shoot(self):
        print("пистолет стреляет")
class LaserGun(Weapon):
    def shoot(self):
        print("Бззз! Лазер стреляет")
class Player:
    def __init__(self, weapon: Weapon):
        self.weapon = weapon
    def attack(self):
        self.weapon.shoot()
