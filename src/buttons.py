import pygame

class Button(pygame.sprite.Sprite):

    def __init__(self,x,y, image="assets/button.png"):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.if_pressed = False
