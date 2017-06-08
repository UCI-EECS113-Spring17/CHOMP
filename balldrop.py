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

class Ball(pygame.sprite.Sprite):
    def __init__(self, color, w, h):
        super().__init__()
        self.image = pygame.Surface([50,50])
        self.image.fill(color)
        self.w = w
        self.h = h
        # flag to check if the ball has fallen off the screen
        self.failed = False
        self.dropped = False
        
        self.rect = self.image.get_rect()

        self.vy = random.randrange(-7, 7, 2)
        self.vx = random.randrange(-7, 7, 2)
    def update(self):
        if self.dropped == True:
            self.rect.y += self.vy
            self.rect.x += self.vx
            if self.rect.y >= int(self.h - self.h/7): #620
                self.failed = True
                #self.vy = random.randrange(-20,-15)
            elif self.rect.y <= 0:            
                self.vy = random.randrange(3, 6) #(15, 20)
            if self.rect.x >= 590: #1180
                self.vx = random.randrange(-6,-3) #(-20,-15)
            elif self.rect.x <= 0:
                self.vx = random.randrange(3, 6) #(15, 20)
        else:
            self.rect.y += 10
            if self.rect.y >= 0:
                self.dropped = True
    def bounce(self):
        self.vy *= (-1)

    def fail(self):
        return self.failed
    
class Player(pygame.sprite.Sprite):
    """ This class represents the Player. """
 
    def __init__(self, com):
        """ Set up the player on creation. """
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        self.image = pygame.Surface([100, 50])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.coms = com
        
    def update(self):
        """ Update the player's position. """
        # Get the current mouse position. This returns the position
        # as a list of two numbers.
        #x, y = self.cam.read()
        x, y = self.coms.updateCoords()
        self.rect.x = x        

        #pos = pygame.mouse.get_pos()
        # Set the player x position to the mouse x position
        #self.rect.x = pos[0]    
        
def balldrop(screen, clock, coms):
    all_sprites_list = pygame.sprite.Group()
    ball_list        = pygame.sprite.Group()

    w, h = screen.get_size()

    ball = Ball(BLACK, w, h)
    ball_list.add(ball)
    all_sprites_list.add(ball)

    ball.rect.x = int(w/2)
    ball.rect.y = -h

    player = Player(coms)
    all_sprites_list.add(player)
    player.rect.y = int(h - h/7) #700
    
    done = False

    pygame.mouse.set_visible(True)

    time = utils.Timer(10, screen)
    complete = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        screen.fill(WHITE)
        all_sprites_list.update()

        for balls in ball_list:
            block_hit_list = pygame.sprite.spritecollide(player, ball_list, False)

            for balls in block_hit_list:
                balls.bounce()
                
                
        all_sprites_list.draw(screen)
        if(time.step()):
            done = True
            complete = True
        elif (ball.fail()):
            done = True        
        pygame.display.flip()
        
        clock.tick(60)
    return complete
