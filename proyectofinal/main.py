import pygame, sys
import os
import random


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
os.chdir(os.path.dirname(os.path.abspath(__file__)))


        

class Flower(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("flor.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.wasPolin = False

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
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("abeja.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
    
    def findFlower(self, flower:Flower):
        print(flower.rect.x)
        if self.rect.x == flower.rect.x:
            self.rect.x = self.rect.x
        elif self.rect.x < flower.rect.x:
            self.rect.x += 1
        elif self.rect.x > flower.rect.x:
            self.rect.x -= 1

        if self.rect.y == flower.rect.y:
            self.rect.y = self.rect.y
        elif self.rect.y < flower.rect.y:
            self.rect.y += 1
        elif self.rect.y > flower.rect.y:
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
    flower_list = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    for i in range(5):
        flower = Flower()
        flower.setRandomFlower()
        flower_list.add(flower)
        all_sprites.add(flower)
    
    bee = Bee()
    all_sprites.add(bee)
    
    while running:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                running = False
        
        bee.rect.x = 190
        bee.rect.y = 50
        bee.findFlower(flower=flower)
        
        all_sprites.update()
        #Color de fondo
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