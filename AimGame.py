import pygame  # pygame module
from pygame import *  # pygame modules
import math  # Checking collisions in circle
import random  # giving circles a random spot

# Defines screens and starts pygame
pygame.init()

width = 1000
height = 800
display = pygame.display.set_mode((width, height))  # Displays screen

# colours for circles
red = (255, 51, 51)
blue = (0, 0, 255)
yellow = (255, 255, 51)
green = (51, 255, 51)
purple = (153, 51, 255)
pink = (255, 51, 255)
white = (255, 255, 255)  # background
colour = [red, blue, yellow, green, purple, pink]

scoreX, scoreY = 0,0
score = 0

def showScore(x, y, score):
    font = pygame.font.Font('freesansbold.ttf', 32)
    score = font.render("Score : " + str(score), True, (255, 255, 255))
    display.blit(score, (x, y))


def showEndScreen(finalScore):
    font = pygame.font.Font('freesansbold.ttf', 32)
    blurb = font.render("YOU LOSE :(", True, (255, 255, 255))
    display.blit(blurb, ((width/2)-50, (height/2)-30))
    showScore((width/2)-50, height/2, finalScore)  # center and show score


showScore(scoreX, scoreY, score)

#Title and Icon
pygame.display.set_caption("Aim Game")
icon = pygame.image.load('res\icon.png')
pygame.display.set_icon(icon)

# Background
#background= pygame.image.load('firstgame/space.png')

# First circle will appear if statement will then produce another circle
cx = random.randint(20, width-20)  # (left side of screen, width-20)
cy = random.randint(20, height-20)
# random radius of circle / adjust for difficulty
rad_circle = random.randint(14, 20)
pygame.draw.circle(display, random.choice(colour),
                   (cx, cy), rad_circle)  # displays circle

running = True
lost = False
counter = 1
currentColour = (50, 255, 100)


trailLength = 25

lastPoints = [(0,0)]*trailLength

pygame.mouse.set_visible(False)

# main loop
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Define FPS (+ score * 8 to increase the speed of the game based on how far the player gets)
    FPS = 60 + score * 8

    clock = pygame.time.Clock()
    clock.tick(FPS)  # Sets framerate
    
    #speed = 60 + score * 8


    x = pygame.mouse.get_pos()[0]  # pos left mouse button
    y = pygame.mouse.get_pos()[1]
    click = pygame.mouse.get_pressed()

    sqx = (x-cx)**2  # finds collision with circle
    sqy = (y - cy)**2

    if lost == False and math.sqrt(sqx+sqy) < rad_circle and click[0] == 1:
        cx = random.randint(20, width-20)  # (left side of screen, width-20)
        cy = random.randint(20, height-20)
        rad_circle = random.randint(14, 20)  # random radius of circle

        display.fill((0, 0, 0))
        currentColour = random.choice(colour)
        score = score+1
        showScore(scoreX, scoreY, score)
        counter = 0
    else:
        try:
            display.fill(((counter), 0, 0))
            pygame.draw.circle(display, currentColour, (cx, cy),
                               rad_circle)  # displays circle
            showScore(scoreX, scoreY, score)
        except:
            lost = True
    
    def getMouseCoords():
        x,y = pygame.mouse.get_pos()
        return (x,y)
    
    # Draw a solid blue circle in the center
    
    lastPoints.pop(0)
    lastPoints.append(getMouseCoords())
    

    for i in range(trailLength):
        #circleColorR, circleColorG, circleColorB
        
        temp = i/trailLength
        
        
        #print(currentColorR, currentColorG, currentColorB)
        pygame.draw.circle(display, (255, 255, 255), (lastPoints[i]), 5)
    
    pygame.draw.circle(display, (255, 255, 0), (getMouseCoords()), 8)    
    #draw health bar
    pygame.draw.rect(display, [0,255,255], (((width/4),25),((counter/255)*((width/4)*2),25)))
    
    #outline
    pygame.draw.rect(display, [255,255,255], (((width/4),25),((width/4)*2,25)) , 2)
    
    

    if lost == True:
        display.fill(((255), 0, 0))
        showEndScreen(score)

    pygame.display.update() # sets the screen

    counter += 1  # increase by 1 one every frame
