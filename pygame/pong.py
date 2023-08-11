import pygame
from pygame.locals import *
pygame.init()

clock=pygame.time.Clock()

screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Shapes!!")
white=(255,255,255)
black=(0,0,0)
rect1y=200
rect2y=200
circx=300
circy=300
right_move=0
left_move=0
speedx=10
speedy=5
score1=0
score2=0

def show_text(msg, x, y, color, size):
        fontobj= pygame.font.SysFont("freesans", size,bold=True,italic=True)
        msgobj = fontobj.render(msg,False,color)
        screen.blit(msgobj,(x, y))

while True:
    screen.fill(black)
    paddle1=pygame.draw.rect(screen,white,(10,rect1y,10,200))   ###height is 200
    paddle2=pygame.draw.rect(screen,white,(580,rect2y,10,200))
    ball=pygame.draw.circle(screen,white,(circx,circy),20)   ###radius is 20
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key==K_UP:
                right_move=+1
            if event.key==K_DOWN:
                right_move=-1
            if event.key==K_w:
                left_move=+1
            if event.key==K_s:
                left_move=-1

    if right_move==1 and rect2y>=0:    ### to edge of screen only :limiting    
        rect2y-=10                  ###right paddle to go up
    elif right_move==-1 and rect2y<=400:
        rect2y+=10                   ###right paddle to go down
    if left_move==1 and rect1y>=0:
        rect1y-=10                  ###left paddle to go up
    elif left_move==-1 and rect1y<=400:
        rect1y+=10             ### left paddle to go down    height of paddle 200 hence 600-200 =400

    if circx==580:      ##radius 20
        speedx=-speedx
        score1+=1     ### if ball touches the extreme left screen , player 1 gets score
    if circx==20:
        speedx=-speedx
        score2+=1    #### if ball touches the extreme right screen, player 2 gets score
    if circy==580:
        speedy=-speedy
    if circy==20:
        speedy=-speedy
    if paddle1.colliderect(ball) or paddle2.colliderect(ball):     ##If ball in collision  with either left or right paddles
        speedx=-speedx        

    circx=circx+speedx
    circy=circy+speedy

    
    clock.tick(20)

    
    show_text("Score1:",10,10,white,20)        
    show_text(str(score1),80,10,white,20)   ##To print score continously on screen
    show_text("Score2:",500,10,white,20)
    show_text(str(score2),580,10,white,20)

    if score1==2 or score2==2:
        if score1>score2:
            screen.fill((0,255,0))
            show_text("Player 1 wins",200,200,white,50)    ### Condition to end the game and print the score
        else:
            screen.fill((0,255,0))
            show_text("Player 2 wins",200,200,white,50)
    pygame.display.update()
    
    
