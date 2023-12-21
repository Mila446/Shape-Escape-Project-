
from cmu_graphics import *
import random
from PIL import Image, ImageDraw

class Point:
    def __init__(self,cx,cy):
        self.x = cx
        self.y = cy
    
    def getPoint(self):
        return (self.x,self.y)
    
    def getX(self):
        return self.x
    
    def addX(self,other):
        if isinstance(other,int):
            self.x+=other
    
    def getY(self):
        return self.y
    
    def addY(self,other):
        if isinstance(other,int):
            self.y+=other
    def setX(self,otherx):
        if isinstance(otherx,int):
            Point(otherx,self.y)

class Player:
    def __init__(self,name):
        self.name = name
    
    def __repr__(self):
        return f"{self.name}"
    
class Obstacle:
    def __init__(self,coord,width,height):
        self.coord = coord
        self.width= width
        self.height = height

    def getCoord(self):
        return self.coord
    
    def getWidth(self):
        return self.width
    
    def getHeight(self):
        return self.height
    

def onAppStart(app):
    #Makes background for opening screen and game
    app.image = Image.open("background1.jpeg")
    newWidth, newHeight = (app.image.width // 10, app.image.height // 5)
    app.imageScaled = app.image.resize((newWidth,newHeight))
    app.imageScaled = CMUImage(app.imageScaled)
    #icon num 1
    app.image2 = Image.open("icon1.png")
    newWidth2,newHeight2 = (app.image2.width // 3, app.image2.height // 3)
    app.image2 = app.image2.resize((newWidth2,newHeight2))
    app.imageScaled2 = CMUImage(app.image2)
    #icon num 2
    app.image3 = Image.open("icon2.jpeg")
    newWidth34,newHeight34 = (app.image3.width // 9, app.image3.height // 9)
    app.image3 = app.image3.resize((newWidth34,newHeight34))
    app.imageScaled3 = CMUImage(app.image3)
    #icon num 3
    app.image4 = Image.open("icon3.jpeg")
    app.image4 = app.image4.resize((newWidth34,newHeight34))
    app.imageScaled4 = CMUImage(app.image4)
    #background when user is typing their name
    app.background2 = Image.open("player-name-wallpaper.jpeg")
    app.background2 = CMUImage(app.background2)
    #background when user is paused
    app.image5 = Image.open("pause-screen.jpeg")
    newWidth5,newHeight5 = (app.image5.width // 4, app.image5.height // 4)
    app.imageScaled5 = app.image5.resize((newWidth5,newHeight5))
    app.image5 = CMUImage(app.imageScaled5)
    #background for rocket mode
    app.rocketbackground = Image.open("rocketbackground.jpeg")
    app.rocketbackground = app.rocketbackground.resize((newWidth,newHeight))
    app.rocketbackground = CMUImage(app.rocketbackground)
    #obstacle 1
    app.image6 = Image.open("obstacle.png")
    newWidth6,newHeight6 = (app.image6.width // 3, app.image6.height // 3)
    app.imageScaled6 = app.image6.resize((newWidth6,newHeight6))
    app.image6 = CMUImage(app.imageScaled6)
    app.obstacle1Width = newWidth6
    app.obstacle1Height = newHeight6 
    #background when user quits
    app.background3 = Image.open("pause-end.jpeg")
    newWidth7,newHeight7 = (app.background3.width//3, app.background3.height//3)
    app.background3 = app.background3.resize((newWidth7,newHeight7))
    app.background3 = CMUImage(app.background3)
    #rocket's with icons
    app.rocket1 = Image.open('rocket1.png')
    app.rocket2 = Image.open('rocket2.png')
    app.rocket3 = Image.open('rocket3.png')
    newWidth8,newHeight8 = (app.rocket1.width // 6, app.rocket1.height // 6)
    app.rocket1 = app.rocket1.resize((newWidth8,newHeight8))
    app.rocketWidth,app.rocketHeight = app.rocket1.width,app.rocket1.height
    app.rocket1 = CMUImage(app.rocket1)
    app.rocket2 = app.rocket2.resize((newWidth8,newHeight8))
    app.rocket2 = CMUImage(app.rocket2)
    app.rocket3 = app.rocket3.resize((newWidth8,newHeight8))
    app.rocket3 = CMUImage(app.rocket3)
    #teleport for rocket mode and out of rocket mode
    app.image8 = Image.open("teleport1.png")
    app.image9 = Image.open("teleport2.png")
    newWidth8,newHeight8 = (app.image8.width//5, app.image8.height//5)
    app.image8 = app.image8.resize((newWidth8,newHeight8))
    app.image9 = app.image9.resize((newWidth8,newHeight8))
    app.teleport1 = CMUImage(app.image8)
    app.teleport2 = CMUImage(app.image9)
    app.teleportX = 360
    app.teleportY = 270
    app.teleportHeight = app.image8.height
    #hearts for life
    app.image10 = Image.open("hearts.png")
    newWidth10,newHeight10 = (app.image10.width//20, app.image10.height//20)
    app.scaledImage10 = app.image10.resize((newWidth10,newHeight10))
    app.image10 = CMUImage(app.scaledImage10)
    #star to capture:
    app.star = Image.open("star.png")
    newWidthstar,newHeightstar = (app.star.width//14, app.star.height//14)
    app.scaledStar = app.star.resize((newWidthstar,newHeightstar))
    app.star = CMUImage(app.scaledStar)
    app.starX = None
    app.starY = None 
    app.countOfStar = 0
    app.starOnScreen = False
    #ghost to capture
    app.ghost = Image.open("ghost.png")
    newWidthghost,newHeightghost = (app.ghost.width//7, app.ghost.height//7)
    app.scaledGhost = app.ghost.resize((newWidthghost,newHeightghost))
    app.ghost = CMUImage(app.scaledGhost)
    app.ghostX = None
    app.ghostY = None 
    app.countOfGhost = 0
    app.ghostOnScreen = False
    app.shield = False
    app.numOfPastObstacles = 0
    #choice
    app.rocket = None
    app.fly = None
    app.rocketX = 20
    app.rocketY = 340
    #counter until rocket mode
    app.untilRocketMode = 0#WORK ON
    app.untilNormalMode = 0
    #rocket obstacles
    app.robstacle1 = Image.open("obstacle1Rocket.png")
    newWidthr1,newHeightr1 = (app.robstacle1.width // 2, app.robstacle1.height // 2)
    app.scaledOb1 = app.robstacle1.resize((newWidthr1,newHeightr1))
    app.robstacle1 = CMUImage(app.scaledOb1)
    app.obstacleR1Width = newWidthr1
    app.obstacleR1Height = newHeightr1 
    app.robstacle = None#general choice
    app.robstacle_2 = None#general choice

    app.robstacle2 = Image.open("obstacle2Rocket.png")
    app.robstacle3 = Image.open("obstacle3Rocket.png")
    newWidthr2,newHeightr2 = (app.robstacle2.width // 3, app.robstacle2.height // 3)
    newWidthr3,newHeightr3 = (app.robstacle3.width //3, app.robstacle3.height // 3)
    app.scaledOb2 = app.robstacle2.resize((newWidthr2,newHeightr2))
    app.scaledOb3 = app.robstacle3.resize((newWidthr3,newHeightr3))
    app.robstacle2 = CMUImage(app.scaledOb2)
    app.robstacle3 = CMUImage(app.scaledOb3)
    app.obstacleR2Width = newWidthr2
    app.obstacleR2Height = newHeightr2
    app.obstacleR3Width = newWidthr3
    app.obstacleR3Height = newHeightr3
    #user's icon
    app.selection = None
    app.player = ''
    app.icon = None
    #to make icon jump
    app.jump = False
    app.jumpIndex = -1
    app.YMove = [0,20,40,60,80,100,120,140,160,140,120,100,80,60,40,20,0]

    #obstacles
    app.obstacle = None
    app.obstacle2 = None
    app.obstacleX = None #coord of obstacle onscreen
    app.obstacleY = None
    app.obstacle2X = None #coord of obstacle onscreen
    app.obstacle2Y = None
    app.numOfObstacle = 0
    #icon coordinates
    app.x = 20
    app.currY = 325 #for recording
    app.y = 325
    #APP
    #app.stepsPerSecond=30
    app.transitions = 1
    app.lives = 3 #how many lives the player gets
    #game over
    myGif = Image.open('gameover.gif')
    app.spriteList = []
    for frame in range(myGif.n_frames):
        #Set the current frame
        myGif.seek(frame)
        #Resize the image
        fr = myGif.resize((myGif.size[0]//2, myGif.size[1]//2))
        #Convert to CMUImage
        fr = CMUImage(fr)
        #Put in our sprite list
        app.spriteList.append(fr)

    print(app.spriteList)

    ##Fix for broken transparency on frame 0
    #app.spriteList.pop(0)

    app.spriteCounter = 0
    app.stepsPerSecond = 10

def newgame(app):
    app.obstacle = None
    app.obstacle2 = None
    app.obstacleX = None #coord of obstacle onscreen
    app.obstacleY = None
    app.obstacle2X = None #coord of obstacle onscreen
    app.obstacle2Y = None
    app.numOfObstacle = 0
    #icon coordinates
    app.x = 20
    app.currY = 325 #for recording
    app.y = 325
    #APP
    app.stepsPerSecond=30
    # app.transitions = 1
    app.untilRocketMode = 0#WORK ON
    app.untilNormalMode = 0
    app.fly = False
    app.teleportX = 360#need to reset
    app.teleportY = 270
    app.robstacle = None#general choice
    app.robstacle_2 = None#general choice
    app.rocketX = 20
    app.rocketY = 340
    


def welcome_redrawAll(app):
    drawImage(app.imageScaled,0,0)
    drawLabel("S H A P E  E S C A P E", app.width/2, app.height/3, 
              size = 25, font = 'Monospace',fill = 'lightgreen',
              bold = True)
    drawLabel("Press the space bar to begin", app.width/2,
              app.height/4*2, size = 10, font = 'Monospace',
              fill = 'lightgreen', bold = True)
    drawImage(app.imageScaled4,170,290, rotateAngle = 20)
    
def welcome_onKeyPress(app, key):
    if key == 'space':
        setActiveScreen('choose')

# #---------------------------------------------------
def choose_redrawAll(app):
    colors = ["blue",'red','yellow'] #3 types of icons
    #background
    drawRect(0,0,app.width,app.height, fill = 'grey',
             border = 'darkgrey', borderWidth = 10)
    drawRect(0,0,70,70,fill = 'darkslateblue')
    drawRect(app.width-70,0,70,70,fill = 'darkslateblue')
    drawRect(0,app.height-70,70,70,fill = 'darkslateblue')
    drawRect(app.width-70,app.height-70,70,70,fill = 'darkslateblue')
    
    #icon color choices
    for i in range(1,4):
        drawRect(95*i,280,40,40,fill = colors[i-1],
                 border = 'black', borderWidth = 5)
        
    #displays user's choice of icon
    if app.selection!=None:
        if app.selection==0:
            drawImage(app.imageScaled2,180,190)
        elif app.selection==1:
            drawImage(app.imageScaled3,180,190)
        elif app.selection==2:
            drawImage(app.imageScaled4,180,190)
    
    drawLabel("Click the enter key",
              200,100,font = 'Monospace', fill = 'darkslateblue',
              bold = True, size = 25)
    drawLabel("to finalize your choice",
              200,120,font = 'Monospace', fill = 'darkslateblue',
              bold = True, size = 25)
    drawLabel("of icon.",
              200,140,font = 'Monospace', fill = 'darkslateblue',
              bold = True, size = 25)
        
def choose_onMousePress(app,mouseX,mouseY):
    #check blue
    if 95 <= mouseX <= 95+40 and 280 <= mouseY <= 280+40:
        app.selection = 0
        app.icon = app.imageScaled2
        app.rocket = app.rocket1
    elif 190 <= mouseX <= 190+40 and 280 <= mouseY <= 280+40:
        app.selection = 1
        app.icon = app.imageScaled3
        app.rocket = app.rocket2
    #check red
    elif 285 <= mouseX <= 285+40 and 280 <= mouseY <= 280+40:
        app.selection = 2
        app.icon = app.imageScaled4
        app.rocket = app.rocket3

def choose_onKeyPress(app,key):
    if key=='enter' and app.selection!=None:
        setActiveScreen('player')

##-----------------------------------------------------
def player_redrawAll(app):
    drawImage(app.background2,0,0)
    drawImage(app.icon,180,200)
    drawLabel("Enter your name below:", 200,80,
              font = 'Monospace', size = 18, fill = 'white')
    drawLabel("Click enter once done:", 200,100,
              font = 'Monospace', size = 18, fill = 'white')
    if app.player!='':
        drawLabel(app.player,200,180,font = 'Monospace',
                  fill = 'white', size = 16, bold = True)

def player_onKeyPress(app,key):
    if key=='backspace' and app.player!='':
        app.player = app.player[:-1]
    elif (key!='enter' and key!='backspace' and key!='tab' and
          key!='space'):
        app.player = app.player + key
    elif key=='enter':
        app.player = Player(app.player)
        setActiveScreen('game')

##-----------------------------------------------------
def getIconCoord(app):
    if app.selection==0:
        width = app.image2.width
        height = app.image2.height
    elif app.selection==1:
        width = app.image3.width
        height = app.image3.height
    elif app.selection==2:
        width = app.image4.width
        height = app.image4.height
    return width,height

def game_onStep(app):
    if app.transitions>4:
        setActiveScreen('win')
    app.stepsPerSecond = 10 + 5*(app.transitions)
    if app.jump:
        app.jumpIndex+=1
    if app.jumpIndex==len(app.YMove):
        app.jump = False
        app.jumpIndex=0
    if app.jump:
        app.currY = app.y-app.YMove[app.jumpIndex]

    if app.untilRocketMode>=10:
        moveTeleport(app)
    else:
        if app.obstacle==None:
            chooseObstacle(app)
        if not app.shield:
            collisionCheck(app)
        if isinstance(app.obstacle,Obstacle):
            moveObstacle(app)
        #can only get star at level 2
        if app.countOfStar==0 and app.transitions>=2:
            selectStar(app)
        if app.starOnScreen:
                moveStar(app)
                if app.starX!=None and captureStar(app):
                    app.lives+=1
                    app.starOnScreen=False
        if app.countOfGhost==0 and app.transitions>=2:
            selectGhost(app)
        if app.ghostOnScreen:
            moveGhost(app)
            if app.ghostX!=None and captureGhost(app):
                app.ghostOnScreen = False
        if app.numOfPastObstacles>3 :
            app.shield = False
        

def selectGhost(app):
    if 5<=app.untilRocketMode<=8 and app.lives<2:
        app.ghostOnScreen = True
        app.ghostX = 400
        app.ghostY = 150
        app.countOfGhost+=1

def captureGhost(app):
    widthOfGhost = app.scaledGhost.width
    heightOfGhost = app.scaledGhost.height
    #subtract 10 to improve appearance on screen 
    if (app.ghostX-10<=app.x<=app.ghostX + widthOfGhost and 
        app.ghostY<=app.currY<=app.ghostY + heightOfGhost+10):
        app.shield = True
        return True
    return False

def moveGhost(app):
    app.ghostX-=20
    if app.ghostX<-50:
        app.ghostOnScreen = False
        app.ghostX = None#unsure
        app.ghostY=None
        app.shield = False

def selectStar(app):
    choice = random.randint(1,2)
    if choice==2 and app.lives<2:
        app.starOnScreen = True
        app.starX = 400
        app.starY = 150
        app.countOfStar+=1

def moveStar(app):
    app.starX-=20
    if app.starX<-50:
        app.starOnScreen = False
        app.starX = None#unsure
        app.starY=None

def captureStar(app):
    widthOfStar = app.scaledStar.width
    heightOfStar = app.scaledStar.height
    #subtract 10 to improve appearance on screen 
    if (app.starX-10<=app.x<=app.starX + widthOfStar and 
        app.starY<=app.currY<=app.starY + heightOfStar+10):
        return True
    return False

def game_redrawAll(app):
    drawImage(app.imageScaled,0,0)
    if app.jump: 
        drawImage(app.icon,app.x,app.currY)
    elif app.shield:
        width,height = getIconCoord(app)
        #look like shield of icon
        #subtract 4 to center
        drawRect(app.x-4,app.y-4,width+8,height+8,fill = 'palegoldenrod')
        drawImage(app.icon,app.x,app.y)
    else:
        drawImage(app.icon,app.x,app.y)
    drawLabel(f"L e v e l   {app.transitions}",100,40,font = 'Monospace',
                  size = 20, fill = 'lightGreen', bold = True)
    
    if app.obstacle2!=None:
        drawRect(app.obstacle2X,app.obstacle2Y, app.obstacle2.getWidth(),
                 app.obstacle2.getHeight(),fill = 'black',border = 'white')

    #check for point 1
    if app.obstacleY == 310:
        drawImage(app.image6,app.obstacleX,app.obstacleY)
    elif isinstance(app.obstacle,Obstacle):
        drawRect(app.obstacleX,app.obstacleY,
                 app.obstacle.getWidth(),
                 app.obstacle.getHeight(),
                 fill = 'black',border = "white")
    if app.untilRocketMode>=10:
        drawImage(app.teleport1,app.teleportX,app.teleportY)
    drawLabel(f"{app.player}'s lives",340,20, fill = 'lightGreen',size = 16,
              font = 'Monospace',bold = True)
    #draws how many lives the user has
    for i in range(app.lives):
        drawImage(app.image10,290 + i*40,40)
    #draws star
    if app.starOnScreen:
        drawImage(app.star,app.starX,app.starY)
    if app.ghostOnScreen:
        drawImage(app.ghost,app.ghostX,app.ghostY)
    

def game_onKeyPress(app, key):
    #add 10 to jump
    if key=='up':
        app.jump = True
    elif key=='p':
        setActiveScreen('pause')
    elif key=='e':
        setActiveScreen('win')
    elif key=='t':
        app.transitions=2

def chooseObstacle(app):
    if app.shield:
        app.numOfPastObstacles+=1

    app.untilRocketMode+=1
    #first obstacle
    point1 = Point(400,310)#first obstacle
    point2 = Point(400,325)#second obstacle
    point3 = Point(400,275)#third obstacle
    point4 = Point(400,250)

    choice = random.randint(1,3)#picks the obstacle type
    if choice==2:
        app.obstacle = Obstacle(point2,50,50)
        app.obstacleX = point2.getX()
        app.obstacleY = point2.getY()
        app.numOfObstacle+=1
    elif choice==3:
        app.obstacle = Obstacle(point3,50,100)
        app.obstacleX = point3.getX()
        app.obstacleY = point3.getY()
        app.numOfObstacle+=1
    else:
        app.obstacle=Obstacle(point1,app.obstacle1Width,app.obstacle1Height)
        app.obstacleX = point1.getX()
        app.obstacleY = point1.getY()
        app.numOfObstacle+=1
        
    #if choice is 1, then won't use obstacle class b/c polygon has
    #multiple points

def moveTeleport(app):
    if app.x<app.teleportX:
        app.teleportX-=20
    elif app.x-5<app.teleportX:
        app.teleportX-=5
        if not teleportLegalityCheck(app):
            app.lives-=1
            if app.lives==0:
                setActiveScreen('dead')
            else:
                newgame(app)
                setActiveScreen('game')
    else:
        app.obstacle = None
        app.obstacleX =None
        app.obstacleY = None

        app.obstacle2 = None
        app.obstacle2X =None
        app.obstacle2Y = None
        if app.untilRocketMode>0:
            app.teleportX = 360#need to reset for when second teleport comes
            app.teleportY = 270
            app.fly = True
            app.jump = False
            setActiveScreen('rocket')
        elif app.untilNormalMode>0:
            # app.robstacle = None
            app.teleportX = 360#need to reset for when second teleport comes
            app.teleportY = 270
            app.fly = False
            app.transitions+=1
            setActiveScreen('game')

def teleportLegalityCheck(app):
    if app.fly:#if in rocket mode, need to make sure rocket goes into teleport
        if app.teleportY<=app.rocketY<=app.teleportY + app.teleportHeight:
            return True
        return False
    else:
        if app.teleportY<=app.currY<=app.teleportY + app.teleportHeight:
            return True
        return False

def slide(app):
    width,height = getIconCoord(app)
    if ((app.obstacleY==325 or app.obstacleY==275) and app.x+width>=app.obstacleX
        and app.currY<=app.obstacleY and app.jumpIndex>=len(app.YMove)//2+4):
        #app.slideOnTop=True
        endOfObstacle = app.obstacleX + app.obstacle.getWidth()
        distanceTillEnd = endOfObstacle - app.x
        distanceTillEnd-=20
        if distanceTillEnd<=0:
            if app.obstacleY==325:
                app.currY = app.y-app.YMove[app.jumpIndex]
            else:
                app.currY = app.y
        app.currY = app.obstacleY - height

def moveObstacle(app):
    app.untilNormalMode = 0
    app.obstacleX-=20
    if app.obstacle2!=None:
        app.obstacle2X-=20
        if app.obstacle2X<-250:
            app.obstacle2 = None
            app.obstacle2X=None
            app.obstacle2Y = None
    if app.obstacleX<-50:
        app.obstacleX = 300#unsure
        app.obstacle=None
        app.numOfObstacle=0
        chooseObstacle(app)
    slide(app)
    

def collisionCheck(app):
    #check collision if triangle
    if app.obstacle.getCoord().getY()==310:#if triangle
        xtop = app.obstacleX
        xbot = app.obstacleX + app.obstacle1Width
        ytop = app.obstacleY
        ybot = app.obstacleY + app.obstacle1Height
        if xtop <= app.x < xbot and ytop <= app.currY <ybot:
            app.lives-=1
            if app.lives==0:
                setActiveScreen("dead")
            else:
                newgame(app)
                setActiveScreen("game")
    elif app.fly:
        width1,height1 = app.rocketWidth, app.rocketHeight
        xleft = app.rocketX
        ytop = app.rocketY
        xright = xleft + width1
        ybot = ytop + height1
    
        obleft = app.obstacleX
        obtop = app.obstacleY
        obright = obleft + app.obstacle.getWidth()
        obbot = obtop + app.obstacle.getHeight()
        #if there are 2 obstacles
        if app.obstacle2!=None:
            obleft2 = app.obstacle2X
            obtop2 = app.obstacle2Y
            obright2 = obleft2 + app.obstacle2.getWidth()
            obbot2 = obtop2 + app.obstacle2.getHeight()
            if ((ybot>=obtop2) and (ytop<=obbot2) and 
                (xright>=obleft2+35) and (xleft<=obright2)):
                app.lives-=1
                if app.lives==0:
                    setActiveScreen("dead")
                else:
                    newgame(app)
                    setActiveScreen("game")
        if app.rocketX > obleft+20:
            pass
        elif ((ybot>=obtop) and (ytop<=obbot) and 
            (xright>=obleft+35) and (xleft<=obright)):
            app.lives-=1
            if app.lives==0:
                setActiveScreen("dead")
            else:
                newgame(app)
                setActiveScreen("game")
    else:#if rectange
        #icon coordinates
        width1,height1 = getIconCoord(app)
        left1 = app.x
        top1 = app.currY
        #obstacle 1 coordinates
        width2,height2 = app.obstacle.getWidth(),app.obstacle.getHeight()
        left2 = app.obstacleX
        top2 = app.obstacleY
        #icon
        bot1 = top1 + height1
        right1 = left1 + width1
        #obstacle 1
        bot2 = top2 + height2
        right2 = left2 + width2
        if app.obstacle2!=None:#if obstacle 2 exists
            width3,height3 = app.obstacle2.getWidth(),app.obstacle2.getHeight()
            left3 = app.obstacle2X
            top3 = app.obstacle2Y
            bot3 = top3 + height3
            right3 = left3 + width3
            #legal check for obstacle 2 if it exists
            if bot1<=top3 or app.jumpIndex>=len(app.YMove)//2:
                pass
            elif ((bot1>=top3) and (top1<=bot3) and 
                (right1>=left3) and (left1<=right3)):
                setActiveScreen('dead')
        #for first obstacle
        if bot1<=top2 or app.jumpIndex>=len(app.YMove)//2:
            pass
        elif ((bot1>=top2) and (top1<=bot2) and 
            (right1>=left2) and (left1<=right2)):
            app.lives-=1
            if app.lives==0:
                setActiveScreen("dead")
            else:
                newgame(app)
                setActiveScreen("game")

    #check collision if block
# #---------------------------------------------------
def dead_redrawAll(app):
    drawImage(app.imageScaled,0,0)
    x, y = app.width/2, app.height/2
    #drawRect(0, 0, app.width, app.height, fill='palegreen')
    drawImage(app.spriteList[app.spriteCounter], 
              x, y, align = 'center')

def dead_onStep(app):
    #Set spriteCounter to next frame
    app.stepsPerSecond = 10
    app.spriteCounter = (app.spriteCounter + 1) % len(app.spriteList)

# #---------------------------------------------------
def rocket_redrawAll(app):
    drawImage(app.rocketbackground,0,0)
    drawImage(app.rocket,app.rocketX,app.rocketY)
    if app.obstacle!=None:
        drawImage(app.robstacle,app.obstacleX,app.obstacleY)
    if app.obstacle2!=None and app.untilNormalMode<10:
        drawImage(app.robstacle_2,app.obstacle2X,app.obstacle2Y)
    if app.untilNormalMode>=10:
        drawImage(app.teleport2,app.teleportX,app.teleportY)

def chooseObstacleR(app):
    #first obstacle
    choice = random.randint(1,3)
    app.untilNormalMode+=1
    if choice==1:#first obstacle
        app.robstacle = app.robstacle1#the image
        point1 = Point(400,330)#first obstacle
        app.numOfObstacle+=1
        app.obstacle=Obstacle(point1,app.obstacleR1Width,app.obstacleR1Height)
        app.obstacleX = point1.getX()
        app.obstacleY = point1.getY()
    elif choice==2:
        app.robstacle = app.robstacle2
        point2 = Point(400,200)
        app.numOfObstacle+=1
        app.obstacle=Obstacle(point2,app.obstacleR2Width,app.obstacleR2Height)
        app.obstacleX = point2.getX()
        app.obstacleY = point2.getY()
    elif choice==3:
        app.robstacle = app.robstacle3
        point3 = Point(400,275)
        app.numOfObstacle+=1
        app.obstacle=Obstacle(point3,app.obstacleR3Width,app.obstacleR3Height)
        app.obstacleX = point3.getX()
        app.obstacleY = point3.getY()
    choice2 = random.randint(1,2)
    if choice2==2:
        point4 = Point(400,0)
        app.obstacle2=Obstacle(point4,app.obstacleR3Width,app.obstacleR3Height)
        app.obstacle2X = point4.getX()
        app.obstacle2Y = point4.getY()
        app.numOfObstacle+=1
        app.robstacle_2 = app.robstacle3


def moveObstacleR(app):
    app.untilRocketMode = 0
    if isinstance(app.obstacle,Obstacle):
        app.obstacleX-=20
    if app.obstacle!=None and app.obstacleX<-300:
        app.obstacleX = 400#unsure
        app.obstacle=None
        app.numOfObstacle-=1
        chooseObstacleR(app)
    if app.obstacle2!=None:
        app.obstacle2X-=20
        if app.obstacle2X<-300:
            app.obstacle2=None
            app.obstacle2X = None
            app.obstacle2Y = None

def rocket_onStep(app):
    if app.untilNormalMode>=10:
        moveTeleport(app)
    else:
        if app.obstacle==None:
            chooseObstacleR(app)
        app.numOfObstacle+=1
        collisionCheck(app)
        moveObstacleR(app)

def rocket_onKeyPress(app,key):
    if key=='up' and app.rocketY-20>0:
        app.rocketY-=20 
    elif key=='down' and app.rocketY+20<350:#if it'll go off screen
        app.rocketY+=20
    elif key=='up':
        app.rocketY = 20
    elif key=='down':
        app.rocketY = 350
    elif key=='p':
        setActiveScreen('pause')
# #---------------------------------------------------
def win_redrawAll(app):
    drawImage(app.imageScaled,0,0)
    drawLabel("T H A N K    Y O U", app.width/2, app.height/3, 
              size = 25, font = 'Monospace',fill = 'lightgreen',
              bold = True)
    drawLabel("F O R    P L A Y I N G", app.width/2, app.height/3+50, 
              size = 25, font = 'Monospace',fill = 'lightgreen',
              bold = True)
    drawLabel("Press r to start a new game", app.width/2, app.height/3+100, 
              size = 20, font = 'Monospace',fill = 'lightgreen',
              bold = True)
    
def win_onKeyPress(app,key):
    if key=='r':
        app.obstacleX=400
        app.jump = False
        setActiveScreen('choose')
    
# #---------------------------------------------------
def pause_onKeyPress(app, key):
    if key=='c':#continue
        setActiveScreen('game')
    if key=='q':
        setActiveScreen('pauseEnd')

def pause_redrawAll(app):
    drawImage(app.imageScaled,0,0)
    drawImage(app.image5,60,150)
    drawLabel("Press 'c' to continue",200,120,
              fill = 'white', font = 'Monospace',
              size = 25, bold = True)
    drawLabel("or press 'q' to quit",200,280,
              fill = 'white', font = 'Monospace',
              size = 25, bold = True)

# #---------------------------------------------------
def pauseEnd_onKeyPress(app, key):
    if key=='s':
        setActiveScreen('welcome')

def pauseEnd_redrawAll(app):
    drawRect(0,0,app.width,app.height,fill = 'darkblue')
    drawImage(app.background3,50,100)
    drawLabel('Thanks for Playing!', app.width/2, app.height/2+50,
              font = 'Monospace', fill = 'white',size = 24,
              bold = True)

# #---------------------------------------------------
# # Your screen names should be strings
runAppWithScreens(initialScreen='welcome')
