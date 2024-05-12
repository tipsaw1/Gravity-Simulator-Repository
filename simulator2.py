import pygame, math

# Pygame setup
pygame.init()

screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Gravity 2')


# Surfaces

# clock
clock = pygame.time.Clock()

# Screen loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
    clock.tick(60)
