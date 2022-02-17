###This is Legacy code... do not use 


from graphics import *
import random 
import time

makeGraphicsWindow(800, 600)

############################################################

# this function is called once to initialize your new world

 

def startWorld(world):


#all painting names 
    world.paintingNames = ["Otahi","The Scream","Garçon à la pipe","Twelve Landscape Screens","Bal du moulin de la Galette","Three Studies of Lucian Freud","Portrait of Adele Bloch-Bauer II","Le Rêve","Portrait of Adele Bloch-Bauer I","Masterpiece","Woman III","No. 5","Nu couché","Les Femmes d'Alger", "No. 6 (Violet, Green and Red)","Salvator Mundi","Interchange", "The Card Players","Nafea Faa Ipoipo", "Number 17A","Wasserschlagen II"]
#loads in all images
    world.wassershlagenII = loadImage("Wasserschlagen II.jpg")
    world.number17A = loadImage("Number 17A.jpg")
    world.nafeaFaaIpoipo = loadImage("Nafea Faa Ipoipo.jpg")
    world.theCardPlayers = loadImage("The Card Players.jpg")
    world.interchange = loadImage("Interchange.jpg")
    world.salvatorMundi = loadImage("Salvator Mundi.jpg")
    world.no6 = loadImage("No. 6 (Violet, Green and Red).jpg")
    world.lesFemmesDAlger = loadImage("Les Femmes d'Alger.jpg")
    world.nuCouche = loadImage("Nu couché.jpg")
    world.no5 = loadImage("No. 5.jpg")
    world.womanIII = loadImage("Woman III.jpg")
    world.masterpiece = loadImage("Masterpiece.jpg")
    world.portraitOfAdeleBlochBauerI = loadImage("Portrait of Adele Bloch-Bauer I.jpg")
    world.leReve = loadImage("Le Rêve.jpg")
    world.portraitOfAdeleBlochBauerII = loadImage("Portrait of Adele Bloch-Bauer II.jpg")
    world.threeStudiesOfLucianFreud = loadImage("Three Studies of Lucian Freud.jpg")
    world.balDuMoulinDeLaGalette = loadImage("Bal du moulin de la Galette.jpg")
    world.twelvelandscapescreens = loadImage("Twelve Landscape Screens.jpg")
    world.garconALaPipe = loadImage("Garçon à la pipe.jpg")
    world.theScream = loadImage("The Scream.jpg")
    world.otahi = loadImage("Otahi.jpg")

