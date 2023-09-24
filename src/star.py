import pygame

class Star:
	def __init__(self, x, y, scale):
		self.x = x * scale
		self.y = y * scale
		self.scale = scale

	def getX(self):	return self.x
	def getY(self):	return self.y

	def createStarPoints(self):
		x = self.x
		y = self.y
		s = self.scale

		return [((x-35) /s, (y+131)/s), (x/s, y/s), 
				((x+35) /s, (y+131)/s),
				((x+171)/s, (y+124)/s), 
				((x+57) /s, (y+199)/s),
				((x+106)/s, (y+326)/s), (x/s, (y+240)/s), 
				((x-116)/s, (y+326)/s), 
				((x-57) /s, (y+199)/s), 
				((x-171)/s, (y+124)/s)]


	def createRect(self):
		w = (171 / self.scale)*2
		x = (self.x / self.scale) - w/2
		y = self.y / self.scale
		h = 326 / self.scale 
		return (x, y, w, h)

	def draw(self, screen, color, points):
		pygame.draw.polygon(screen, color, points)