import pygame, sys
import os
import random
from button import Button

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
os.chdir(os.path.dirname(os.path.abspath(__file__)))
pygame.init()
size = (800,500)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
background_img=pygame.image.load('./assets/fondo2.png').convert()
flowerNum = 0
beesNum = 0
flowerInput = ''
beesInput = ''
otherPolinInput = ''
input_rect = pygame.Rect(200,200,142,32)
input_color = pygame.Color('lightskyblue3')
def get_font(size):
    return pygame.font.Font('./assets/font.ttf',size=size)


class Flower(pygame.sprite.Sprite):
    def __init__(self, name):
        super().__init__()
        self.image = pygame.image.load("./assets/flor.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.wasPolin = False
        self.isTaked = False
        self.name = name

    def setRandomFlower(self):
        #220490430623
        self.rect.x = random.randrange(220,623,32)
        self.rect.y = random.randrange(430,490,32)

    def getWasPolin(self):
        return self.wasPolin
    def changePolin(self):
        if self.wasPolin:
            self.wasPolin = False
        else:
            self.wasPolin = True

class Bee(pygame.sprite.Sprite):
    def __init__(self,name):
        super().__init__()
        self.image = pygame.image.load("./assets/abeja.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.isPoli = False
        self.name = name
        self.flowerSelect = None
    def changeIsPoli(self):
        if self.isPoli:
            self.isPoli = False
        else:
            self.isPoli = True
    def getIsPoli(self):
        return self.isPoli
            
    def findAFlower(self,flower:Flower):
        
        if self.rect.x < flower.rect.x:
            self.rect.x += 1
        elif self.rect.x > flower.rect.x:
            self.rect.x -= 1
        
        if self.rect.y < flower.rect.y:
            self.rect.y += 1
        elif self.rect.y > flower.rect.y:
            self.rect.y -= 1
    
    def moveToCor(self, x:int, y:int):
        
        if self.rect.x < x:
            self.rect.x += 1
        elif self.rect.x > x:   
            self.rect.x -= 1
        
        if self.rect.y < y:
            self.rect.y += 1
        elif self.rect.y > y:
            self.rect.y -= 1

class Inputs():
    def __init__(self,pos, color,font,text_input = '', height = 0, width = 0, isCenter = False, isInput = False, inputColor = 'lightskyblue3'):
        self.x = pos[0]
        self.y = pos[1]
        self.h = height
        self.w = width
        self.color = color
        self.font = font
        self.isCenter = isCenter
        self.isInput = isInput
        self.inputColor = inputColor
        self.text_input = text_input
        self.text = self.font.render(self.text_input,True,color)
        self.inputRect = pygame.Rect(self.x,self.y,self.w,self.h)
        self.isModiText = False
    def update(self, screen):
        if self.isInput:
            pygame.draw.rect(screen,self.inputColor,self.inputRect,2)
            self.text = self.font.render(self.text_input,True,self.color)
            screen.blit(self.text,(self.inputRect.x + 5, self.inputRect.y + 5))
            self.inputRect.w = max(100, self.text.get_width() +10)
        if self.isCenter:
            screen.blit(self.text,self.text.get_rect(center=(self.x,self.y)))
    def getRect(self):
        return self.inputRect
def beesPoliAnimation(flower_list, bees_list):
    for f in flower_list:
            if not f.wasPolin:
                for b in bees_list:
                    if not b.isPoli:
                        if b.flowerSelect is not None:
                            if b.flowerSelect == f.name:
                                if b.rect.x == f.rect.x and b.rect.y == f.rect.y:
                                    b.isPoli = True
                                    f.wasPolin = True
                                else:
                                    b.findAFlower(f)
                        else:
                            if not f.isTaked:
                                b.flowerSelect = f.name
                                f.isTaked = True
                            
                    else:
                        if b.rect.x == 190 and b.rect.y == 50:
                            b.isPoli = False
                            b.flowerSelect = None
                        else:
                            b.moveToCor(x=190,y=50)
            else:
                aux = 0
                for f2 in flower_list:
                    if f2.wasPolin:
                        aux+=1
                if aux == len(flower_list):
                    for b in bees_list:
                        b.moveToCor(x=190,y=50)
      
        
def play(numFlowers,numberBees,numberAnotherInsect):
    
    panal_img = pygame.image.load('./assets/panal.png').convert()
    panal_img.set_colorkey([0,0,0])
    running = True
    flower_list = []
    all_sprites = pygame.sprite.Group()
    bees_list = []
    
    for i in range(numFlowers):
        flower = Flower(name=i)
        flower.setRandomFlower()
        flower_list.append(flower)
        all_sprites.add(flower)
    for i in range(numberBees):
        bee = Bee(name=i)
        bee.rect.x = 190
        bee.rect.y = 50
        bees_list.append(bee)
        all_sprites.add(bee)
    
    while running:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                running = False
                
        beesPoliAnimation(flower_list, bees_list)
        screen.fill("black")

        screen.blit(background_img, [0,0])
        screen.blit(panal_img,[190, 50])
        all_sprites.draw(screen)

        #Actualiza pantalla
        pygame.display.flip()
        clock.tick(60)
    sys.exit()
def middleware(numFlowers, numberBees, numberAnotherInsect):
    if  numFlowers:
        numFlowers = int(numFlowers)
    else:
        numFlowers = random.randint(1,10)
        
    if numberBees:
        numberBees = int(numberBees)
    else:
        numberBees = random.randint(0,10)
    if numberAnotherInsect:
        numberAnotherInsect = int(numberAnotherInsect)
    else:
        numberAnotherInsect = 0
    
    if numberBees == 0 and numberAnotherInsect == 0:
        if random.randint(1,2) == 1:
            numberBees = 1
        else:
            numberAnotherInsect = 1
    play(numFlowers,numberBees,numberAnotherInsect)
def form():
    font = get_font(12)
    input_rect.x = 230
    input_rect.y = 125
    title = Inputs((400,50),WHITE,get_font(18),text_input="Ingrese los siguientes datos",isCenter= True)
    flowerText = Inputs((400,100),WHITE,font,"Ingrese la cantidad de flores",isCenter=True)
    flowerInputText = Inputs((230,115),WHITE,font,height=32,width=142,isInput=True)
    beeText = Inputs((400,175),WHITE,font,"Ingrese la cantidad de abejas",isCenter=True)
    beeInput = Inputs((230,215),WHITE,font,height=32,width=142,isInput=True)
    insectText = Inputs((400,275),WHITE,font,"Ingrese la cantidad de abejas",isCenter=True)
    insectInput = Inputs((230,300),WHITE,font,height=32,width=142,isInput=True)
    while True:
        NEXT_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(630, 430), 
                            text_input="Siguiente", font=get_font(12), base_color="#d7fcd4", hovering_color="White")
        BACK_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(150, 430), 
                            text_input="Atras", font=get_font(12), base_color="#d7fcd4", hovering_color="White")
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if flowerInputText.inputRect.collidepoint(event.pos):
                    flowerInputText.isModiText = True
                    beeInput.isModiText = False
                    insectInput.isModiText = False
                      
                elif beeInput.inputRect.collidepoint(event.pos):
                    flowerInputText.isModiText = False
                    beeInput.isModiText = True
                    insectInput.isModiText = False
                elif insectInput.inputRect.collidepoint(event.pos):
                    flowerInputText.isModiText = False
                    beeInput.isModiText = False
                    insectInput.isModiText = True
                
                if NEXT_BUTTON.checkForInput(pygame.mouse.get_pos()):
                    middleware(flowerInputText.text_input, beeInput.text_input, insectInput.text_input)
                elif BACK_BUTTON.checkForInput(pygame.mouse.get_pos()):
                    main_menu()
                                
            if flowerInputText.isModiText:
                print("entre a este if")
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        if flowerInputText.text_input:
                            flowerInputText.text_input = flowerInputText.text_input[:-1]
                    elif event.key == pygame.K_RETURN:
                        flowerInputText.isModiText = False
                    else:
                        if len(flowerInputText.text_input) < 20 and event.key != pygame.K_RETURN:
                            flowerInputText.text_input += event.unicode
            elif beeInput.isModiText:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        if beeInput.text_input:
                            beeInput.text_input = beeInput.text_input[:-1]
                    elif event.key == pygame.K_RETURN:
                        beeInput.isModiText = False
                    else:
                        if len(beeInput.text_input) < 20 and event.key != pygame.K_RETURN:
                            beeInput.text_input += event.unicode
            elif insectInput.isModiText:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        if insectInput.text_input:
                            insectInput.text_input = insectInput.text_input[:-1]
                    elif event.key == pygame.K_RETURN:
                        insectInput.isModiText = False
                    else:
                        if len(insectInput.text_input) < 20 and event.key != pygame.K_RETURN:
                            insectInput.text_input += event.unicode
        screen.fill("black")
        
        for button in [NEXT_BUTTON, BACK_BUTTON]:
            button.changeColor(pygame.mouse.get_pos())
            button.update(screen)
        
        for inputText in [title,flowerText,flowerInputText,beeText,beeInput, insectText, insectInput]:
            inputText.update(screen)
        
        pygame.display.flip()
        clock.tick(60)     
def main_menu():
    while True:
        screen.fill("black")
        screen.blit(background_img,[0,0])
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        MENU_TEXT = get_font(26).render("SIMULACION DE POLINIZADORES", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(400, 100))
        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(400, 200), 
                            text_input="INICIAR", font=get_font(26), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(400, 300), 
                            text_input="SALIR", font=get_font(30), base_color="#d7fcd4", hovering_color="White")
        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    #play()
                    form()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
       
if __name__=="__main__":
    main_menu()