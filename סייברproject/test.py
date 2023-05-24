import pygame
import os

import pyautogui
width, height = pyautogui.size()
WIDTH, HEIGHT = 2460, 1350
CH2_IMAGEO = pygame.image.load(os.path.join('Assets', 'c2.jpg'))
image = pygame.transform.scale(CH2_IMAGEO, (3000,  2000))

fakeScreenO = pygame.image.load(os.path.join('Assets', 'background.jpg'))
fakeScreen = pygame.transform.scale(fakeScreenO, (3000,  2000))

screen = pygame.display.set_mode((width/2+width/4, height/2+height/4))

CH2_IMAGEO = pygame.image.load(os.path.join('Assets', 'c2.jpg'))
image = pygame.transform.scale(CH2_IMAGEO, (3000,  2000))

#image.blit(CH2_IMAGEO, (90,90))
screenUpdate = pygame.transform.scale(image, (500, 400))

while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    fakeScreen.blit(screenUpdate, (100, 100))
    fake = pygame.transform.scale(fakeScreen, (width/2+width/4, height/2+height/4))
    #screen.fill((250,250, 250))
    screen.blit(fake, (0,0))
    
    #screen.blit(screenUpdate, (0,0))
    pygame.display.update()