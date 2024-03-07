from typing import Any
from pygame import *

window = display.set_mode((500,400))
display.set_caption("ping-pong")

clock = time.Clock()
FPS = 60
run=True
win_width=500
win_height=500
speed_x=5
speed_y=5
back=(0,0,0)

font.init()
text = font.SysFont("Arial", 50)

img_pl="player.png"
img_ball="ball.png"

class GameSprite(sprite.Sprite):
    #конструктор класу
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        #кожен спрайт повинен зберігати властивість rect - прямокутник, в який він вписаний
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 325:
            self.rect.y += self.speed

player=Player(img_pl,20,200,20,75,5)

class Ball(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, speed_x,speed_y):
        sprite.Sprite.__init__(self)
        
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed_x=speed_x
        self.speed_y=speed_y
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def update(self):

        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.top <= 0 or self.rect.bottom >= 400:
            self.speed_y = -self.speed_y
        if self.rect.left <= 0 or self.rect.right >= 500:
            self.speed_x = -self.speed_x
        if self.rect.colliderect(player):
            self.speed_y = -self.speed_y
            self.speed_x = -self.speed_x
        
      
ball=Ball(img_ball,200,200,20,20,5,5)

class Enemy(GameSprite):
    def update(self):
        self.rect.y = ball.rect.y


enemy=Enemy(img_pl,480,200,20,75,50)

while run:
    
    for e in event.get():
        if e.type == QUIT:
            run= False
    
    player.update()
    enemy.update()
    ball.update()

    if ball.rect.x == 0:
        message = text.render("You lose!", True, (255, 0, 0))
        window.blit(message, (150, 150))
        display.update()
        time.delay(2500)
        run = False
    elif ball.rect.y == 500:
        message = text.render("You win!", True, (0, 255, 0))
        window.blit(message, (150, 150))
        display.update()
        time.delay(2500)
        run = False
    
    window.fill(back)
    window.blit(ball.image, ball.rect)
    window.blit(player.image, player.rect)
    window.blit(enemy.image, enemy.rect)

    display.update()
    clock.tick(FPS)
