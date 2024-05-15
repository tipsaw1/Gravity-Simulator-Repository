import math
import pygame
from sys import exit

# Pygame setup
pygame.init()

screen_width = 1000
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Gravity')

background = pygame.Surface((screen_width, screen_height))
background.fill('black')

scale = 3/3475
G = 5.75827338*(10**-14)

# Objects
earth = pygame.Surface((11, 11))
earth.fill('blue')
earth_rect = earth.get_rect(center=((screen_width / 2), screen_height / 2))
earth_mass = 5.15568345*(10**21)

moon = pygame.Surface((3, 3))
moon.fill('white')
moon_rect = moon.get_rect(center = (earth_rect.centerx-50, earth_rect.centery))
moon_mass = 6.3433149*(10**19)

# clock
clock = pygame.time.Clock()
# speeds = []
largest_distance = 0
x_distance = earth_rect.centerx - moon_rect.centerx
y_distance = earth_rect.centery - moon_rect.centery
distance = math.sqrt(x_distance ** 2 + y_distance ** 2)
horizontal_speed = 10
vertical_speed = 20
# Screen loop
while True:
    x_distance = moon_rect.centerx - earth_rect.centerx
    y_distance = moon_rect.centery - earth_rect.centery
    if x_distance != 0:
        angle = math.atan(abs(y_distance/x_distance))
    else:
        angle = math.pi/2
    if x_distance >= 0 and y_distance >= 0:
        horizontal_speed += -math.cos(angle)
        vertical_speed += -math.sin(angle)
    elif x_distance <= 0 and y_distance >= 0:
        horizontal_speed += math.cos(angle)
        vertical_speed += -math.sin(angle)
    elif x_distance <= 0 and y_distance <= 0:
        horizontal_speed += math.cos(angle)
        vertical_speed += math.sin(angle)
    elif x_distance >= 0 and y_distance <= 0:
        horizontal_speed += -math.cos(angle)
        vertical_speed += math.sin(angle)




    # speeds.append(distance)

    # Quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(angle*180/math.pi)
            print(horizontal_speed, vertical_speed)
        #    for d in speeds:
        #        if d >= largest_distance:
        #            largest_distance = d
        #    print(largest_distance)
            pygame.quit()
            exit()

    screen.blit(background, (0,0))
    screen.blit(earth, earth_rect)
    screen.blit(moon, moon_rect)
    moon_rect.centerx += horizontal_speed
    moon_rect.centery += vertical_speed
    pygame.display.update()
    clock.tick(60)