#gets size of window
    world.sizeOfWindowX, world.sizeOfWindowY = getScreenSize()

    #game name text settings
    world.gameName = "higher or lower; art edition"
    world.gameNameColor = "black"
    world.gameNameSize = 60
    
    #game start text settings
    world.startButtonText = "start"
    world.startButtonTextColor = "black"
    world.startButtonTextSize =  88
    world.startButtonRectColor = "black"
    #dont touch
    world.gameNameWidth, world.gameNameHeight = sizeString(world.gameName, world.gameNameSize)
    world.startButtonTextWidth, world.startButtonTextHeight = sizeString(world.startButtonText, world.startButtonTextSize) 
    #game start box settings
    world.areaAroundStartBoxX = 30
    world.areaAroundStartBoxY = 15

    #dont touch
    world.startButtonRectX = world.sizeOfWindowX / 2  - (world.startButtonTextWidth / 2) - (world.areaAroundStartBoxX / 2)
    world.startButtonRectY = world.sizeOfWindowY / 2 + 50  - (world.startButtonTextHeight / 2) + (world.areaAroundStartBoxY / 2) + (world.startButtonTextHeight / 2)

    #game background hiding 
    world.leftSideColor = "white"
    world.rightSideColor = "white"
    world.leftSideOpactiy = 0
    world.rightSideOpacity = 0
	
    world.leftSide1 =world.sizeOfWindowX + 100
    world.leftSide2 = world.sizeOfWindowY + 100
    world.leftSide3 =world.sizeOfWindowX + 100
    world.leftSide4 = world.sizeOfWindowY + 100

    world.rightSide1 = world.sizeOfWindowX + 100
    world.rightSide2 = world.sizeOfWindowY + 100
    world.rightSide3 = world.sizeOfWindowX + 100
    world.rightSide4 = world.sizeOfWindowY + 100
    world.compare1ImageX = world.sizeOfWindowX + 100
    world.compare1ImageY = world.sizeOfWindowY + 100
    world.painting1Name = random.choice(world.paintingNames)

    #sets variable defaults
    world.compare1Image = loadImage("Wasserschlagen II.jpg")
    world.compare1Price = paintingCost(world.painting1Name,world)
    world.compare1Artist = artistName(world.painting1Name, world)

    artistName(world.painting1Name, world)     
    variableName(world.painting1Name, world)
    paintingCost(world.painting1Name,world)
    world.compare1ImageScale = 1
    world.compare1TextName = " "
    world.compare1TextNameX = world.sizeOfWindowX + 100
    world.compare1TextNameY = world.sizeOfWindowY + 100 
    world.compare1TextNameSize = 20
    
    world.compare1TextArtist = " "
    world.compare1ImageTextArtistSizeW,world.compare1ImageTextArtistSizeH = sizeString(world.compare1TextArtist)
    world.compare1TextArtistX = 200 - world.compare1ImageTextArtistSizeW / 2
    world.compare1TextArtistY = 400
    world.compare1TextArtistSize = 30 

    world.compare1TextPrice = " "
    world.compare1ImageTextPriceSizeW,world.compare1ImageTextPriceSizeH = sizeString(world.compare1TextPrice)
    world.compare1TextPriceX = 200 - world.compare1ImageTextPriceSizeW / 2
    world.compare1TextPriceY = 420
    world.compare1TextPriceSize = 30


    #painting 2 
    world.compare2Painting = " " 
    world.compare2Image = world.paintingNameVar
    world.compare2ImageHeight = getImageHeight(world.compare2Image)
    world.compare2ImageWidth = getImageWidth(world.compare2Image)
    world.compare2ImageX = world.sizeOfWindowX + 1000
    world.compare2ImageY = world.sizeOfWindowY + 1000
    world.compare2ImageScale = 1 
    world.compare2TextName = " "
    world.compare2ImageTextNameSizeW,world.compare2ImageTextNameSizeH = sizeString(world.compare1TextName)
    world.compare2TextNameX = 600 - world.compare2ImageTextNameSizeW / 2
    world.compare2TextNameY = 350 
    world.compare2TextNameSize = 30
    world.compare2Price = world.paintingPrice

 
    #higher text
    world.higherButtonText = "  "
    world.higherButtonTextSizeW, world.higherButtonTextSizeH = sizeString(world.higherButtonText)
    world.higherButtonTextX =world.sizeOfWindowY + 100
    world.higherButtonTextY = world.sizeOfWindowY + 100

    #higher box 
    world.higherButtonRectX = world.sizeOfWindowX + 100
    world.higherButtonRectY = world.sizeOfWindowY + 100

    #lower text
    world.lowerButtonText = "Lower"
    world.lowerButtonTextSizeW,world.lowerButtonTextSizeH = sizeString(world.lowerButtonText)
    world.lowerButtonTextX = world.sizeOfWindowX + 100
    world.lowerButtonTextY = world.sizeOfWindowY + 100 

    #higher box 
    world.lowerButtonRectX = world.sizeOfWindowX + 100
    world.lowerButtonRectY =  world.sizeOfWindowY + 100 

    #scores 
    world.score = 0
    world.scoreHigh = 0 
#-----------------------------------------------

