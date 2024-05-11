import pygame, math
from sys import exit

# Initiate pygame
pygame.init()

# Create screen
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Gravity')

#Create pixels
pixel = pygame.Surface((100,100))
pixel.fill('red')

# Frame rate
clock = pygame.time.Clock()

# Game loop
while True:
    screen.blit(pixel, (50,50))

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Update screen
    pygame.display.update()
    clock.tick(240)