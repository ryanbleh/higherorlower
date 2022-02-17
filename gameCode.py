from graphics import *
#random 
import random
#saves scores to file
import json 
#copy to clipboard  
import pyperclip as pc
#imports table for artwork
import csv 
#download files from web
from urllib.request import urlretrieve 
#check if file exists 
from pathlib import Path
import time

#https://www.pythontutorial.net/python-basics/python-check-if-file-exists/ 
makeGraphicsWindow(1440, 855)

#Purpose: Aligns text with a certain defined percentage
#Args: String, Font Size, Whaxt % you want text located on screen (50% is middle)
#Result: Returns a X postion which is x percent down the screen
def alignTextX(string, stringSize, location,):
    at_w, at_h = sizeString(string,stringSize)
    return location / 100 * getWindowWidth() - at_w / 2

#Purpose: Aligns text with a certain defined percentage
#Args: String, Font Size, What % you want text located on screen (50% is middle)
#Result: Returns a Y postion which is x percent down the screen
def alignTextY(string, stringSize, location):
    at_w, at_h = sizeString(string,stringSize)
    return location / 100 * getWindowHeight() - at_h / 2

#Purpose: Every click goes through all buttons to see if they have been clicked on
#Args: MouseX, MouseY, and mouse button
#Results: None 
def clickDetect(world, mouseX, mouseY,button):
    for i in world.buttons: 
        i.buttonClicks(world,mouseX,mouseY,button)

def fileLoader(world):
    with open('art_data.csv', 'r') as a_d:
        world.art_data = list(csv.reader(a_d))    
    with open('easy_scores.json', 'r') as s:
        world.easy_scores = json.load(s)
    with open('easy_all_scores.json', 'r') as s:
        world.easy_all_scores = json.load(s)
    with open('easy_names.json', 'r') as s:
       world.easy_names = json.load(s)
    with open('normal_scores.json', 'r') as s:
        world.normal_scores = json.load(s)
    with open('normal_all_scores.json', 'r') as s:
        world.normal_all_scores = json.load(s)
    with open('normal_names.json', 'r') as s:
        world.normal_names = json.load(s)
    with open('hard_scores.json', 'r') as s:
        world.hard_scores = json.load(s)
    with open('hard_all_scores.json', 'r') as s:
        world.hard_all_scores = json.load(s)
    with open('hard_names.json', 'r') as s:
        world.hard_names = json.load(s)
    print("all files loaded")

class Artwork:
    def __init__(self,art_name,artist,price,file_name):
        self.art_name = art_name
        self.artist = artist
        self.price = price 
        self.file_name = file_name
        self.image = loadImage(f"{self.file_name}")

class String:
    def __init__(self,posX,posY,screen,string,size):
        print("started")
        self.xPercentage = posX
        print("posx")
        self.yPercentage = posY
        print("posy")
        self.string = string
        print("string")
        self.size = size
        print("size")
        self.screen = screen
        print("screen")
        self.alignedPosX = alignTextX(self.string,self.size,self.xPercentage)
        self.alignedPosY = alignTextY(self.string,self.size,self.yPercentage)
        print("alignment")
        #self.alignedPosX = 10
        #self.alignedPosY = 10
    def drawString(self,world):
        print("string draw called")
        if world.screen == self.screen: 
            drawString(self.string,self.alignedPosX ,self.alignedPosY,self.size,)

