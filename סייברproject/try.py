import pygame
import os


import pygame

pygame.init()





WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) 
pygame.display.set_caption("KOTLC")

WHITE = (255, 255, 255)
BLACK = (0, 0 ,0)

BORDER = pygame.Rect(WIDTH/2 - 5, 0, 10, HEIGHT) 

FPS = 60
VEL = 10
BULLET_VEL = 7
MAX_BULLETS = 3
CHARACTER_WIDTH, CHARACTER_HIEHGT = 130, 180

SOPHIE_IMAGE = pygame.image.load(
    os.path.join('Assets', 'sophie.png'))
SOPHIE = pygame.transform.rotate(pygame.transform.scale(
    SOPHIE_IMAGE, (CHARACTER_WIDTH, CHARACTER_HIEHGT)), 360 )

KEEFE_IMAGE = pygame.image.load(
    os.path.join('Assets', 'keefe.png'))
KEEFE = pygame.transform.rotate(pygame.transform.scale(
    KEEFE_IMAGE, (CHARACTER_WIDTH, CHARACTER_HIEHGT)), 360 )
BALL_IMAGE = pygame.image.load(
    os.path.join('Assets', 'ball.png'))
BALL = pygame.transform.rotate(pygame.transform.scale(
    BALL_IMAGE, (150, 150 )), 360 )


def draw_window(ch1, ch2, ball):
    WIN.fill(WHITE) 
    WIN.blit(SOPHIE, (ch1.x, ch1.y))
    WIN.blit(KEEFE, (ch2.x, ch2.y))
    WIN.blit(BALL, (ball.x, ball.y))

    pygame.display.update()

def handle_ball(ch1, ch2, ball):
    global run
    for i in range(1):
        if ball < ch1:
            print("ch2 win!")
            print(ch1)
        elif ball > ch2:
            print("ch1 win!")







clock = pygame.time.Clock()



"""
def ball_movement(keys_pressed, ball):
    #if keys_pressed[pygame.K_d] and ball.x + VEL < 800: #right
    #   ball.x += VEL
    if keys_pressed[pygame.K_a] and ball.x - VEL > -50: #left
        ball.x -= VEL
    if keys_pressed[pygame.K_w] and ball.y - VEL > -101: #up
        ball.y -= VEL
    elif keys_pressed[pygame.K_w]:
        ball.y = 400
    if keys_pressed[pygame.K_s] and ball.y + VEL < 500: #down
        ball.y += VEL
    elif keys_pressed[pygame.K_s]:
        ball.y = -101


    if keys_pressed[pygame.K_RIGHT]  and ball.x + VEL < 800: #right
        ball.x += VEL
    #if keys_pressed[pygame.K_LEFT] and ball.x - VEL > -50: #left
    #   ball.x -= VEL
    if keys_pressed[pygame.K_UP] and ball.y - VEL > -101: #up
        ball.y -= VEL
    elif keys_pressed[pygame.K_UP]:
        ball.y = 400
    if keys_pressed[pygame.K_DOWN] and ball.y + VEL < 500: #down
        ball.y += VELa
    elif keys_pressed[pygame.K_DOWN]:
        ball.y = -101
        """

def main():
    ch1_bullets = []
    ch2_bullets = []
    ch1 = pygame.Rect(80, 150, CHARACTER_WIDTH, CHARACTER_HIEHGT)
    ch2 = pygame.Rect(700, 150, CHARACTER_WIDTH, CHARACTER_HIEHGT)
    ball = pygame.Rect(375, 150, 150, 150)

    clock = pygame.time.Clock()
    run = True
    while run:


        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    ball.y -= VEL
                if event.key == pygame.K_a:
                    ball.x -= VEL
                if event.key == pygame.K_s:
                    ball.y += VEL
                if event.key == pygame.K_d:
                    ball.x += VEL
                if event.key == pygame.K_UP:
                    ball.y -= VEL
                if event.key == pygame.K_LEFT:
                    ball.x -= VEL
                if event.key == pygame.K_DOWN:
                    ball.y += VEL
                if event.key == pygame.K_RIGHT:
                    ball.x += VEL
                
                draw_window(ch1, ch2, ball)
                handle_ball(ch1.x, ch2.x, ball.x)
                if ch1.x > ball.x or ball.x > ch2.x:  
                    run = False              



                """if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LCTRL and len(ch1_bullets) < MAX_BULLETS:
                        bullet = pygame.Rect(ch1.x + ch1.width, ch1.y + ch1.height/2 -2, 10, 5)
                        ch1_bullets.append(bullet)
                    if event.key == pygame.K_RCTRL and len(ch2_bullets) < MAX_BULLETS:
                        bullet = pygame.Rect(ch2.x, ch2.y + ch2.height/2 -2, 10, 5)
                        ch2_bullets.append(bullet)"""

                
                 
        

        #pygame.key.set_repeat()
        """keys_pressed = pygame.KEYDOWN:
        ball_movement(keys_pressed, ball)
        draw_window(ch1, ch2, ball)"""


    pygame.quit()


if __name__ == "__main__":
    main()

