from pyray import *
from raylib import *
import random


SIDE= 40
WIDTH = 21
HEIGHT = 21
init_window(SIDE*WIDTH,SIDE*HEIGHT,"Mon jeu")
set_target_fps(100)

snake=[[1,1], [2,1],[3,1]]
vitesse=[1,0]
perdu=False
fruit = [WIDTH//2, HEIGHT//2]
Spomme=[random.randint(0,WIDTH-1),random.randint(0,HEIGHT-1)]
Bombe=[random.randint(0,WIDTH-1),random.randint(0,HEIGHT-1)]
S=[0]
s=0
k=0
N=0
while not window_should_close():
    begin_drawing()
    if not perdu : 
        clear_background(BLACK)
        #ANIMATION
        vx,vy=vitesse
        hx,hy=snake[-1]
        new_head=[hx+vx, hy+vy]
        #REACTIVITE DU SERPENT
        if N%10==0:
            if new_head==fruit:
                fruit=[random.randint(0,WIDTH-1), random.randint(0,HEIGHT-1)]
                s=s+10
                k=k+1
            elif new_head==Spomme and k%5==0:
                Spomme=[random.randint(0,WIDTH-1), random.randint(0,HEIGHT-1)]
                s=s+20
                k=k+1
            else:  
                snake=snake[1:]
            snake=snake+[new_head]
            for i in range(len(snake)):
                snake[i][0]=(snake[i][0]%WIDTH)
                snake[i][1]=(snake[i][1]%HEIGHT)
        #MOUVEMENT
        if is_key_pressed(KEY_UP) :
            if vitesse!=[0,1]:
                vitesse=[0,-1]
        if is_key_pressed(KEY_DOWN) : 
            if vitesse!=[0,-1]:
                vitesse=[0,1]
        if is_key_pressed(KEY_LEFT) : 
            if vitesse!=[1,0]:
                vitesse=[-1,0]
        if is_key_pressed(KEY_RIGHT) : 
            if vitesse!=[-1,0]:
                vitesse= [1,0]

        #CONDITIONS DE FIN DE PARTIE
        #CONDTION A MASQUER POUR LE JEU CIRCULAIRE
        #hx,hy=snake[-1]
        #if hx>=WIDTH or hx<0 or hy>=HEIGHT or hy<0:
        #   perdu=True
        #  print("Perdu")
        if new_head in snake[:-1]:
            perdu=True
        elif new_head==Bombe and k%10 in {0,1,2}:
            perdu=True
        
        #DESSIN
        draw_text(f"Score {s}",0,0,50,WHITE)
        if k%5==0:
            draw_rectangle(Spomme[0]*SIDE,Spomme[1]*SIDE,SIDE-2,SIDE-2,YELLOW)
        if k%10 in {0,1,2}:
            draw_rectangle(Bombe[0]*SIDE,Bombe[1]*SIDE,SIDE-2,SIDE-2,DARKGRAY)
            draw_text('BOOM',int((Bombe[0]+1/8)*SIDE),int((Bombe[1]+1/3)*SIDE),5,WHITE)
        if k%10==9:
            Bombe=[random.randint(0,WIDTH-1),random.randint(0,HEIGHT-1)]
        draw_rectangle(fruit[0]*SIDE,fruit[1]*SIDE,SIDE-2,SIDE-2,RED)
        for i,(x,y) in enumerate(snake):
            color=GREEN if i==len(snake)-1 else DARKGREEN
            draw_rectangle(x*SIDE,y*SIDE,SIDE-2,SIDE-2,color)    
        N=N+1
    if perdu :
        #ECRAN DE FIN DE JEU
        if s not in S:
            S.append(s)
        clear_background(BLACK)
        draw_text(f"Score : {s}",0,0,50,WHITE)
        draw_text(f'Best score : {max(S)}',0,SIDE+3,20,WHITE)
        draw_text("GAME OVER", (WIDTH-9)*SIDE//2,(HEIGHT-2)*SIDE//2,50,WHITE)
        if new_head in snake[:-1]:
            draw_text('Vous vous êtes mordu la queue !',(WIDTH-13)*SIDE//2,(HEIGHT-6)*SIDE//2, 30,WHITE)
        elif new_head==Bombe and k%10 in {0,1,2}:
            draw_text('Vous avez mangé une bombe !',(WIDTH-11)*SIDE//2,(HEIGHT-6)*SIDE//2, 30,WHITE)
        #REPRENDRE LE JEU
        draw_text('Presser ENTRER pour rejouer', (WIDTH-9)*SIDE//2, (HEIGHT+1)*SIDE//2, 20, WHITE)
        if is_key_pressed(KEY_ENTER):
            snake=[[1,1], [2,1],[3,1]]
            vitesse=[1,0]
            perdu=False
            fruit = [WIDTH//2, HEIGHT//2]
            Spomme=[random.randint(0,WIDTH-1),random.randint(0,HEIGHT-1)]
            Bombe=[random.randint(0,WIDTH-1),random.randint(0,HEIGHT-1)]
            while Bombe in [[3,1],[4,1],[5,1]]: #Eviter la bombe dès le début de partie
                Bombe=[random.randint(0,WIDTH-1),random.randint(0,HEIGHT-1)]
            s=0
            k=0
            N=0
    end_drawing()
close_window()

