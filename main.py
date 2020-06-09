# Main file to this projects here:

import pygame # Import Main library (pygame) here:

from settings import SettingsDisplay
from player import Player
from enemy import Enemy

class Main:
    def __init__(self):
        # Construct here:
        self.settings_dis = SettingsDisplay() # Created Objects Settings.
        self.settings_dis.Created_Display()

    def main(self):
        # Main While and Main code here:

        hero = Player()
        enemy = Enemy()

        pygame.init()

        RunGame = True
        while RunGame: # Check if RunGame == True created Main While here:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # Check if player click close program:
                    RunGame = False # Main While == False : Programs close.
                    quit()

            hero.Go_Player() # Created Go Player (hero) Objects.
            hero.Draw_Player() # Created Player (Draw) here.

            pygame.display.update() # Update Displaye evry While here.

def main_object():
    # Created Main objects (Main) here:

    main = Main()
    main.main()

main_object()