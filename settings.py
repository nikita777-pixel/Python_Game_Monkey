# Oll Settings to this projects here:

import pygame # Import pygame.

class SettingsDisplay:
    # Craeted Display and Crated  Variiable for Display here:

    def __init__(self):
        self.WIDTH_DISPLAY = 1200
        self.HEIGHT_DISPLAY = 850
        self.DISPLAY = pygame.display.set_mode((self.WIDTH_DISPLAY, self.HEIGHT_DISPLAY))
        self.TITLE = pygame.display.set_caption("My Game On Python!!!")

    def Created_Display(self):
        return self.DISPLAY # Return Display here.
        return self.Craeted_Title_Display()

    def Craeted_Title_Display(self):
        return self.TITLE

    def Craeted_Color_Display(self):
        self.DISPLAY.fill((255, 255, 255))
