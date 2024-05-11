from pygame import *

window = display.set_mode((700,500))
display.set_caption('Пинг-Понг')
back = (133,122,222)
window.fill(back)
game = True 
finish = False
font.init()
font = font.Font(None,70)
lose1 = font.render('You lose',True,(44,55,66))
lose2 = font.render('You lose',True,(44,55,66))
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,size_x,size_y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(size_x,size_y))
        self.player_speed = player_speed
        self.size_x = size_x
        self.size_y = size_y
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(GameSprite):
    derection = 'left'
    derection = 'right'
    def updatel(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.player_speed
        if keys[K_DOWN] and self.rect.y < (700 - 5 - self.size_y):
            self.rect.y += self.player_speed
    def updater(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.player_speed
        if keys[K_s] and self.rect.y < (700 - 5 - self.size_y):
            self.rect.y += self.player_speed
player = Player('ракетка.png',620,440,50,100,5)
player1 = Player('ракетка.png',10,440,50,100,5)
ball = GameSprite('product_14.png',250,220,30,30,5)
speed_x = 3
speed_y = 3
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.fill(back)
        
        player.updatel()
       
        player1.updater()
        
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if sprite.collide_rect(player,ball) or sprite.collide_rect(player1,ball):
            speed_y *= -1
            speed_x *= -1
        if ball.rect.y > 500-50 or ball.rect.y < 0:
            speed_y *= -1
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1,(200,200))
            game = True
        if ball.rect.x > 700:
            finish = True
            window.blit(lose2,(200,200))
            game = True
        player.reset()
        player1.reset()
        ball.reset()
        display.update()
    time.delay(50)

