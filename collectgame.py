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
# sw = the width of the screen (700)
# sh = the height of the screen (400)
    
class Block(pygame.sprite.Sprite):
    """ This class represents the block. """
    def __init__(self, color):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        self.image = pygame.Surface([30, 20])
        self.image.fill(color)
 
        self.rect = self.image.get_rect()
 
 
class Player(pygame.sprite.Sprite):
    """ This class represents the Player. """
 
    def __init__(self, com):
        """ Set up the player on creation. """
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        self.image = pygame.Surface([50, 50])
        self.image.fill(RED) 
        self.rect = self.image.get_rect()
        self.coms = com
    def update(self):
        """ Update the player's position. """
        # Get the current mouse position. This returns the position
        # as a list of two numbers.
        x, y = self.coms.updateCoords()
        self.rect.x = x
        self.rect.y = y
        """
        pos = pygame.mouse.get_pos()
 
        # Set the player x position to the mouse x position
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        """   
def collectGame(screen, clock, coms):
    all_sprites_list = pygame.sprite.Group()
    coin_list        = pygame.sprite.Group()

    w, h = screen.get_size()

    for i in range(15):
        coin = Block((255,215,0))
        coin.rect.x = random.randrange(int(w/6),int(w - (w/6)))
        coin.rect.y = random.randrange(int(h/6),int(h - (h/6)))

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
    timeout = False
    complete = False
    # -------- Main Program Loop -----------
    while not done:
        # --- Event Processing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                
            
                # launch fail screen                
        # --- Game logic
        
        
        # Call the update() method on all the sprites
        all_sprites_list.update()
     
        # Calculate mechanics for each bullet
        for coin in coin_list:
     
            # See if it hit a block
            block_hit_list = pygame.sprite.spritecollide(player, coin_list, True)
     
            # For each block hit, remove the bullet and add to the score
            for coin in block_hit_list:
                
                score += 1
                print(score)

        
        # --- Draw a frame
        
        # Clear the screen
        screen.fill(WHITE)
     
        # Draw all the spites
        all_sprites_list.draw(screen)
        if(time.step()):
            done = True
        elif(int(score) >= 15):
            done = True
            complete = True
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
     
        # --- Limit to 20 frames per second
        clock.tick(60)
    return complete
