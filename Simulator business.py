import pygame
import sys
import time
import math

#import player as pl

#square = pygame.Surface((50, 50))
#square.fill('Blue')

#myfont = pygame.font.Font('ClimateCrisis-Regular.ttf', 40)
#text_surface = myfont.render('itProger', False, 'Black')

width = 204
height = 170

dx = 0
dy = 0

clock = pygame.time.Clock()

def run():
    dx = 1
    dy = 0
    #global dx

    pygame.init()
    win = pygame.display.set_mode((width,height), flags=pygame.RESIZABLE) #flags=pygame.NOFRAME
    current_size = win.get_size()
    pygame.display.set_caption("Simulator business")
    icon = pygame.image.load('4.png')
    bg = pygame.image.load('grass6.png')
    tablet = pygame.image.load('tablet.png')
    #virtual_surface = Surface((width, height))
    #player = pygame.image.load('p3.png')
    walk_right = [
        pygame.image.load('pl1.png'),
        pygame.image.load('pl2.png'),
        pygame.image.load('pl3.png'),
        pygame.image.load('pl4.png'),
        pygame.image.load('pl5.png'),
        pygame.image.load('pl6.png'),
        pygame.image.load('pl7.png'),
        pygame.image.load('pl8.png'),
    ]
    walk_left = [
        pygame.image.load('pl9.png'),
        pygame.image.load('pl10.png'),
        pygame.image.load('pl11.png'),
        pygame.image.load('pl12.png'),
        pygame.image.load('pl13.png'),
        pygame.image.load('pl14.png'),
        pygame.image.load('pl15.png'),
        pygame.image.load('pl16.png'),
    ]
    player = [
        pygame.image.load('p3.png'),
    ]

    player_anim_count = 0
    bg_x = 0

    a = 1

    player_speed = 5
    player_x = 100
    player_y = 100
    table_x = 100
    table_y = 100

    pygame.display.set_icon(icon)
    #pygame.display.set_buground (icon)
    #bg_color = (0, 0, 0)
    #player = player(win)

    while True:

        #pygame.draw.circle(win, 'red', (10, 7), 5)
        #win.blit(square, (600, 400))
        #win.blit(player, (500, 300))
        #win.blit(text_surface, (300, 100))
        win.blit(bg, (bg_x, 0))
        win.blit(tablet, (table_x, table_y))
        #win.blit(bg, (bg_x + 225, 0))
        win.blit(walk_right[player_anim_count], (player_x, player_y))

        if player_anim_count == 3:
            player_anim_count = 0
        else:
            player_anim_count += 1

        #bg_x -= 2
        if bg_x == -290:
            bg_x = 0

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        #player.output()


        #if player_x == table_x:
            #if player_y == table_y:
                #print("Нигер")
        if a == 1:
            #time.sleep(1)
            x = print(player_x, "x")
            y = print(player_y, 'y')

        #Контроль столкновений
        if player_x == 80 or player_x == 90 or player_x == 100 or player_x == 110 or player_x == 120:
            if player_y == 90 or player_y == 80:
                if dx > 0:
                    player_x -= 2
                elif dx < 0:
                    player_x += 2
                elif dy > 0:
                    player_x += 2
                elif dy < 0:
                    player_y -= 2


        keys = pygame.key.get_pressed()

        #Хотьба на стрілочки
        if keys[pygame.K_RIGHT] and player_x < 100:
            player_x += 2
            dx = 1
        elif keys[pygame.K_LEFT] and player_x > 20:
            player_x -= 2
            dx = -1
        elif keys[pygame.K_UP] and player_y > 20:
            player_y -= 2
        elif keys[pygame.K_DOWN] and player_y < 130:
            player_y += 2

        #хоттба
        elif keys[pygame.K_d]:
            player_x += 2
            dx = 1
        elif keys[pygame.K_a]:
            player_x -= 2
            dx = -1
        elif keys[pygame.K_w]:
            player_y -= 2
        elif keys[pygame.K_s]:
            player_y += 2


        clock.tick(10)
        pygame.display.flip()

run()
