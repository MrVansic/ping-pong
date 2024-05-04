from pygame import *
window = display.set_mode((700,500))
display.set_caption('Пинг-Понг')
back = (133,122,222)
window.fill(back)
game = True 
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.fill(back)
        display.update()
    time.delay(50)

