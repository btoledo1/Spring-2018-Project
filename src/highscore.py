import pygame

class Highscore:

    def __init__(self, file, playerscore):
        '''
        controller

        file: filename to use fore score as a parameter
        playerscore: way to track the player score
        '''
        pygame.font.init()
        self.f = open(file, 'r+')
        self.highscore = int(self.f.readline())
        self.playerscore = playerscore
        self.myfont = pygame.font.SysFont(pygame.font.get_default_font(), 32)

    def highscore(self):
        if (self.highscore > self.playerscore):
            surface = self.myfont.render(str(self.highscore), True, (0, 0, 0))
        else:
            self.f.write(str(self.playerscore))
            surface = self.myfont.render(str(self.playerscore), True, (0, 0, 0))

        self.f.close()
        return surface