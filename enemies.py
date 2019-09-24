import pygame
pygame.init()
# enemy class
class enemy(pygame.sprite.Sprite):

    def __init__(self,x,y,width,height,):
        super().__init__()
        self.rect = pygame.Rect(x,y,width,height)
        self.vel = 2
        self.health = 3
        self.canMove = True

    #draw function
    def draw(self,win):
        pygame.draw.rect(win, (0, 255, 0), self.rect)

    #movement
    def move(self, target):
        if self.canMove:
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
        self.health -= 1
        if self.health == 0:
            enemies.remove(self)
            all_sprite_list.remove(self)
        enemy_hit_list.remove(self)
