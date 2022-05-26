from pygame import *

#игроавя сцена:
back = (200, 255, 255) #цвет фона (background)
win_width = 600
win_height = 500
win_display = display.set_mode((win_width, win_height))
win_display.fill(back)

#создание игрвого класа
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_width, player_height):
        super().__init__()
        self.player = player_image
        self.width = player_width
        self.height = player_height
        self.image = transform.scale(image.load(self.player), (self.width, self.height)) 
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = player_speed

    def reset(self):
        win_display.blit(self.image, (self.rect.x, self.rect.y))
    
class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        elif keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        elif keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

finish = False
clock = time.Clock()
game = True
FPS = 60



racket1 = Player('racket.png', 30, 200, 4, 25, 120)
racket2 = Player('racket.png', 550, 200, 4, 25, 120)
ball = GameSprite('ball.png', 200, 200, 4, 50, 50)

font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE!',  True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!',  True, (180, 0, 0))


speed_x = 3 
speed_y = 3
 
while game:
    for e in event.get():
        if e.type == QUIT: 
            game = False

    if finish != True: 
        win_display.fill(back)
        racket1.update_r()
        racket2.update_l()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1 
            speed_y *= 1


        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1 


        if ball.rect.x < 0:
            finish = True
            win_display.bilt(lose1, (200, 200))
            game_over = True


        if ball.rect.x > win_width:
            finish = True
            win_display.blit(lose2, (200, 200))
            game_over = True

        racket1.reset()
        racket2.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)












