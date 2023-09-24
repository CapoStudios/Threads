import pygame

class Hammer:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.w = 50
		self.h = 50
		self.rotate = 0
		self.hasCollideWithPlayer = False

	def draw(self, screen, img):
		if self.hasCollideWithPlayer == False:
			rotate_hammer = pygame.transform.rotate(img, self.rotate)
			screen.blit(rotate_hammer, (self.x, self.y), (0, 0, self.w, self.w))
			self.rotate += 1

	def createRect(self):	return (self.x, self.y, self.w, self.h)

	def reset(self): self.hasCollideWithPlayer = False
