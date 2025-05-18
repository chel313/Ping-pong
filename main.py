from pygame import *

window = display.set_mode((700,500))
background = transform.scale(image.load("3773.jpg"),(700,500))
font.init()
font1 = font.Font(None, 72)
lose1 = font1.render("Player 1 lose",True,(180,0,0))
lose2 = font1.render("Player 2 lose",True,(180,0,0))

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
        if k_p[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if k_p[K_s] and self.rect.y < 450:
            self.rect.y += self.speed
    
    def update_r(self):
        k_p = key.get_pressed()
        if k_p[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if k_p[K_DOWN] and self.rect.y < 450:
            self.rect.y += self.speed

r1 = Player("Rocketka-Photoroom.png",0,250,3,100,100)
r2 = Player("Rocketka-Photoroom.png",600,250,3,100,100)

ball = GameSprite("mc-Photoroom.png",350,250,2,50,50)

speed_x = 2
speed_y = 2

finish = False
game = True 
while game:

    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background,(0,0))
        ball.recet()
        r1.recet()
        r1.update_l()
        r2.recet()
        r2.update_r()

        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y > 450 or ball.rect.y < 0:
            speed_y *= -1
        
        if sprite.collide_rect(r1,ball) or sprite.collide_rect(r2,ball):
            speed_x *= -1


        if ball.rect.x < 0:
            finish = True  
            window.blit(lose1,(200,230))
        if ball.rect.x > 700:
            finish = True
            window.blit(lose2,(200,230))

    display.update()
