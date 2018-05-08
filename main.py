import pygame
from src import level
from src import menu
from src import highscore


class Controller:

    def __init__(self, game_name="Star's Labyrinth", width=1280, height=720):

        pygame.init()
        pygame.font.init()
        pygame.mixer.init()
        pygame.mixer.music.load("assets/song.mp3")

        self.w = width
        self.h = height
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.w, self.h))
        self.screenName = pygame.display.set_caption(game_name)
        self.gameExit = False
        self.menu = menu.Menu()
        self.in_menu = True
        self.in_instructions = False
        self.pause = False
        self.image = "assets/background.png"
        self.background = pygame.image.load(self.image)
        self.player_hit_sound = pygame.mixer.Sound("assets/playerhit.wav")
        self.player_hitting = pygame.mixer.Sound("assets/whip.wav")
        self.in_highscore = False
        self.myfont = pygame.font.SysFont(pygame.font.get_default_font(), 32)

    def mainLoop(self):

        pygame.key.set_repeat(1, 60)
        self.cooldown = 0
        self.iframes = 0

        while not self.gameExit:
            self.background = pygame.image.load("assets/background.png")

            #Runs the pause screen when the game is paused
            while self.pause:
                #Quits the game if the quit event is triggered
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.gameExit = True
                        quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            self.pause = False
                self.menu.pauseButtons()
                #Checks to see if the mouse is over the button and highlights the button if clicked
                #This unpauses the game
                if self.menu.resume.rect.collidepoint(pygame.mouse.get_pos()):
                    self.background = pygame.image.load("assets/paused_resume.png")
                    if pygame.mouse.get_pressed() == (True, False, False):
                        self.menu.pause_buttons.empty()
                        self.pause = False
                #Sends the game to the main menu once clicked in game
                elif self.menu.menu.rect.collidepoint(pygame.mouse.get_pos()):
                    self.background = pygame.image.load("assets/paused_menu.png")
                    if pygame.mouse.get_pressed() == (True, False, False):
                        self.pause = False
                        self.in_menu = True
                        self.in_instructions = False
                        self.menu.pause_buttons.empty()
                #quits the game is the quit button is pressed
                elif self.menu.quit.rect.collidepoint(pygame.mouse.get_pos()):
                    self.background = pygame.image.load("assets/paused_quit.png")
                    if pygame.mouse.get_pressed() == (True, False, False):
                        self.gameExit = True
                        quit()

                self.screen.blit(pygame.image.load("assets/paused.png"), (0, 0))
                pygame.display.flip()
                self.clock.tick(60)

            #Runs the menu if the game is in in_menu is True
            if self.in_menu:
                self.levels = level.Levels()
                self.levels.entities.empty()
                self.levels.whichLevel = 0
                pygame.mouse.set_visible(True)
                self.menu.menuButtons()
                self.background = pygame.image.load("assets/menu.png")
                pygame.display.flip()
                #Checks if the mouse is ontop of the play button is working
                if self.menu.play.rect.collidepoint(pygame.mouse.get_pos()):
                    self.background = pygame.image.load("assets/play_highlighted.png")
                    if pygame.mouse.get_pressed() == (True, False, False):
                        self.menu.menu_buttons.empty()
                        self.in_menu = False
                        self.levels.whichLevel = 1
                        pygame.mixer.music.play(-1)
                #Checks if the mouse is over the help button and it changes it to the instruction page
                if self.menu.help.rect.collidepoint(pygame.mouse.get_pos()):
                    self.background = pygame.image.load("assets/help_highlighted.png")
                    if pygame.mouse.get_pressed() == (True, False, False):
                        self.menu.menu_buttons.empty()
                        self.in_instructions = True
                        self.in_menu = False
                #checks if the mouse is over the quit button and ends the game
                elif self.menu.quit.rect.collidepoint(pygame.mouse.get_pos()):
                    self.background = pygame.image.load("assets/quit_highlighted.png")
                    if pygame.mouse.get_pressed() == (True, False, False):
                        self.gameExit = True
                        quit()
            #Checks if the game is on the instructions page and loads its buttons
            if self.in_instructions:
                self.background = pygame.image.load("assets/instructions.png")
                self.menu.instructionButtons()
                pygame.display.flip()
                #Checks to see if the mouse is on the play button and starts the game if clicked
                if self.menu.play.rect.collidepoint(pygame.mouse.get_pos()):
                    self.background = pygame.image.load("assets/instructions_play_highlighted.png")
                    if pygame.mouse.get_pressed() == (True, False, False):
                        self.menu.menu_buttons.empty()
                        self.in_instructions = False
                        self.levels.whichLevel = 1
                #checks to see if the mouse is over the menu button and goes to the menu if clicked
                if self.menu.menu.rect.collidepoint(pygame.mouse.get_pos()):
                    self.background = pygame.image.load("assets/instructions_menu_highlighted.png")
                    if pygame.mouse.get_pressed() == (True, False, False):
                        self.menu.instruction_buttons.empty()
                        self.in_instructions = False
                        self.in_menu = True
                #checks to see if the mouse if over the quit button and quits the game once clicked
                elif self.menu.quit.rect.collidepoint(pygame.mouse.get_pos()):
                    self.background = pygame.image.load("assets/instructions_quit_highlighted.png")
                    if pygame.mouse.get_pressed() == (True, False, False):
                        self.gameExit = True
                        quit()
            #Once the player dies it runs the score screen and blits the score onto the screen
            if self.in_highscore:
                self.background = pygame.image.load("assets/score.png")
                self.menu.scoreButtons()
                self.highscore_sur = self.myfont.render(str(highscore.Highscore('src/score.txt', self.levels.player.score)),1, (255, 255, 255))
                self.screen.blit(self.highscore_sur, (500, 375))
                pygame.display.flip()
                if self.menu.play.rect.collidepoint(pygame.mouse.get_pos()):
                    if pygame.mouse.get_pressed() == (True, False, False):
                        self.in_highscore = False
                        self.in_menu = False
                        self.levels.whichLevel = 1

            #Checks whatever button is being pressed
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.gameExit = True
                    quit()

                if event.type == pygame.KEYDOWN:
                    # This works to stop the player from moving beyond the wall works with exact numbers
                    if event.key == pygame.K_a and (self.levels.player.rect.x > 115):  # self.border_left.rect.x+90):
                        self.levels.player.move_left()

                    elif event.key == pygame.K_d and (self.levels.player.rect.x < 1090):
                        self.levels.player.move_right()

                    elif event.key == pygame.K_w and (self.levels.player.rect.y > 55):
                        self.levels.player.move_down()

                    elif event.key == pygame.K_s and (self.levels.player.rect.y < 525):
                        self.levels.player.move_up()
