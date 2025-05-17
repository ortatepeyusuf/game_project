import pygame
import sys


def calculate_score():
    current_time=( pygame.time.get_ticks()-start_time)//100
    score_surface=text_font.render(f"Score:{current_time}",True,(0,0,0))
    score_surface_rect=score_surface.get_rect(center=(320,20))
    screen.blit(score_surface,score_surface_rect)





pygame.init()
screen=pygame.display.set_mode((640,480))
pygame.display.set_caption("My_first_game")
clock=pygame.time.Clock()
text_font=pygame.font.Font("fonts/CrotahFreeVersionItalic-z8Ev3.ttf",50)


is_game_active=True
 

ground_surface=pygame.image.load("graphics/ground.jpg")
sky_surface=pygame.image.load("graphics/sky_image.jpg")



game_over_text_surface=text_font.render("Game Over",True,(255,0,0))
game_over_text_surface_rect=game_over_text_surface.get_rect(center=(320,240))


restart_text_surface=text_font.render("Press Space To Restart",True,(255,0,0))
restart_text_surface_rect=restart_text_surface.get_rect(center=(320,300))



enemy_surface=pygame.image.load("graphics/gorilla-Photoroom.png")
enemy_rect=enemy_surface.get_rect(midbottom=(640,420))

player_surface=pygame.image.load("graphics/player3-Photoroom.png")
player_rect=player_surface.get_rect(midleft=(20,400))

player_gravity=0
ground_level=420
top_level=0
start_time=0



while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if is_game_active:
            if event.type==pygame.KEYDOWN:
                if player_rect.bottom==ground_level:
                    if event.key==pygame.K_SPACE:
                        player_gravity=-20
            
        else:
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    is_game_active=True
                    enemy_rect.left=640
                    start_time=pygame.time.get_ticks()

        
    if is_game_active:
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,410))
        calculate_score()




        #Düşman Hareketi
        if enemy_rect.right<=0:
            enemy_rect.right=640
        else:
            enemy_rect.left-=3   
        enemy_rect.y=370

        screen.blit(enemy_surface,enemy_rect)

        #Karakter işlemleri

        player_gravity+=1
        player_rect.y+=player_gravity
        
        
        if player_rect.bottom>=ground_level:
            player_rect.bottom=ground_level
            player_gravity=0
            
        if player_rect.top<=top_level:
            player_rect.top=top_level   

        screen.blit(player_surface,(player_rect.x,player_rect.y))
        
        if player_rect.colliderect(enemy_rect):
            # print("collision")
            is_game_active=False
            
            
    else:
        screen.fill('Black')
        screen.blit(game_over_text_surface,game_over_text_surface_rect)
        screen.blit(restart_text_surface,restart_text_surface_rect)

    
    pygame.display.update()
    clock.tick(60)

