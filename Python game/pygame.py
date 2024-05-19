import time
import pygame

def wait(x):
   time.sleep(x)


pygame.init()
screen = pygame.display.set_mode((700, 350)) #, flags=pygame.NOFRAME
pygame.display.set_caption('my first game')
pygame.display.set_icon(pygame.image.load('images/game_icon.png'))
screen.fill((0,206,209))


player = pygame.image.load('images/player.png')
enemy = pygame.image.load('images/enemy.png')

running = True
while running :
    wait(0.1)
    screen.blit(player, (300,100))
    screen.blit(enemy, (400, 100))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
         on = False
         pygame.quit()
        
           
         