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

class Ball(pygame.sprite.Sprite):
    def __init__(self, color, w, h):
        super().__init__()
        self.image = pygame.Surface([50,50])
        self.image.fill(color)
        self.w = w
        self.h = h
        self.rect = self.image.get_rect()

        self.vy = random.randrange(-7, 7, 2)
        self.vx = random.randrange(-7, 7, 2)
    def update(self):
        self.rect.y += self.vy
        self.rect.x += self.vx
        if self.rect.y >= 430: #520
            self.vy = random.randrange(-10,-7)
        elif self.rect.y <= 0:            
            self.vy = random.randrange(7, 10)
        if self.rect.x >= self.w - 50:
            self.vx = random.randrange(-7,-10)
        elif self.rect.x <= 0:
            self.vx = random.randrange(7, 10)
        
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
        #pos = pygame.mouse.get_pos()
 
        # Set the player x position to the mouse x position
        #self.rect.x = pos[0]
        #self.rect.y = pos[1]
        
def surviveBall(screen, clock, coms):
    all_sprites_list = pygame.sprite.Group()
    ball_list        = pygame.sprite.Group()

    w, h = screen.get_size()

    ball = Ball(BLACK, w, h)
    ball_list.add(ball)
    all_sprites_list.add(ball)
    """
    for i in range(15):
        coin = Block((255,215,0))
        coin.rect.x = random.randrange(100,1180)
        coin.rect.y = 0

        coin_list.add(coin)
        all_sprites_list.add(coin)
    """
    ball.rect.x = 100
    ball.rect.y = 100
    player = Player(coms)
    all_sprites_list.add(player)
     
    # Loop until the user clicks the close button.
    done = False
     
    # Used to manage how fast the screen updates 
    score = 0
    pygame.mouse.set_visible(False)

    time = utils.Timer(8, screen)
    
    timeout = False
    complete = True
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
     
        # Calculate mechanics 
        for ball in ball_list:
     
            # See if it hit a block
            block_hit_list = pygame.sprite.spritecollide(player, ball_list, False)
     
            # For each block hit, reset coin and add to the score
            for ball in block_hit_list:
                done = True
                complete = False
                print("Failure!")

        
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
