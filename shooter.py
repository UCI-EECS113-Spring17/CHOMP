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

class Block(pygame.sprite.Sprite):
    """ This class represents the block. """
    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()        
        self.image = pygame.Surface([50, 50])
        self.image.fill(color)
        self.h = height
        self.w = width
        self.rect = self.image.get_rect()
        #self.script = randrange(1,3)
        self.wait = random.randrange(1,4) * 60
        self.returning = False
    def update(self):
        if self.returning == True:
            self.rect.y += 10
            if self.rect.y >= int(self.h/7):#was 100 before
                self.returning = False            
        else:  
            if self.wait <= 0:
                self.rect.y += 15
                if self.rect.y >= self.h:
                    self.wait = 60
                    self.returning = True
                    self.rect.y = -100
            else:
                self.wait -= 1
        
 
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
        #pos = pygame.mouse.get_pos()
        # Set the player x position to the mouse x position
        #self.rect.x = pos[0]    

class Bullet(pygame.sprite.Sprite):
    """ This class represents the bullet . """
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        self.image = pygame.Surface([4, 10])
        self.image.fill(BLACK)
 
        self.rect = self.image.get_rect()
 
    def update(self):
        """ Move the bullet. """
        self.rect.y -= 3

def shooter(screen, clock, coms):
    all_sprites_list = pygame.sprite.Group()
    block_list = pygame.sprite.Group()
    bullet_list = pygame.sprite.Group()

    w, h = screen.get_size()
    
    xpos = int(w/6)
    for i in range(5):
        block = Block(BLUE, w, h)
        block_list.add(block)
        all_sprites_list.add(block)
        block.rect.x = xpos
        block.rect.y = int(0 + h/7)
        xpos += 100
    player = Player(coms)
    all_sprites_list.add(player)

    done = False

    player.rect.y = int(h - h/7)

    pygame.mouse.set_visible(False)
    time = utils.Timer(14, screen)
    x = 0
    complete = False
    while not done:
        # --- Event Processing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        x += 1
        if x == 25:
            x = 0
            bullet = Bullet()
            bullet.rect.x = player.rect.x + 25
            bullet.rect.y = player.rect.y
            all_sprites_list.add(bullet)
            bullet_list.add(bullet)

        all_sprites_list.update()

        for block in block_list:
            player_died = pygame.sprite.spritecollide(player, block_list, False)
            for block in player_died:
                done = True
                print("You died")

        for bullet in bullet_list:

            block_hit_list = pygame.sprite.spritecollide(bullet, block_list, True)

            for block in block_hit_list:
                bullet_list.remove(bullet)
                all_sprites_list.remove(bullet)

            if bullet.rect.y < -10:
                bullet_list.remove(bullet)
                all_sprites_list.remove(bullet)

        screen.fill(WHITE)
        all_sprites_list.draw(screen)
        if(time.step()):
            done = True
        elif not block_list:
            done = True
            complete = True
        pygame.display.flip()
        clock.tick(60)
    return complete    
