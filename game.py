from pygame import *
from random import randrange,randint

L = 1920
W = 1200
window = display.set_mode((L,W))
display.set_caption("test")
fon = transform.scale(image.load("png/fon.jpg"),(L,W)) 
clock = time.Clock()
FPS = 60
step = 5
body_asteroid = ["png/астероид2.1.png","png/астероид3.1.png"]
asteroid1 = ["png/астероид2.1.png","png/астероид2.2.png"]
asteroid2 = ["png/астероид3.1.png","png/астероид3.2.png"]
patronage = list()
list_meteor = list()
num_charges = 0
stuts_fly = 6
time_metero = 0

stutus = False

    

class GameSprite(sprite.Sprite):
    def __init__(self,main_body,x_coor,y_coor,l=200,w=200,step=None):
        super().__init__()
        self.tols = main_body
        self.x = x_coor
        self.y = y_coor
        self.l = l
        self.w = w
        var2 = randint(1,2)
        if var2 == 2:
            self.step = -10
        if var2 == 1:
            self.step = 10

        if self.tols == "png/астероид2.1.png":
            self.array = asteroid1
        elif self.tols == "png/астероид3.1.png":
            self.array = asteroid2
        else:
            pass
        
        self.persona = transform.scale(image.load(self.tols),(self.l,self.w))
        self.rect = self.persona.get_rect()
    
    def DRAW(self):
        window.blit(self.persona,(self.x,self.y))
        display.update()

class player(GameSprite):   
    def update(self):
        if going[K_RIGHT]:
            self.x += step
        if going[K_LEFT]:
            self.x -= step
    
class bullet(GameSprite):
    def update(self):
        if self.y > -50:
            self.y -= step+10
        else:
            pass
    
class asteroid(GameSprite):
    
    def update(self):
        self.x += self.step
        self.y += step
    
    def style(self):
        if self.step == -10:
            self.tols = self.array[0]
        elif self.step == 10:
            self.tols = self.array[1]
        self.persona = transform.scale(image.load(self.tols),(self.l,self.w))




hero = player("png/pers.png",670,1000)
for i in range(15):
    var = randint(1,2) - 1
    angry = asteroid(body_asteroid[var],randrange(0,1820,10),-50,100,100)
    list_meteor.append(angry)



game = True
while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
        
        if i.type == MOUSEBUTTONDOWN:
            x,y = i.pos
            print(x,y)
    going = key.get_pressed()
    
    hero.DRAW()
    hero.update()   

#region движение пули(не доработано)
    if going[K_UP] and len(patronage) < 5 and stuts_fly > 5:
        pul = bullet("png/fireboll.png",hero.x+75,hero.y,50,50)
        patronage.append(pul)
    
        stuts_fly = 0
        stutus = True
    
    if stutus == True:
        stuts_fly += 1
        
        for i in patronage:
            i.DRAW()
            i.update()
            if i.y <= -50:
                num_charges += 1
        
        if num_charges == 5:
            patronage = list()
            print(patronage)
            stutus = False
            stuts_fly = 6
        else:
            num_charges = 0
#endregion 
    
    for i in list_meteor:
        i.DRAW()
        i.style()
        i.update()
        if i.x < 0:
            i.step = 10
        elif i.x > 1820:
            i.step = -10
        if i.y > 1300:
            i.x = randrange(0,1820,10)
            i.y = -50

    
    



    window.blit(fon,(0,0))
    clock.tick(FPS)
    display.update()