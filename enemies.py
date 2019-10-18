import pygame
pygame.init()
# enemy class
class enemy(pygame.sprite.Sprite):

    def __init__(self,x,y,width,height,):
        # gives instatiation as pygame sprite
        super().__init__()
        # creates hit box
        self.rect = pygame.Rect(x,y,width,height)
        # creates speed
        self.vel = 2
        # creates health
        self.health = 3
        # sets no collisions
        self.canMove = True
        #if they are chasing the player down
        self.agro = 0

    #draw function
    def draw(self,win, coords):
        # at the moment just a green square
        pygame.draw.rect(win, (0, 255, 0), coords)

    #movement
    def move(self, target):
        # checks for collisions
        if self.canMove:
            if target.rect.x > self.rect.x - 200 and target.rect.x < self.rect.x + 200 and target.rect.y > self.rect.y - 200 and target.rect.y < self.rect.y + 200:
                self.agro = 1
            # if the enemy is agro at the player chase them down    
            if self.agro == 1:
                # moves towards target, at the moment it is basic as the map hasn't been implemented so no need for path finding 
                if self.rect.x < target.rect.x:
                    self.rect.x += self.vel
                elif self.rect.x > target.rect.x:
                    self.rect.x -= self.vel

                if self.rect.y < target.rect.y:
                    self.rect.y += self.vel
                elif self.rect.y > target.rect.y:
                    self.rect.y -= self.vel
        else:
            self.canMove = True

    
    def shot(self, enemies, all_sprite_list, enemy_hit_list):
        self.agro = 1
        self.health -= 1
        if self.health == 0:
            enemies.remove(self)
            all_sprite_list.remove(self)
        enemy_hit_list.remove(self)