class Button: 
    def __init__(self,posX,posY,width,height,button_name,screen,button_text,text_size=30,text_color="black",button_background_color="gray",button_outline_color="black"):
        self.xPercentage = posX
        print("POSX")
        self.yPercentage = posY
        print("POSY")
        self.width = width
        print("WIDTH")
        self.height = height
        print("HEIGHT")
        self.button_name = button_name
        print("BUTTON NAME")
        self.text = str(button_text)
        print("TEXT")
        self.text_size = int(text_size)
        print("TEXT SIZE")
        self.text_color = text_color
        print("TEXT COLOR")
        self.button_background_color = button_background_color
        print("BACKGROUND COLOR")
        self.button_outline_color = button_outline_color
        print("BACKGROUND OUTLINE COLOR")
        self.screen = screen
        print("SCREEN")
        self.w, self.h = sizeString(str(self.text), int(self.text_size))
        print("ALIGNMENT")
        #self.w = 10
        #self.h = 10
        #print(69)

    def buttonClicks(self,world, mouseX, mouseY,button):
        if world.screen == self.screen: 
            if mouseX > self.xPercentage / 100 * world.windowWidth - self.width / 2 and mouseX < self.xPercentage / 100 * world.windowWidth - self.width / 2 + self.width:
                if mouseY > self.yPercentage / 100 * world.windowHeight - self.height / 2 and mouseY <  self.yPercentage / 100 * world.windowHeight - self.height / 2 + self.height:
                    if self.button_name == "startGame":
                        if world.mode == "normal":                      
                            world.screen = "game"
                            world.game.restart(world)
                        else:
                            world.start = time.time()
                            world.screen = "game"
                    if self.button_name == "highScore":
                        world.screen = "leaderboard"
                    if self.button_name == "modes":
                        world.screen = "modes"
                    if self.button_name == "higher":
                        world.game.higher(world)
                    if self.button_name == "lower":
                        world.game.lower(world)
                    if self.button_name == "restart":
                        world.screen = "game"
                        world.game.restart(world)
                    if self.button_name == "mainmenu":
                        world.screen = "start"
                    if self.button_name == "save":
                        if world.mode == "easy":
                            if not world.score > world.easy_scores[9]:
                                world.error = True
                            else:   
                                world.screen = "save"
                        if world.mode == "normal":
                            if not world.score > world.normal_scores[9]:
                                world.error = True
                            else:   
                                world.screen = "save"
                        if world.mode == "hard":
                            if not world.score > world.hard_scores[9]:
                                world.error = True
                            else:   
                                world.screen = "save"
                    if self.button_name == "copy":
                        pc.copy("I scored " + str(world.score) + " in Higher or Lower | Art Edition")
                    if self.button_name == "back":
                        world.screen = "start"
                    if self.button_name == "easy":
                        world.mode = "easy"
                    if self.button_name == "normal":
                        world.mode = "normal"
                    if self.button_name == "hard":
                        world.mode = "hard"
                    if self.button_name == "easylb":
                        world.modelb = "easylb"
                    if self.button_name == "normallb":
                        world.modelb = "normallb"
                    if self.button_name == "hardlb":
                        world.modelb = "hardlb"

                        
    def drawButton(self,world):
        

        if self.w > self.width: 
            raise Exception("Button is less wide than text, please change values: " + self.text)
        if self.h > self.height: 
            raise Exception("Button is shorter than text, please change values: " + self.text)
        print(3)
        
        if world.screen == self.screen: 
            print(4)
            fillRectangle(self.xPercentage / 100 * world.windowWidth - self.width / 2 , self.yPercentage / 100 * world.windowHeight - self.height / 2 ,self.width, self.height, self.button_background_color)
            print(4.2)
            print(self.text, self.xPercentage / 100 * world.windowWidth - self.w / 2, self.yPercentage / 100 * world.windowHeight - self.h / 2 ,self.text_size)
            
            drawString(self.text, self.xPercentage / 100 * world.windowWidth - self.w / 2, self.yPercentage / 100 * world.windowHeight - self.h / 2 ,self.text_size)
            print(4.5)
            drawRectangle(self.xPercentage / 100 * world.windowWidth - self.width / 2 , self.yPercentage / 100 * world.windowHeight - self.height / 2 ,self.width, self.height,self.button_outline_color) 
            print(4.9)
            print(5)

            self.fancyButtons = ["hard","easy","normal"]  
            for i in self.fancyButtons:
                if world.mode == i:
                    if self.button_name == i:
                        fillRectangle(self.xPercentage / 100 * world.windowWidth - self.width / 2 , self.yPercentage / 100 * world.windowHeight - self.height / 2 ,self.width, self.height, "lime")
                        drawString(self.text, self.xPercentage / 100 * world.windowWidth - self.w / 2, self.yPercentage / 100 * world.windowHeight - self.h / 2 ,self.text_size)
                        drawRectangle(self.xPercentage / 100 * world.windowWidth - self.width / 2 , self.yPercentage / 100 * world.windowHeight - self.height / 2 ,self.width, self.height,"green") 
            self.fancyButtons2 = ["hardlb","easylb","normallb"]
            #print(6)  
            for i in self.fancyButtons2:
                if world.modelb == i:
                    if self.button_name == i:
                        fillRectangle(self.xPercentage / 100 * world.windowWidth - self.width / 2 , self.yPercentage / 100 * world.windowHeight - self.height / 2 ,self.width, self.height, "lime")
                        drawString(self.text, self.xPercentage / 100 * world.windowWidth - self.w / 2, self.yPercentage / 100 * world.windowHeight - self.h / 2 ,self.text_size)
                        drawRectangle(self.xPercentage / 100 * world.windowWidth - self.width / 2 , self.yPercentage / 100 * world.windowHeight - self.height / 2 ,self.width, self.height,"green") 
        if world.screen == self.screen:
            if world.mode == "normal":
                if world.screen == "game":
                    drawString("Average Score: " + str(world.avg_score), alignTextX("Average Score: " + str(world.avg_score),40,50),135,40)
        #print(f"Button Drawn: {self.xPercentage}, {self.yPercentage}, {self.width}, {self.height}, {self.button_name}, {self.text}")            
