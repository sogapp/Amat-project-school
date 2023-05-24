import pygame
from pygame.locals import *
import os

# Define some constants
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
IMAGE_SCALE = 10
FPS = 60

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pixel Art Maker")

# Load the image
image_path = pygame.image.load(os.path.join('Assets', 'c4.jpg'))
image = pygame.transform.scale(image_path, (100,  100))
# Scale the image
image_scaled = pygame.transform.scale(image, (SCREEN_WIDTH // IMAGE_SCALE, SCREEN_HEIGHT // IMAGE_SCALE))

# Create a new surface to draw the pixel art on
pixel_art = pygame.Surface(image_scaled.get_size())

# Lock the pixel art surface for faster pixel access
pixel_art.lock()

# Loop over each pixel in the scaled image and draw a rectangle on the pixel art surface
for x in range(image_scaled.get_width()):
    for y in range(image_scaled.get_height()):
        color = image_scaled.get_at((x, y))
        rect = pygame.Rect(x * IMAGE_SCALE, y * IMAGE_SCALE, IMAGE_SCALE, IMAGE_SCALE)
        pygame.draw.rect(pixel_art, color, rect)

# Unlock the pixel art surface
pixel_art.unlock()

# Set up the clock
clock = pygame.time.Clock()

# Start the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Draw the pixel art to the screen
    screen.blit(pixel_art, (0, 0))

    # Update the display
    pygame.display.flip()

    # Wait for the next frame
    clock.tick(FPS)

# Clean up
pygame.quit()
