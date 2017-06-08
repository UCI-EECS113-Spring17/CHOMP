import pygame
import random
import math
import utils
import camera
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

class Arrow(pygame.sprite.Sprite):
    def __init__(self, direction, w, h):
        super().__init__()
        self.image = pygame.Surface([10,200])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.w = w
        self.h = h

        if direction == 10:
            self.rect.y = int(-self.h/4) #-200
        else:
            self.rect.y = int(self.h + self.h/4) #920
            
        self.rect.x = random.randrange(int(self.w/6), int(self.w - self.w/6)) #100, 1180
        self.vy = direction

        self.wait = random.randrange(30, 300)
        
    def update(self):        
        if self.wait <= 0:
            self.rect.y += self.vy
            if  self.rect.y >=self.h and self.vy == 10:
                self.wait = random.randrange(30, 300)
                self.rect.y = int(-self.h/4)
                self.rect.x = random.randrange(int(self.w/6), int(self.w - self.w/6))
            elif self.rect.y <= int(-self.h/4) and self.vy == -10:
                self.wait = random.randrange(30, 300)
                self.rect.y = int(self.h + self.h/4)
                self.rect.x = random.randrange(int(self.w/6), int(self.w - self.w/6))
        else:
            self.wait -= 1
        

class Player(pygame.sprite.Sprite):
    """ This class represents the Player. """
 
    def __init__(self, com):
        """ Set up the player on creation. """
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        self.image = pygame.Surface([30, 25])
        self.image.fill(RED) 
        self.rect = self.image.get_rect()
        self.coms = com
        
    def update(self):
        """ Update the player's position. """
        # Get the current mouse position. This returns the position
        # as a list of two numbers.
        x, y = self.coms.updateCoords()        
        self.rect.x = x
    
        #pos = pygame.mouse.get_pos()
 
        # Set the player x position to the mouse x position
        #self.rect.x = pos[0]
        #self.rect.y = pos[1]
    

def avoidgame(screen, clock, coms):
    all_sprites_list = pygame.sprite.Group()
    arrow_list        = pygame.sprite.Group()

    w, h = screen.get_size()
    
    for i in range(20):
        arrow = Arrow(random.randrange(-5, 5, 10), w, h)
        arrow_list.add(arrow)
        all_sprites_list.add(arrow)

    player = Player(coms)
    all_sprites_list.add(player)

    player.rect.y = int(h/2)
    done = False

    pygame.mouse.set_visible(False)

    time = utils.Timer(8, screen)
    complete = True

    while not done:
        # --- Event Processing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                
        
        # --- Game logic
        screen.fill(WHITE)

        
        # Call the update() method on all the sprites
        all_sprites_list.update()
     
        # Calculate mechanics 
        for arrow in arrow_list:
     
            # See if it hit a block
            arrow_hit_list = pygame.sprite.spritecollide(player, arrow_list, False)
     
            # For each block hit, reset coin and add to the score
            for arrow in arrow_hit_list:
                done = True
                complete = False
                print("Failure!")
                break
        
        # --- Draw a frame
        
        # Clear the screen
     
        # Draw all the spites
        all_sprites_list.draw(screen)
        if(time.step()):
            done = True
        
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
     
        # --- Limit to 20 frames per second
        clock.tick(60)
    return complete
