from random import uniform as func
from time import sleep
import pygame

pygame.init()

WIDTH, HEIGHT = 600, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ball Game")

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)

bound = 20

# Початкове положення та розміри м'яча
x, y = WIDTH // 2, HEIGHT // 2
radius = 10

# Швидкість м'яча
velocity = 8
vx = velocity * func(-1, 1)
vy = velocity * func(-1, 1)
num = 1.5

# Межі для центра м'яча
border_l = bound + radius
border_r = WIDTH - bound - radius
border_u = bound + radius
border_d = HEIGHT - bound - radius

# Положення та розміри майданчика
height = 10
width = 80
xp = (WIDTH - width) // 2
yp = HEIGHT - height
vp = 10

# Очки гравця
score = 0
score_step = 10


def drawScore(current_score):
    win.fill(black)
    pygame.font.init()
    path = pygame.font.match_font("arial")
    font = pygame.font.Font(path, 30)
    text = f"Your score: {current_score}"
    surface_text = font.render(text, True, white)
    rect_text = surface_text.get_rect(center=(WIDTH // 2, HEIGHT // 3))
    win.blit(surface_text, rect_text)
    pygame.display.update()


def drawWindow():
    win.fill(black)

    # Ліва, верхня та права границі (нижню прибрано за умовою)
    pygame.draw.rect(win, white, (0, 0, bound, HEIGHT))
    pygame.draw.rect(win, white, (0, 0, WIDTH, bound))
    pygame.draw.rect(win, white, (WIDTH - bound, 0, bound, HEIGHT))

    # Нижня границя закоментована:
    # pygame.draw.rect(win, white, (0, HEIGHT - bound, WIDTH, bound))

    # М'яч
    pygame.draw.circle(win, green, (int(x), int(y)), radius)

    # Майданчик
    pygame.draw.rect(win, white, (xp, yp, width, height))

    pygame.display.update()


clock = pygame.time.Clock()
run = True

while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Рух майданчика
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and xp > bound:
        xp -= vp
    if keys[pygame.K_RIGHT] and xp < WIDTH - bound - width:
        xp += vp

    # Відбиття від лівої, правої та верхньої границь
    if x + vx < border_l or x + vx > border_r:
        vx = -vx
    if y + vy < border_u:
        vy = -vy

    # Перевірка нижньої межі та попадання на майданчик
    if y + vy > border_d:
        if xp <= x + vx <= xp + width:
            vy = -vy
            vx *= num
            vy *= num
            score += score_step
        else:
            drawScore(score)
            sleep(10)
            run = False

    # Оновлення координат м'яча
    x += vx
    y += vy

    drawWindow()

pygame.quit()
