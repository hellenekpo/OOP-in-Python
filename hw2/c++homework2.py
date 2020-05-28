class Weapon:
    def __init__(self, name, strength):
        self.name = name
        self.strength = strength
    def __str__(self):
        return self.name + ", " + str(self.strength)

class Warrior:

    def __init__(self, name, weaponName, strength):
        self.name = name
        self.weapon = Weapon(weaponName, strength)

    def __str__(self):
        return "Warrior: " + self.name + ", Weapon: " + str(self.weapon)

    def battle(self, other):
        print(self.name + " battles " + other.name)
        if (self.weapon.strength > other.weapon.strength):
            if (other.weapon.strength == 0):
                print("He's dead, " + self.name)
            else:
                print(self.name + " defeats " + other.name)
                self.weapon.strength -= other.weapon.strength
                other.weapon.strength = 0
        elif (self.weapon.strength < other.weapon.strength):
            if (self.weapon.strength == 0):
                print("He's dead, " + other.name + "\n")
            else:
                print(other.name + " defeats " + self.name)
                other.weapon.strength -= self.weapon.strength
                self.weapon.srength = 0
        elif (self.weapon.strength == other.weapon.strength):
            if (self.weapon.strength == 0):
                print("Oh, NO! They're both dead! YUCK!")
            else:
                print("Mutual Annihilation: " + self.name + " and " +
                      other.name + " die at each others hands!")
                self.weapon.strength = 0
                other.weapon.strength = 0
                
def status(listWarriors):
    print("There are", len(listWarriors), "warriors")
    for i in range(len(listWarriors)):
        print(listWarriors[i])

            

def main():
    listWarriors = []
    war1 = Warrior("Jim", "Glamdring", 42)
    war2 = Warrior("Lancelot", "Naegling", 15)
    war3 = Warrior("Arthur", "Excalibur", 15)
    war4 = Warrior("Torvalds", "Narsil", 20)
    war5 = Warrior("Gates", "Orcrist", 8)
    listWarriors.append(war1)
    listWarriors.append(war2)
    listWarriors.append(war3)
    listWarriors.append(war4)
    listWarriors.append(war5)
    status(listWarriors)
    war3.battle(war2)
    war1.battle(war2)
    war4.battle(war5)
    war5.battle(war2)
    status(listWarriors)