#                   #This works to enable the player to attack enemies with a cooldown to not be too over powered
                    elif event.key == pygame.K_SPACE and self.cooldown > 30:
                        self.cooldown = 0
                        self.player_hitting.play()
                        self.levels.weapon.draw(self.screen)
                        pygame.display.flip()
                        if pygame.sprite.spritecollideany(self.levels.attack, self.levels.enemies) in list(self.levels.enemies):
                            pygame.sprite.spritecollideany(self.levels.attack, self.levels.enemies).health -= self.levels.player.damage
                            self.levels.player.score += 10

                    elif event.key == pygame.K_ESCAPE:
                        self.pause = True
            #checks if the enemy collides the player
            if pygame.sprite.spritecollideany(self.levels.player, self.levels.enemies) in list(self.levels.enemies) and self.iframes > 50:
                self.iframes = 0
                self.player_hit_sound.play()
                self.levels.player.health -= 1
            else:
                self.iframes += 1
            #Checks when the player collides with the powerup
            if pygame.sprite.spritecollideany(self.levels.player, self.levels.perks) in list(self.levels.perks):
                pygame.sprite.spritecollideany(self.levels.player, self.levels.perks).activateRandom(self.levels.player)

            #Checks if the player's health is zero and runs the score page once it does
            if self.levels.player.health <= 0:
                self.in_highscore = True
                self.levels.entities.empty()

            #loads the open door image when the level is done
            if self.levels.inProgress and self.levels.whichLevel != 0 and self.levels.openDoor:
                self.background = pygame.image.load("assets/background_open.png")

            print(self.levels.player.rect.x,self.levels.player.rect.y)
            #print(self.levels.player.health, self.levels.player.max_health, self.levels.player.damage)

            #Renders the player's health
            self.health_meter = self.myfont.render("Health:" + str(self.levels.player.health), 1, (255, 255, 255))
            self.levels.loadLevel()
            for c in self.levels.enemies:
                c.chasePlayer(self.levels.player)
                c.updateEnemy(self.levels.player)
            self.levels.attack.update(self.levels.player)
            self.levels.entities.draw(self.background)
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.health_meter, (0, 0))
            pygame.display.flip()
            self.cooldown += 1
            self.clock.tick(60)


def main():
    main_window = Controller()
    main_window.mainLoop()


main()