class Compare: 
    def __init__(self,world):
        self.compare_1 = random.choice(world.images)
        self.compare_2 = random.choice(world.images)
        while self.compare_2.artist == self.compare_1.artist: 
            self.compare_2 = random.choice(world.images)  

        self.tries = 3
        world.score = 0 
    def restart(self,world):
        self.tries = 3 
        world.error = False
        world.score = 0  
        self.compare_1 = random.choice(world.images)
        self.compare_2 = random.choice(world.images)
        while self.compare_2.artist == self.compare_1.artist: 
            self.compare_2 = random.choice(world.images)   
        world.start = time.time()
        world.strings.pop()
        

    def success(self,world):
            self.compare_1 = self.compare_2
            self.compare_2 = random.choice(world.images)
            world.score += 1
            while self.compare_2.artist == self.compare_1.artist: 
                self.compare_2 = random.choice(world.images) 
            if world.mode == "hard":
                world.start = time.time() 


    def fail(self,world):
        if world.mode == "normal": 
            world.screen = "fail"
            world.normal_all_scores.append(world.score)
            with open('normal_all_scores.json', 'w') as a_s:
                json.dump(world.normal_all_scores, a_s)
        if world.mode == "hard":
            world.screen = "fail"
            world.hard_all_scores.append(world.score)
            with open('hard_all_scores.json', 'w') as a_s:
                json.dump(world.hard_all_scores, a_s)
        if world.mode == "easy":
            if self.tries > 1:
                self.tries -= 1 
                world.bigX = True
                world.bigXscale = 5
            else:
                world.screen = "fail"
                world.strings.append(String(50,35,"fail",world.score,150))
                world.easy_all_scores.append(world.score)
                with open('easy_all_scores.json', 'w') as a_s:
                    json.dump(world.easy_all_scores, a_s)
                world.bigX = False
                

    def hack(self,world):
        if world.screen == "game":
            if world.hack == True:
                if int(self.compare_2.price) > int(self.compare_1.price):
                    drawString("Correct Answer: Higher",30,30, 50)
                else:
                    drawString("Correct Answer: Lower",30,30, 50)
        
        
    def higher(self,world):
        if int(self.compare_2.price) > int(self.compare_1.price):
            self.success(world)
        else: 
            self.fail(world)
            

    def lower(self,world):
        if int(self.compare_2.price) < int(self.compare_1.price):
            self.success(world)
        else: 
            self.fail(world)      

    def drawImages(self,world): 
        if world.screen == "game":
            drawImage(self.compare_1.image,25 / 100 * world.windowWidth,35 / 100 * world.windowHeight)
            drawString(self.compare_1.art_name,alignTextX(self.compare_1.art_name,40,25),alignTextY(self.compare_1.art_name,40,55),40)
            drawString(self.compare_1.artist,alignTextX(self.compare_1.artist,40,25),alignTextY(self.compare_1.artist,40,60),40)
            drawString("$" + f"{int(self.compare_1.price):,}",alignTextX(self.compare_1.price,40,25),alignTextY(self.compare_1.price,40,65),40)
            drawImage(self.compare_2.image,75 / 100 * world.windowWidth,35 / 100 * world.windowHeight)
            drawString(self.compare_2.art_name,alignTextX(self.compare_2.art_name,40,75),alignTextY(self.compare_2.art_name,40,55),40)
            drawString(self.compare_2.artist,alignTextX(self.compare_2.artist,40,75),alignTextY(self.compare_2.artist,40,60),40)
            drawString("Score: " + str(world.score),alignTextX("Score: " + str(world.score),60,50),alignTextY("Score: " + str(world.score),60,3),60)
            if world.mode == "easy":
                drawString("High Score: " + str(world.easy_high_score),alignTextX("High Score: " + str(world.easy_high_score),60,50),alignTextY("High Score: " + str(world.easy_high_score),60,8),60)
            if world.mode == "normal":
                drawString("High Score: " + str(world.normal_high_score),alignTextX("High Score: " + str(world.normal_high_score),60,50),alignTextY("High Score: " + str(world.normal_high_score),60,8),60)
            if world.mode == "hard":
                drawString("High Score: " + str(world.hard_high_score),alignTextX("High Score: " + str(world.hard_high_score),60,50),alignTextY("High Score: " + str(world.hard_high_score),60,8),60)
            drawString("costs",alignTextX("costs",30,75),alignTextY("costs",30,66),30)
            drawString("or",alignTextX("or",30,75),alignTextY("or",30,74),30)
            drawString(f"than {self.compare_1.art_name}",alignTextX(f"than {self.compare_1.art_name}",30,75),alignTextY(f"than {self.compare_1.art_name}",30,83),30)
            #yes I realize there is probably a better way to do this with loops but i dont want to spend an hour to figure it out 
            if world.mode == "easy":
                if self.tries == 3:
                    drawImage(world.heart, world.windowWidth / 2 + 100, 150)
                    drawImage(world.heart, world.windowWidth / 2, 150)
                    drawImage(world.heart, world.windowWidth / 2 - 100, 150)
                if self.tries == 2:
                    drawImage(world.greyheart, world.windowWidth / 2 + 100, 150)
                    drawImage(world.heart, world.windowWidth / 2, 150)
                    drawImage(world.heart, world.windowWidth / 2 - 100, 150)
                if self.tries == 1:
                    drawImage(world.greyheart, world.windowWidth / 2 + 100, 150)
                    drawImage(world.greyheart, world.windowWidth / 2, 150)
                    drawImage(world.heart, world.windowWidth / 2 - 100, 150)

