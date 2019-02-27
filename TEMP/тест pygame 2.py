import pygame

display_width = 1920
display_heigth = 1080

pygame.init()
window = pygame.display.set_mode((display_width, display_heigth),pygame.FULLSCREEN)
bg = pygame.image.load("bg1.jpg")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            
    window.blit(bg,(0,0))
    pygame.display.update()
    clock.tick(100)
    
pygame.quit()
quit()