#This function is for the main menu and gets the first "control" painting 
def startScreen(world, mouseX, mouseY, button):

    if button == 1:
            if mouseX > world.startButtonRectX and mouseX < world.startButtonRectX + world.startButtonTextWidth + world.areaAroundStartBoxX:
                if button == 1 and mouseY > world.startButtonRectY and mouseY < world.startButtonRectY + world.startButtonTextHeight + world.areaAroundStartBoxY:
                    #sif world.startButtonTextColor == "black":
                        #gets rid of start screen text
                        world.gameNameColor = "White"
                        world.startButtonTextColor = "White"
                        world.startButtonRectColor = "White"
                        world.leftSideColor = "lightblue"
                        world.rightSideColor = "green"
                        #enables background 
                        world.leftSide1 = 0 
                        world.leftSide2 = 0
                        world.leftSide3 = 400
                        world.leftSide4 = 800
                        world.rightSide1 = 400
                        world.rightSide2 = 0 
                        world.rightSide3 = 400
                        world.rightSide4 = 800
                        #gets random image
                        world.compare1Painting = random.choice(world.paintingNames)
                        #calling dicts                     
                        artistName(world.compare1Painting, world)     
                        variableName(world.compare1Painting, world)
                        paintingCost(world.compare1Painting,world)
                        world.compare1Price = world.paintingPrice
                        #gets variable name for image 
                        world.compare1Image = world.paintingNameVar
                        #gets random images' height and width for later use
                        world.compare1ImageHeight = getImageHeight(world.compare1Image)
                        world.compare1ImageWidth = getImageWidth(world.compare1Image)
                        
                        #image scaler so all photos are not wider than 150pixels (goes all wonky if wider than 150px)
                        if world.compare1ImageWidth > 150:
                            world.compare1ImageScale =  150 / world.compare1ImageWidth 
                        else: 
                            world.compare1ImageScale = 1 
                        
                        world.compare1ImageX = world.sizeOfWindowX / 2 - 50 - world.compare1ImageWidth * (abs(world.compare1ImageScale))
                        world.compare1ImageY = 200

                        #gets & prints name of left side painting
                        world.compare1TextName = world.compare1Painting
                        world.compare1ImageTextNameSizeW,world.compare1ImageTextNameSizeH = sizeString(world.compare1TextName)
                        world.compare1TextNameX = 200 - world.compare1ImageTextNameSizeW / 2
                        world.compare1TextNameY = 350 
                        #size of font; default 30... changing this value will require a change in the Y value 
                        world.compare1TextNameSize = 30 

                        #gets & prints artist of left side painting
                        world.compare1TextArtist = world.paintingNameArtist
                        world.compare1ImageTextArtistSizeW,world.compare1ImageTextArtistSizeH = sizeString(world.compare1TextArtist)
                        world.compare1TextArtistX = 200 - world.compare1ImageTextArtistSizeW / 2
                        world.compare1TextArtistY = 380

                        #size of font; default 30... changing this value will require a change in the Y value 
                        world.compare1TextArtistSize = 30

                        #gets & prints price of left side painting
                        #https://stackoverflow.com/questions/1823058/how-to-print-number-with-commas-as-thousands-separators
                        world.compare1TextPrice = f"{world.paintingPrice:,}"
                        world.compare1ImageTextPriceSizeW,world.compare1ImageTextPriceSizeH = sizeString(world.compare1TextPrice)
                        world.compare1TextPriceX = 200 - world.compare1ImageTextPriceSizeW / 2
                        world.compare1TextPriceY = 410
                        #size of font; default 30... changing this value will require a change in the Y value 
                        world.compare1TextPriceSize = 30
                        comparisonPaintingGeneration(world)
    
    if button == 1:
        if mouseX > world.higherButtonRectX and mouseX < world.higherButtonRectX + world.higherButtonTextSizeW + 20:
            if button == 1 and mouseY > world.higherButtonRectY and mouseY <  world.higherButtonRectY + world.higherButtonTextSizeH + 15:
                if world.compare2Price <= world.compare1Price: 
                    world.score += 1
                    world.compare1Image = world.compare2Image
                    #gets random images' height and width for later use
                    world.compare1ImageHeight = getImageHeight(world.compare2Image)
                    world.compare1ImageWidth = getImageWidth(world.compare2Image)
                    world.compare1TextArtist = world.compare2Artist
                    world.compare1TextName = world.compare2Painting
                    world.compare1TextPrice = f"{world.compare2Price:,}"
                    world.compare1ImageTextPriceSizeW,world.compare1ImageTextPriceSizeH = sizeString(world.compare1TextPrice)
                    world.compare1ImageTextArtistSizeW,world.compare1ImageTextArtistSizeH = sizeString(world.compare1TextArtist)
                    world.compare1ImageTextNameSizeW,world.compare1ImageTextNameSizeH = sizeString(world.compare1TextName)
                    world.compare1TextNameX = 200 - world.compare1ImageTextNameSizeW / 2
                    world.compare1TextArtistX = 200 - world.compare1ImageTextArtistSizeW / 2
                    #image scaler so all photos are not wider than 150pixels (goes all wonky if wider than 150px)
                    if world.compare1ImageWidth > 150:
                        world.compare1ImageScale =  150 / world.compare1ImageWidth 
                    else: 
                           world.compare1ImageScale = 1 
                        
                    world.compare1ImageX = world.sizeOfWindowX / 2 - 50 - world.compare1ImageWidth * (abs(world.compare1ImageScale))
                    world.compare1ImageY = 200 
                    comparisonPaintingGeneration(world)
    if button == 1:
        if mouseX > world.lowerButtonRectX and mouseX < world.lowerButtonRectX + world.lowerButtonTextSizeW + 20:
            if button == 1 and mouseY > world.lowerButtonRectY and mouseY <  world.lowerButtonRectY + world.lowerButtonTextSizeH + 15:
                if world.compare2Price >= world.compare1Price: 
                    world.score += 1
                    world.compare1Image = world.compare2Image
                    #gets random images' height and width for later use
                    world.compare1ImageHeight = getImageHeight(world.compare2Image)
                    world.compare1ImageWidth = getImageWidth(world.compare2Image)
                    world.compare1TextArtist = world.compare2Artist
                    world.compare1TextName = world.compare2Painting
                    world.compare1TextPrice = f"{world.compare2Price:,}"
                    world.compare1ImageTextPriceSizeW,world.compare1ImageTextPriceSizeH = sizeString(world.compare1TextPrice)
                    world.compare1ImageTextArtistSizeW,world.compare1ImageTextArtistSizeH = sizeString(world.compare1TextArtist)
                    world.compare1ImageTextNameSizeW,world.compare1ImageTextNameSizeH = sizeString(world.compare1TextName)
                    world.compare1TextNameX = 200 - world.compare1ImageTextNameSizeW / 2
                    world.compare1TextArtistX = 200 - world.compare1ImageTextArtistSizeW / 2
                    #image scaler so all photos are not wider than 150pixels (goes all wonky if wider than 150px)
                    if world.compare1ImageWidth > 150:
                        world.compare1ImageScale =  150 / world.compare1ImageWidth 
                    else: 
                           world.compare1ImageScale = 1 
                        
                    world.compare1ImageX = world.sizeOfWindowX / 2 - 50 - world.compare1ImageWidth * (abs(world.compare1ImageScale))
                    world.compare1ImageY = 200 
                    comparisonPaintingGeneration(world)


