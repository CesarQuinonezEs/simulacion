import pygame, sys
import os
import random


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
os.chdir(os.path.dirname(os.path.abspath(__file__)))


        

class Flower(pygame.sprite.Sprite):
    def __init__(self, name):
        super().__init__()
        self.image = pygame.image.load("flor.png").convert()
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
        self.image = pygame.image.load("abeja.png").convert()
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
          
        
        
def main():
    pygame.init()
    size = (800,500)
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    background_img=pygame.image.load('fondo2.png').convert()
    panal_img = pygame.image.load('panal.png').convert()
    panal_img.set_colorkey([0,0,0])
    running = True
    flower_list = []
    all_sprites = pygame.sprite.Group()
    bees_list = []
    
    for i in range(5):
        flower = Flower(name=i)
        flower.setRandomFlower()
        flower_list.append(flower)
        all_sprites.add(flower)
    for i in range(3):
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
        aux = True 
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
                        else:
                            b.moveToCor(x=190,y=50)
        """
        for b in bees_list:
            if not b.isPoli:
                for f in flower_list:
                    if not f.wasPolin:
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
                else:
                    b.moveToCor(x=190,y=50)
                """
                        
        screen.fill((255,255,255))

        screen.blit(background_img, [0,0])
        screen.blit(panal_img,[190, 50])
        all_sprites.draw(screen)

        #Actualiza pantalla
        pygame.display.flip()
        clock.tick(60)
    sys.exit()



if __name__=="__main__":
    main()