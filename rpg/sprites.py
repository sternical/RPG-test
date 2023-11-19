import pygame
from config import *
import math
import random

class spritesheet:
    def __init__(self,file):
        self.sheet=pygame.image.load(file).convert()
    
    def get_sprite(self,x,y,width,height):
        sprite = pygame.Surface([width,height])
        sprite.blit(self.sheet,(0,0),(x,y,width,height))
        sprite.set_colorkey(BLACK)
        return sprite

class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.game=game
        self.layer=PLAYER_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE
        
        self.x_change=0
        self.y_change=0
        
        self.facing = 'down'

        self.image = self.game.character_spritesheet.get_sprite(3,2,self.width,self.height)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        
    def update(self):
        self.movement()
        
        self.rect.x += self.x_change
        self.collide_blocks('x')
        self.rect.y += self.y_change
        self.collide_blocks('y')
        
        self.x_change=0
        self.y_change=0

    def movement(self):
        keys =  pygame.key.get_pressed()
        global PLAYER_SPEED
        global stamina
        #if keys[pygame.K_LEFT]:
        #    self.x_change-=PLAYER_SPEED
        #    self.facing = 'left'
        #if keys[pygame.K_RIGHT]:
        #    self.x_change+=PLAYER_SPEED
        #    self.facing = 'right'
        #keys =  pygame.key.get_pressed()
        #if keys[pygame.K_UP]:
        #    self.y_change-=PLAYER_SPEED
        #    self.facing = 'up'
        #if keys[pygame.K_DOWN]:
        #    self.y_change+=PLAYER_SPEED
        #    self.facing = 'down'

        #stamina regen
        if stamina<totalstamina:
            if keys[pygame.K_LSHIFT] != True:
                stamina=stamina+staminaregen
            


        if keys[pygame.K_a]:
            #if keys[pygame.K_LSHIFT]:
            #    if stamina>0:
            #        PLAYER_SPEED = PLAYER_SPEED * SHIFT_CALCULATION
            #        self.x_change-=PLAYER_SPEED
            #        self.facing = 'left' 
            #        for sprite in self.game.all_sprites:
            #            sprite.rect.x += PLAYER_SPEED
            #        PLAYER_SPEED = PLAYER_SPEED / SHIFT_CALCULATION
            #        stamina=stamina-staminadrain
            #    if stamina<=0:
            #        for sprite in self.game.all_sprites:
            #            sprite.rect.x += PLAYER_SPEED
            #        self.x_change-=PLAYER_SPEED
            #        self.facing = 'left'
            #else:
            #    for sprite in self.game.all_sprites:
            #        sprite.rect.x += PLAYER_SPEED
            #    self.x_change-=PLAYER_SPEED
            #    self.facing = 'left'
            for sprite in self.game.all_sprites:
                sprite.rect.x += PLAYER_SPEED
            self.x_change-=PLAYER_SPEED
            self.facing = 'left'
            
        if keys[pygame.K_d]:
            #if keys[pygame.K_LSHIFT]:
            #    if stamina>0:
            #        PLAYER_SPEED = PLAYER_SPEED * SHIFT_CALCULATION
            #        self.x_change+=PLAYER_SPEED
            #        self.facing = 'right'
            #        for sprite in self.game.all_sprites:
            #            sprite.rect.x -= PLAYER_SPEED
            #        PLAYER_SPEED = PLAYER_SPEED / SHIFT_CALCULATION   
            #        stamina=stamina-staminadrain
            #    if stamina<=0:
            #        for sprite in self.game.all_sprites:
            #            sprite.rect.x -= PLAYER_SPEED
            #        self.x_change+=PLAYER_SPEED
            #        self.facing = 'right'
            #else:
            #    for sprite in self.game.all_sprites:
            #        sprite.rect.x -= PLAYER_SPEED
            #    self.x_change+=PLAYER_SPEED
            #    self.facing = 'right'
            for sprite in self.game.all_sprites:
                sprite.rect.x -= PLAYER_SPEED
            self.x_change+=PLAYER_SPEED
            self.facing = 'right'
            
        if keys[pygame.K_w]:
            #if keys[pygame.K_LSHIFT]:
            #    if stamina>0:
            #        PLAYER_SPEED = PLAYER_SPEED * SHIFT_CALCULATION
            #        self.y_change-=PLAYER_SPEED
            #        self.facing = 'up'
            #        for sprite in self.game.all_sprites:
            #            sprite.rect.y += PLAYER_SPEED
            #        PLAYER_SPEED = PLAYER_SPEED / SHIFT_CALCULATION
            #        stamina=stamina-staminadrain
            #    if stamina<=0:
            #        for sprite in self.game.all_sprites:
            #            sprite.rect.y += PLAYER_SPEED
            #        self.y_change-=PLAYER_SPEED
            #        self.facing = 'up'
            #else:
            #    for sprite in self.game.all_sprites:
            #        sprite.rect.y += PLAYER_SPEED
            #    self.y_change-=PLAYER_SPEED
            #    self.facing = 'up'
            for sprite in self.game.all_sprites:
                sprite.rect.y += PLAYER_SPEED
            self.y_change-=PLAYER_SPEED
            self.facing = 'up'
            
        if keys[pygame.K_s]:
            #if keys[pygame.K_LSHIFT]:
            #    if stamina>0:
            #        PLAYER_SPEED = PLAYER_SPEED * SHIFT_CALCULATION
            #        self.y_change+=PLAYER_SPEED
            #        self.facing = 'down'
            #        for sprite in self.game.all_sprites:
            #            sprite.rect.y -= PLAYER_SPEED
            #        PLAYER_SPEED = PLAYER_SPEED / SHIFT_CALCULATION
            #        stamina=stamina-staminadrain
            #    if stamina<=0:
            #        for sprite in self.game.all_sprites:
            #            sprite.rect.y -= PLAYER_SPEED
            #        self.y_change+=PLAYER_SPEED
            #        self.facing = 'down'
            #else:
            #    for sprite in self.game.all_sprites:
            #        sprite.rect.y -= PLAYER_SPEED
            #    self.y_change+=PLAYER_SPEED
            #    self.facing = 'down'
            for sprite in self.game.all_sprites:
                sprite.rect.y -= PLAYER_SPEED
            self.y_change+=PLAYER_SPEED
            self.facing = 'down'
        
    def collide_blocks(self,direction):
        keys =  pygame.key.get_pressed()
        if direction == "x":
            hits = pygame.sprite.spritecollide(self,self.game.blocks, False)
            if hits:
                if self.x_change>0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                    for sprite in self.game.all_sprites:
                            sprite.rect.x+=PLAYER_SPEED
                    #if keys[pygame.K_LSHIFT] and stamina>0:
                    #    for sprite in self.game.all_sprites:
                    #        sprite.rect.x+=PLAYER_SPEED*SHIFT_CALCULATION  
                    #else:
                    #    for sprite in self.game.all_sprites:
                    #        sprite.rect.x+=PLAYER_SPEED
                if self.x_change<0:
                    self.rect.x = hits[0].rect.right
                    for sprite in self.game.all_sprites:
                        sprite.rect.x-=PLAYER_SPEED
                    #if keys[pygame.K_LSHIFT] and stamina>0:
                    #    for sprite in self.game.all_sprites:
                    #        sprite.rect.x-=PLAYER_SPEED*SHIFT_CALCULATION  
                    #else:
                    #    for sprite in self.game.all_sprites:
                    #        sprite.rect.x-=PLAYER_SPEED
        if direction == "y":
            hits = pygame.sprite.spritecollide(self,self.game.blocks, False)
            if hits:
                if self.y_change>0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                    for sprite in self.game.all_sprites:
                        sprite.rect.y+=PLAYER_SPEED
                    #if keys[pygame.K_LSHIFT] and stamina>0:
                    #    for sprite in self.game.all_sprites:
                    #        sprite.rect.y+=PLAYER_SPEED*SHIFT_CALCULATION  
                    #else:
                    #    for sprite in self.game.all_sprites:
                    #        sprite.rect.y+=PLAYER_SPEED
                if self.y_change<0:
                    self.rect.y=hits[0].rect.bottom
                    for sprite in self.game.all_sprites:
                            sprite.rect.y-=PLAYER_SPEED
                    #if keys[pygame.K_LSHIFT] and stamina>0:
                    #    for sprite in self.game.all_sprites:
                    #        sprite.rect.y-=PLAYER_SPEED*SHIFT_CALCULATION  
                    #else:
                    #    for sprite in self.game.all_sprites:
                    #        sprite.rect.y-=PLAYER_SPEED


class Block(pygame.sprite.Sprite):
    def __init__(self,game,x,y):
        self.game = game
        self._LAYER = BLOCK_LAYER
        self.groups=self.game.all_sprites, self.game.blocks
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x= x*TILESIZE
        self.y = y*TILESIZE
        self.width=TILESIZE
        self.height=TILESIZE
        
        self.image = self.game.terrain_spritesheet.get_sprite(960,448,self.width,self.height)
        
        self.rect=self.image.get_rect()
        self.rect.x = self.x
        self.rect.y=self.y
        
class Ground(pygame.sprite.Sprite):
    def __init__(self,game,x,y):
        self.game=game
        self._layer=GROUND_LAYER
        self.groups=self.game.all_sprites
        pygame.sprite.Sprite.__init__(self,self.groups)
        
        self.x = x*TILESIZE
        self.y=y*TILESIZE
        self.width=TILESIZE
        self.height=TILESIZE
        
        self.image=self.game.terrain_spritesheet.get_sprite(64,352,self.width,self.height)
        self.rect=self.image.get_rect()
        self.rect.x=self.x
        self.rect.y=self.y
        