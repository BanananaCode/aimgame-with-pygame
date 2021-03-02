import pygame   #pygame module
import math #Checking collisions in circle
import random   #giving circles a random spot 

#Defines screens and starts pygame
pygame.init()

width=800
height=900
display = pygame.display.set_mode((width,height)) #Displays screen

#colours for circles
red=(255,51,51)
blue=(0,0,255)
yellow=(255,255,51)
green=(51,255,51)
purple=(153,51,255)
pink=(255,51,255)
white=(0,0,0) #background
colour=[red,blue,yellow,green,purple,pink]

#Define FPS
FPS=60

scorex= 0
scorey= 0

score = 0

def show_score(x, y, score):
    font = pygame.font.Font('freesansbold.ttf', 32)
    score = font.render("Score : " + str(score), True, (255, 255, 255))
    display.blit(score, (x, y))

show_score(scorex,scorey, score)

#Title and Icon
pygame.display.set_caption("Aim Game")  
icon = pygame.image.load('res\icon.png')
pygame.display.set_icon(icon)

#Background
#background= pygame.image.load('firstgame/space.png')

#First circle will appear if statement will then produce another circle
cx= random.randint(20,width-20) #(left side of screen, width-20)
cy=random.randint(20,height-20)
rad_circle=random.randint(14,20) #random radius of circle / adjust for difficulty
pygame.draw.circle(display, random.choice(colour),(cx,cy),rad_circle)   #displays circle

running = True

#main loop
while running:
    
    #background image
    #display.blit(background,(0,0)) 
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    clock = pygame.time.Clock()
    clock.tick(FPS) #Sets framerate
    
    x = pygame.mouse.get_pos()[0] #pos left mouse button
    y = pygame.mouse.get_pos()[1]
    click = pygame.mouse.get_pressed()
    
    sqx = (x-cx)**2 # finds collision with circle
    sqy = (y - cy)**2
    
    if math.sqrt(sqx+sqy) < rad_circle and click[0] ==1: 
        display.fill(white) # sets background to space / resets screen
        cx= random.randint(20,width-20) #(left side of screen, width-20)
        cy=random.randint(20,height-20)
        rad_circle=random.randint(14,20) #random radius of circle
        pygame.draw.circle(display, random.choice(colour),(cx,cy),rad_circle)   #displays circle
        score=score+1
        show_score(scorex,scorey,score)
    
    
    pygame.display.update()

