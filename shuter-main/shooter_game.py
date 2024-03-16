#Створи власний Шутер!
import random
from pygame import *

window = display.set_mode((700, 500))

bg = image.load("galaxy.jpg")
bg = transform.scale(bg, (700, 500))

game = True
clock = time.Clock()

mixer.init()
space = mixer.Sound("space.ogg")
space.play()

class Hero(sprite.Sprite):
    def __init__ (self, x, y, width, height, speed, img_name="rocket.png"):
        super().__init__()

        self.image = image.load(img_name)
        self.image = transform.scale(self.image, (width, height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y 
        
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
        
class Player(Hero):
    def move (self):
        keys = key.get_pressed()
        if keys [K_a] and self.rect.x > 5:
            self.rect.x -= self.speed

        if keys [K_d] and self.rect.x < 700:
            self.rect.x += self.speed

def fire(self):
    bullet = Bullet(self.rect,centerx, self.rect/y, 10, 10, 10, 'bullet.png')

counter = 0
bullets = []

class Enemy (Hero):
    def move(self):
        self.rect.y += self.speed
        global counter
        if self.rect.y > 560:
            counter += 1
            self.rect.x = random.randint(50, 565)
            self.speed = random.randint(2,6)
            self.rect.y = -100
        


rocket = Player(350,400,50,100,5)

enemys = []
for i in  range(5):
    enemy1 = Enemy (random.randint(50, 565), -100, 100, 40, random.randint(1,4), "ufo.png")
    enemys.append(enemy1)

font.init()

font1 = font.Font(None, 40)

while game:
    window.blit(bg, (0,0))
    print(counter)
    window.blit(font1.render(f"Лічильник: {counter}",True, (255,255,255)), (0,0))
    for i in enemys:
        i.reset()
        i.move()

    for e in event.get():
        if e.type == QUIT:
            game = False

    enemy1.reset()
    enemy1.move()
    rocket.reset()
    rocket.move()
    clock.tick(60)
    display.update()
