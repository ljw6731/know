import pygame, random, time, sys

pygame.init()
screen = pygame.display.set_mode((1500, 800))

charater_image = pygame.image.load('fff.svg')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    screen.blit(charater_image, (100,100))
    pygame.display.update()