def comparisonPaintingGeneration(world):
    world.compare2Painting = random.choice(world.paintingNames)
    variableName(world.compare2Painting, world)
    artistName(world.compare2Painting, world)     
    paintingCost(world.compare2Painting,world)
    world.compare2Image = world.paintingNameVar
    world.compare2Artist = world.paintingNameArtist
    world.compare2Price = world.paintingPrice
    world.compare2ImageHeight = getImageHeight(world.compare2Image)
    world.compare2ImageWidth = getImageWidth(world.compare2Image)
    world.compare2TextName = world.compare2Painting
    world.compare2Price = world.paintingPrice
    if world.compare2ImageWidth > 150:
        world.compare2ImageScale =  150 / world.compare2ImageWidth 
    else: 
        world.compare2ImageScale = 1 
                            
    world.compare2ImageX = world.sizeOfWindowX - 50 - world.compare2ImageWidth * (abs(world.compare2ImageScale))
    world.compare2ImageY = 200

    #text
    world.compare2ImageTextNameSizeW,world.compare2ImageTextNameSizeH = sizeString(world.compare2TextName)
    world.compare2TextNameX = 600 - world.compare2ImageTextNameSizeW / 2
    world.compare2TextNameY = 350 
    #size of font; default 30... changing this value will require a change in the Y value 
    world.compare2TextNameSize = 30 
    #higher text
    world.higherButtonText = "Higher"
    world.higherButtonTextSizeW,world.higherButtonTextSizeH = sizeString(world.higherButtonText)
    world.higherButtonTextX = 600 - world.higherButtonTextSizeW / 2 
    world.higherButtonTextY = 400 
    #lower text
    world.lowerButtonText = "Lower"
    world.lowerButtonTextSizeW,world.higherButtonTextSizeH = sizeString(world.higherButtonText)
    world.lowerButtonTextX = 600 - world.higherButtonTextSizeW / 2 
    world.lowerButtonTextY = 400 + 60

    #higher box 
    world.higherButtonRectX = 600 - world.higherButtonTextSizeW / 2 - 10
    world.higherButtonRectY =  400 - 10
    #lower box
    world.lowerButtonRectX = 600 - world.lowerButtonTextSizeW / 2 - 10
    world.lowerButtonRectY =  400 + 50

