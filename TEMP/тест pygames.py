
import pygame
import random
import time

WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLUE = (0, 0, 200)
bright_GREEN =(0, 255, 0)
bright_RED = (255, 0, 0)
bright_BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

#display_width =
#display_heigth = 

pygame.init()

window = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
clock = pygame.time.Clock()

bg = pygame.image.load("bg.jpg")
game_map = pygame.image.load("game_map_new.jpg")
acacia = pygame.image.load("acacia.jpg")
cheetah = pygame.image.load("cheetah.jpg")
elephant = pygame.image.load("elephant.jpg")
giraffe = pygame.image.load("giraffe.jpg")
hyena = pygame.image.load("hyena.jpg")
vulture = pygame.image.load("vulture.jpg")
zebra = pygame.image.load("zebra.jpg")

acacia_top = pygame.image.load("acacia.png")
cheetah_top = pygame.image.load("cheetah.png")
elephant_top = pygame.image.load("elephant.png")
giraffe_top = pygame.image.load("giraffe.png")
hyena_top = pygame.image.load("hyena.png")
vulture_top = pygame.image.load("vulture.png")
zebra_top = pygame.image.load("zebra.png")

X = 350
Y = 175
width = 10
height = 1

pygame.display.update()

def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

def game_quit():
    pygame.quit()
    quit()

def button(msg,x,y,w,h,color1,color2,action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(window,color2,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(window,color1,(x,y,w,h))
    smallText = pygame.font.Font('freesansbold.ttf',20)
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
        button("START GAME",710,420,500,80,(200, 69, 42),(231, 123, 42),game_loop)
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
        smallText = pygame.font.Font('freesansbold.ttf',20)
        textSurf, textRect = text_objects("В процессе создания", smallText)
        textRect.center = ((display_width/2), (display_heigth/2))
        window.blit(textSurf, textRect)
    

def game_loop():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        window.fill((232, 202, 68)) # 1620x696 сетка через 202,5 и 232
        window.blit(game_map,(192,108)) # x с 192  по 1728
        window.blit(elephant,(192,696)) # y с 108 по 972
        window.blit(elephant_top,(108+192+100,108+196))
        button("to move", 1428,696,300,92,BLUE,bright_BLUE)
        button("to attack", 1428,788,300,92,RED,bright_RED)
        button("to spawn", 1428,880,300,92,GREEN,bright_GREEN)
        
        pygame.display.update()
        clock.tick(15)

game_intro()
pygame.quit()
quit()
