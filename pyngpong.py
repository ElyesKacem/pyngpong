import pygame
import time
import random
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (250,100)
pygame.init()

w=600
h=604

win = pygame.display.set_mode((w,h))
pygame.display.set_caption("First Game")

clock=pygame.time.Clock()
white=(255,255,255)

x = 2
y = 220
width = 10
height = 60
vel = 15
x2=w-12
y2=220

xc=w//2
yc=h//2

pygame.draw.line(win,(255,0,0),(w//2,0),(w//2,h),1)
directionx=-10
directiony=8
scoreJoueur1=scoreJoueur2=0

def ballmov():
    global xc,yc,directionx,directiony,x,speed

    if((xc<=x+width) and (yc>=y)and (yc<=y+height))or((xc>=x2)and(yc>=y2) and(yc<=y2+height)):
        directionx=-directionx
        speed+=2
    if(yc<=4) or (yc>=h):
        directiony=-directiony
    xc+=directionx
    yc+=directiony
    winner()

def winner():
    global scoreJoueur1,scoreJoueur2,xc,speed
    if(xc<=-20):
        scoreJoueur2+=1
        xc=w//2
        yc=h//2
        speed=20
        print(scoreJoueur2)
        time.sleep(3)
    if(xc>=w+20):
        scoreJoueur1+=1
        xc=w//2
        yc=h//2
        speed=20
        print(scoreJoueur1)
        time.sleep(3)
        
        

run = True
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
X = 400
Y = 400
 
# create the display surface object
# of specific dimension..e(X, Y).
 
 
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('GeeksForGeeks', True, green, blue)
speed=20
while run:
    #pygame.time.delay(100)
    clock.tick(speed)
    win.blit(text, (200,200))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    

    if keys[pygame.K_UP]:
        if(y2>0):
            y2 -= vel
    if keys[pygame.K_DOWN]:
        if(y2<h-60):
            y2 += vel
        print(y)
    
    if keys[pygame.K_e]:
        if(y>0):
            y -= vel
    if keys[pygame.K_d]:
        if(y<h-60):
            y += vel
    '''if keys[pygame.K_s]:
        print(pygame.mouse.get_pos())
        time.sleep(1)'''
    if keys[pygame.K_F1]:
        run=False
    
    
    win.fill((0.5,0.5,0))  # Fills the screen with black
    pygame.draw.circle(win,white,(xc,yc),5)
    ballmov()    
    pygame.draw.rect(win, (255,0,0), (x, y, width, height))
    pygame.draw.rect(win, (255,0,0), (x2, y2, width, height))
    pygame.draw.line(win,(255,0,0),(w//2,0),(w//2,h),1)
    pygame.display.update() 
    
pygame.quit()
