import pygame
import sys
from random import randint



def calculate_score():
    score=( pygame.time.get_ticks()-start_time)//100
    score_surface=text_font.render(f"Score:{score}",True,(0,0,0))
    score_surface_rect=score_surface.get_rect(center=(320,20))
    screen.blit(score_surface,score_surface_rect)
    return score


def enemy_movement(enemy_list):
    new_enemy_list=[ ]
    if enemy_list:
        for enemy,enemy_rect in enemy_list:
            enemy_rect.x-=3

            if enemy_rect.right > -100:
                screen.blit(enemy,enemy_rect)
                new_enemy_list.append((enemy,enemy_rect))
    return new_enemy_list
            




pygame.init()
screen=pygame.display.set_mode((640,480))
pygame.display.set_caption("My_first_game")
clock=pygame.time.Clock()
text_font=pygame.font.Font("fonts/CrotahFreeVersionItalic-z8Ev3.ttf",40)


is_game_active=False
 

ground_surface=pygame.image.load("graphics/ground.jpg")
sky_surface=pygame.image.load("graphics/sky_image.jpg")



game_over_text_surface=text_font.render("Game Over",True,(255,0,0))
game_over_text_surface_rect=game_over_text_surface.get_rect(center=(320,160))


restart_text_surface=text_font.render("Press Space To Restart",True,(255,0,0))
restart_text_surface_rect=restart_text_surface.get_rect(center=(320,300))



enemy_surface=pygame.image.load("graphics/gorilla-Photoroom.png")
enemy_rect=enemy_surface.get_rect(midbottom=(640,420))

enemy_surface2=pygame.image.load("graphics/eagle.png")
enemy_surface2_rect=enemy_surface2.get_rect()
enemy_surfaces=[enemy_surface,enemy_surface2]

enemy_list=[]



player_surface=pygame.image.load("graphics/player3-Photoroom.png")
player_rect=player_surface.get_rect(midleft=(20,400))

player_gravity=0
ground_level=420
top_level=0
start_time=0

#Başlangıç Ekranı
start_screen_surface=pygame.transform.smoothscale((pygame.image.load("graphics/start_screen_final.png")),(640,480))
start_screen_surface_rect=start_screen_surface.get_rect(topleft=(0,0))


start_text = text_font.render("Press Space To Start Game", True, (0, 0, 0))
start_text_rect=start_text.get_rect(center=(320,240))


enemy_spawn=pygame.USEREVENT+1

pygame.time.set_timer(enemy_spawn,randint(900,1200))




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
            elif event.type==enemy_spawn:
                random_number=randint(0,1)
                if random_number==0:
                    new_enemy=enemy_surfaces[random_number]
                    new_enemy_rect=new_enemy.get_rect(midbottom=(640,420))
                else:
                    new_enemy=enemy_surfaces[random_number]
                    new_enemy_rect=new_enemy.get_rect(midbottom=(640,370))

                enemy_list.append((new_enemy,new_enemy_rect))
                
            
        else:
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    is_game_active=True
                    enemy_rect.left=640
                    start_time=pygame.time.get_ticks()

        
    if is_game_active:
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,410))
        global score
        score=calculate_score()


        enemy_list=enemy_movement(enemy_list)

        #Karakter işlemleri

        player_gravity+=1
        player_rect.y+=player_gravity
        
        
        if player_rect.bottom>=ground_level:
            player_rect.bottom=ground_level
            player_gravity=0
            
        if player_rect.top<=top_level:
            player_rect.top=top_level   

        screen.blit(player_surface,(player_rect.x,player_rect.y))
        
        for enemy,enemy_rect in enemy_list:
            if player_rect.colliderect(enemy_rect):
                is_game_active=False
                enemy_list=[]


            
            
    else:
        if start_time==0:
            screen.blit(start_screen_surface,start_screen_surface_rect)
            screen.blit(start_text,start_text_rect)
        else:
            screen.fill((0,0,0))
            screen.blit(game_over_text_surface,game_over_text_surface_rect)
            screen.blit(restart_text_surface,restart_text_surface_rect)
            score_surface=text_font.render(f"Your Score:{score}",True,(255,0,0))
            score_surface_rect=score_surface.get_rect(center=(320,240 ))
            screen.blit(score_surface,score_surface_rect)
            


        


    
    pygame.display.update()
    clock.tick(60)

