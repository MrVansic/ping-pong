from pygame import *

window = display.set_mode((700,500))
display.set_caption('Пинг-Понг')
back = (133,122,222)
window.fill(back)
game = True 
finish = False
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
player = Player('ракетка.jpg',10,440,50,50,5)
player1 = Player('ракетка.jpg',10,440,50,50,5)
sprite = GameSprite('product_14.png',10,440,50,50,5)
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.fill(back)
        player.reset()
        player.updatel()
        player1.reset()
        player1.updater()
        sprite.reset()
        
        display.update()
    time.delay(50)

