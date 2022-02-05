import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites):
        super().__init__(groups)
        self.sprite_sheet = pygame.image.load('./NinjaAdventure/Actor/Characters/GreenNinja/SpriteSheet.png').convert_alpha()
        self.image = self.get_image(0, 0)
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect(topleft=pos)

        self.direction = pygame.math.Vector2()
        self.speed = 5

        self.obstacle_sprites = obstacle_sprites
    

    def get_image(self, x, y):
        image = pygame.Surface([16, 16])
        image.blit(self.sprite_sheet, (0, 0), (x,y, 16, 16))
        return image

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.rect.x += self.direction.x * speed
        self.collision('horizontal')
        self.rect.y += self.direction.y * speed
        self.collision('vertical')
        # self.rect.center += self.direction * speed

    def collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.x > 0: #moving right
                        self.rect.right = sprite.rect.left
                    if self.direction.x < 0: #moving left
                        self.rect.left = sprite.rect.right

        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.y < 0: #moving up
                        self.rect.top = sprite.rect.bottom
                    if self.direction.y > 0: #moving down
                        self.rect.bottom = sprite.rect.top
    
    def update(self):
        self.input()
        self.move(self.speed)
        # events = pygame.event.get()
        # for event in events:
        #     if event.type == pygame.KEYDOWN:
        #         if event.key == pygame.K_LEFT:
        #             pass
        #         if event.key == pygame.K_RIGHT:
        #             pass
        #         if event.key == pygame.K_UP:
        #             pass
        #         if event.key == pygame.K_DOWN:
        #             pass