def paintingCost(painting,world):
    price = {
        "Salvator Mundi": 475400000,
        "Interchange": 328000000,
        "The Card Players": 288000000,
        "Nafea Faa Ipoipo": 229000000,
        "Number 17A": 218000000,
        "Wasserschlagen II": 204200000,
        "No. 6 (Violet, Green and Red)": 203000000,
        "Les Femmes d'Alger": 195800000,
        "Nu couché":186100000,
        "No. 5":179700000,
        "Woman III":176500000,
        "Masterpiece":174200000,
        "Portrait of Adele Bloch-Bauer I":173300000,
        "Le Rêve":172200000,
        "Portrait of Adele Bloch-Bauer II":161800000,
        "Three Studies of Lucian Freud":158200000,
        "Bal du moulin de la Galette":154700000,
        "Twelve Landscape Screens":148700000,
        "Garçon à la pipe":142700000,
        "The Scream":135200000,
        "Otahi":133300000,
    }
    if painting not in price:
        print(painting  + "is missing")
        raise Exception("Painting entry is missing from name (paintingPrice)")
    world.paintingPrice = price[painting]

def artistName(painting,world):    
    artist = {
        "Salvator Mundi": "Leonardo Da Vinci",
        "Interchange": "Willem de Kooning",
        "The Card Players": "Paul Cézanne",
        "Nafea Faa Ipoipo": "Paul Gaugin",
        "Number 17A": "Jackson Pollock",
        "Wasserschlagen II": "Gustav Klimt",
        "No. 6 (Violet, Green and Red)": "Mark Rothko",
        "Les Femmes d'Alger Version O": "Pablo Picasso",
        "Nu couché":"Amedeo Modigliani",
        "No. 5":"Jackson Pollock",
        "Woman III":"Willem de Kooning",
        "Masterpiece":"Roy Lichtenstein",
        "Portrait of Adele Bloch-Bauer I":"Gustav Klimt",
        "Le Rêve":"Pablo Picasso",
        "Portrait of Adele Bloch-Bauer II":"Gustav Klimt",
        "Three Studies of Lucian Freud":"Francis Bacon",
        "Bal du moulin de la Galette":"Pierre-Aguste Renoir",
        "Twelve Landscape Screens":"Qi Baishi",
        "Garçon à la pipe":"Pablo Picasso",
        "The Scream":"Edvard Munch",
        "Otahi":"Paul Gauguin",
        "Les Femmes d'Alger":"Eugène Delacroix",
    }
    if painting not in artist:
        print(painting + " is missing")
        raise Exception("Painting entry is missing from name (artistName)")
    world.paintingNameArtist = artist[painting]
