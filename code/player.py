import pygame
from settings import *

class Player(pygame.sprite.Sprite):
	def __init__(self,pos,groups):
		super().__init__(groups)
		self.image = pygame.Surface((40,80))
		self.rect = self.image.get_rect(topleft = pos)