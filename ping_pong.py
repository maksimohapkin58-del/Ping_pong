from pygame import *
font.init()
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
ball1 = GameSprite("ball1.jpg", 3, 350, 250, 30, 30)
font1 = font.Font(None, 35)
lose1 = font1.render('PLAYER 1 LOSE', True, (180, 0, 0))
lose2 = font1.render('PLAYER 2 LOSE', True, (180, 0, 0))
speed_x = 3
speed_y = 3
finish = False
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill(back)
        ball1.rect.x += speed_x
        ball1.rect.y += speed_y
        if ball1.rect.y > 470 or ball1.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(racker1, ball1) or sprite.collide_rect(racker2, ball1):
            speed_x *= -1
        if ball1.rect.x < 0:
            finish = True
            window.blit(lose1, (300, 250))
        if ball1.rect.x > 699:
            finish = True
            window.blit(lose2, (300, 250))
        racker1.update_l()
        racker1.reset()
        racker2.update_r()
        racker2.reset()
        ball1.reset()
        display.update()
        clock.tick(50)