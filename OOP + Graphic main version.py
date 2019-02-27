
import pygame
import random
import math
import time
import re

# прорисовку промежуточных фаз движения
# добавить конструктор карты и название игры на главный экран
# добавить звуки и музыку, мб анимации смерти и атаки
# возможность назначить управление животным боту

pygame.init()
window = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
clock = pygame.time.Clock()

bg = pygame.image.load("Sprites/bg.jpg")
game_map = pygame.image.load("Sprites/game_map_new.jpg")
smallText = pygame.font.Font('freesansbold.ttf',20)
pygame.mixer.music.load('Music and Sounds/The Lion Sleeps Tonight.mp3')
#pygame.mixer.music.set_volume
pygame.mixer.music.play(-1)
sound_click = pygame.mixer.Sound("Music and Sounds/Sounds/final/click.wav")

pygame.display.update()

data = 0
all_objects = []
hero = None
wos = 196 # width_of_square
hos = 192 # heigth_of_square

move = False
eat = False
spawn = False

class unit():
    hp=int()
    X=int()
    Y=int()
    lifespend=int()
    #_seks=7
    damage=int()
    energe=int()
    name = str()
    last_move = "right"
    def __init__(self,name,X,Y):
        self.X = X
        self.Y = Y
        self.name = name[:-1]
    def aging(self):
        if data%5 == 0:
            self.lifespend += 1
        self.hp -= self.lifespend
    def renovation(self):
        self.energe += 1
    def spawn(self,new_X,new_Y):
        if self.energe < 5:
            attention("Don't have enough energy")
        elif self.energe >=5: # Проверить наличие энергии у второго животного
            self.energe -= 5
            add_object(new_X,new_Y,re.findall(r'^[a-z]+', str(self)[10:])[0])
    def draw(self):
        window.blit(self.pict[self.last_move],(108 + wos*self.X+75, 108 + hos*self.Y))
    def dvig(self,new_X,new_Y):
        if self.energe >= 1*(abs(new_X - self.X) + abs(new_Y - self.Y)):
            if (new_X - self.X) > 0:
                self.last_move = "right"
            elif (new_X - self.X) < 0:
                self.last_move = "left"
            elif (new_X - self.X) == 0 and (new_Y - self.Y) > 0:
                self.last_move = "down"
            elif (new_X - self.X) == 0 and (new_Y - self.Y) < 0:
                self.last_move = "up"
            self.energe -= 1*(abs(new_X - self.X) + abs(new_Y - self.Y))
            self.X = new_X
            self.Y = new_Y
        else:
            attention("Don't have enough energy")
    def show_inf(self):
        window.blit(self.pict["art"],(192,696))

        textSurf, textRect = text_objects(re.findall(r'^[a-z]+', str(self)[10:])[0] + " " + self.name, smallText)
        textRect.center = ((605),(720))
        window.blit(textSurf, textRect)
        
        textSurf, textRect = text_objects("HP of this unit is " + str(self.hp), smallText)
        textRect.center = ((605),(780))
        window.blit(textSurf, textRect)
        
        textSurf, textRect = text_objects("Energy of this unit is " + str(self.energe), smallText)
        textRect.center = ((620),(840))
        window.blit(textSurf, textRect)

        textSurf, textRect = text_objects("Damage of this unit is " + str(self.damage), smallText)
        textRect.center = ((626),(900))
        window.blit(textSurf, textRect)

        textSurf, textRect = text_objects("Lifespend of this unit is " + str(self.lifespend), smallText)
        textRect.center = ((636),(960))
        window.blit(textSurf, textRect)

        
class plant(unit):
    def aging(self):
        self.hp -= self.lifespend

class vegeterian(unit):
    seks = str()
    def __init__(self,name,seks,X,Y):
        self.X = X
        self.Y = Y
        self.name = name
        self.seks = seks
    def eat (self,plant):
        if re.findall(r'^[a-z]+', str(plant)[10:])[0] == 'acacia':
            if self.energe >=1:
                if (plant.X - self.X) > 0:
                    self.last_move = "right"
                elif (plant.X - self.X) < 0:
                    self.last_move = "left"
                elif (plant.X - self.X) == 0 and (plant.Y - self.Y) > 0:
                    self.last_move = "down"
                elif (plant.X - self.X) == 0 and (plant.Y - self.Y) < 0:
                    self.last_move = "up"
                self.hp += self.damage
                self.energe -= 1
                plant.hp -= self.damage
                sound = pygame.mixer.Sound("Music and Sounds/Sounds/final/eating_branches.wav")
                sound.play()
            else:
                attention("Don't have enough energy")
        else:
            attention("This is not a plant! Vegeterian animals can attack and eat only plants")

