import random
import pygame
from pygame.locals import *
import os
import pyautogui

pygame.font.init()

#import pygame

class character():
    energy = 0
    shield = 0

    
    #random.randint(self.attack_speed1, self. attackSpeed2)
    def __init__(self, name,  maximumHp, lightAttack, heavyAttack, image, chname):
        
        self.name = name
        self.maximumHp = maximumHp
        self.hp = maximumHp
        self.lightAttack = lightAttack
        self.heavyAttack = heavyAttack
        self.image = image
        self.chname = chname
        
    def hurt(self, hpattack):
        if self.hp > 0 and self.shield <= 0:
            self.hp -= hpattack
        elif self.shield > 0 and self.shield >= hpattack:
            self.shield -= hpattack 
        elif self.shield > 0 and self.shield < hpattack:
            a = self.shield
            self.shield -= hpattack 
            self.hp -= hpattack-a

        
    def heal(self, aid):
        if aid + self.hp <= self.maximumHp:
            self.hp = self.hp + aid
        elif aid + self.hp > self.maximumHp:
            self.hp = self.maximumHp
        
    def heal_full(self):
        self.hp = self.maximumHp
    def general_situation(self, c1 = 0, c2 = 0, c3 = 0, c4 = 0, c5 = 0, c6 = 0):
        def iffy(c):
            if c != 0:
                c.situation()
        iffy(c1)
        iffy(c2)
        iffy(c3)
        iffy(c4)
        iffy(c5)
        iffy(c6)
    def getImage(self):
        return(self.image)
    
    

    
class button1():
    
    def __init__(self, xPos, yPos,image, Pimage):
        self.xPos = xPos
        self.yPos = yPos  
        self.image = image 
        self.Pimage = Pimage 
    
class energybar():
    charge = 0
    
    def __init__(self, xPos, yPos,image0, image1, image2, image3, charge):
        self.xPos = xPos
        self.yPos = yPos  
        self.image0 = image0 
        self.image1 = image1 
        self.image2 = image2 
        self.image3 = image3     
        self.charge = charge
         
#test = character("test", 100, 100, 100, 100)       
#sog = character("sog", 100, 5, 3, 9)
#yuv = character("yuv", 100, 10, 1, 10)

def imageGeneration(name, width, height):
    IMAGEO = pygame.image.load(os.path.join('Assets', name))
    IMAGE = pygame.transform.scale(IMAGEO, (width,  height))
    return(IMAGE)


#test.general_situation(sog, yuv)
#print("yuv situation: ")
#yuv.situation()
#print("sog situation: ")            
#sog.situation()
#print("")
#sog.attack1(yuv)            
#test.general_situation(sog, yuv)
#print("")
#print("yuv situation: ")
#yuv.situation()
#print("sog situation: ")
#sog.situation()
#sog.heal(2)
#yuv.heal_full()

#flags = pygame.FULLSCREEN | pygame.HWSURFACE | pygame.DOUBLEBUF
#CHW, CHH = 240.0 ,  410.5
WIDTH, HEIGHT = 2460, 1350
Swidth, Sheight = pyautogui.size()

CHW, CHH = 360 ,  615.75
BW = 200
BH = 100

#WIN = pygame.display.set_mode((WIDTH, HEIGHT))
screen = pygame.display.set_mode((WIDTH, HEIGHT),HWSURFACE|DOUBLEBUF|RESIZABLE)
WIN = screen.copy()

#fake_screen = WIN.copy()


#fake_screen.fill('black')
#WIN.blit(pygame.transform.scale(fake_screen, WIN.get_rect().size), (0, 0))
pygame.display.flip()
#False_WIN = pygame.display.set_mode((WIDTH, HEIGHT))

#WINO = pygame.image.load(os.path.join('Assets', 'background.jpg'))
#WIN = pygame.transform.rotate(pygame.transform.scale(WINO, (Swidth, Sheight)), 360)


#False_WIN  = pygame.display.set_mode((2460//2, 1350//2), pygame.RESIZABLE)
#for event in pygame.event.get():
#        if event.type == pygame.VIDEORESIZE:
#            # There's some code to add back window content here.
#           WIN = pygame.display.set_mode((event.w, event.h),
#                                             pygame.RESIZABLE)


WHITE = (250,250, 250)
pygame.display.set_caption("oc battle")

FPS = 60

CH1_IMAGEO = pygame.image.load(os.path.join('Assets', 'c1.jpg'))
CH1_IMAGE = pygame.transform.rotate(pygame.transform.scale(CH1_IMAGEO, (CHW,  CHH)), 360)

CH2_IMAGEO = pygame.image.load(os.path.join('Assets', 'c2.jpg'))
CH2_IMAGE = pygame.transform.scale(CH2_IMAGEO, (CHW,  CHH))

CH3_IMAGEO = pygame.image.load(os.path.join('Assets', 'c3.jpg'))
CH3_IMAGE = pygame.transform.scale(CH3_IMAGEO, (CHW,  CHH))

CH4_IMAGEO = pygame.image.load(os.path.join('Assets', 'c4.jpg'))
CH4_IMAGE = pygame.transform.scale(CH4_IMAGEO, (CHW,  CHH))
#self, name,  maximumHp, lightAttack, heavyAttack, image):
ARROWIMAGEO = pygame.image.load(os.path.join('Assets', 'arrow.jpg'))
ARROWIMAGE = pygame.transform.rotate(pygame.transform.scale(ARROWIMAGEO, (50,  150)), 45)

