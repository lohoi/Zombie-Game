import pygame
import random
import math
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Constants
IDLE = -1
WIDTH = 700
HEIGHT = 500


class Projectile(pygame.sprite.Sprite):
    def __init__(self,position,fire_direction):
        super().__init__()

        #Creates a fireball with the correct direction
        direct = 0
        direct = fire_direction
        self.dir = direct
        if self.dir == 0:
            self.image = pygame.image.load("fireball1.png").convert()
            self.image = pygame.transform.scale(self.image, [25, 25])
            self.image.set_colorkey(WHITE)
            self.image = pygame.transform.flip(self.image,True,True)
            self.rect = self.image.get_rect()
        elif self.dir == 1:
            self.image = pygame.image.load("fireball1.png").convert()
            self.image = pygame.transform.scale(self.image, [25, 25])
            self.image.set_colorkey(WHITE)
            self.image = pygame.transform.flip(self.image,True,False)
            self.rect = self.image.get_rect()
        else:# self.dir == 3:
            self.image = pygame.image.load("fireball1.png").convert()
            self.image = pygame.transform.scale(self.image, [25, 25])
            self.image.set_colorkey(WHITE)
            self.rect = self.image.get_rect()

            
        # Moves the fireball slightly so that it doesn't
        # fire from Player's head
        pos = [0.0 , 0.0]
        pos[0] = position[0] +7
        pos[1] = position[1] + 20

        self.dist = 0
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        
    def update(self):
        # updates fireball with a speed of 3
        if self.dist == 140:
            # kills the fireball when it reaches a certain distance
            self.kill()
        elif self.dir == 0:
           self.rect.y += 3
        elif self.dir == 1:
            self.rect.x += 3
        elif self.dir == 2:
           self.rect.y -= 3
        elif self.dir == 3:
            self.rect.x -= 3

        self.dist += 3

    #end update()
#end Projectile()

