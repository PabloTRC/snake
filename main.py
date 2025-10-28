from pyray import *
from raylib import *
import random
SIDE= 40
WIDTH = 21
HEIGHT = 21
init_window(SIDE*WIDTH,SIDE*HEIGHT,"Mon jeu")
set_target_fps(10)

snake=[[1,1], [2,1],[3,1]]
vitesse=[1,0]
perdu=False
fruit = [WIDTH//2, HEIGHT//2]
Spomme=[random.randint(0,WIDTH-1),random.randint(0,HEIGHT-1)]
s=0
k=0
N=0
while not window_should_close() and not perdu:
    begin_drawing()
    clear_background(BLACK)
    #ANIMATION
    vx,vy=vitesse
    hx,hy=snake[-1]
    new_head=[hx+vx, hy+vy]

    if new_head==fruit:
        fruit=[random.randint(0,WIDTH-1), random.randint(0,HEIGHT-1)]
        s=s+10
        k=k+1
    elif new_head==Spomme:
        Spomme=[random.randint(0,WIDTH-1), random.randint(0,HEIGHT-1)]
        s=s+20
    else:  
        snake=snake[1:]
    snake=snake+[new_head]

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
    hx,hy=snake[-1]
    if hx>=WIDTH or hx<0 or hy>=HEIGHT or hy<0:
        perdu=True
        print("Perdu")
    elif new_head in snake[:-1]:
        perdu=True
        print("Perdu")
    #DESSIN
    
    draw_text(f"Score {s}",0,0,10,WHITE)
    print(f"Score : {s}")
    if k%5==0:
        draw_rectangle(Spomme[0]*SIDE,Spomme[1]*SIDE,SIDE-2,SIDE-2,YELLOW)
    draw_rectangle(fruit[0]*SIDE,fruit[1]*SIDE,SIDE-2,SIDE-2,RED)
    for i,(x,y) in enumerate(snake):
        color=GREEN if i==len(snake)-1 else DARKGREEN
        draw_rectangle(x*SIDE,y*SIDE,SIDE-2,SIDE-2,color)    
    N=N+1
    
    end_drawing()
close_window()

