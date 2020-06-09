# Realization Enemy here:

import pygame

from settings import SettingsDisplay

class Enemy:
    def __init__(self):
        self.X_POS_ENEMY = 100
        self.Y_POS_ENEMY = 1
        self.SPEED_ENEMY = 10

    def Draw_Enemy(self):
        # Realization Draw Here:

        settings = SettingsDisplay() # Created Objects (settings)

        image_enemy = pygame.image.load('alien1.png') # Load Enemy Sprite here.
        settings.DISPLAY.blit(image_enemy, (self.X_POS_ENEMY, self.Y_POS_ENEMY))

    def Realization_Draw_Enemy(self):
        # Realization Draw Enemy here:

        pass

    def Realization_Go_Enemy(self):
        # Realization Go Enemy here:

        pass