class predator(unit): #хищник
    seks = str()
    def __init__(self,name,seks,X,Y):
        self.X = X
        self.Y = Y
        self.name = name
        self.seks = seks
    def eat (self,animal):
        if self.energe >=1:
            temp=True
            if re.findall(r'^[a-z]+', str(animal)[10:])[0] == 'acacia':
                attention("This is not an animal")
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
                if (animal.X - self.X) > 0:
                    self.last_move = "right"
                elif (animal.X - self.X) < 0:
                    self.last_move = "left"
                elif (animal.X - self.X) == 0 and (animal.Y - self.Y) > 0:
                    self.last_move = "down"
                elif (animal.X - self.X) == 0 and (animal.Y - self.Y) < 0:
                    self.last_move = "up"
                self.hp += self.damage
                self.energe -= 1
                animal.hp -= self.damage
                sound = pygame.mixer.Sound("Music and Sounds/Sounds/final/eating_branches.wav")
                sound.play()
        else:
            attention("Don't have enough energy")

def attention(msg):
    run = True
    text = []
    while len(msg) >= 50:
        text.append(msg[0:50])
        msg = msg[50:]
    text.append(msg)
    while run:
        pygame.draw.rect(window, (255,255,255),(700,400,500,200))
        for line in range(0,len(text)):
            textSurf, textRect = text_objects(text[line], smallText)
            textRect.center = ((950), (440+line*25))
            window.blit(textSurf, textRect)
        button("OK",900,500,100,70,(255,255,255),(255,255,255))
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if 900 + 100 > mouse[0] > 900 and 500 + 70 > mouse[1] > 500:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    run = False
        pygame.display.update()

class vulture(predator): #гриф
    hp=25
    energe=2
    damage=3
    lifespend=1
    pict = {"small_art" : pygame.image.load("Sprites/vulture_small.png"),"art" : pygame.image.load("Sprites/vulture.jpg"),"right" : pygame.image.load("Sprites/vulture_right.png"),"down" : pygame.image.load("Sprites/vulture_down.png"),"left" : pygame.image.load("Sprites/vulture_left.png"),"up" : pygame.image.load("Sprites/vulture_up.png")}
    sound = pygame.mixer.Sound("Music and Sounds/Sounds/final/vulture.wav")

class cheetah(predator): #гепард
    hp=23
    energe=4
    damage=4
    lifespend=3
    pict = {"small_art" : pygame.image.load("Sprites/cheetah_small.png"),"art" : pygame.image.load("Sprites/cheetah.jpg"),"right" : pygame.image.load("Sprites/cheetah_right.png"),"down" : pygame.image.load("Sprites/cheetah_down.png"),"left" : pygame.image.load("Sprites/cheetah_left.png"),"up" : pygame.image.load("Sprites/cheetah_up.png")}
    sound = pygame.mixer.Sound("Music and Sounds/Sounds/final/gepard.wav")

class hyena(predator): #гиена
    hp=17
    energe=3
    damage=2
    lifespend=2
    count_attacks=0
    pict = {"small_art" : pygame.image.load("Sprites/hyena_small.png"),"art" : pygame.image.load("Sprites/hyena.jpg"),"right" : pygame.image.load("Sprites/hyena_right.png"),"down" : pygame.image.load("Sprites/hyena_down.png"),"left" : pygame.image.load("Sprites/hyena_left.png"),"up" : pygame.image.load("Sprites/hyena_up.png")}
    sound = pygame.mixer.Sound("Music and Sounds/Sounds/final/hyena.wav")
    def renovation(self):
        self.energe += 1
        self.count_attacks = 0

class elephant(vegeterian): #слон
    hp=30
    energe=3
    damage=2
    lifespend=2
    pict = {"small_art" : pygame.image.load("Sprites/elephant_small.png"),"art" : pygame.image.load("Sprites/elephant.jpg"),"right" : pygame.image.load("Sprites/elephant_right.png"),"down" : pygame.image.load("Sprites/elephant_down.png"),"left" : pygame.image.load("Sprites/elephant_left.png"),"up" : pygame.image.load("Sprites/elephant_up.png")}
    sound = pygame.mixer.Sound("Music and Sounds/Sounds/final/elephant.wav")

