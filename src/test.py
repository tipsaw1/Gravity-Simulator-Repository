import pygame
from sys import exit

# Initiate pygame
pygame.init()

# Create screen
screen_width = 800
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Gravity')

# Extra variables
text_font = pygame.font.Font('fonts/Argentina free promo.ttf', 50)

# Create surfaces
sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
text_surface = text_font.render('My Game', True, 'black')

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(bottomleft=(600, 300))

player_surface = pygame.image.load('graphics/Player/player_walk_1.png')
player_rect = player_surface.get_rect(bottomleft=(80, 300))

# Frame rate
clock = pygame.time.Clock()

# Game loop
while True:
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Draw surfaces
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (300, 50))
    screen.blit(snail_surface, snail_rect)
    screen.blit(player_surface, player_rect)

    if player_rect.colliderect(snail_rect):
        print('collision')

    # Update screen
    pygame.display.update()
    clock.tick(60)
