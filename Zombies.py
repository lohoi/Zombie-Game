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
        
        pos = [0.0 , 0.0]
        pos[0] = position[0] +7
        pos[1] = position[1] + 20

        self.dist = 0
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        
    def update(self):
        if self.dist == 170:
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
        pos[0] = random.uniform(0.0,700)  # x
        pos[1] = random.uniform(0.0,500) # y
        self.image = pygame.image.load("zombie1front.png").convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

        #self.player_pos[0] = Alby.rect.x
        #self.player_pos[1] = Alby.rect.y

        self.speed = .5
        
    # end ctor

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

        #print(type(self.rect.x))
        #print(type(num.x))
        
    #end update()
#end Zombie()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.timer = 0

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

        self.rect.x = 250
        self.rect.y = 250
        print(type(self.rect.x))
        '''
        self.left_rect = self.pos
        self.right_rect = self.pos
        self.back_rect = self.pos
        '''
        
        # -1 is a key to remember prev (for idle)
        # 0 for down
        # 1 for right
        # 2 for up
        # 3 for left
        self.direction = 0;
    #end ctor()

    def update_pos(self,screen,keys_pressed):
        if keys_pressed[pygame.K_DOWN]:
            if self.rect.y + 1 < HEIGHT - 50:
                self.rect.y += 1.0
                self.prev = 0
            screen.blit(self.image, self.rect)
        if keys_pressed[pygame.K_RIGHT]:
            if self.rect.x + 1 < WIDTH - 50:
                self.rect.x += 1.0
                self.prev = 1
            screen.blit(self.char_right, self.rect)
        if keys_pressed[pygame.K_UP]:
            if self.rect.y - 1 > 0:
                self.rect.y -= 1.0
                self.prev = 2
            screen.blit(self.char_back, self.rect)
        if keys_pressed[pygame.K_LEFT]:
            if self.rect.x - 1 > 0:
                self.rect.x -= 1.0
                self.prev = 3
            screen.blit(self.char_left, self.rect)
        if self.direction == IDLE:
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
    
    background_img = pygame.image.load("zombie.png").convert()
    Alby = Albert();
    all_sprites_list = pygame.sprite.Group()
    all_sprites_list.add(Alby)

    fire_list = pygame.sprite.Group()
    zombie_list = pygame.sprite.Group()
     
    # -------- Main Program Loop -----------
    while not done:
        # --- Main event loop
        for event in pygame.event.get():
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

            keys_pressed = pygame.key.get_pressed()
            
            

        # --- Game logic should go here
     
        # --- Screen-clearing code goes here
     
        # Here, we clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
     
        # If you want a background image, replace this clear with blit'ing the
        # background image.
        
     
        # Intro Page
        if intro_trigger:
            screen.blit(background_img, [0,0])

            if flickr_count < 20:
                start = Startfont.render("Hit Start to Play",True, WHITE) 
                screen.blit(start,[75,400])
                flickr_count += 1
            else:
                flickr_count +=1
                if flickr_count > 30:
                    flickr_count = 0
            title = Titlefont.render("Insert Name Here",True, BLACK)
            screen.blit(title, [60, 100])
            
            authors = Authorfont.render("Created by Chris Quinones and Albert Lo", True, BLACK)
            illustrator = Authorfont.render("Art by Doug Wu", True,BLACK)
            screen.blit(authors, [60,150])
            screen.blit(illustrator, [60,175])

        # Choose character screen
        elif choose_character:
            screen.fill(RED)

            name = Namefont.render(Alby.name, True, BLACK)
            Alby.spin(screen)
            screen.blit(name,[285, 345])
            

        # Regular gameplay
        else:
            screen.fill(WHITE)
            Alby.update_pos(screen,keys_pressed)
            fire_list.update()
            fire_list.draw(screen)
            zombie_list.update(Alby.rect)
            zombie_list.draw(screen)
        
            pygame.sprite.groupcollide(zombie_list, fire_list,True,True)

            for zombie in zombie_list:
                if Alby.rect.colliderect(zombie):
                    print("YOU LOSE!")
                    done = True
     
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
     
        # --- Limit to 60 frames per second
        clock.tick(60)
     
    # Close the window and quit.
    pygame.quit()
# end main()

if __name__ == "__main__":
    main()
