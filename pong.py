import pygame
import random


pygame.init()


screen = pygame.display.set_mode((1920,880))
BLACK = (0,0,0)
WHITE = (255,255,255)
font = pygame.font.Font(None, 128)


rect1_Y = 500
rect2_Y = 500
rect_1_change = 0
rect_2_change = 0
score_1 = 0
score_2 = 0


# BALL VARIABLES -----------------------------------------------------------------------
ballX = 945
ballY = 425
ballX_change = 0
ballY_change = 0
small = 0.5
big = 1


def ball_speed():
    global small, big
    small += 0.05
    big += 0.1


ball_dir = random.randint(1,14)


def ball_direction():
    global ballX, ballY
    if ball_dir == 1:
        ballX += small
        ballY += -big
    if ball_dir == 2:
        ballX += big
        ballY += -big
    if ball_dir == 3:
        ballX += big
        ballY += -small
    if ball_dir == 4:
        ballX += big
    if ball_dir == 5:
        ballX += big
        ballY += small
    if ball_dir == 6:
        ballX += big
        ballY += big
    if ball_dir == 7:
        ballX += small
        ballY += big


    if ball_dir == 8:
        ballX += -small
        ballY += big
    if ball_dir == 9:
        ballX += -big
        ballY += big
    if ball_dir == 10:
        ballX += -big
        ballY += small
    if ball_dir == 11:
        ballX += -big
    if ball_dir == 12:
        ballX += -big
        ballY += -small
    if ball_dir == 13:
        ballX += -big
        ballY += -big
    if ball_dir == 14:
        ballX += -small
        ballY += -big


running = True
while running:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                rect_1_change -= 2
            if event.key == pygame.K_s:
                rect_1_change += 2
            if event.key == pygame.K_UP:
                rect_2_change -= 2
            if event.key == pygame.K_DOWN:
                rect_2_change += 2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                rect_1_change = 0
            if event.key == pygame.K_s:
                rect_1_change = 0
            if event.key == pygame.K_UP:
                rect_2_change = 0
            if event.key == pygame.K_DOWN:
                rect_2_change = 0
   
    rect1_Y += rect_1_change
    rect2_Y += rect_2_change


    pygame.draw.rect(screen, WHITE, (200, rect1_Y, 20, 200))
    pygame.draw.rect(screen, WHITE, (1700, rect2_Y, 20, 200))
    pygame.draw.rect(screen, WHITE, (ballX, ballY, 30, 30))


    player_1_rect = pygame.Rect(200, rect1_Y, 20, 200)
    player_2_rect = pygame.Rect(1700, rect2_Y, 20, 200)
    ball_rect = pygame.Rect(ballX, ballY, 30, 30)


    if ballY <= 0:
        if ball_dir == 1:
            ball_dir = 7
        if ball_dir == 2:
            ball_dir = 6
        if ball_dir == 3:
            ball_dir = 5
        if ball_dir == 14:
            ball_dir = 8
        if ball_dir == 13:
            ball_dir = 9
        if ball_dir == 12:
            ball_dir = 10
        ball_speed()


    if ballY >= 850:
        if ball_dir == 7:
            ball_dir = 1
        if ball_dir == 6:
            ball_dir = 2
        if ball_dir == 5:
            ball_dir = 3
        if ball_dir == 8:
            ball_dir = 14
        if ball_dir == 9:
            ball_dir = 13
        if ball_dir == 10:
            ball_dir = 12
        ball_speed()


    if ball_rect.colliderect(player_1_rect):
        ball_dir = random.randint(1,7)
        ball_speed()


    if ball_rect.colliderect(player_2_rect):
        ball_dir = random.randint(8,14)
        ball_speed()


    if ballX <= 0:
        ballX = 945
        ballY = 425
        small = 0.5
        big = 1
        ball_dir = random.randint(1,14)
        ball_direction()
        score_2 += 1


    if ballX >= 1920:
        ballX = 945
        ballY = 425
        small = 0.5
        big = 1
        ball_dir = random.randint(1,14)
        ball_direction()
        score_1 += 1
   
    if rect1_Y <= 0:
        rect1_Y = 0
    if rect1_Y >= 680:
        rect1_Y = 680
    if rect2_Y <= 0:
        rect2_Y = 0
    if rect2_Y >= 680:
        rect2_Y = 680


    if score_1 >= 10 or score_2 >= 10:
        running = False


    score_text  = font.render(f"{score_1}", True, (255,255,255))
    screen.blit(score_text, (845, 780))
    score_text  = font.render(f"{score_2}", True, (255,255,255))
    screen.blit(score_text, (994, 780))


    ball_direction()


    pygame.display.update()