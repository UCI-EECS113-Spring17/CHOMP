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
 
# --- Classes

        
class Block(pygame.sprite.Sprite):
    """ This class represents the block. """
    def __init__(self, color, height, width):
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.h = height
        self.w = width
        self.image = pygame.Surface([30, 20])
        self.image.fill(color)
 
        self.rect = self.image.get_rect()
        self.yvelocity = random.randrange(5,15)
    def update(self):
        self.rect.y += self.yvelocity
        if self.rect.y >= self.h:
            self.rect.y = 0
            self.rect.x = random.randrange(int((self.w)/6),int(self.w - (self.w)/6))
    def reset(self):
        self.rect.y = 0
        self.rect.x = random.randrange(int((self.w)/6),int(self.w - (self.w)/6))
        
class Player(pygame.sprite.Sprite):
    """ This class represents the Player. """
 
    def __init__(self, com):
        """ Set up the player on creation. """
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        self.image = pygame.Surface([60, 10])
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
    
def collectGame2(screen, clock, coms):
    all_sprites_list = pygame.sprite.Group()
    coin_list        = pygame.sprite.Group()
    w, h = screen.get_size()
    
    
    for i in range(10):
        coin = Block((255,215,0), h, w)
        coin.rect.x = random.randrange(int(w/6),int(w - w/6))
        coin.rect.y = 0

        coin_list.add(coin)
        all_sprites_list.add(coin)



    player = Player(coms)
    all_sprites_list.add(player)
     
    # Loop until the user clicks the close button.
    done = False
     
    # Used to manage how fast the screen updates 
    score = 0
    pygame.mouse.set_visible(False)

    time = utils.Timer(10, screen)
    scoretrack = utils.Score(screen, 20)
    timeout = False
    player.rect.y = h - int(h/7)
    complete = False
    # -------- Main Program Loop -----------
    while not done:
        # --- Event Processing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                
        
        # --- Game logic
        screen.fill(WHITE)

        
        # Call the update() method on all the sprites
        all_sprites_list.update()
     
        # Calculate mechanics for each bullet
        for coin in coin_list:
     
            # See if it hit a block
            block_hit_list = pygame.sprite.spritecollide(player, coin_list, False)
     
            # For each block hit, reset coin and add to the score
            for coin in block_hit_list:
                coin.reset()
                score += 1
                complete = scoretrack.step()  
                print(score)

        
        # --- Draw a frame
        
        # Clear the screen
     
        # Draw all the spites
        all_sprites_list.draw(screen)
        if(time.step()):
            done = True
        elif(int(score) >= 20):
            done = True
        elif complete:
            done = True
        scoretrack.display()
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
     
        # --- Limit to 20 frames per second
        clock.tick(60)
    return complete
