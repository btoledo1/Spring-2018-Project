import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self,x,y,name="starboy_left"):
        pygame.sprite.Sprite.__init__(self)

        self.position = (name)
        self.speed = 10
        self.image = pygame.image.load('assets/'+self.position+'.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.health = 5
        self.damage = 1
        self.score = 0
        self.max_health = 5

    def move_up(self):
        self.rect.y += self.speed

    def move_down(self):
        self.rect.y -= self.speed

    def move_left(self):
        self.image = pygame.image.load("assets/starboy_left.png")
        self.rect.x -= self.speed

    def move_right(self):
        self.position = "starboy_right"
        self.image = pygame.image.load("assets/starboy_right.png")
        self.rect.x += self.speed

    def update(self):
        if self.health <= 0:
            self.kill()

class Attack(pygame.sprite.Sprite):

    def __init__(self,x,y,name="assets/whip"):
        pygame.sprite.Sprite.__init__(self)

        self.name = str(name)
        self.speed = 5
        self.image = pygame.image.load(self.name+'.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def move(self,x,y):
        self.rect.x += x
        self.rect.y += y

    def update(self,player):
        self.rect.x,self.rect.y = player.rect.x- 100, player.rect.y-70






















        

  
