import pygame, sys

MOUSEBUTTONLEFT = 1

# Handle Input events
def handleInputEvents(player, elements, height, CELL):
	# Input Events
    for event in pygame.event.get():
        # Exit
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Keyboard Events
        if event.type == pygame.KEYDOWN:
            # Exit
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

            # Restart
            if event.key == pygame.K_r: 
                player.restart = True

        # Mouse Events
        if event.type == pygame.MOUSEBUTTONDOWN:
            player.click()
            if event.button == MOUSEBUTTONLEFT:
                mouseX, mouseY = pygame.mouse.get_pos()
                if mouseY > height/2 and player.blocks > 0:
                    for element in elements:
                        if pygame.Rect(element) != pygame.Rect(CELL*(int(mouseX/CELL)), CELL*(int(mouseY/CELL)), 25, 25):
                            elements.append((CELL*(int(mouseX/CELL)), CELL*(int(mouseY/CELL)), 25, 25))
                            player.blocks -= 1
                            break