class Background:
    def __init__(self,world):
        self.image = random.choice(world.images)
        self.x = random.randint(0,1440)
        self.y = random.randint(0,900)
    
    def drawImg(self):
        drawImage(self.image.image,self.x,self.y,scale=0.5)

def listToString(lists): 
    string = "" 
    for item in lists: 
        string += item  
    return string

def Save(world,key):
    currentkey = getKeyName(key)
    if currentkey in world.typeletters:
        if len(world.save_name) < 3:
            world.save_name.append(currentkey.upper())
    elif currentkey == "backspace":
        if len(world.save_name) > 0:
            world.save_name.pop()
    elif currentkey == "enter":

        temp = listToString(world.save_name)
        if world.mode == "easy":
            for i in range(10):
                if world.score > world.easy_scores[i]:
                    world.easy_scores.insert(i, world.score)
                    world.easy_scores.pop(-1)
                    world.easy_names.insert(i,temp.upper())
                    world.easy_names.pop(-1)
                    with open('easy_names.json', 'w') as n:
                        json.dump(world.easy_names, n)
                    with open('easy_scores.json', 'w') as s:
                        json.dump(world.easy_scores,s)
                    world.screen = "start"
                    world.save_name = [ ]
                    break
        elif world.mode == "normal":   
            for i in range(10):
                if world.score > world.normal_scores[i]:
                    world.normal_scores.insert(i, world.score)
                    world.normal_scores.pop(-1)
                    world.normal_names.insert(i,temp.upper())
                    world.normal_names.pop(-1)
                    with open('normal_names.json', 'w') as n:
                        json.dump(world.normal_names, n)
                    with open('normal_scores.json', 'w') as s:
                        json.dump(world.normal_scores,s)
                    world.screen = "start"
                    world.save_name = [ ]
                    break
        elif world.mode == "hard":   
            for i in range(10):
                if world.score > world.hard_scores[i]:
                    world.hard_scores.insert(i, world.score)
                    world.hard_scores.pop(-1)
                    world.hard_names.insert(i,temp.upper())
                    world.hard_names.pop(-1)
                    with open('hard_names.json', 'w') as n:
                        json.dump(world.hard_names, n)
                    with open('hard_scores.json', 'w') as s:
                        json.dump(world.hard_scores,s)
                    world.screen = "start"
                    world.save_name = [ ]
                    break
