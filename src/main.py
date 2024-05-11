import pygame, math
from sys import exit

# Initiate pygame
pygame.init()

# Create screen
screen_width = 1200
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Gravity')

#Create pixels
pixel = pygame.Surface((1,1))
colors = ('red', 'orange', 'yellow', 'green', 'blue', 'purple')

# Frame rate
clock = pygame.time.Clock()
x = 0
color = 1

# Wave characteristics
amplitude = screen_height/4
period = 2*math.pi/(screen_width/6)
vertical_shift = screen_height/2
def wave(x):
    y = -amplitude * math.sin(period * x) + vertical_shift
    return y

# Quadratic characteristics

# Game loop
while True:
    #Add surfaces
    if x < screen_width:
        x += 1
        pixel.fill(colors[color-1])
        screen.blit(pixel, (x, wave(x)))
        if color < len(colors):
            color += 1
        else:
            color = 1

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Update screen
    pygame.display.update()
    clock.tick(240)