def variableName(painting,world):
    name = {

        "Otahi":world.otahi,
        "The Scream" : world.theScream,
        "Garçon à la pipe":world.garconALaPipe,
        "Twelve Landscape Screens": world.twelvelandscapescreens,
        "Bal du moulin de la Galette":world.balDuMoulinDeLaGalette,
        "Three Studies of Lucian Freud":world.threeStudiesOfLucianFreud,
        "Portrait of Adele Bloch-Bauer II": world.portraitOfAdeleBlochBauerII,
        "Le Rêve":world.leReve,
        "Portrait of Adele Bloch-Bauer I":world.portraitOfAdeleBlochBauerI,
        "Masterpiece":world.masterpiece,
        "Woman III":world.womanIII,
        "No. 5":world.no5,
        "Nu couché":world.nuCouche,
        "Les Femmes d'Alger":world.lesFemmesDAlger,
        "No. 6 (Violet, Green and Red)":world.no6,
        "Salvator Mundi":world.salvatorMundi,
        "Interchange":world.interchange,
        "The Card Players":world.theCardPlayers,
        "Nafea Faa Ipoipo":world.nafeaFaaIpoipo,
        "Number 17A":world.number17A,
        "Wasserschlagen II":world.wassershlagenII,
    }
    if painting not in name:
        print(painting + " is missing")
        raise Exception("Painting entry is missing from name (variableName")
    world.paintingNameVar = name[painting]
    




############################################################

# this function is called every frame to update your world

 

def updateWorld(world):
    onMousePress(startScreen)

    
    
    

    
 
    

############################################################

# this function is called every frame to draw your world


def drawWorld(world):
    drawLine(0,300, 800,300, "lightblue")
    drawLine(400,0, 400, 800, "lightblue")
    drawString(world.gameName, world.sizeOfWindowX / 2 - (world.gameNameWidth / 2), world.sizeOfWindowY / 2 - (world.gameNameHeight / 2) - 150, size=world.gameNameSize, color=world.gameNameColor)
    drawRectangle(world.startButtonRectX, world.startButtonRectY,world.startButtonTextWidth + world.areaAroundStartBoxX, world.startButtonTextHeight + world.areaAroundStartBoxY, color=world.startButtonRectColor)
    drawString(world.startButtonText, world.startButtonRectX + world.areaAroundStartBoxX / 2, world.startButtonRectY + (world.areaAroundStartBoxY / 2)  , size=world.startButtonTextSize,color=world.startButtonTextColor)
    fillRectangle(world.rightSide1,world.rightSide2, world.rightSide3 , world.rightSide4 , world.rightSideColor,)
    fillRectangle(world.leftSide1,world.leftSide2, world.leftSide3, world.leftSide4, world.leftSideColor,)
    drawImage(world.compare1Image, world.compare1ImageX,world.compare1ImageY,scale=world.compare1ImageScale)
    drawString(world.compare1TextName, world.compare1TextNameX, world.compare1TextNameY, world.compare1TextNameSize)
    drawString(world.compare1TextArtist,world.compare1TextArtistX,world.compare1TextArtistY, world.compare1TextArtistSize)
    drawString(world.compare1TextPrice,world.compare1TextPriceX,world.compare1TextPriceY, world.compare1TextPriceSize)


    #img 2 
    drawString(world.compare2TextName, world.compare2TextNameX, world.compare2TextNameY, world.compare2TextNameSize)
    drawImage(world.compare2Image, world.compare2ImageX,world.compare2ImageY,scale=world.compare2ImageScale)

    #higher
    drawString(world.higherButtonText, world.higherButtonTextX,world.higherButtonTextY)
    drawRectangle(world.higherButtonRectX,world.higherButtonRectY, world.higherButtonTextSizeW + 20, world.higherButtonTextSizeH + 15 )

    drawString(world.lowerButtonText, world.lowerButtonTextX,world.lowerButtonTextY)
    drawRectangle(world.lowerButtonRectX,world.lowerButtonRectY, world.lowerButtonTextSizeW + 20, world.lowerButtonTextSizeH + 15 )

############################################################

 

runGraphics(startWorld, updateWorld, drawWorld)