class giraffe(vegeterian): #жираф
    hp=27
    energe=2
    damage=1
    lifespend=1
    pict = {"small_art" : pygame.image.load("Sprites/giraffe_small.png"),"art" : pygame.image.load("Sprites/giraffe.jpg"),"right" : pygame.image.load("Sprites/giraffe_right.png"),"down" : pygame.image.load("Sprites/giraffe_down.png"),"left" : pygame.image.load("Sprites/giraffe_left.png"),"up" : pygame.image.load("Sprites/giraffe_up.png")}
    sound = pygame.mixer.Sound("Music and Sounds/Sounds/final/giraffe.wav")
        
class zebra(vegeterian): #зебра
    hp=25
    energe=4
    damage=1
    lifespend=2
    pict = {"small_art" : pygame.image.load("Sprites/zebra_small.png"),"art" : pygame.image.load("Sprites/zebra.jpg"),"right" : pygame.image.load("Sprites/zebra_right.png"),"down" : pygame.image.load("Sprites/zebra_down.png"),"left" : pygame.image.load("Sprites/zebra_left.png"),"up" : pygame.image.load("Sprites/zebra_up.png")}
    sound = pygame.mixer.Sound("Music and Sounds/Sounds/final/zebra.wav")
    #def aging(self):
        #if self.hp < 10:
            #self.lifespend = 0
        #else:
            #self.lifespend = 2 + data/5
        #self.hp -= self.lifespend
        #self.death()

class acacia(plant): # кактус
    hp=15
    energy=2
    lifespend=1
    pict = {"small_art" : pygame.image.load("Sprites/acacia_small.png"), "art" : pygame.image.load("Sprites/acacia.jpg"),"right" : pygame.image.load("Sprites/acacia.png")}
    sound = pygame.mixer.Sound("Music and Sounds/Sounds/final/acacia.wav")

def add_object(X,Y,klass):
    file = open("Names.txt",'r')
    num = random.randint(0,28)
    while num == 6 and klass == "elephant": # перерандом, если Вика - слон
        num = random.randint(0,28)
    for i in range(0,29):
        line = file.readline()
        if i == num:
            name = re.findall(r'[А-Я][а-я]+',line)[0]
            seks = re.findall(r'[a-z]+',line)[0]
            break
    # name = linecache.getline("Names.txt",random.randint(0,29)) считать определенную строку
    # file.seek()
    file.close()
    if klass == "vulture":
        all_objects.append(vulture(name,seks,X,Y))
    elif klass == "cheetah":
        all_objects.append(cheetah(name,seks,X,Y))
    elif klass == "hyena":
        all_objects.append(hyena(name,seks,X,Y))
    elif klass == "elephant":
        all_objects.append(elephant(name,seks,X,Y))
    elif klass == "giraffe":
        all_objects.append(giraffe(name,seks,X,Y))
    elif klass == "zebra":
        all_objects.append(zebra(name,seks,X,Y))
    elif klass == "acacia":
        all_objects.append(acacia(name,X,Y))

def text_objects(text, font):
    textSurface = font.render(text, True, (0,0,0))
    return textSurface, textSurface.get_rect()

def game_quit():
    pygame.quit()
    quit()

def button(msg,x,y,w,h,color1,color2,action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(window,color2,(x,y,w,h))
        if action != None and click[0] == 1:
            sound_click.play()
            action()
    else:
        pygame.draw.rect(window,color1,(x,y,w,h))
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x+w/2), (y+h/2))
    window.blit(textSurf, textRect)

def game_intro():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        window.blit(bg,(0,0))
        button("START GAME",710,420,500,80,(200, 69, 42),(231, 123, 42),game_constructor)
        button("OPTIONS",710,500,500,80,(88, 86, 0),(104, 131, 0),game_options)
        button("QUIT",710,580,500,80,(88, 0, 2),(201, 0, 2),game_quit)
        
        pygame.display.update()
        clock.tick(15)
    
def game_options():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        window.blit(bg,(0,0))
        textSurf, textRect = text_objects("В процессе создания", smallText)
        textRect.center = ((display_width/2), (display_heigth/2))
        window.blit(textSurf, textRect)

