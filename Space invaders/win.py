import pygame

from pygame.locals import *

import sys

class Win:
	def show_win(self):
		pygame.init()
		self.fuente = pygame.font.Font(None, 20)
		self.text = "¡YOU WIN!"
		self.mensaje = self.fuente.render(self.text, 1, (255, 255, 255))
		self.screen.blit(self.mensaje, (200, 200))
