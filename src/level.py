from src import player
from src import enemy
from src import powerups
from src import menu
import pygame
import random


class Levels():
    def __init__(self):

        self.whichLevel = 0
        self.inProgress = False
        self.player = player.Player(590, 515)
        self.attack = player.Attack(self.player.rect.x,self.player.rect.y)
        self.weapon = pygame.sprite.Group(self.attack)
        self.enemies = pygame.sprite.Group()
        self.perks = pygame.sprite.Group()
        self.entities = pygame.sprite.Group()
        self.stairs = menu.Menu()

### Listen to Inheritence in Class

    def Level_1(self):
        """
        Builds the first level and places the enemies and player
        :return:self.player.rect.x:(Int) player's x position
        self.player.rect.y:(Int)player's y position
        self.enemy_one-three(Enemy/Sprite) Enemy class sprites
        self.enemies:(Group): group where the enemies belong
        self.entities:(Group):group of the things needed to be blitted
        """
        self.player.rect.x , self.player.rect.y = 590, 515
        self.enemy_one = enemy.Enemy("skeleton", 130, 100)
        self.enemy_two = enemy.Enemy("skeleton", 1000, 100)
        self.enemy_three = enemy.Enemy("skeleton",130, 515)
        self.enemies = pygame.sprite.Group(self.enemy_one,self.enemy_two,self.enemy_three)
        self.entities = pygame.sprite.Group(self.player, tuple(self.enemies))

    def Level_2_mobs(self):
        """
        Builds the first level and places the enemies and player
        :return:self.player.rect.x:(Int) player's x position
        self.player.rect.y:(Int)player's y position
        self.enemy_one-four(Enemy/Sprite) Enemy class sprites
        self.enemies:(Group): group where the enemies belong
        self.entities:(Group):group of the things needed to be blitted
        """
        self.player.rect.x , self.player.rect.y = 590,515
        self.enemy_one = enemy.Enemy("skeleton",145,500)
        self.enemy_two = enemy.Enemy("skeleton",800,175)
        self.enemy_three = enemy.Enemy("skeleton",200,175)
        self.enemy_four = enemy.Enemy("skeleton",500,175)
        self.enemies = pygame.sprite.Group(self.enemy_one,self.enemy_two,self.enemy_three,self.enemy_four)
        self.entities = pygame.sprite.Group(self.player, tuple(self.enemies))

    def Level_3_mobs(self):
        """
        Builds the first level and places the enemies and player
        :return:self.player.rect.x:(Int) player's x position
        self.player.rect.y:(Int)player's y position
        self.enemy_one-three(Enemy/Sprite) Enemy class sprites
        self.enemies:(Group): group where the enemies belong
        self.entities:(Group):group of the things needed to be blitted
        """
        self.player.rect.x, self.player.rect.y = 590,515
        self.enemy_one = enemy.Enemy("skeleton",150,150)
        self.enemy_two = enemy.Enemy("skeleton",150,300)
        self.enemy_three = enemy.Enemy("skeleton",500,150)
        self.enemy_four = enemy.Enemy("skeleton",700,150)
        self.enemy_five = enemy.Enemy("skeleton",900,150)
        self.enemies = pygame.sprite.Group(self.enemy_one,self.enemy_two)
        self.entities = pygame.sprite.Group(self.player,self.enemy_one,self.enemy_two)

    def Level_4_mobs(self):
        """
        Builds the first level and places the enemies and player
        :return:self.player.rect.x:(Int) player's x position
        self.player.rect.y:(Int)player's y position
        self.enemy_one-five(Enemy/Sprite) Enemy class sprites
        self.enemies:(Group): group where the enemies belong
        self.entities:(Group):group of the things needed to be blitted
        """
        self.player.rect.x, self.player.rect.y = 590,515
        self.enemy_one = enemy.Enemy("bat",1000,50,1,2)
        self.enemy_two = enemy.Enemy("bat",800,50,1,2)
        self.enemy_three = enemy.Enemy("bat",600,50,1,2)
        self.enemy_four = enemy.Enemy("bat",400,50,1,2)
        self.enemy_five = enemy.Enemy("bat",200,50,1,2)
        self.enemies = pygame.sprite.Group(self.enemy_one,self.enemy_two,self.enemy_three,self.enemy_four,self.enemy_five)
        self.entities = pygame.sprite.Group(self.player,tuple(self.enemies))

    def Level_powerup(self):
        """
        Creates the floor where the powerup spawns
        :return:self.player.rect.x:(Int) player's x position
        self.player.rect.y:(Int)player's y position
        self.up(Powerup/Sprite) Powerup class sprites
        self.perks:(Group): group where the powerup belongs
        self.entities:(Group):group of the things needed to be blitted
        """
        self.player.rect.x, self.player.rect.y = 590, 515
        self.up = powerups.Powerups("rage", 600, 325)
        self.hard = self.up.spawnRandomPowerup()
        self.perks = pygame.sprite.Group(self.up)
        self.entities = pygame.sprite.Group(self.player,tuple(self.perks))

    def Level_2(self):
        """
        randomly loads one of the levels based on chance
        :return: Level_powerup()(Function)Loads the powerup level
        Level_2_mobs()(Function)Loads the level with the enemies
        """
        if random.randrange(0,5) == 0:
            self.Level_powerup()
        else:
            self.Level_2_mobs()

    def Level_3(self):
        """
        randomly loads one of the levels based on chance
        :return: Level_powerup()(Function)Loads the powerup level
        Level_3_mobs()(Function)Loads the level with the enemies
        """
        if random.randrange(0,10) == 1:
            self.Level_powerup()
        else:
            self.Level_3_mobs()

    def Level_4(self):
        """
        randomly loads one of the levels based on chance
        :return: Level_powerup()(Function)Loads the powerup level
        Level_4_mobs()(Function)Loads the level with the enemies
        """
        if random.randrange(0,10) == 1:
            self.Level_powerup()
        else:
            self.Level_4_mobs()

    def Level_5(self):
        """
        randomly loads one of the levels based on chance
        :return: self.boss (Enemy/Sprite): creates the final boss of the game
        self.entities(Group): Creates a group with the enemies and players to blit
        self.enemies(Group): Creates a group of only enemies
        """
        self.player.rect.x, self.player.rect.y = 590, 515
        self.boss = enemy.Enemy("loss",200,200,50,2)
        self.entities = pygame.sprite.Group(self.player,self.boss)
        self.enemies = pygame.sprite.Group(self.boss)

    def loadLevel(self):
        """
        Loads the levels based on completion
        :return:Level_1-5()(Function) Runs the function of one of the levels
        self.stairs.nextFloor()(Function) Spawns the hitbox that leads to the other door
        """
        #Checks which level the player is on and loads the level once the stair hitbox was reached
        if len(self.enemies) == 0 and self.inProgress == False:
            self.inProgress = True
            self.openDoor = False
            if self.whichLevel == 1:
                self.Level_1()
            elif self.whichLevel == 2:
                self.Level_2()
            elif self.whichLevel == 3:
                self.Level_3()
            elif self.whichLevel == 4:
                self.Level_4()
            elif self.whichLevel == 5:
                self.Level_5()
        elif len(self.enemies) == 0 and self.whichLevel != 0 and self.inProgress == True:
            self.stairs.nextFloor()
            self.openDoor = True
            #Detects when the player collides with the hitbox and leads to the next level
            if pygame.sprite.collide_rect(self.player,self.stairs.stairs):
                if self.whichLevel != 5:
                    self.whichLevel += 1
                    self.inProgress = False
                elif self.whichLevel == 5:
                    self.whichLevel = 1
                    self.inProgress = False













