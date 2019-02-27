
import re

class man():
    hp=int()
    def __init__(self,hp = 10):
        self.hp=hp
    def death(self):
        if self.hp<=0:
            del self
    
class kamen():
    damage=int()
    def __init__(self,damage = 5):
        self.damage = damage
    def attack(self, enemy):
        if re.findall(r'^[a-z]+', str(enemy)[10:])[0] == 'man':
            enemy.hp -= self.damage
        else:
            print("Mistake")

Yarik = man(10)
bulignik = kamen(5)
bulignik.attack(Yarik)
# определить, является ли объект объектом определенного класса
 
