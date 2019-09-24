class enemy(pygame.sprite.Sprite):

    def __init__(self,x,y,width,height):
        super().__init__()
        self.rect = pygame.Rect(x,y,width,height)
        self.vel = 2
        self.health = 3
        self.canMove = True
        self.image = pygame.draw.rect(win, green, self.rect)

    #draw function
    def draw(self,win):
        self.move()
        pygame.draw.rect(win, green, self.rect)

    #movement
    def move(self):
        if self.canMove:
            if self.rect.x < man.rect.x:
                self.rect.x += self.vel
            elif self.rect.x > man.rect.x:
                self.rect.x -= self.vel

            if self.rect.y < man.rect.y:
                self.rect.y += self.vel
            elif self.rect.y > man.rect.y:
                self.rect.y -= self.vel
        else:
            self.canMove = True
    
    def shot(self):
        self.health -= 1
        if self.health == 0:
            enemies.remove(self)
        enemy_hit_list.remove(self)
