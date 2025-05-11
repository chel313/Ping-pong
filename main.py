from pygame import *

window = display.set_mode((700,500))
background = transform.scale(image.load("3773.jpg"),(700,500))
ball = transform.scale(image.load("mc.jpg"),(50,50))


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed,size_x,size_y):
        super(). __init__()
        self.image = transform.scale(image.load(player_image),(size_x,size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def recet(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        k_p = key.get_pressed()
        if k_p[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if k_p[K_DOWN] and self.rect.y < 450:
            self.rect.y += self.speed
    
    def update_r(self):
        k_p = key.get_pressed()
        if k_p[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if k_p[K_s] and self.rect.y < 450:
            self.rect.y += self.speed

r1 = Player("Rocketka.jpg",450,250,3,100,100)
r2 = Player("Rocketka.jpg",130,250,3,100,100)

# Rockets = sprite.Group()
# Rockets.add(r1)
# Rockets.add(r2)


game = True 
while game:
    window.blit(background,(0,0))
    window.blit(ball,(350,250))
    r1.recet()
    r1.update_l()
    r2.recet()
    r2.update_r()
    for e in event.get():
        if e.type == QUIT:
            game = False

    

    display.update()