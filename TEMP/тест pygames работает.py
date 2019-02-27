
import pygame
import random
import time

display_width = 1920
display_heigth = 1080

WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLUE = (0, 0, 200)
bright_GREEN =(0, 255, 0)
bright_RED = (255, 0, 0)
bright_BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

pygame.init()
window = pygame.display.set_mode((display_width, display_heigth),pygame.FULLSCREEN)
clock = pygame.time.Clock()

bg = pygame.image.load("bg1.jpg")
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
        button("Options",710,500,500,80,(88, 86, 0),(104, 131, 0),game_options)
        button("QUIT",710,580,500,80,(88, 0, 2),(201, 0, 2),game_quit)
        
        pygame.display.update()
        clock.tick(15)
    
def game_options():
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
        
        window.fill(WHITE)
        button("to move", 1450,650,100,50,BLUE,bright_BLUE)
        button("to attack", 1450,700,100,50,RED,bright_RED)
        button("to spawn", 1450,750,100,50,GREEN,bright_GREEN)
        
        pygame.display.update()
        clock.tick(15)

game_intro()
pygame.quit()
quit()
