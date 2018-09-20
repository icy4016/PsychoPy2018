import math, numpy, random #handy system and math functions
from psychopy import core, event, visual, gui #these are the psychopy modules

myWin = visual.Window(color='white', units='pix', size=[1000,1000], fullscr = False, allowGUI = True) #creates a window,  fullscr=False, 
myClock = core.Clock() #this creates and starts a clock which we can later read

frame1 = visual.Rect(myWin, lineWidth=3, lineColor=[1,0,0], fillColor=None)
frame2 = visual.Rect(myWin, lineWidth=3, lineColor=[0,1,0], fillColor=None)
frame3 = visual.Rect(myWin, lineWidth=3, lineColor=[0,0,1], fillColor=None)
box1 =visual.Rect(myWin, pos=[-200,-300], width=20, height=20, lineWidth=3, lineColor=[1,0,0], fillColor=[1,0,0])
box2 =visual.Rect(myWin, pos=[0,-300], width=20, height=20, lineWidth=3, lineColor=[0,1,0], fillColor=None)
box3 =visual.Rect(myWin, pos=[200,-300],width=20, height=20, lineWidth=3, lineColor=[0,0,1], fillColor=None)
dot =visual.Circle(myWin, radius=6, fillColor='black', lineColor=None)

title=visual.TextStim(myWin, pos=[0,305], text='Hierarchical Motion Organisation', height=24, color='green') 
myMouse = event.Mouse() 

# set up coordinates for an ellipse (with axes a and b) and a second ellipse (with axes 2*a and 0)
def prepareCoordinates(a, b):

    angle =0.
    coordsMiddle=[]
    coordsOutside=[]
    
    while angle<360:
        angle = angle +1.5
        angleR = math.radians(angle)
        y =math.cos(angleR) * a
        x =math.sin(angleR) * b
        coordsMiddle.append([x,y])

    aOutside = a*2.
    bOutside = 0.
    angle =0.
    while angle <360:   
        angle = angle +1.5
        angleR = math.radians(angle)
        y =math.cos(angleR) * aOutside
        x =math.sin(angleR) * bOutside
        coordsOutside.append([x,y])
        
    return coordsMiddle, coordsOutside

#draws the animation of the three dots, and also the frames based on the selection made with the mouse
def drawAnimation(coordsMiddle, coordsOutside, a, b):

    finished = False
    frame1on = False
    frame2on = False
    frame3on = False

    
    while not finished:

        buttonWas = 'up'
        for i in range(len(coordsMiddle)):
            
            if frame1on:                                            # this is the static frame of reference - counter-clockwise motion
                frame1.draw() 
            if frame2on:                                            # this is the dots frame of reference - clockwise motion
                frame2.setPos([0,coordsOutside[i][1]]) 
                frame2.draw()
            if frame3on:                                             # this is the horizontal frame of reference
                frame3.setPos([0,coordsMiddle[i][1]]) 
                frame3.draw()
                
            box1.draw()
            box2.draw()
            box3.draw()
            title.draw()
        
            x1 =coordsMiddle[i][0]
            y1 =coordsMiddle[i][1]
            dot.setPos([x1,y1])
            dot.draw()
            
            x1 =coordsOutside[i][0]
            y1 =coordsOutside[i][1]
            dot.setPos([x1+b*2 ,y1])
            dot.draw()
            dot.setPos([x1-b*2,y1])
            dot.draw()

            buttons =myMouse.getPressed()
            if buttons[0]:
                if buttonWas=='up':
                    if box1.contains(myMouse):
                        if frame1on:
                            box1.setFillColor(None)
                            frame1on = False
                        else:
                            box1.setFillColor('black')
                            frame1on = True
                    elif box2.contains(myMouse):
                        if frame2on:
                            box2.setFillColor(None)
                            frame2on = False
                        else:
                            box2.setFillColor('black')
                            frame2on = True
                    elif box3.contains(myMouse):
                        if frame3on:
                            box3.setFillColor(None)
                            frame3on = False
                        else:
                            box3.setFillColor('black')
                            frame3on = True
                buttonWas = 'down'
            else:
                buttonWas = 'up'
                
            myWin.flip()

            if event.getKeys(keyList=['escape']): 
                finished =True
                break
            waitUntil = myClock.getTime() + 1 / 60.   # one second divided by 60 (most monitors are 60Hz), which is 0.016
            while myClock.getTime() <waitUntil:
                pass

# the main loop
def mainLoop():

    a = 60.
    b = 120.
    frame1.setWidth(b*2+ a)
    frame1.setHeight(b*2+ a)
    frame2.setWidth(b*4)
    frame2.setHeight(b*2)
    frame3.setWidth(b*2)
    frame3.setHeight(b*2)
    
    coordsMiddle, coordsOutside = prepareCoordinates(a, b)
    drawAnimation(coordsMiddle, coordsOutside, a, b)

mainLoop() #enters the main loop
myWin.close() #closes the window
core.quit() #quits