cha1 = character("ch1", 1200, 55, 125, CH1_IMAGE, "Spider Lady")  
cha2 = character("ch2", 1200, 50, 100, CH2_IMAGE, "Archer")  
cha3 = character("ch3", 850, 100, 150, CH3_IMAGE, "Chaos")  
cha4 = character("ch4", 1000, 85, 125, CH4_IMAGE, "Goth Witch") 

cha1e = character("ch1", 1200, 55, 125, CH1_IMAGE, "Spider Lady")  
cha2e = character("ch2", 1200, 50, 100, CH2_IMAGE, "Archer")  
cha3e = character("ch3", 850, 100, 150, CH3_IMAGE, "Chaos")  
cha4e = character("ch4", 1000, 85, 125, CH4_IMAGE, "Goth Witch")  

#imageGeneration(name, width, height):
LightAttackButtonImage = imageGeneration('lightattack.png',BW ,BH )
LightAttackButtonImagePressed = imageGeneration('lightattackpressed.png',BW ,BH )
HeavyAttackButtonImage = imageGeneration('heavyattack.png',BW ,BH )
HeavyAttackButtonImagePressed = imageGeneration('heavyattackpressed.png',BW ,BH )
HpImage = imageGeneration('hp.png',400 ,80)
EnergyBar0 = imageGeneration('energyBar0.jpg',80 ,600)
EnergyBar1 = imageGeneration('energyBar1.png',80 ,600)
EnergyBar2 = imageGeneration('energyBar2.jpg',80 ,600)
EnergyBar3 = imageGeneration('energyBar3.png',80 ,600)
RedSquare = imageGeneration('redSquare.png',CHW + CHW//20 ,CHH + CHH//20)
YellowSquare = imageGeneration('yellowSquare.png',CHW + CHW//20 ,CHH + CHH//20)

HEALER = imageGeneration('healer.png',CHW,CHH)
CH3_IMAGESpecial = imageGeneration('c3b.jpg',CHW,  CHH)
CH3_IMAGESpecial2 = imageGeneration('c3b2.jpg',CHW,  CHH)
CH3_IMAGESpecial3 = imageGeneration('c3b3.jpg',CHW,  CHH)
CH3_IMAGESpecial4 = imageGeneration('c3b4.jpg',CHW,  CHH)
CH3_IMAGESpecial5 = imageGeneration('c3b5.jpg',CHW,  CHH)

CH4_IMAGESpecial = imageGeneration('c4b.jpg',CHW,  CHH)


aimbw = 800
aimpw = 30
aimhight = 100
AIMB = imageGeneration('aimbase.png',aimbw,  aimhight)
AIMP = imageGeneration('aimpoint.png',aimpw,  aimhight)

ARROWIMAGEO = pygame.image.load(os.path.join('Assets', 'arrow.jpg'))
ARROWIMAGE = pygame.transform.rotate(pygame.transform.scale(ARROWIMAGEO, (50,  350)), 65)
SHIELDO = pygame.image.load(os.path.join('Assets', 'shield.jpg'))
SHIELD = pygame.transform.rotate(pygame.transform.scale(SHIELDO, (780,  930)), 180)
BULLETO = pygame.image.load(os.path.join('Assets', 'shield.jpg'))
BULLET = pygame.transform.rotate(pygame.transform.scale(BULLETO, (780//5,  930//5)), 360)

#def __init__(self, xPos, yPos,image0, image1, image2, image3, charge):
energybar1 = energybar(2365, 508 ,EnergyBar0, EnergyBar1, EnergyBar2, EnergyBar3 , 0)


#(self, xPos, yPos,image, Pimage):
lightAttackB = button1(1950, 1130, LightAttackButtonImage, LightAttackButtonImagePressed)
heavyAttackB = button1(2210, 1130, HeavyAttackButtonImage, HeavyAttackButtonImagePressed)


BACKGROUNDO = pygame.image.load(os.path.join('Assets', 'background.jpg'))
BACKGROUND = pygame.transform.scale(BACKGROUNDO, (WIDTH,  HEIGHT))



#choosing1 = int(input(("charater 1 selection: 1/2/3/4")))
choosing1 = 2
if choosing1 == 1:
    user = cha1
elif choosing1 == 2:
    user = cha2
elif choosing1 == 3:
    user = cha3
elif choosing1 == 4:
     user = cha4
#choosing2 = int(input(("charater 2 selection: 1/2/3/4")))
choosing2 = 4
if choosing2 == 1:
    enemy = cha1e
elif choosing2 == 2:
    enemy = cha2e
elif choosing2 == 3:
    enemy = cha3e
elif choosing2 == 4:
    enemy = cha4e
user = cha3    
enemy = cha4
def energyUpdate():
     
    if user.energy == 0:
        energyBar1pic = energybar1.image0
    elif user.energy == 1:
        energyBar1pic = energybar1.image1
    elif user.energy == 2:
        energyBar1pic = energybar1.image2
    elif user.energy == 3:
        energyBar1pic = energybar1.image3
    return(energyBar1pic)

def draw_window(ch1, ch2, lightattackbutton, heavyattackbutton, hpdis1, hpback1, lightAttackBimage, heavyAttackBimage, hpdis2, hpback2, energybar1dis, energyBar1pic, arrow = 0, winning = 0, shield = 0):
    hpnum1 = pygame.font.Font(None, 70).render(str(user.hp), True, (0, 0, 0))
    hpnum2 = pygame.font.Font(None, 70).render(str(enemy.hp), True, (0, 0, 0))
    shieldnum1 = pygame.font.Font(None, 70).render(str(enemy.shield), True, (0, 0, 0))
    WIN.fill(WHITE)
    WIN.blit(BACKGROUND, (0, 0))
    #draw a surface(image) to the screen - WIN.blit()
    WIN.blit(user.image, (ch1.x, ch1.y ))
    WIN.blit(enemy.image, (ch2.x, ch2.y ))
    WIN.blit(lightAttackBimage, (lightattackbutton.x, lightattackbutton.y ))
    WIN.blit(heavyAttackBimage, (heavyattackbutton.x, heavyattackbutton.y ))
    WIN.blit(HpImage, (hpback1.x, hpback1.y))
    WIN.blit(hpnum1, (hpdis1.x, hpdis1.y))
    WIN.blit(HpImage, (hpback2.x, hpback2.y))
    WIN.blit(hpnum2, (hpdis2.x, hpdis2.y))
    WIN.blit(energyBar1pic, (energybar1dis.x, energybar1dis.y))


    if arrow != 0 and user.name == "ch2":
        WIN.blit(ARROWIMAGE, (arrow.x, arrow.y))
    elif arrow != 0 and user.name == "ch4":
        WIN.blit(BULLET, (arrow.x, arrow.y))
    
    if winning != 0:
        WIN.blit(winning, (730, Sheight))
    if shield != 0 and enemy.name == "ch4" and enemy.shield > 0:
        WIN.blit(SHIELD, (500, 250))
        WIN.blit(shieldnum1, (800,320 ))
        WIN.blit(CH4_IMAGESpecial, (ch2.x, ch2.y ))
    screen.blit(pygame.transform.scale(WIN, screen.get_rect().size), (0, 0))
    pygame.display.flip()
    pygame.display.update()

def chswitch():
    global user
    global enemy
    if user.energy < 3:
        user.energy += 1
    if enemy.hp > 0 and user.hp > 0:
        disposable1 = user
        user = enemy
        enemy = disposable1

def lifeCheck(): 
    global user
    global enemy   
    if enemy.hp <= 0:
        winning = pygame.font.Font(None, 200).render(str("{} won!".format(user.chname)), True, (0, 0, 0))
    elif user.hp <= 0:
        winning = pygame.font.Font(None, 200).render(str("{} won!".format(enemy.chname)), True, (0, 0, 0))
    else:
        winning = 0
    return(winning)   
        
        

    
    
    
    
    


#bugs/need to add list:
#1: you can spam the attack button and it still works while animation
#2: play again function at the end
#3: add attack bullet animation when crit attack
def main():
    
    global user
    global enemy
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT),HWSURFACE|DOUBLEBUF|RESIZABLE)
    WIN = screen.copy()
    #pic = pygame.surface.Surface((50, 50))
    #pic.fill((255, 100, 200))
    
    ch1 = pygame.Rect(2000, 500, CHW, CHH)
    ch2 = pygame.Rect(100, 80, CHW, CHH)
    lightattackbutton = pygame.Rect(lightAttackB.xPos,lightAttackB.yPos, BW, BH)
    heavyattackbutton = pygame.Rect(heavyAttackB.xPos,heavyAttackB.yPos, BW, BH)
    energybar1dis = pygame.Rect(energybar1.xPos, energybar1.yPos, 1000 ,1000)
    hpdis1 = pygame.Rect(2200,443, 500, 500)
    hpback1 = pygame.Rect(1980,430, 500, 500)
    hpdis2 = pygame.Rect(299,23, 500, 500)
    hpback2 = pygame.Rect(79,10, 500, 500)
    clock = pygame.time.Clock()
    arrow = 0
    winning = 0
    shield = 0
    #main loop
    
    turn = 1
    run = True
    energyBar1pic = energybar1.image0
    bb = 1
    ac = 1
    aa = 1
    run2 = True
    choosing1 = 0
    choosing2 = 0
    while run2:
        
        clock.tick(FPS)
        
        #WIDTH, HEIGHT = 2460, 1350
        player1 = pygame.font.Font(None, 90).render(str("player 1 choosing"), True, (0, 0, 0))
        player2 = pygame.font.Font(None, 90).render(str("player 2 choosing"), True, (0, 0, 0))
        my_string = '''The only way to
                    learn to program is
                    by writing code.'''

        
        chh1 = pygame.font.Font(None, 70).render(str(cha1.name +" "+ cha1.chname), True, (255, 128, 32))
        chh2 = pygame.font.Font(None, 70).render(str(cha2.name +" "+ cha2.chname), True, (51, 255, 255))
        chh3 = pygame.font.Font(None, 70).render(str(cha3.name +" "+ cha3.chname), True, (0, 0, 0))
        chh4 = pygame.font.Font(None, 70).render(str(cha4.name +" "+ cha4.chname), True, (255, 0, 255))

        def statsHp(name11, x, y):
            hpdi = pygame.font.Font(None, 70).render("Hp: " + str(name11.hp), True, (255, 0, 0))
            WIN.blit(hpdi, (x, y))
        def statsLA(name11, x, y):
            hpdi = pygame.font.Font(None, 70).render("Light attack: " + str(name11.lightAttack), True, (192, 192, 192))
            WIN.blit(hpdi, (x, y))
        def statsHA(name11, x, y):
            hpdi = pygame.font.Font(None, 70).render("Heavy attack: " + str(name11.heavyAttack), True, (102, 102, 0))
            WIN.blit(hpdi, (x, y))



        def size1(a):
            return(615*a-move1)
        move1 = 490
        WIN.fill(WHITE)
        WIN.blit(chh1, (size1(1) + 20, 300))
        WIN.blit(CH1_IMAGE, (size1(1), 400 ))
        WIN.blit(chh2, (size1(2)+ 20, 300))
        WIN.blit(CH2_IMAGE, (size1(2), 400 ))
        WIN.blit(chh3, (size1(3)+ 20, 300))
        WIN.blit(CH3_IMAGE, (size1(3), 400 ))
        WIN.blit(chh4, (size1(4)+ 20, 300))
        WIN.blit(CH4_IMAGE, (size1(4), 400 ))

        statsHp(cha1, 120, 1030)
        statsHp(cha2, 740, 1030)
        statsHp(cha3, 740+620, 1030)
        statsHp(cha4, 740+620+620, 1030)

        statsLA(cha1, 120, 1080)
        statsLA(cha2, 740, 1080)
        statsLA(cha3, 740+620, 1080)
        statsLA(cha4, 740+620+620, 1080)

        statsHA(cha1, 120, 1130)
        statsHA(cha2, 740, 1130)
        statsHA(cha3, 740+620, 1130)        
        statsHA(cha4, 740+620+620, 1130)



        if ac == 1:
            WIN.blit(RedSquare, (size1(1)-((CHW//20)//2), 400-((CHH//20)//2) ))
            WIN.blit(CH1_IMAGE, (size1(1), 400 )) 
        elif ac == 2:
            WIN.blit(RedSquare, (size1(2)-((CHW//20)//2), 400-((CHH//20)//2) ))
            WIN.blit(CH2_IMAGE, (size1(2), 400 )) 
        elif ac == 3:
            WIN.blit(RedSquare, (size1(3)-((CHW//20)//2), 400-((CHH//20)//2) ))
            WIN.blit(CH3_IMAGE, (size1(3), 400 )) 
        elif ac == 4:
            WIN.blit(RedSquare, (size1(4)-((CHW//20)//2), 400-((CHH//20)//2) ))
            WIN.blit(CH4_IMAGE, (size1(4), 400 )) 

        if turn == 1:
            WIN.blit(player1, (900,100 ))
        elif turn == 2:
            WIN.blit(player2, (900,100 ))
            
        

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run2 = False
            elif event.type == VIDEORESIZE:
                screen = pygame.display.set_mode(event.size, HWSURFACE|DOUBLEBUF|RESIZABLE)
            if event.type == pygame.MOUSEMOTION:
                mouse_x, mouse_y = event.pos
                if size1(1) < mouse_x < size1(1) + CHW and 400 < mouse_y <400 + CHH:
                    ac = 1
                else:
                    ac = 0
                if size1(2) < mouse_x < size1(2) + CHW and 400 < mouse_y <400 + CHH:
                    ac = 2
                elif ac != 1:
                    ac = 0
                if size1(3) < mouse_x < size1(3) + CHW and 400 < mouse_y <400 + CHH:
                    ac = 3
                elif ac != 2 and ac !=1:
                    ac = 0
                if size1(4) < mouse_x < size1(4) + CHW and 400 < mouse_y <400 + CHH:
                    ac = 4
                elif ac != 2 and ac !=1 and ac!= 3:
                    ac = 0

            if event.type == pygame.MOUSEBUTTONDOWN and turn ==2:
                if event.button == 1 and ac == 1 :
                    choosing2 = 1
                    WIN.blit(YellowSquare, (size1(1)-((CHW//20)//2), 400-((CHH//20)//2) ))
                    WIN.blit(CH1_IMAGE, (size1(1), 400 )) 
                    pygame.display.update()
                    clock.tick(1)
                elif event.button == 1 and ac == 2 :
                    choosing2 = 2
                    WIN.blit(YellowSquare, (size1(2)-((CHW//20)//2), 400-((CHH//20)//2)))
                    WIN.blit(CH2_IMAGE, (size1(2), 400 )) 
                    pygame.display.update()
                    clock.tick(1)
                elif event.button == 1 and ac == 3 :
                    choosing2 = 3
                    WIN.blit(YellowSquare, (size1(3)-((CHW//20)//2), 400-((CHH//20)//2) ))
                    WIN.blit(CH3_IMAGE, (size1(3), 400 )) 
                    pygame.display.update()
                    clock.tick(1)
                elif event.button == 1 and ac == 4 : 
                    choosing2 = 4
                    WIN.blit(YellowSquare, (size1(4)-((CHW//20)//2), 400-((CHH//20)//2) ))
                    WIN.blit(CH4_IMAGE, (size1(4), 400 )) 
                    pygame.display.update()
                    clock.tick(1)

            if event.type == pygame.MOUSEBUTTONDOWN and turn ==1:
                if event.button == 1 and ac == 1 :
                    choosing1 = 1
                    WIN.blit(YellowSquare, (size1(1)-((CHW//20)//2), 400-((CHH//20)//2) ))
                    WIN.blit(CH1_IMAGE, (size1(1), 400 )) 
                    pygame.display.update()
                    clock.tick(1)
                    turn = 2
                elif event.button == 1 and ac == 2 :
                    choosing1 = 2
                    WIN.blit(YellowSquare, (size1(2)-((CHW//20)//2), 400-((CHH//20)//2)))
                    WIN.blit(CH2_IMAGE, (size1(2), 400 )) 
                    pygame.display.update()
                    clock.tick(1)
                    turn = 2
                elif event.button == 1 and ac == 3 :
                    choosing1 = 3
                    WIN.blit(YellowSquare, (size1(3)-((CHW//20)//2), 400-((CHH//20)//2) ))
                    WIN.blit(CH3_IMAGE, (size1(3), 400 )) 
                    pygame.display.update()
                    clock.tick(1)
                    turn = 2
                elif event.button == 1 and ac == 4 : 
                    choosing1 = 4
                    WIN.blit(YellowSquare, (size1(4)-((CHW//20)//2), 400-((CHH//20)//2) ))
                    WIN.blit(CH4_IMAGE, (size1(4), 400 )) 
                    pygame.display.update()
                    clock.tick(1)
                    turn = 2
                    
                            
            
                
            
                            
            if choosing1 == 1:
                user = cha1
            elif choosing1 == 2:
                user = cha2
            elif choosing1 == 3:
                user = cha3
            elif choosing1 == 4:
                user = cha4

            if choosing2 == 1:
                enemy = cha1e
                run2 = False
            elif choosing2 == 2:
                enemy = cha2e
                run2 = False
            elif choosing2 == 3:
                enemy = cha3e
                run2 = False
            elif choosing2 == 4:
                enemy = cha4e
                run2 = False

        screen.blit(pygame.transform.scale(WIN, screen.get_rect().size), (0, 0))
        pygame.display.flip()
            

    lightAttackBimage = lightAttackB.image 
    heavyAttackBimage = heavyAttackB.image 
    
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    user.energy = 3
                    #chswitch()
                    #מחליפים מקומות
                    #turn += 1
                    #if turn%2 == 0:
                    #    ch1.x, ch1.y, ch2.x, ch2.y = ch2.x, ch2.y, ch1.x, ch1.y
                    #else:
                    #    ch2.x, ch2.y, ch1.x, ch1.y = ch1.x, ch1.y, ch2.x, ch2.y        
                if event.key == pygame.K_s:
                    #user.energy = 3
                    chswitch()
                    #מחליפים מקומות
                    #turn += 1
                    #if turn%2 == 0:
                    #    ch1.x, ch1.y, ch2.x, ch2.y = ch2.x, ch2.y, ch1.x, ch1.y
                    #else:
                    #    ch2.x, ch2.y, ch1.x, ch1.y = ch1.x, ch1.y, ch2.x, ch2.y         

            if event.type == pygame.MOUSEMOTION:
                mouse_x, mouse_y = event.pos
                if  lightAttackB.xPos < mouse_x <lightAttackB.xPos + BW and lightattackbutton.y < mouse_y <lightattackbutton.y + BH:
                    lightAttackBimage = lightAttackB.Pimage 
                else:
                    lightAttackBimage = lightAttackB.image 
                if heavyAttackB.xPos < mouse_x <heavyAttackB.xPos + BW and heavyattackbutton.y < mouse_y <heavyattackbutton.y + BH:
                    heavyAttackBimage = heavyAttackB.Pimage 
                else:
                    heavyAttackBimage = heavyAttackB.image
                
            diss = 1
            if event.type == pygame.MOUSEBUTTONDOWN and lightAttackBimage == lightAttackB.Pimage:
                    if event.button == 1 and diss == 1:  # 1 represents left mouse button
                        diss = 0
                        for i in range(50):
                            ch1.x = ch1.x-2
                            ch1.y = ch1.y-2
                            draw_window(ch1, ch2, lightattackbutton, heavyattackbutton, hpdis1, hpback1, lightAttackBimage, heavyAttackBimage, hpdis2, hpback2, energybar1dis, energyBar1pic, arrow, winning, shield)
                        #WIDTH, HEIGHT = 2460, 1350
                        #for i in range(user.lightAttack):

                        
                        aimpointer = pygame.Rect(Swidth//2-aimbw//2, Sheight, 15, aimhight)
                        AIMPR = imageGeneration('aimpointer.png',aimpointer.width,  aimpointer.height)
                        AIMPR2 = imageGeneration('aimpointer2.png',aimpointer.width,  aimpointer.height)
                        
                        WIN.blit(AIMB, (Swidth//2-aimbw//2, Sheight))
                        WIN.blit(AIMP, (Swidth//2-aimbw//2+aimbw//2-aimpw//2, Sheight))
                        WIN.blit(AIMPR, (aimpointer.x, aimpointer.y))
                        pygame.display.update()
                        runn = 1
                        runnn = 1
                        disrun1 = 1 
                        disrun2 = 1 
                        while runn == 1:
                            for event in pygame.event.get():
                                if event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_SPACE:
                                        runn = 0
                            if runnn == 1:
                                disrun1 = 1
                            else:
                                disrun1 = 0
                            while disrun1 == 1:
                                aimpointer.x += 1
                                if aimpointer.x + aimpointer.width > Swidth//2-aimbw//2 + aimbw:
                                    disrun1 = 0
                                WIN.blit(AIMB, (Swidth//2-aimbw//2, Sheight))
                                WIN.blit(AIMP, (Swidth//2-aimbw//2+aimbw//2-aimpw//2, Sheight))
                                WIN.blit(AIMPR, (aimpointer.x, aimpointer.y))
                                pygame.display.update()
                                for event in pygame.event.get():
                                    if event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_SPACE:
                                            disrun1 = 0
                                            runn = 0
                                            runnn = 0

                            if runnn == 1:
                                disrun2 = 1 
                            else:
                                disrun2 = 0
                            while disrun2 == 1:
                                aimpointer.x -= 1
                                if aimpointer.x < Swidth//2-aimbw//2:
                                    disrun2 = 0
                                WIN.blit(AIMB, (Swidth//2-aimbw//2, Sheight))
                                WIN.blit(AIMP, (Swidth//2-aimbw//2+aimbw//2-aimpw//2, Sheight))
                                WIN.blit(AIMPR, (aimpointer.x, aimpointer.y))
                                pygame.display.update()
                                for event in pygame.event.get():
                                    if event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_SPACE:
                                            disrun2 = 0
                                            runn = 0
                                            runnn = 0

                        #aimpointer = pygame.Rect(WIDTH//2-aimbw//2, Sheight, 15, aimhight)
                        #WIN.blit(AIMP, (WIDTH//2-aimbw//2+aimbw//2-aimpw//2, Sheight))
                        
                        if   Swidth//2-aimbw//2+aimbw//2-aimpw//2 < aimpointer.x < Swidth//2-aimbw//2+aimbw//2-aimpw//2 + aimpw:
                            lightA = user.lightAttack + 20/100*user.heavyAttack

                            WIN.blit(AIMB, (Swidth//2-aimbw//2, Sheight))
                            WIN.blit(AIMP, (Swidth//2-aimbw//2+aimbw//2-aimpw//2, Sheight))
                            WIN.blit(AIMPR2, (aimpointer.x, aimpointer.y))
                            pygame.display.update()
                            clock.tick(10)
                        else:
                            lightA = user.lightAttack - 20/100*user.heavyAttack


                            
                        clock.tick(1)
                        i = 0
                        while i < lightA and enemy.hp > 0:
                            i+=1
                            enemy.hurt(1)
                            draw_window(ch1, ch2, lightattackbutton, heavyattackbutton, hpdis1, hpback1, lightAttackBimage, heavyAttackBimage, hpdis2, hpback2, energybar1dis, energyBar1pic, arrow, winning, shield)
                            
                        for i in range(25):
                            ch1.x = ch1.x+4
                            ch1.y = ch1.y+4
                            draw_window(ch1, ch2, lightattackbutton, heavyattackbutton, hpdis1, hpback1, lightAttackBimage, heavyAttackBimage, hpdis2, hpback2, energybar1dis, energyBar1pic, arrow, winning, shield)
                            
                        diss = 1
                        clock.tick(10)
                        chswitch()
                        
            diss = 1
            if event.type == pygame.MOUSEBUTTONDOWN and heavyAttackBimage == heavyAttackB.Pimage and user.energy > 0 :
                    if event.button == 1:  # 1 represents left mouse button
                        diss = 0
                        if user.energy > 0:
                            user.energy -= 1
                        if user.energy == 0:
                            energyBar1pic = energybar1.image0
                        elif user.energy == 1:
                            energyBar1pic = energybar1.image1
                        elif user.energy == 2:
                            energyBar1pic = energybar1.image2
                        elif user.energy == 3:
                            energyBar1pic = energybar1.image3
                        draw_window(ch1, ch2, lightattackbutton, heavyattackbutton, hpdis1, hpback1, lightAttackBimage, heavyAttackBimage, hpdis2, hpback2, energybar1dis, energyBar1pic)

                        for i in range(100):
                            ch1.x = ch1.x-2
                            ch1.y = ch1.y-2
                            draw_window(ch1, ch2, lightattackbutton, heavyattackbutton, hpdis1, hpback1, lightAttackBimage, heavyAttackBimage, hpdis2, hpback2, energybar1dis, energyBar1pic, arrow, winning, shield)
                            
                        aimpointer = pygame.Rect(Swidth//2-aimbw//2, Sheight, 15, aimhight)
                        AIMPR = imageGeneration('aimpointer.png',aimpointer.width,  aimpointer.height)
                        AIMPR2 = imageGeneration('aimpointer2.png',aimpointer.width,  aimpointer.height)
                        WIN.blit(AIMB, (Swidth//2-aimbw//2, Sheight))
                        WIN.blit(AIMP, (Swidth//2-aimbw//2+aimbw//2-aimpw//2, Sheight))
                        WIN.blit(AIMPR, (aimpointer.x, aimpointer.y))
                        screen.blit(pygame.transform.scale(WIN, screen.get_rect().size), (0, 0))
                        pygame.display.flip()
                        pygame.display.update()
                        runn = 1
                        runnn = 1
                        disrun1 = 1 
                        disrun2 = 1 
                        while runn == 1:
                            for event in pygame.event.get():
                                if event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_SPACE:
                                        runn = 0
                            if runnn == 1:
                                disrun1 = 1
                            else:
                                disrun1 = 0
                            while disrun1 == 1:
                                aimpointer.x += 1
                                if aimpointer.x + aimpointer.width > Swidth//2-aimbw//2 + aimbw:
                                    disrun1 = 0
                                WIN.blit(AIMB, (Swidth//2-aimbw//2, Sheight))
                                WIN.blit(AIMP, (Swidth//2-aimbw//2+aimbw//2-aimpw//2, Sheight))
                                WIN.blit(AIMPR, (aimpointer.x, aimpointer.y))
                                screen.blit(pygame.transform.scale(WIN, screen.get_rect().size), (0, 0))
                                pygame.display.flip()
                                pygame.display.update()
                                
                                for event in pygame.event.get():
                                    if event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_SPACE:
                                            disrun1 = 0
                                            runn = 0
                                            runnn = 0

                            if runnn == 1:
                                disrun2 = 1 
                            else:
                                disrun2 = 0
                            while disrun2 == 1:
                                aimpointer.x -= 1
                                if aimpointer.x < Swidth//2-aimbw//2:
                                    disrun2 = 0
                                WIN.blit(AIMB, (Swidth//2-aimbw//2, Sheight))
                                WIN.blit(AIMP, (Swidth//2-aimbw//2+aimbw//2-aimpw//2, Sheight))
                                WIN.blit(AIMPR, (aimpointer.x, aimpointer.y))
                                screen.blit(pygame.transform.scale(WIN, screen.get_rect().size), (0, 0))
                                pygame.display.flip()
                                
                                pygame.display.update()
                                for event in pygame.event.get():
                                    if event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_SPACE:
                                            disrun2 = 0
                                            runn = 0
                                            runnn = 0

                        #aimpointer = pygame.Rect(WIDTH//2-aimbw//2, Sheight, 15, aimhight)
                        #WIN.blit(AIMP, (WIDTH//2-aimbw//2+aimbw//2-aimpw//2, Sheight))
                        clock.tick(100)
                        if  Swidth//2-aimbw//2+aimbw//2-aimpw//2 < aimpointer.x < Swidth//2-aimbw//2+aimbw//2-aimpw//2 + aimpw:
                            heavyA = user.heavyAttack + 20/100*user.heavyAttack
                            WIN.blit(AIMB, (Swidth//2-aimbw//2, Sheight))
                            WIN.blit(AIMP, (Swidth//2-aimbw//2+aimbw//2-aimpw//2, Sheight))
                            WIN.blit(AIMPR2, (aimpointer.x, aimpointer.y))
                            screen.blit(pygame.transform.scale(WIN, screen.get_rect().size), (0, 0))
                            pygame.display.flip()
                            
                            pygame.display.update()
                            clock.tick(10)
                        else:
                            heavyA = user.heavyAttack - 20/100*user.heavyAttack


                        i = 0
                        while i < heavyA and enemy.hp > 0:
                            i+=1
                            enemy.hurt(1)
                            draw_window(ch1, ch2, lightattackbutton, heavyattackbutton, hpdis1, hpback1, lightAttackBimage, heavyAttackBimage, hpdis2, hpback2, energybar1dis, energyBar1pic, arrow, winning, shield)
                        for i in range(50):
                            ch1.x = ch1.x+4
                            ch1.y = ch1.y+4
                            draw_window(ch1, ch2, lightattackbutton, heavyattackbutton, hpdis1, hpback1, lightAttackBimage, heavyAttackBimage, hpdis2, hpback2, energybar1dis, energyBar1pic, arrow, winning, shield)
                        diss = 1
                        clock.tick(100)
                        chswitch()
                       
            if event.type == pygame.MOUSEMOTION:
                mouse_x, mouse_y = event.pos
                if energybar1.xPos < mouse_x < energybar1.xPos + 80 and energybar1.yPos < mouse_y <energybar1.yPos + 600:
                    aa = 1
                else:
                    aa = 0

            if event.type == pygame.MOUSEBUTTONDOWN:
                
                if event.button == 1 and aa == 1:
                    
                    
                    if user.energy == 3:
                        
                        #user.specialActivate
                        if user.name == "ch1":
                            user.energy -= 3
                            draw_window(ch1, ch2, lightattackbutton, heavyattackbutton, hpdis1, hpback1, lightAttackBimage, heavyAttackBimage, hpdis2, hpback2, energybar1dis, energyBar1pic, 0, winning, shield)
                            pygame.display.update()
                            for i in range(150):
                                if user.hp < user.maximumHp:
                                    user.heal(2)
                                    draw_window(ch1, ch2, lightattackbutton, heavyattackbutton, hpdis1, hpback1, lightAttackBimage, heavyAttackBimage, hpdis2, hpback2, energybar1dis, energyBar1pic, 0, winning, shield)
                                    pygame.display.update()

                            
                        if user.name == "ch2":
                            bb= 1
                            arrow = pygame.Rect(2000,500, 50, 150)
                            WIN.blit(ARROWIMAGE, (arrow.x, arrow.y))
                            #clock.tick(1)
                            for i in range(3):
                                user.energy -= 1
                                energyBar1pic = energyUpdate()
                                draw_window(ch1, ch2, lightattackbutton, heavyattackbutton, hpdis1, hpback1, lightAttackBimage, heavyAttackBimage, hpdis2, hpback2, energybar1dis, energyBar1pic, 0, winning, shield)
                                clock.tick(10)
                            arrow = pygame.Rect(1700,700, 50, 150)
                            for i in range(102):
                                arrow.x -= 12
                                arrow.y -= 5
                                draw_window(ch1, ch2, lightattackbutton, heavyattackbutton, hpdis1, hpback1, lightAttackBimage, heavyAttackBimage, hpdis2, hpback2, energybar1dis, energyBar1pic, arrow, winning, shield)
                            arrow = 0
                            enemy.hurt(200)
                            clock.tick(100)
                            enemy.hurt(150)
                            draw_window(ch1, ch2, lightattackbutton, heavyattackbutton, hpdis1, hpback1, lightAttackBimage, heavyAttackBimage, hpdis2, hpback2, energybar1dis, energyBar1pic, arrow, winning, shield)
                            clock.tick(1)
                            
                        else:
                            arrow = 0
                        if user.name == "ch3":
                            for i in range(3):
                                user.energy -= 1
                                energyBar1pic = energyUpdate()
                                draw_window(ch1, ch2, lightattackbutton, heavyattackbutton, hpdis1, hpback1, lightAttackBimage, heavyAttackBimage, hpdis2, hpback2, energybar1dis, energyBar1pic, arrow, winning, shield)
                                clock.tick(1)

                            

                            user.image = CH3_IMAGESpecial

                            draw_window(ch1, ch2, lightattackbutton, heavyattackbutton, hpdis1, hpback1, lightAttackBimage, heavyAttackBimage, hpdis2, hpback2, energybar1dis, energyBar1pic, arrow, winning, shield)
                            clock.tick(10)
                            for i in range(150):
                                user.hurt(1)
                                draw_window(ch1, ch2, lightattackbutton, heavyattackbutton, hpdis1, hpback1, lightAttackBimage, heavyAttackBimage, hpdis2, hpback2, energybar1dis, energyBar1pic, arrow, winning, shield)
                                user.lightAttack = 200
                                user.heavyAttack = 300
                            
                            

                        if user.name == "ch4":
                            user.energy -= 3
                            spec = random.randint(0, 1)
                            WIN.blit(CH4_IMAGESpecial, (ch1.x, ch1.y ))
                            pygame.display.update()
                            clock.tick(1)
                            #WIN.blit(CH4_IMAGE, (ch2.x, ch2.y ))
                            if spec == 0:
                                user.heal(100)
                                user.shield = 275
                                shield = pygame.Rect(1800,400, 380, 330)
                                draw_window(ch1, ch2, lightattackbutton, heavyattackbutton, hpdis1, hpback1, lightAttackBimage, heavyAttackBimage, hpdis2, hpback2, energybar1dis, energyBar1pic, arrow, winning, shield)
                            elif spec == 1:
                                
                                
                                arrow = pygame.Rect(1700,700, 50, 150)
                                for i in range(102):
                                    arrow.x -= 12
                                    arrow.y -= 5
                                    ddss = pygame.Rect(9000,4000, 380, 330)
                                    draw_window(ch1, ch2, lightattackbutton, heavyattackbutton, hpdis1, hpback1, lightAttackBimage, heavyAttackBimage, hpdis2, hpback2, energybar1dis, energyBar1pic, arrow)
                                    
                                arrow = 0
                                enemy.hurt(70)
                                clock.tick(10)
                                enemy.hurt(180)
                                draw_window(ch1, ch2, lightattackbutton, heavyattackbutton, hpdis1, hpback1, lightAttackBimage, heavyAttackBimage, hpdis2, hpback2, energybar1dis, energyBar1pic, arrow)
                                clock.tick(1)
                            cha4.image = CH4_IMAGE
                        chswitch()
                        #if
            energyBar1pic = energyUpdate()
            ##if user.energy == 0:
            #    energyBar1pic = energybar1.image0
            #elif user.energy == 1:
            #    energyBar1pic = energybar1.image1
            #elif user.energy == 2:
             #   energyBar1pic = energybar1.image2
            #elif user.energy == 3:
             #   energyBar1pic = energybar1.image3
            
        
        
        #WIN.blit(ARROWIMAGE, (arrow.x, arrow.y))
        winning = lifeCheck()    
        draw_window(ch1, ch2, lightattackbutton, heavyattackbutton, hpdis1, hpback1, lightAttackBimage, heavyAttackBimage, hpdis2, hpback2, energybar1dis, energyBar1pic, arrow, winning, shield)
        

    pygame.quit()


if __name__ == "__main__":
    
    main()



