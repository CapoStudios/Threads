from level1 import Level1
from level2 import Level2
from level3 import Level3
from level4 import Level4
from level5 import Level5
from level6 import Level6
from level7 import Level7

class Levels():
	def start():
		levels = [	Level1, Level2, Level3, Level4, 
					Level5, Level6, Level7	]
		for level in levels:
			currentLevel = level()
			currentLevel.start()
