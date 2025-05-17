import pygame
import sys




pygame.init()
screen=pygame.display.set_mode((640,480))
pygame.display.set_caption("My_first_game")
clock=pygame.time.Clock()
text_font=pygame.font.Font("fonts/CrotahFreeVersionItalic-z8Ev3.ttf",50)


ground_surface=pygame.image.load("graphics/ground.jpg")
sky_surface=pygame.image.load("graphics/sky_image.jpg")

text_surface=text_font.render("MyGame",True,(0,0,0))
text_rect=text_surface.get_rect(center=(320,20))



enemy_surface=pygame.image.load("graphics/gorilla-Photoroom.png")
enemy_rect=enemy_surface.get_rect()

player_surface=pygame.image.load("graphics/player3-Photoroom.png")
player_rect=player_surface.get_rect(midleft=(0,400))



while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,410))
    screen.blit(text_surface,(text_rect.x,text_rect.y))

    
    if enemy_rect.right<=0:
        enemy_rect.right=640
    else:
        enemy_rect.left-=3    
    screen.blit(enemy_surface,(enemy_rect.left,370))
    if player_rect.right>=640:
        player_rect.left=0
    else:
        player_rect.right+=3

    screen.blit(player_surface,(player_rect.x,player_rect.y))

    
    pygame.display.update()
    clock.tick(60)