def rotate(image,angle):
    loc = image.get_rect().center
    rot_sprite = pygame.transform.rotate(image,angle)
    rot_sprite.get_rect().center = loc
    return rot_sprite

def draw_interface():
    global move, eat, spawn
    window.fill((232, 202, 68)) # 1536x864 сетка через 192 и 196
    window.blit(game_map,(192,108)) # x с 192  по 1728,  y с 108 по 972
    textSurf, textRect = text_objects(str(data)+" Turn", smallText)
    textRect.center = ((1370),(940))
    window.blit(textSurf, textRect)
    for unit in all_objects:
        unit.draw()

def key(msg,x,y,w,h,color1,color2,action = None):
    if action == True:
        pygame.draw.rect(window,color2,(x,y,w,h))
    elif action == False:
        pygame.draw.rect(window,color1,(x,y,w,h))
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x+w/2),(y+h/2))
    window.blit(textSurf, textRect)
    
def end_of_turn():
    global data, hero, eat, move, spawn
    data += 1
    for unit in all_objects:
        unit.aging()
        unit.renovation()
    hero = None
    eat = False
    move = False
    spawn = False
        
def draw_main_animal():
    global hero
    if hero != None:
        hero.show_inf()
    
def game_loop():
    global hero, all_objects, move, eat, spawn
    if len(all_objects) == 0:
        attention("In your map dont locate anyone")
    while True:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sound_click.play()
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if  1428 + 300 > mouse[0] > 1428 and 696 + 69 > mouse[1] > 696:
                    sound_click.play()
                    if move == True:
                        move = False
                    else:
                        move = True
                        eat = False
                        spawn = False
                elif  1428 + 300 > mouse[0] > 1428 and 765 + 69 > mouse[1] > 765:
                    sound_click.play()
                    if eat == True:
                        eat = False
                    else:
                        eat = True
                        move = False
                        spawn = False
                elif  1428 + 300 > mouse[0] > 1428 and 834 + 69 > mouse[1] > 834:
                    sound_click.play()
                    if spawn == True:
                        spawn = False
                    else:
                        spawn = True
                        eat = False
                        move = False
                elif  1428 + 300 > mouse[0] > 1428 and 903 + 69 > mouse[1] > 903:
                    sound_click.play()
                    end_of_turn()
                elif 1728 > mouse[0] > 192 and 972 > mouse[1] > 108 and move or spawn == True:
                    new_X = int()
                    new_Y = int()
                    for x in range(0,8):
                        if 192 + wos*(x+1) > mouse[0] > 192 + wos*x: # изменил вот здесь
                            new_X = x
                    for y in range(0,3):
                        if 108 + hos*(y+1) > mouse[1] > 108 + hos*y: # и здесь
                            new_Y = y
                    test = True
                    for unit in all_objects:
                        if unit.X == new_X and unit.Y == new_Y:
                            test = False
                            break
                    if test == True:
                        if move == True and re.findall(r'^[a-z]+', str(hero)[10:])[0] == 'acacia':
                            attention("Plants can't use movement")
                        elif move == True:
                            all_objects[all_objects.index(hero)].dvig(new_X, new_Y)
                            move = False
                        if spawn == True:
                            check = False
                            for unit in all_objects:
                                if re.findall(r'^[a-z]+', str(hero)[10:])[0] == 'acacia':
                                    check = True
                                else:
                                    if (abs(hero.X-unit.X) == 1 and abs(hero.Y-unit.Y) == 1) or (abs(hero.X-unit.X) == 0 and abs(hero.Y-unit.Y) == 1) or (abs(hero.X-unit.X) == 1 and abs(hero.Y-unit.Y) == 0):
                                        if re.findall(r'^[a-z]+', str(hero)[10:])[0] == re.findall(r'^[a-z]+', str(unit)[10:])[0]:
                                            if hero.seks != unit.seks:
                                                check = True # проверить на достаточность энергии у ОБОИХ существ
                            if check == True:
                                hero.spawn(new_X,new_Y)
                                spawn = False
                            else:
                                attention("Don't have a partner, that locate in 1 square or  Aimals have different classes or Animal have one seks")
                    elif test == False:
                        attention("In this square located another unit")
        draw_interface()
        draw_main_animal()
        for unit in all_objects:
            if unit.hp <= 0:
                sound = pygame.mixer.Sound("Music and Sounds/Sounds/final/death marsh.wav")
                sound.play()
                attention("Your " + re.findall(r'^[a-z]+', str(unit)[10:])[0]+" is rip")
                all_objects.pop(all_objects.index(unit))
            if (unit.X+1)*wos + 192 > mouse[0] > unit.X*wos + 192 and (unit.Y+1)*hos + 108 > mouse[1] > unit.Y*hos + 108:
                if click[0] == 1: 
                    if eat == False and move == False and spawn == False:
                        hero = unit
                        hero.sound.play()
                    elif re.findall(r'^[a-z]+', str(hero)[10:])[0] == 'acacia':
                        attention("Plants cant attack anybody")
                    elif eat == True:
                        if (abs(hero.X-unit.X) == 1 and abs(hero.Y-unit.Y) == 1) or (abs(hero.X-unit.X) == 0 and abs(hero.Y-unit.Y) == 1) or (abs(hero.X-unit.X) == 1 and abs(hero.Y-unit.Y) == 0):
                            all_objects[all_objects.index(hero)].eat(all_objects[all_objects.index(unit)])
                            eat = False
        key("To move",1428,696,300,69,(0,0,200),(0,0,255),move)
        key("To attack",1428,765,300,69,(200,0,0),(255,0,0),eat)
        key("To spawn",1428,834,300,69,(0,200,0),(0,255,0),spawn)
        button("Next turn",1428,903,300,69,(58, 58, 58),(100, 100, 100))
        pygame.display.update()
        clock.tick(15)

