import pygame
import random


class Powerups(pygame.sprite.Sprite):

    def __init__(self,name,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.image = pygame.image.load("assets/rage.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


    def spawnRandomPowerup(self):
        """
        Spawns a random powerup
        :return:self.roll(string): Using the random module it picks a random powerup from a list of strings which
        represents powerups
        self.image(Surface): Loads the random powerup image to be blitted onto the game
        """
        self.roll = random.choice(['rage','healthUp','damageUp'])
        self.image = pygame.image.load('assets/'+self.roll+'.png')

    def health(self,player):
        """
        This increases the player's health but it does not exceed the maximum health
        :param player:(Player): Takes the player class so their stats can be increased
        :return: player.health:(int): The number of health the player has
        """
        if player.health + 1 <= 5 :
            player.health += 1
        else:
            pass

    def damageUp(self,player):
        """
        This increases the player's health
        :param player:(Player): Takes the player class so their stats can be increased
        :return: player.damage:(int): number of health the player does when it attacks the enemy
        """
        player.damage += 1

    def healthUp(self,player):
        """
        this increases the player's maximum health
        :param player: (Player): Takes the player class so their stats can be increased
        :return: player.max_health:(int):the maximum health the player class can carry
        """
        player.max_health += 1

    def rage(self,player):
        """
        This increases the player's damage greatly but decreases the health to minimum
        :param player:(Player): Takes the player class so their stats can be increased
        :return:player.damage:(int): the damage a player does to an enemy
        player.max_health:(int):the maximum health the player class can carry
        player.damage:(int): number of health the player does when it attacks the enemy
        """
        player.damage += 3
        player.health = 1
        player.max_health = 1

    def activateRandom(self,player):
        """
        activates the powerup when the player walks ontop of it by calling a powerup function
        :param player:(Player): Takes the player class so their stats can be increased
        """
        if self.roll == 'rage':
            self.rage(player)
        elif self.roll == 'healthUp':
            self.healthUp(player)
        elif self.roll == 'damageUp':
            self.damageUp(player)
        self.kill()





