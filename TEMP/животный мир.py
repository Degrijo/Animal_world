
import math
import re
import random

data = 0 # колво ходов
all_objects = []

class unit():
    hp=int()
    X=int()
    Y=int()
    lifespend=int()
    #_seks=7
    damage=int()
    energe=int()
    def __init__(self,coord):
        self.coord = coord
    def aging(self): # старение (веяние смерти)
        if data%5 == 0:
            self.lifespend += 1
        self.hp -= self.lifespend
        self.death()
    def death(self):
        if self.hp <= 0:
            del self
    def renovation(self):
        self.energe += 1
    def get_inf(self):
        print("HP of this unit is ",self.hp)
        print("Energy of this unit is ",self.energe)

class plant(unit):
    def aging(self):
        self.hp -= self.lifespend
        if self.hp <= 0:
            del self

class vegeterian(unit):
    def eat_plant (self,plant):
        if plant == cactus():
            if self.energe >=1:
                self.hp += self.damage
                self.energe -= 1
                plant.hp -= self.damage
                plant.death()
            else:
                print("Not enough energy")
        else:
            print("This is not a plant")
    def dvig(self,coord):
        if self.energe >= 1*(math.fabs(coord[0] - self.coord[0]) + math.fabs(coord[1] - self.coord[1])): #хватает ли энергии на движение
            self.energe -= 1*(math.fabs(coord[0] - self.coord[0]) + math.fabs(coord[1] - self.coord[1])) #потеря энергии 1 за клетку
            self.coord = coord
        else:
            print("Не хватает энергии, дождитесь следующего хода")

class predator(unit): #хищник
    def eat_meat (self,animal):
        if self.energe >=1:
            temp=True
            if re.findall(r'^[a-z]+', str(animal)[10:])[0] == 'acacia':
                print("This is not a plant")
                temp=False
            elif re.findall(r'^[a-z]+', str(animal)[10:])[0] == 'cheetah':
                a = random.randint(1,10)
                if a <=3:
                    temp=False
                    self.energy-=1
            elif re.findall(r'^[a-z]+', str(animal)[10:])[0] == 'vulture':
                self.hp -= 1
            elif re.findall(r'^[a-z]+', str(animal)[10:])[0] == 'elephant':
                animal.hp += 1
                self.hp -= 1
            elif re.findall(r'^[a-z]+', str(animal)[10:])[0] == 'giraffe':
                animal.energe += 1
            if re.findall(r'^[a-z]+', str(self)[10:])[0] == 'hyena' and self.count_attacks == 0:
                self.energe += 1
                self.count_attacks += 1
            if temp == True:
                self.hp += self.damage
                self.energe -= 1
                animal.hp -= self.damage
                animal.death()
        else:
            print("Not enough energy")
    def dvig(self,coord):
        if self.energe >= 1*(math.fabs(coord[0] - self.coord[0]) + math.fabs(coord[1] - self.coord[1])): #хватает ли энергии на движение
            self.energe -= 1*(math.fabs(coord[0] - self.coord[0]) + math.fabs(coord[1] - self.coord[1])) #потеря энергии 1 за клетку
            self.coord = coord
        else:
            print("Не хватает энергии, дождитесь следующего хода")

class vulture(predator): #гриф
    hp=20
    energe=2
    damage=3
    lifespend=1
    

class cheetah(predator): #гепард
    hp=17
    energe=4
    damage=4
    lifespend=3

class hyena(predator): #гиена
    hp=15
    energe=3
    damage=2
    lifespend=2
    count_attacks=0
    def renovation(self):
        self.energe += 1
        self.count_attacks = 0

class elephant(vegeterian): #слон
    hp=30
    energe=3
    damage=2
    lifespend=2

class giraffe(vegeterian): #жираф
    hp=27
    energe=2
    damage=1
    lifespend=1
        
class zebra(vegeterian): #зебра
    hp=25
    energe=4
    damage=1
    lifespend=2
    def aging(self):
        if self.hp < 10:
            self.lifespend = 0
        else:
            self.lifespend = 2 + data/5
        self.hp -= self.lifespend
        self.death()

class acacia(plant): # кактус
    hp=15
    lifespend=1

def add_object(coord):#dont work
    #print("Введите номер вида юнита, которого хотите создать")
    #klass = input("1 - Гриф, 2 - Гепард, 3 - Гиена, 4 - Слон, 5 - Жираф, 6 - Зебра или 7 - Кактус    ")
    if klass == 1:
        all_objects.append(vulture(X,Y))
    elif klass == 2:
        all_objects.append(cheetah(X,Y))
    elif klass == 3:
        all_objects.append(hyena(X,Y))
    elif klass == 4:
        all_objects.append(elephant(X,Y))
    elif klass == 5:
        all_objects.append(giraffe(X,Y))
    elif klass == 6:
        all_objects.append(zebra(X,Y))
    elif klass == 7:
        all_objects.append(acacia(X,Y))
    

'''gepard = cheetah()
giena = hyena()
for i in range(4):
    giena.eat_meat(gepard)
    print("Гиена")
    giena.get_inf()
    print("Гепард")
    gepard.get_inf()'''
