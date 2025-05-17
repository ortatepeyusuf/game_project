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
    new_enemy_list = []
    for enemy_surf, enemy_rect in enemy_list:
        enemy_rect.x -= 3

        if enemy_rect.right > -100:
            if enemy_rect.bottom == 360:
                current_surf = flies[fly_index]
            elif enemy_rect.bottom == 420:
                current_surf = skeleton_list[skeleton_index]
            else:
                current_surf = enemy_surf  

            screen.blit(current_surf, enemy_rect)
            new_enemy_list.append((current_surf, enemy_rect))
    return new_enemy_list

            
def player_movement():
    global player_surf,player_index,player_jump,player_rect
    if player_rect.bottom<=400:
        player_surf=player_jump
    else:
        player_index+=0.13
        if player_index>=len(player_walk_list) :
            player_index=0
        player_surf=player_walk_list[int(player_index)]



pygame.init()
screen=pygame.display.set_mode((640,480))
pygame.display.set_caption("GAME_SCREEN")
clock=pygame.time.Clock()
text_font=pygame.font.Font("assets/fonts/CrotahFreeVersionItalic-z8Ev3.ttf",40)

pygame.mixer.music.load("assets/sounds/back_ground_music.wav")
jumping_sound=pygame.mixer.Sound("assets/sounds/jumping_sound_2.mp3")
pygame.mixer.music.play(loops=-1)



is_game_active=False
 

ground_surface=pygame.image.load("assets/graphics/ground.jpg")
sky_surface=pygame.image.load("assets/graphics/sky_image.jpg")



game_over_text_surface=text_font.render("Game Over",True,(255,0,0))
game_over_text_surface_rect=game_over_text_surface.get_rect(center=(320,160))


restart_text_surface=text_font.render("Press Space To Restart",True,(255,0,0))
restart_text_surface_rect=restart_text_surface.get_rect(center=(320,300))

#Düşman işlemleri
fly1=pygame.transform.scale(pygame.image.load("assets/graphics/Fly1.png"),(50,36))
fly2=pygame.transform.scale(pygame.image.load("assets/graphics/Fly2.png"),(50,36))

flies=[fly1,fly2]
fly_index=0
enemy_surface=flies[fly_index]



skeleton1=pygame.image.load("assets/graphics/skeleton1.png")
skeleton2=pygame.image.load("assets/graphics/skeleton2.png")
skeleton3=pygame.image.load("assets/graphics/skeleton3.png")
skeleton_list=[skeleton1,skeleton2,skeleton3,]
skeleton_index=0
enemy_surface2=skeleton_list[skeleton_index]



enemy_surfaces=[enemy_surface,enemy_surface2]

enemy_list=[]


#Karakter işlemleri
player_walk_1=pygame.image.load("assets/character_sprite/character_walk_2.png")
player_walk_2=pygame.image.load("assets/character_sprite/character_walk_3.png")
player_stable=pygame.image.load("assets/character_sprite/character_walk_1.png")


player_walk_list=[player_walk_1,player_stable,player_walk_2,player_stable]
player_index=0
player_jump=pygame.image.load("assets/character_sprite/character_walk_2.png")
player_surf=player_walk_list[player_index]
player_rect=player_surf.get_rect(midleft=(20,400))
player_gravity=0


ground_level=420
top_level=0
start_time=0
map_length_min=0
map_length_max=480

#Başlangıç Ekranı
start_screen_surface=pygame.transform.smoothscale((pygame.image.load("assets/graphics/start_screen_final.png")),(640,480))
start_screen_surface_rect=start_screen_surface.get_rect(topleft=(0,0))


start_text = text_font.render("Press Space To Start Game", True, (0, 0, 0))
start_text_rect=start_text.get_rect(center=(320,240))


enemy_spawn=pygame.USEREVENT+1
fly_event=pygame.USEREVENT+2
skeleton_event=pygame.USEREVENT+3

pygame.time.set_timer(skeleton_event,350)
pygame.time.set_timer(fly_event,300)
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
                        jumping_sound.play()
                            
            elif event.type==enemy_spawn:
                random_number=randint(0,1)
                if random_number==0:
                    new_enemy=enemy_surfaces[random_number]
                    new_enemy_rect=new_enemy.get_rect(midbottom=(640,360))
                else:
                    new_enemy=enemy_surfaces[random_number]
                    new_enemy_rect=new_enemy.get_rect(midbottom=(640,420))

                enemy_list.append((new_enemy,new_enemy_rect))
            elif event.type==fly_event:
                if fly_index==0:
                    fly_index=1
                else:
                    fly_index=0
                enemy_surface=flies[fly_index]    
            elif event.type==skeleton_event:
                if skeleton_index==0:
                    skeleton_index=1
                elif skeleton_index==1:
                    skeleton_index=2
                elif skeleton_index==2:
                    skeleton_index=0
                enemy_surface2=skeleton_list[skeleton_index]
 
        else:
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    is_game_active=True
                    # enemy_rect.left=640
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

        player_movement()
        

        screen.blit(player_surf,(player_rect.x,player_rect.y))
        
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

