import pygame
pygame.init()
# enemy class
class enemy(pygame.sprite.Sprite):

    def __init__(self,x,y,width,height):
        # gives instatiation as pygame sprite
        super().__init__()
        # creates hit box
        self.rect = pygame.Rect(x,y,width,height)
        # creates speed
        self.vel = 2
        # creates health
        self.health = 5
        # sets no collisions
        self.canMove = True
        #if they are chasing the player down
        self.agro = False
        #checks which way to face
        self.right = True
        self.left = False

        self.walkCount = 0
        self.slowIdle = 0
        self.idle = [pygame.image.load("art/big_demon_idle_anim_f0.png"),pygame.image.load("art/big_demon_idle_anim_f1.png"),pygame.image.load("art/big_demon_idle_anim_f2.png"),pygame.image.load("art/big_demon_idle_anim_f3.png")]
        self.walk = [pygame.image.load('art/big_demon_run_anim_f0.png'),pygame.image.load('art/big_demon_run_anim_f1.png'),pygame.image.load('art/big_demon_run_anim_f2.png'),pygame.image.load('art/big_demon_run_anim_f3.png')]

    #draw function
    def draw(self,win, coords):
        if self.walkCount >= len(self.walk) * 3:
            self.walkCount = 0

        if self.agro:
            if self.right:
                self.image = self.walk[self.walkCount//3]
            elif self.left:
                self.image = pygame.transform.flip(self.walk[self.walkCount//3], 1, 0)
            self.walkCount += 1
        else:
            self.image = self.idle[self.walkCount//3]
            
            if self.slowIdle == 0:
                self.slowIdle += 1
            else:
                self.walkCount += 1
                self.slowIdle = 0

        win.blit(self.image,coords)



    #movement
    def move(self, target):
        # checks for collisions
        if self.canMove:
            if target.rect.x > self.rect.x - 200 and target.rect.x < self.rect.x + 200 and target.rect.y > self.rect.y - 200 and target.rect.y < self.rect.y + 200:
                self.agro = True
            # if the enemy is agro at the player chase them down    
            if self.agro:
                # moves towards target, at the moment it is basic as the map hasn't been implemented so no need for path finding 
                if self.rect.x + self.rect.width < target.rect.x:
                    self.rect.x += self.vel
                    self.right = True
                    self.left = False
                elif self.rect.x > target.rect.x + target.rect.width:
                    self.rect.x -= self.vel
                    self.right = False
                    self.left = True

                if self.rect.y < target.rect.y:
                    self.rect.y += self.vel
                elif self.rect.y > target.rect.y:
                    self.rect.y -= self.vel
        else:
            self.canMove = True

    
    def shot(self, enemies, all_sprite_list, enemy_hit_list):
        
        self.agro = True
        self.health -= 1

        if self.health == 0:
            enemies.remove(self)
            all_sprite_list.remove(self)
        enemy_hit_list.remove(self)


class demon(enemy):

    def __init__(self,x,y,width,height):
        super().__init__(x,y,width,height)
        self.health = 2
        self.vel = 3
        self.slowIdle = 0
        self.idle = [pygame.image.load("art/chort_idle_anim_f0.png"),pygame.image.load("art/chort_idle_anim_f1.png"),pygame.image.load("art/chort_idle_anim_f2.png"),pygame.image.load("art/chort_idle_anim_f3.png")]
        self.walk =[pygame.image.load("art/demon4.png"),pygame.image.load("art/demon5.png"),pygame.image.load("art/demon6.png"),pygame.image.load("art/demon7.png")]    

    def draw(self,win, coords):
        if self.walkCount >= len(self.walk) * 3:
            self.walkCount = 0

        if self.agro:
            if self.right:
                self.image = self.walk[self.walkCount//3]
            elif self.left:
                self.image = pygame.transform.flip(self.walk[self.walkCount//3], 1, 0)

            self.walkCount += 1
        else:
            self.image = self.idle[self.walkCount//3]
            
            if self.slowIdle == 0:
                self.slowIdle += 1
            else:
                self.walkCount += 1
                self.slowIdle = 0

        win.blit(self.image,coords)

    
    
    def move(self, target):
        super().move(target)
    
    
    def shot(self, enemies, all_sprite_list, enemy_hit_list):
        super().shot(enemies, all_sprite_list, enemy_hit_list)
