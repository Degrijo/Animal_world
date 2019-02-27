
import pygame

pygame.init()
window = pygame.display.set_mode((1200,700))
pict = pygame.image.load("enigma.jpeg")
pygame.display.update()

def rotate(image,angle):
    loc = image.get_rect().center
    rot_sprite = pygame.transform.rotate(image,angle)
    rot_sprite.get_rect().center = loc
    return rot_sprite

while True:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
    window.fill((232, 202, 68))
    #window.blit(pict,(0,0))
    window.blit(rotate(pict,90),(0,0))
    pygame.display.update()
