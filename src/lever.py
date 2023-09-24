import pygame

class Lever:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.w = 25
		self.h = 25
		self.hasCollideWithPlayer = False

	def draw(self, screen, img):
		screen.blit(pygame.transform.flip(img, self.hasCollideWithPlayer, True), (self.x, self.y), (0, 0, 21*2, 16*2))

	# get a Rect from the Lever
	def createRect(self):
		return (self.x, self.y, self.w, self.h)

	# reset the lever variable
	def reset(self): 
		self.hasCollideWithPlayer = False