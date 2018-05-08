import pygame
from src import buttons


class Menu(pygame.sprite.Sprite):
    def __init__(self,x=0,y=0,image="assets/menu.png"):
        pygame.font.__init__("Okay")
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def menuButtons(self):
        """
        Creates the Button classes for the menu
        :return: self.play(Button) a button for the menu to play the game
        self.help(Button) a button for the instructions page
        self.quit(Button) a button to quit the game
        self.menu_buttons(Group) a group of buttons
        """
        self.play = buttons.Button(98,399,"assets/button.png")
        self.help = buttons.Button(511,399,"assets/button.png")
        self.quit = buttons.Button(922,399,"assets/button.png")
        self.menu_buttons = pygame.sprite.Group(self.play,self.help,self.quit)

    def instructionButtons(self):
        """
        Creates the Button classes for the instructions page
        :return: self.play(Button) a button for the page to play
        self.menu(Button) a button for the instructions page to lead to the menu
        self.quit(Button) a button to quit the game
        self.instruction_buttons(Group) a group of buttons
        """
        self.play = buttons.Button(117,589,"assets/instructions_button.png")
        self.menu = buttons.Button(500,589,"assets/instructions_button.png")
        self.quit = buttons.Button(915,589,"assets/instructions_button.png")
        self.instruction_buttons = pygame.sprite.Group(self.play,self.menu,self.quit)

    def pauseButtons(self):
        """
        Creates the Button classes for the menu
        :return: self.resume(Button) a button to resume the game
        self.menu(Button) a button for the menu page
        self.quit(Button) a button to quit the game
        self.pause_buttons(Group) a group of buttons
        """
        self.resume = buttons.Button(98, 399, "assets/button.png")
        self.menu = buttons.Button(511, 399, "assets/button.png")
        self.quit = buttons.Button(922, 399, "assets/button.png")
        self.pause_buttons = pygame.sprite.Group(self.resume, self.menu, self.quit)

    def scoreButtons(self):
        """
        Creates the Button classes for the menu
        :return: self.play(Button) a button for the menu
        self.menu(Button) a button for the menu page
        self.quit(Button) a button to quit the game
        self.score_buttons(Group) a group of buttons
        """
        self.play = buttons.Button(98,399,"assets/button.png")
        self.menu = buttons.Button(511,399,"assets/button.png")
        self.quit = buttons.Button(922,399,"assets/button.png")
        self.score_buttons = pygame.sprite.Group(self.play,self.help,self.quit)

    def nextFloor(self):
        """
        creates the trigger that causes the next floor to load
        :return:self.stairs(Button)a button used to trigger the next level
        """
        self.stairs = buttons.Button(600,100,"assets/next_floor.png")







