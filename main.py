import pygame
from pygame.locals import *
import random

from pygame import mixer

# shape parameters
size = width, height = (800, 800)
road_w = int(width / 1.6)
roadmark_w = int(width / 80)
# location parameters
right_lane = width / 2 + road_w / 4
left_lane = width / 2 - road_w / 4
# animation parameters
speed = 1
# sound
mixer.init()
mixer.music.load('Trackmania PF.mp3')
mixer.music.play(loops=-1)

# initiallize the app
pygame.init()

running = True

# set window size
screen = pygame.display.set_mode(size)
# set window title
pygame.display.set_caption("2d car game ")
# icon
icon = pygame.image.load('sport-car.png')
pygame.display.set_icon(icon)
# set background colour
screen.fill((60, 220, 0))
# apply changes
pygame.display.update()

# load player vehicle
car = pygame.image.load("car.png")
# resize image
# car = pygame.transform.scale(car, (250, 250))
car_loc = car.get_rect()
car_loc.center = right_lane, height * 0.8

# load enemy vehicle
car2 = pygame.image.load("Car (1).png")
car2_loc = car2.get_rect()
car2_loc.center = left_lane, height * 0.2

counter = 0
# game loop
while running:
    counter += 1

    # increase game difficulty overtime
    if counter == 5000:
        speed += 0.15
        counter = 0
        print("level up", speed)

    # animate enemy vehicle
    car2_loc[1] += speed
    if car2_loc[1] > height:
        # randomly select lane
        if random.randint(0, 1) == 0:
            car2_loc.center = right_lane, -200
        else:
            car2_loc.center = left_lane, -200

    # end game logic
    if car_loc[0] == car2_loc[0] and car2_loc[1] > car_loc[1] - 50:
        print("GAME OVER!")
        break

    # event listeners
    for event in pygame.event.get():
        if event.type == QUIT:
            # collapse the app
            running = False
        if event.type == KEYDOWN:
            # move user car to the left
            if event.key in [K_d, K_LEFT]:
                car_loc = car_loc.move([-int(road_w / 2), 0])

                left_sound = pygame.mixer.Sound('click.mp3')
                left_sound.play()
            # move user car to the right
            if event.key in [K_d, K_RIGHT]:
                left_sound = pygame.mixer.Sound('click.mp3')
                left_sound.play()
                car_loc = car_loc.move([int(road_w / 2), 0])

            if event.key in [K_w, K_UP]:
                left_sound = pygame.mixer.Sound('click.mp3')
                left_sound.play()
                car_loc = car_loc.move(0, -50)
            if event.key in [K_s, K_DOWN]:
                left_sound = pygame.mixer.Sound('click.mp3')
                left_sound.play()
                car_loc = car_loc.move(0, 50)

    # draw road
    pygame.draw.rect(
        screen,
        (50, 50, 50),
        (width / 2 - road_w / 2, 0, road_w, height))
    # draw centre line
    pygame.draw.rect(
        screen,
        (255, 240, 60),
        (width / 2 - roadmark_w / 2, 0, roadmark_w, height))
    # draw left road marking
    pygame.draw.rect(
        screen,
        (255, 255, 255),
        (width / 2 - road_w / 2 + roadmark_w * 2, 0, roadmark_w, height))
    # draw right road marking
    pygame.draw.rect(
        screen,
        (255, 255, 255),
        (width / 2 + road_w / 2 - roadmark_w * 3, 0, roadmark_w, height))

    # place car images on the screen
    screen.blit(car, car_loc)
    screen.blit(car2, car2_loc)
    # apply changes
    pygame.display.update()

# collapse application window
pygame.quit()