def game_constructor():
    attention("Let's locate game's units on the map")
    global hero, all_objects
    while True:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sound_click.play()
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and 756 > mouse[0] > 192 and 972 > mouse[1] > 696 and hero == None:
                if 696 + 138 > mouse[1] > 696:
                    if 192 + 141 > mouse[0] > 192:
                        hero = "acacia"
                    elif 192 + 141*2 > mouse[0] > 192+141:
                        hero = "zebra"
                    elif 192 + 141*3 > mouse[0] > 192+141*2:
                        hero = "giraffe"
                    elif 192 + 141*4 > mouse[0] > 192+141*3:
                        hero = "elephant"
                elif 696 + 138*2 > mouse[1] > 696 + 138:
                    if 192 + 141 > mouse[0] > 192:
                        hero = "cheetah"
                    elif 192 + 141*2 > mouse[0] > 192+141:
                        hero = "hyena"
                    elif 192 + 141*3 > mouse[0] > 192+141*2:
                        hero = "vulture"
            elif event.type == pygame.MOUSEBUTTONUP and 1728 > mouse[0] > 192 and 972 > mouse[1] > 108 and hero != None:  
                new_X = int()
                new_Y = int()
                for x in range(0,8):
                    if 192 + wos*(x+1) > mouse[0] > 192 + wos*x:
                        new_X = x
                for y in range(0,3):
                    if 108 + hos*(y+1) > mouse[1] > 108 + hos*y:
                        new_Y = y
                test = True
                for unit in all_objects:
                    if unit.X == new_X and unit.Y == new_Y:
                        test = False
                        break
                if test == True:
                    add_object(new_X,new_Y,hero)
                    hero = None
            # от 804 до 972. 2 ряда картинок высотой по 84 пкс
        window.fill((232, 202, 68)) # 1536x864 сетка через 192 и 196
        window.blit(game_map,(192,108)) # x с 192  по 1728,  y с 108 по 972
        draw_interface()
        button("To move",1428,696,300,69,(0,0,200),(0,0,255))
        button("To attack",1428,765,300,69,(200,0,0),(255,0,0))
        button("To spawn",1428,834,300,69,(0,200,0),(0,255,0))
        button("Next turn",1428,903,300,69,(58, 58, 58),(100, 100, 100))
        button("Finish location of units",1028,853,390,119,(58, 58, 58),(100, 100, 100),game_loop)
        window.blit(acacia.pict["small_art"],(192,696))
        window.blit(zebra.pict["small_art"],(192+141,696))
        window.blit(giraffe.pict["small_art"],(192+141*2,696))
        window.blit(elephant.pict["small_art"],(192+141*3,696))
        window.blit(cheetah.pict["small_art"],(192,696+138))
        window.blit(hyena.pict["small_art"],(192+141,696+138))
        window.blit(vulture.pict["small_art"],(192+141*2,696+138))
        pygame.display.update()
        clock.tick(15)

game_intro()
pygame.quit()
quit()