class Zombie(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        pos = [0.0 , 0.0]

        #spawns zombie in random location within map
        pos[0] = random.uniform(0.0,700)  # x
        pos[1] = random.uniform(0.0,500) # y

        #creates the zombie
        self.image = pygame.image.load("zombie1front.png").convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

        self.speed = 1
    # end ctor()

    # loses precision if speed is not an integer
    def update(self,num):
        if self.rect.x < num.x:
            self.rect.x += self.speed
        if self.rect.x > num.x:
            self.rect.x -= self.speed
        if self.rect.y < num.y:
            self.rect.y += self.speed
        if self.rect.y > num.y:
            self.rect.y -= self.speed
    #end update()
#end Zombie()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.timer = 0

    #spin is used for char select screen
    def spin(self,screen):
        if self.timer < 20:
            screen.blit(self.image,[250, 250])
        elif self.timer >= 20 and self.timer < 40:
            screen.blit(self.char_right,[250, 250])
        elif self.timer >= 40 and self.timer < 60:
            screen.blit(self.char_back,[250, 250])
        elif self.timer >= 60 and self.timer < 80:
            screen.blit(self.char_left,[250, 250])
        else:
            self.timer = 0
            screen.blit(self.image,[250, 250])
        self.timer += 1
        return
    # end spin()
# end Player()

class Albert(Player):
    def __init__(self):
        super().__init__()
        self.name = "Alby"

        #loads the 4 directions of Alby
        self.image = pygame.image.load("f_albwhite.png").convert()
        self.image.set_colorkey(WHITE)
        self.image = pygame.transform.scale(self.image, [50,50])
        self.rect = self.image.get_rect()

        
        self.char_left = pygame.image.load("rl_alb.png").convert()
        self.char_left.set_colorkey(BLACK)
        self.char_left = pygame.transform.scale(self.char_left,[50,50])

        self.char_right = pygame.transform.flip(self.char_left,True,False)

        self.char_back = pygame.image.load("b_alb.png").convert()
        self.char_back.set_colorkey(BLACK)
        self.char_back = pygame.transform.scale(self.char_back,[50, 50])
        
        self.prev = 0

        #Alby spawns at loc. x = 250, y = 250
        self.rect.x = 250
        self.rect.y = 250
        
        # -1 is a key to remember prev (for idle)
        # 0 for down
        # 1 for right
        # 2 for up
        # 3 for left
        self.direction = 0;
    #end ctor()

    def update_pos(self,screen,keys_pressed):
        #For movemen
        if keys_pressed[pygame.K_DOWN]:
            if self.rect.y + 2 < HEIGHT - 50:
                # Conditions create boundaries for map
                self.rect.y += 2.0
                self.prev = 0
            screen.blit(self.image, self.rect)
        elif keys_pressed[pygame.K_RIGHT]:
            if self.rect.x + 2 < WIDTH - 50:
                self.rect.x += 2.0
                self.prev = 1
            screen.blit(self.char_right, self.rect)
        elif keys_pressed[pygame.K_UP]:
            if self.rect.y - 2 > 0:
                self.rect.y -= 2.0
                self.prev = 2
            screen.blit(self.char_back, self.rect)
        elif keys_pressed[pygame.K_LEFT]:
            if self.rect.x - 2 > 0:
                self.rect.x -= 2.0
                self.prev = 3
            screen.blit(self.char_left, self.rect)
        elif self.direction == IDLE:
            #If no direction
            if self.prev == 0:
                screen.blit(self.image, self.rect)
            elif self.prev == 1:
                screen.blit(self.char_right, self.rect)
            elif self.prev == 2:
                screen.blit(self.char_back, self.rect)
            else:
                if self.prev == 3:
                    screen.blit(self.char_left,self.rect)  
    # end update_pos()
#end Albert()
      
    
def main():
    pygame.init()

    # Set the width and height of the screen [width, height]
    size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(size)
     
    pygame.display.set_caption("Zombie Survival")
     
    # Loop until the user clicks the close button.
    done = False
     
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # Intro_Trigger is true until the player hits play
    intro_trigger = True
    choose_character = False
    flickr_count = 0

    #fonts
    Titlefont =  pygame.font.SysFont('Calibri',50,True,False)
    Authorfont = pygame.font.SysFont('Calibri',30,False,True)
    Namefont = pygame.font.SysFont('Calibri', 20, False,False)
    Startfont = pygame.font.SysFont('Arial', 30, True, False)

    #background img
    background_img = pygame.image.load("zombie.png").convert()

    #init the sprite groups
    Alby = Albert();
    all_sprites_list = pygame.sprite.Group()
    all_sprites_list.add(Alby)
    fire_list = pygame.sprite.Group()
    zombie_list = pygame.sprite.Group()

    #Any variables for indexing
    indexer = 1
    time_indexer = 0
    
    end_scene = False

    points = 0
    num_fired = 0
     
    # -------- Main Program Loop -----------
    while not done:
        # --- Main event loop
        for event in pygame.event.get():
            # extracts player actions from keyboard
            # and stores within keys_pressed
            if event.type == pygame.QUIT:
                done = True
                break;
            if event.type == pygame.KEYUP:
                 Alby.direction = IDLE
            if event.type == pygame.KEYDOWN:
                if choose_character == True and event.key == pygame.K_RETURN:
                    choose_character = False;
                if intro_trigger == True and event.key == pygame.K_RETURN:
                    intro_trigger = False
                    choose_character = True
                if event.key == pygame.K_DOWN:
                    Alby.direction = 0
                elif event.key == pygame.K_RIGHT:
                    Alby.direction = 1
                elif event.key == pygame.K_UP:
                    Alby.direction = 2
                elif event.key == pygame.K_LEFT:
                    Alby.direction = 3
                elif event.key == pygame.K_SPACE:
                    if Alby.direction == IDLE:
                        fire = Projectile(Alby.rect,Alby.prev)
                        fire_list.add(fire)
                    else:    
                        fire = Projectile(Alby.rect,Alby.direction)
                        fire_list.add(fire)
                        num_fired += 1

            keys_pressed = pygame.key.get_pressed()      

        if intro_trigger:
            # Intro Page
            screen.blit(background_img, [0,0])
            #flickr is used to control how fast the text flashes
            if flickr_count < 20:
                start = Startfont.render("Hit Start to Play",True, WHITE) 
                screen.blit(start,[75,400])
                flickr_count += 1
            else:
                flickr_count +=1
                if flickr_count > 30:
                    flickr_count = 0

            # Title page text
            title = Titlefont.render("Zombie Game",True, BLACK)
            screen.blit(title, [60, 100])
            authors = Authorfont.render("Created by Chris Quinones and Albert Lo", True, BLACK)
            illustrator = Authorfont.render("Player Sprite Art by Doug Wu", True,BLACK)
            screen.blit(authors, [60,150])
            screen.blit(illustrator, [60,175])
            
        elif choose_character:
            # Choose character screen

            #Background color
            screen.fill(RED)

            #text
            instruct = Authorfont.render("Instructions: ",True, BLACK)
            instructions = Namefont.render("Use the arrows keys to move and spacebar to fire projectiles. ",True,BLACK)
            start = Startfont.render("Hit Start to Play",True, WHITE) 
            name = Namefont.render(Alby.name, True, BLACK)

            #display text to screen
            screen.blit(instruct, [10,10])
            screen.blit(instructions, [10,40])
            screen.blit(start,[400,400])
            screen.blit(name,[260, 305])

            # spins the character
            Alby.spin(screen)
            
        elif(end_scene):
            #end scene  
            screen.fill(RED)

            #calculates accuracy
            if num_fired == 0:
                accuracy = 0.0
            else:
                accuracy = (points/num_fired) * 100
            
            accuracy = Namefont.render("Accuracy: " + str(accuracy) ,True,BLACK)
            restart_print = Namefont.render("Hit enter to try again", True, WHITE)
            point_print = Namefont.render("Number of zombies killed: " + str(points), True, BLACK)
            lose_print = Titlefont.render("YOU LOSE!", True, BLACK)

            screen.blit(lose_print, [250,200])
            screen.blit(point_print, [250, 250])
            screen.blit(accuracy, [250,270])
            screen.blit(restart_print, [250, 300])

            # Restarts the game
            if keys_pressed[pygame.K_RETURN]:
                intro_trigger = True
                choose_character = False
                zombie_list = zombie_list = pygame.sprite.Group()
                end_scene = False
                fire_list = pygame.sprite.Group()
                indexer = 1
                time_indexer = 0
                points = 0
                continue
        else:
            # Regular gameplay
            if (time_indexer == 0):
                # Creates zombies only when time_indexer is 0
                for i in range(indexer):
                    test = Zombie()
                    while(abs(test.rect.x - Alby.rect.x) < 200 or abs(test.rect.y - Alby.rect.y) < 200):
                        # If zombie spawns within 200 units of character
                        test.rect.x = random.uniform(0.0,700) # x
                        test.rect.y = random.uniform(0.0,500) # y
                    zombie_list.add(Zombie())
                #increase the capacity of zombies spawned for next round
                indexer += 1
            time_indexer += 1
            if(time_indexer > 200):
                #time_indexer controls how much time is between zombie spawns
                time_indexer = 0
            screen.fill(WHITE)
            Alby.update_pos(screen,keys_pressed)
            fire_list.update()
            fire_list.draw(screen)
            zombie_list.update(Alby.rect)
            zombie_list.draw(screen)

            #kills zombies if they collide with projectiles
            hit_list = pygame.sprite.groupcollide(zombie_list, fire_list,True,True)

            #increment points if zombie hit
            for i in hit_list:
                points += 1
            
            for zombie in zombie_list:
                if Alby.rect.colliderect(zombie):
                    end_scene = True
                    continue
     
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
     
        # --- Limit to 60 frames per second
        clock.tick(60)
     
    # Close the window and quit.
    pygame.quit()
# end main()

if __name__ == "__main__":
    main()
