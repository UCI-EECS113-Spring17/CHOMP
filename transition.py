import pygame
import random
import math
import time

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

def transition(screen, clock, instruct, sw, sh):    
   

    done = False
    x = sw
    x2 = 0 
    font = pygame.font.Font(None, 50)
    text = font.render(instruct, 1, (255,255,255))
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        pygame.draw.rect(screen, BLACK, (x,0,sw, sh))
        screen.blit(text, ((sw + sw/4)  - x2, sh/2))

        x -= 20
        x2 += 20
        if(x <= -40):
            done = True
            pause(60, screen, clock)
        pygame.display.flip()
        clock.tick(60)

    done = False
    x -= 20
    x2 += 20
    
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen.fill(BLACK)
        pygame.draw.rect(screen, BLACK, (x,0,sw, sh))
        screen.blit(text, ((sw + sw/4) - x2, sh/2))

        x -= 20
        x2 += 20
        if(x <= (-1 * sw)):
            done = True            
        pygame.display.flip()
        clock.tick(60)
    
# pauses time for set amount
# each number is 1/60 of a second
def pause(timetopause, screen, clock):
    
    done = False
    track = 0
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        track += 1
        if track == timetopause:
            done = True
        clock.tick(60)

    
        
