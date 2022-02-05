import pygame
from settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.sprite_sheet = pygame.image.load('./NinjaAdventure/Backgrounds/Tilesets/TilesetNature.png').convert_alpha()
        self.image = self.get_image(144, 208)
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect(topleft=pos)
    
    def get_image(self, x, y):
        image = pygame.Surface([16, 16])
        image.blit(self.sprite_sheet, (0, 0), (x,y, 16, 16))
        return image