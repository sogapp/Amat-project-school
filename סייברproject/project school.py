print("check")
import pygame
class character():
    def __init__(self, clicks, ability):
        self.ability = ability
        self.clicks = clicks
Sophie = character(1, "teleporting")



# Initialize Pygame
pygame.init()

# Set the width and height of the window
width, height = 640, 480

# Create the window with the specified width and height
screen = pygame.display.set_mode((width, height))

# Create a font object
font = pygame.font.Font(None, 36)

# Run the Pygame loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the window with white
    screen.fill((255, 255, 255))

    # Render the text "player 1"
    text = font.render("player 1", True, (0, 0, 0))

    # Get the rectangle surrounding the text
    text_rect = text.get_rect()

    # Center the text on the screen
    text_rect.center = (width // 2, height // 2)

    # Blit the text onto the screen
    screen.blit(text, text_rect)

    # Update the window
    pygame.display.flip()

# Quit Pygame
pygame.quit()
