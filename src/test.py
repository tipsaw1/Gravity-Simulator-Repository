import pygame, math
from sys import exit

# Initiate pygame
pygame.init()

# Create screen
screen_width = 800
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('test')

# Create surfaces
sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

text_font = pygame.font.Font('fonts/Argentina free promo.ttf', 50)
text_surface = text_font.render('My Game', True, '#FFAA00')
text_rect = text_surface.get_rect(midtop = (screen_width/2, 20))

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(bottomleft=(600, 300))

player_surface = pygame.image.load('graphics/Player/player_walk_1.png')
player_rect = player_surface.get_rect(bottomleft=(80, 300))

snail_speed = 2
player_speed = 2

angle = math.atan((screen_height/2)/(screen_width/2))
# Frame rate
clock = pygame.time.Clock()

# Game loop
while True:
    # Variables
    mouse_pos = pygame.mouse.get_pos()
    snail_rect.x += snail_speed

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

    # Draw surfaces
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))

    pygame.draw.rect(screen, '#880000', text_rect, 0, 5)
    screen.blit(text_surface, text_rect)

    screen.blit(snail_surface, snail_rect)
    screen.blit(player_surface, player_rect)

    pygame.draw.circle(screen, '#AA0000', (screen_width/2, screen_height/2), 40, 5)

    pygame.draw.line(screen, 'black', (0,0), (screen_width/2-40*math.cos(angle), screen_height/2-40*math.sin(angle)), 5)
    pygame.draw.line(screen, 'black', (screen_width/2+40*math.cos(angle), screen_height/2+40*math.sin(angle)), (screen_width, screen_height), 5)
    pygame.draw.line(screen, 'black', (screen_width,0), (screen_width/2+40*math.cos(angle), screen_height/2-40*math.sin(angle)), 5)
    pygame.draw.line(screen, 'black', (screen_width/2-40*math.cos(angle), screen_height/2+40*math.sin(angle)), (0,screen_height), 5)

    pygame.draw.ellipse(screen, '#0000BB', pygame.Rect(screen_width/2-50,screen_height/2-20, 100, 40), 5)
    pygame.draw.ellipse(screen, '#FFFF00', pygame.Rect(screen_width/2-20,screen_height/2-50, 40, 100), 5)

    if snail_rect.colliderect(player_rect) or snail_rect.left <= 0 or snail_rect.right >= screen_width:
        print('snail collision')
        snail_speed *= -1

    # Update screen
    pygame.display.update()
    clock.tick(60)
