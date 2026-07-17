from pygame import *

back = (135, 206, 235)
window = display.set_mode((700, 500))
display.set_caption("Шутер")
clock = time.Clock()
class GameSprite(sprite.Sprite):
    def __init__(self, image_p, speed, x, y, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(image_p),(size_x, size_y))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_l(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if key_pressed[K_s] and self.rect.y < 375:
            self.rect.y += self.speed
    def update_r(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if key_pressed[K_DOWN] and self.rect.y < 375:
            self.rect.y += self.speed
racker1 = Player("racket1.png", 3, 20, 300, 30, 125)
racker2 = Player("racket2.png", 3, 665, 300, 30, 125)
finish = False
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill(back)
        racker1.update_l()
        racker1.reset()
        racker2.update_r()
        racker2.reset()
        display.update()
        clock.tick(50)