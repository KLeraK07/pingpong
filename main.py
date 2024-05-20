import pygame
import time
pygame.init()

back = (225, 255, 225)
mw = pygame.display.set_mode((500,500))
mw.fill(back)
clock = pygame.time.Clock()

racket_x1 = 70
racket_y1 = 200

racket_x2 = 410
racket_y2 = 200

dx = -2
dy = -2

move_Up_l = False
move_Down_l = False

move_Up_r = False
move_Down_r = False

game_over = False

class Area():
    def  __init__(self, x = 0, y = 0, widht = 10, height = 10, color = None):
        self.rect = pygame.Rect(x, y, widht, height)
        self.fill_color = back
        if color:
            self.fill_color = color
    def color(self, new_color):
        self.fill_color = new_color
    def fill(self):
        pygame.draw.rect(mw, self.fill_color,self.rect)
    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)



    def colliderect(self, rect):
        return self.rect.colliderect(rect)


class Picture(Area):
    def __init__(self, filename, x = 0, y = 0, widht = 10, height = 10):
        Area.__init__(self, x = x, y = y, widht = widht, height = height, color = None)
        self.image = pygame.image.load(filename)

    def draw(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))

class Label(Area):
    def set_text(self, text, fsize = 12, text_color = (0,0,0)):
        self.image = pygame.font.SysFont("verdana", fsize).render(text, True, text_color)
    def draw(self, shift_x, shift_y):
        self.fill()
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))


ball = Picture("enemy.png", 160, 200, 50, 50)
platformLeft = Picture("platformLeft.png", racket_x1, racket_y1, 30, 100)
platformRight = Picture("platformRight.png", racket_x2, racket_y2, 30, 100)
wall = Area(0,60,500,5, (0,0,0))
        
RED = (225, 0, 0)        
GREEN =(0, 225, 0)  

score_text_l = Label(10, 10 ,70, 30, back)
score_text_l.set_text("Гравець 1:", 20, (0,0,0))
score_text_l.draw(0,10)
score_l = Label(130, 10 ,30, 30, back)
score_l.set_text("0", 20, (0,0,0))
score_l.draw(0,10)
        
score_text_r = Label(330, 10 ,70, 30, back)
score_text_r.set_text("Гравець 2:", 20, (0,0,0))
score_text_r.draw(0,10)
score_r = Label(450, 10 ,30, 30, back)
score_r.set_text("0", 20, (0,0,0))
score_r.draw(0,10)

points_l = 0
points_r = 0

while not game_over:
    wall.fill()
    ball.fill()
    platformLeft.fill()
    platformRight.fill()

    score_l.set_text(str(points_l),20,(0,0,0))
    score_l.draw(0,10)
    score_r.set_text(str(points_r),20,(0,0,0))
    score_r.draw(0,10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                move_Up_r = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                move_Down_r = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                move_Up_r = False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                move_Down_r = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                move_Up_l = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                move_Down_l = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                move_Up_l = False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                move_Down_l = False

    if move_Up_l:
        platformLeft.rect.y -= 5
    if move_Down_l:
        platformLeft.rect.y += 5

    if move_Up_r:
        platformRight.rect.y -= 5
    if move_Down_r:
        platformRight.rect.y += 5

    ball.rect.x += dx
    ball.rect.y += dy

    if ball.rect.y > 450:
        dy *= -1

    if ball.rect.colliderect(wall.rect):
        dy *= -1
    

    if ball.rect.colliderect(platformLeft.rect) or ball.rect.colliderect(platformRight.rect):
        dx *= -1


    if ball.rect.x > 455:
        points_l +=1
        ball.rect.x = 250
        ball.rect.y = 200


    if ball.rect.x < 25:
        points_r +=1
        ball.rect.x = 250
        ball.rect.y = 200

    if points_l >= 3 :
        win = Label(0, 0, 500, 500, GREEN)
        win.set_text("Гравець 1,", 40, (0,0,0))
        win.draw(150, 180)
        win1 = Label(50, 250, 100, 50, GREEN)
        win1.set_text("перемога за тобою!", 40, (0,0,0))
        win1.draw(0, 0)
        break

    if points_r >= 3:
        win = Label(0, 0, 500, 500, GREEN)
        win.set_text("Гравець 2,", 40, (0,0,0))
        win.draw(150, 180)
        win1 = Label(50, 250, 100, 50, GREEN)
        win1.set_text("перемога за тобою!", 40, (0,0,0))
        win1.draw(0, 0)
        break

    if platformLeft.rect.y < 60:
        platformLeft.rect.y += 10
    if platformLeft.rect.y > 400:
        platformLeft.rect.y -=10

    if platformRight.rect.y < 60:
        platformRight.rect.y += 10
    if platformRight.rect.y > 400:
        platformRight.rect.y -=10


    ball.draw()
    platformLeft.draw()
    platformRight.draw()

    pygame.display.update()
    clock.tick(40)
pygame.display.update()
time.sleep(7)
