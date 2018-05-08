import pygame
import random


class Enemy(pygame.sprite.Sprite):

    def __init__(self, name, x, y, health=5, speed=2):
        '''
        constructor
        name: enemy name
        x: enemy position on the x coord
        y: enemy position on the y coord
        health: enemy health
        speed: enemy speed
        '''
        pygame.sprite.Sprite.__init__(self)

        self.name = str(name)
        self.image = pygame.image.load('assets/' + self.name + '.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.health = health
        self.speed = speed
        self.bosses = pygame.sprite.Group()

    def move(self, x, y):
        '''
        amount to move enemy by
        x:amount to move on x coord
        y: anount to move on y coord
        '''
        self.rect.x += x
        self.rect.y += y

    def chasePlayer(self, player):
        '''
        decide wether to chase player or run away from player

        player: player as a parameter
        '''
        if (abs(player.rect.x - self.rect.x) > abs(player.rect.y - self.rect.y)) and player.rect.x > self.rect.x:
            self.move(self.speed, 0)
        elif (abs(player.rect.x - self.rect.x) > abs(player.rect.y - self.rect.y)) and player.rect.x < self.rect.x:
            self.move(-self.speed, 0)
        elif (abs(player.rect.y - self.rect.y) > abs(player.rect.x - self.rect.x)) and player.rect.y > self.rect.y:
            self.move(0, self.speed)
        elif (abs(player.rect.y - self.rect.y) > abs(player.rect.x - self.rect.x)) and player.rect.y < self.rect.y:
            self.move(0, -self.speed)
        elif (abs(player.rect.x - self.rect.y) == abs(player.rect.y - self.rect.y)):
            self.move(1, 1)

    def updateEnemy(self, player):
        '''
        checks whether enemy is dead
        player: player name
        '''

        if self.health <= 0:
            self.kill()
            player.score += 100

