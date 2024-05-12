import pygame
from sys import exit

# Initiate pygame
pygame.init()

# Create screen
screen_width = 800
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('test')

# Extra variables
text_font = pygame.font.Font('fonts/Argentina free promo.ttf', 50)
# Create surfaces
sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

text_surface = text_font.render('My Game', True, 'black')
text_rect = text_surface.get_rect(midtop = (screen_width/2, 20))

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(bottomleft=(600, 300))

player_surface = pygame.image.load('graphics/Player/player_walk_1.png')
player_rect = player_surface.get_rect(bottomleft=(80, 300))

snail_speed = 2
player_speed = 2

# Frame rate
clock = pygame.time.Clock()

# Game loop
while True:
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print('mouse down')
        if event.type == pygame.MOUSEBUTTONUP:
            print('mouse up')
        if event.type == pygame.MOUSEMOTION:
            if player_rect.collidepoint(event.pos):
                print('mouse collision')
    mouse_pos = pygame.mouse.get_pos()

    # Draw surfaces
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, text_rect)
    screen.blit(snail_surface, snail_rect)
    screen.blit(player_surface, player_rect)

    snail_rect.x += snail_speed

    if snail_rect.colliderect(player_rect) or snail_rect.left <= 0 or snail_rect.right >= screen_width:
        print('snail collision')
        snail_speed *= -1


    # Update screen
    pygame.display.update()
    clock.tick(60)
