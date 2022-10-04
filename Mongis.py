import pygame
import random
pygame.init()
pygame.display.set_caption("Wire Task")
screen = pygame.display.set_mode((800,800))
screen.fill((0,0,0))

BoxList=[]
LeftPositions=[(100,100), (100, 300), (100,500), (100,700)]
RightPositions=[(550,100), (550, 300), (550,500), (550,700)]

#colores####################
YELLOW = (250,250,0)
RED = (250,0,0)
PINK = (200,0,200)
BLUE = (0,0,200)

LeftColors=[YELLOW, RED, PINK, BLUE]
RightColors=[YELLOW, RED, PINK, BLUE]

random.shuffle(LeftPositions)
random.shuffle(RightPositions)
random.shuffle(LeftColors)
random.shuffle(RightColors)

mouseDown = False
mousePos = (0,0)

#box collision-----------------------------
def BBcollision(xpos, ypos, x, y):
    if x <xpos+100 and x>xpos and y>ypos and y<ypos+50:
        return True
    else:
        return False
    
    
    
class Box():
    def __init__(self, position, color):
        self.position = position
        self.color = color
        self.connected = False
        self.hovering = False
        #self.drawing = False
        
    def isHovering(self, MouseX, MouseY):
        if BBcollision(self.position[0], self.position[1], MouseX, MouseY) == True:
            self.hovering = True
            
        else:
            self.hovering = False
            
    def draw(self):
        pygame.draw.rect(screen, self.color, (self.position[0], self.position[1], 100, 50), 2)
        if self.hovering == True:
            pygame.draw.rect(screen, (255,255,255), (self.position[0], self.position[1], 100, 50), 2)
        

for i in range(4):
    BoxList.append(Box(LeftPositions[i],LeftColors[i]))
    BoxList.append(Box(RightPositions[i],RightColors[i]))
        
while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        break
    
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouseDown = True
        
    if event.type == pygame.MOUSEBUTTONUP:
        mouseDown = False
        
    if event.type == pygame.MOUSEMOTION:
        mousePos = event.pos
        
    for i in range (len(BoxList)):
        BoxList[i].isHovering(mousePos[0], mousePos[1])
    #rendering--------------------------------------------------
        screen.fill((0,0,0))
        
        for i in range (len(BoxList)):
            BoxList[i].draw()
            
        pygame.display.flip()
        
#The End----------------------------------------------------------
        
pygame.quit()
