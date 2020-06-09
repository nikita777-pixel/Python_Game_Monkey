# Realization Player here:

import pygame # Import main library

from settings import SettingsDisplay

class Player:
    def __init__(self):
        # Construct here:

        self.WIDTH_PLAYER = 50
        self.HEIGHT_PLAYER = 50
        self.X_POS_PLAYER = 50
        self.Y_POS_PLAYER = 50
        self.SPEED_PAYER = 15

    def Draw_Player(self):
        # Realization Draw Player here:

        land = pygame.image.load('chimp.bmp')

        settings = SettingsDisplay() # Created settings objects (Get Display) here.

        settings.DISPLAY.blit(land, (self.X_POS_PLAYER, self.Y_POS_PLAYER))

    def Go_Player(self):
        # Realization Go Player here:

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]: # Check If You clikc left realization Go Player here:
            self.Go_Player_Left() # Player Go : Left.

        if keys[pygame.K_RIGHT]:
            self.Go_Plyaer_Right() # Player Go : Right.

        if keys[pygame.K_UP]:
            self.Go_Player_UP() # Player Go : UP

        if keys[pygame.K_DOWN]:
            self.Go_Player_DOWN()

    def Go_Player_Left(self):
        # Realization Go Player Left here:

        self.X_POS_PLAYER -= self.SPEED_PAYER

    def Go_Plyaer_Right(self):
        # Realization Go Player Right here:

        self.X_POS_PLAYER += self.SPEED_PAYER

    def Go_Player_UP(self):
        # Realization Go Player UP here:

        self.Y_POS_PLAYER -= self.SPEED_PAYER

    def Go_Player_DOWN(self):
        # Realization Go Player DOWN here:

        self.Y_POS_PLAYER += self.SPEED_PAYER

    def Realization_Player_Shots(self):
        # Realization Plyaer Shots here:

        pass