def startWorld(world):
    #world.music = loadMusic('background.wav', 0.5)
    world.windowHeight = getWindowHeight()
    world.windowWidth = getWindowWidth()
    world.draw = True
    print("test1")
    world.bigX = False
    world.bigXscale = 5
    world.timeLimit = 5
    world.start = time.time()
    world.mode = "normal"
    world.modelb = "normallb"
    world.hack = False 
    print("test2")
    fileLoader(world)
    print("test3")

    
    for i in [("art_data.csv","https://raw.githubusercontent.com/ryanbleh/higherorlower/main/art_data.csv"),("greyheart.png","https://raw.githubusercontent.com/ryanbleh/higherorlower/main/greyheart.png"),("heart.png","https://raw.githubusercontent.com/ryanbleh/higherorlower/main/heart.png"),
    ('easy_scores.json',"https://raw.githubusercontent.com/ryanbleh/higherorlower/main/easy_scores.json"),("easy_all_scores.json","https://raw.githubusercontent.com/ryanbleh/higherorlower/main/easy_all_scores.json"),("easy_names.json","https://raw.githubusercontent.com/ryanbleh/higherorlower/main/easy_names.json"),
    ('normal_scores.json',"https://raw.githubusercontent.com/ryanbleh/higherorlower/main/normal_scores.json"),("normal_all_scores.json","https://raw.githubusercontent.com/ryanbleh/higherorlower/main/normal_all_scores.json"),("normal_names.json","https://raw.githubusercontent.com/ryanbleh/higherorlower/main/normal_names.json"),
    ('hard_scores.json',"https://raw.githubusercontent.com/ryanbleh/higherorlower/main/hard_scores.json"),("hard_all_scores.json","https://raw.githubusercontent.com/ryanbleh/higherorlower/main/hard_all_scores.json"),("hard_names.json","https://raw.githubusercontent.com/ryanbleh/higherorlower/main/hard_names.json")]:
        path_to_file = i[0]
        path = Path(path_to_file)
        if path.is_file():
            pass
        else: 
            #if you are getting an error here, please check your internet connection 
            urlretrieve(i[1], i[0])  
    print("test3")
    for i in range(len(world.art_data)):
        path_to_file = f'{world.art_data[i][4]}.jpg'
       
        path = Path(path_to_file)
        if path.is_file():
            pass
        else:
            urlretrieve(world.art_data[i][3], f'{world.art_data[i][4]}.jpg')
    print("test4")
    world.heart = loadImage("heart.png", scale= .2)
    world.greyheart = loadImage("greyheart.png", scale= 0.2)
    world.easy_high_score = world.easy_scores[0]
    world.normal_high_score = world.normal_scores[0]
    world.hard_high_score = world.hard_scores[0]
    world.avg_score = 0
    print("test5")
    for item in world.normal_all_scores:
        world.avg_score += item
    world.avg_score /= len(world.normal_all_scores)
    world.avg_score = round(world.avg_score,2)
    print("test6")
    world.error = False
    world.images = [ ] 
    world.save_name = [ ]
    world.typeletters = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
    for i in range(len(world.art_data)):
        world.images.append(Artwork(world.art_data[i][1],world.art_data[i][0],world.art_data[i][2],f"{world.art_data[i][4]}.jpg"))
    print("test7")
    world.game = Compare(world)
    world.screen = "start"
    world.buttons_info = [
    [50,60,300,100,"startGame","start","Start Game", 70],
    [50,75,300,100,"highScore","start","High Scores",70],
    [50,90,300,100,"modes","start","Modes",70],
    [75,70,200,50,"higher","game","Higher",40],
    [75,78.5,200,50,"lower","game","Lower",40],
    [50,10,300,230,"scores","game"," ",40],
    [50,0,300,200,"scores","game"," ",40],
    [43.01,60,200, 100, "restart","fail","Restart",40],
    [56.91,60,200, 100, "mainmenu","fail","Back to Menu",40],
    [50,71.8,402,100,"save","fail","Save score to Leaderboard",40],
    [50,83.5,402,100,"copy","fail","Copy Score to Clipboard",40],
    [8.5,93,200,100,"back","leaderboard","Back",60],
    [25,50,300, 600, "easy","modes","Easy",60],
    [50,50,300, 600, "normal","modes","Normal",60],
    [75,50,300, 600, "hard","modes","Hard",60],
    [8.5,93,200,100,"back","modes","Back",60],
    [82,25,300,100,"easylb","leaderboard","Easy",40],
    [82,50,300,100,"normallb","leaderboard","Normal",40],
    [82,75,300,100,"hardlb","leaderboard","Hard",40]
                            ]
    world.buttons = [ ]

    #args are posX,posY,screen,string,size,color="black",bold=False,italic=False
    world.strings_info = [
        [50,25,"start","Higher or Lower | Art Edition",70],
        [50,25,"fail","You scored:",100],
        [50,40,"save","Type Your Initials:",100],
        [50,60,"save","Press Enter once ready",30]]
    world.strings = [ ]
    print("test8")
    for i in range(len(world.buttons_info)):
        print(f"Button String: {world.buttons_info[i][6]}")
        world.buttons.append(Button(world.buttons_info[i][0],world.buttons_info[i][1],world.buttons_info[i][2],world.buttons_info[i][3],world.buttons_info[i][4],world.buttons_info[i][5],world.buttons_info[i][6],world.buttons_info[i][7]))
        
    print("test9")
    for i in range(len(world.strings_info)):
        world.strings.append(String(world.strings_info[i][0],world.strings_info[i][1],world.strings_info[i][2],world.strings_info[i][3],world.strings_info[i][4]))
        #print(world.strings_info[i][0],world.strings_info[i][1],world.strings_info[i][2],world.strings_info[i][3],world.strings_info[i][4])


    world.leaderboard_background = [ ]
    print("test10")
    for i in range(500):
        world.leaderboard_background.append(Background(world))
    print("startWorld fully loaded")

