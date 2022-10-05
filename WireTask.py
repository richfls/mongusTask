import pygame as py
import random
py.init()
py.display.set_caption("wire task")
w = py.display.set_mode((800,800))
w.fill((0,0,0))

gameloop = True

#Color variables
Y = (250,250,0)
R = (200,0,0)
P = (200,0,200)
B = (0,0,200)
W = (255,255,255)

#makes the lists
boxlist = []
LEFTPOSITIONS = [(100,150),(100,300),(100,450),(100,600)]
RIGHTPOSITIONS = [(600,150),(600,300),(600,450),(600,600)]
LEFTCOLORS = [Y,R,P,B]
RIGHTCOLORS = [Y,R,P,B]

#Shuffles the lists
random.shuffle(LEFTPOSITIONS)
random.shuffle(RIGHTPOSITIONS)
random.shuffle(LEFTCOLORS)
random.shuffle(RIGHTCOLORS)

mouseDOWN = False
mousePOS = (0,0) #stores two numbers to mousePOS
class box():
    def __init__(self,position,color):
        self.position = position
        self.color = color
        self.connected = False
        self.clicked = False
        self.hovering = False
    
        
    def isHovering(self,mousex,mousey):
        if boxcollision(self.position[0], self.position[1], mousex, mousey)==True:
            self.hovering = True
        else:
            self.hovering = False
    def draw(self):
        py.draw.rect(w,self.color,(self.position[0],self.position[1],100,50))
        if self.hovering == True:
            py.draw.rect(w,W,(self.position[0],self.position[1],100,50),2)
            
    
def boxcollision(xpos,ypos,x,y):
    if xpos <= x and ypos <= y and xpos+100>= x and ypos+50 >= y:
        return True
    else:
        return False
    
for i in range(4):
    boxlist.append(box(LEFTPOSITIONS[i],LEFTCOLORS[i]))
    boxlist.append(box(RIGHTPOSITIONS[i],RIGHTCOLORS[i]))
while gameloop != False:
    event = py.event.wait()
    
    if event.type == py.QUIT:
        break
    
    if event.type == py.MOUSEBUTTONDOWN:
        mouseDOWN = True
        
    if event.type == py.MOUSEBUTTONUP:
        mouseDOWN = False
        
    if event.type == py.MOUSEMOTION:
        mousePOS = event.pos
    
    
    for i in range(len(boxlist)):
        boxlist[i].isHovering(mousePOS[0],mousePOS[1])

    w.fill((0,0,0))
    
    for i in range(len(boxlist)):
        boxlist[i].draw()
        
    py.display.flip()
    
py.quit()
