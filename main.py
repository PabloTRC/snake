from pyray import *
SIDE= 40
WIDTH = 20
HEIGHT = 20
init_window(SIDE*WIDTH,SIDE*HEIGHT,"Mon jeu")
set_target_fps(10)

snake=[[1,1], [2,1],[3,1]]
vitesse=[1,0]
while not window_should_close():
    begin_drawing()
    clear_background(BLACK)
    #ANIMATION
    vx,vy=vitesse
    hx,hy=snake[-1]
    new_head=[hx+vx, hy+vy]
    snake=snake[1:]+[new_head]
    if is_key_pressed(KEY_UP) : 
        vitesse=[0,-1]
    if is_key_pressed(KEY_DOWN) : 
        vitesse=[0,1]
    if is_key_pressed(KEY_LEFT) : 
        vitesse=[-1,0]
    if is_key_pressed(KEY_RIGHT) : 
        vitesse= [1,0]
    
    #DESSIN
    for i,(x,y) in enumerate(snake):
        color=GREEN if i==len(snake)-1 else DARKGREEN
        draw_rectangle(x*SIDE,y*SIDE,SIDE-2,SIDE-2,color)
    
    end_drawing()
close_window()