def updateWorld(world):
    onMousePress(clickDetect)
    if world.screen == "save":
        onAnyKeyPress(Save)
    if world.screen == "game":
        if world.mode == "hard":
            if world.end - world.start > world.timeLimit: 
                world.game.fail(world)
    world.end = time.time()
    if world.hack == True:
        if world.screen == "game":
            world.game.success(world)
    
    if world.bigX == True:
        if world.bigXscale > 0.5:
            world.bigXscale -= 0.1 
        else:
            world.bigX = False
            world.bigXscale = 5


def drawWorld(world):
    if world.draw == True:
        if world.bigX == True:
            drawImage(world.heart,world.windowWidth / 2,world.windowHeight / 2,scale=world.bigXscale)
        if world.screen == "fail":
            if world.error == True:
                at_w, at_h = sizeString("Error: Score is too low to save ",40)
                drawString("Error: Score is too low to save", 50 / 100 * world.windowWidth - at_w / 2,50 / 100 * world.windowHeight - at_h / 2,size=40,color="red")
        if world.screen == "save":
            drawString(listToString(world.save_name),alignTextX(listToString(world.save_name),70,50),alignTextY(listToString(world.save_name),70,50),70)
        if world.screen == "leaderboard":
            for i in world.leaderboard_background:
                i.drawImg()
                fillRectangle(world.windowWidth / 2 - 200, 0 + 35, 400,800,"white")
            for i in range(1,10):
                drawLine(world.windowWidth / 2 - 200,i * 80 + 35,world.windowWidth / 2 + 200,i * 80 + 35)
            if world.modelb == "easylb":
                for i in range(len(world.easy_names)):
                    drawString(world.easy_names[i], world.windowWidth / 2 - 170, i * 80 + 40 - 10 + 35, 40 )
                    drawString(world.easy_scores[i], world.windowWidth / 2 + 150, i * 80 + 40 - 10 + 35, 40 )
            if world.modelb == "normallb":
                for i in range(len(world.normal_names)):
                    drawString(world.normal_names[i], world.windowWidth / 2 - 170, i * 80 + 40 - 10 + 35, 40 )
                    drawString(world.normal_scores[i], world.windowWidth / 2 + 150, i * 80 + 40 - 10 + 35, 40 )
            if world.modelb == "hardlb":
                for i in range(len(world.hard_names)):
                    drawString(world.hard_names[i], world.windowWidth / 2 - 170, i * 80 + 40 - 10 + 35, 40 )
                    drawString(world.hard_scores[i], world.windowWidth / 2 + 150, i * 80 + 40 - 10 + 35, 40 )
        
        for i in world.buttons:
            i.drawButton(world)
        print("buttons loaded")
        
        for i in world.strings:
            i.drawString(world)
        print("strings loaded")
        
        world.game.drawImages(world)
        
        world.game.hack(world)
        if world.screen == "game":
            if world.mode == "hard":
                drawString(round(world.end - world.start,2),world.windowWidth / 2 - 60, 120,100)
        if world.screen == "fail":
            drawString(world.score,alignTextX(world.score,150,50),alignTextY(world.score,150,35),150)
runGraphics(startWorld, updateWorld, drawWorld,)
