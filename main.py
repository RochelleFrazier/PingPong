import pygame
import sys
import random


def ball_animation():
    global ball_speed_x, ball_speed_y, player_one_score, player_two_score, score_time

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1

    if ball.left <= 0:
        player_two_score += 1
        score_time = pygame.time.get_ticks()

    if ball.right >= screen_width:
        player_one_score += 1
        score_time = pygame.time.get_ticks()

    if ball.colliderect(player_one) or ball.colliderect(player_two):
        ball_speed_x *= -1


def player_one_animation():
    player_one.y += player_one_speed

    if player_one.top <= 0:
        player_one.top = 0

    if player_one.bottom >= screen_height:
        player_one.bottom = screen_height


def player_two_animation():
    if player_two.top < ball.y:
        player_two.top += player_two_speed

    if player_two.bottom > ball.y:
        player_two.bottom -= player_two_speed

    if player_two.top <= 0:
        player_two.top = 0

    if player_two.bottom >= screen_height:
        player_two.bottom = screen_height


def ball_start():
    global ball_speed_x, ball_speed_y, score_time

    current_time = pygame.time.get_ticks()
    ball.center = (screen_width/2, screen_height/2)

    if current_time - score_time < 700:
        number_three = game_font.render("3", False, ball_color)
        screen.blit(number_three, (screen_width/2 - 10, screen_height/2 + 20))

    if 700 < current_time - score_time < 1400:
        number_two = game_font.render("2", False, ball_color)
        screen.blit(number_two, (screen_width / 2 - 10, screen_height / 2 +20))

    if 1400 < current_time - score_time < 2100:
        number_one = game_font.render("1", False, ball_color)
        screen.blit(number_one, (screen_width / 2 - 10, screen_height / 2 +20))

    if current_time - score_time < 2100:
        ball_speed_x, ball_speed_y = 0, 0
    else:
        ball_speed_y = 7 * random.choice((1, -1))
        ball_speed_x = 7 * random.choice((1, -1))
        score_time = None


# General Setup
pygame.init()
clock = pygame.time.Clock()

# Main Window
screen_width = 1300

screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Ping Pong')

# Game Rectangles
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30)
player_one = pygame.Rect(screen_width - 20, screen_height/2 - 70, 10, 140)
player_two = pygame.Rect(10, screen_height/2 - 70, 10, 140)

# Game Colors
bg_color = pygame.Color('purple')
ball_color = (255, 255, 255)
player_one_color = (235, 85, 52)
player_two_color = (110, 52, 235)
vert_line_color = (0, 0, 0)

# Game Variables
ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))
player_one_speed = 0
player_two_speed = 7

# Text Variables
player_one_score = 0
player_two_score = 0
game_over = "GAME OVER!"
game_font = pygame.font.Font("freesansbold.ttf", 42)
game_over_font = pygame.font.Font("freesansbold.ttf", 100)

# Score Timer
score_time = True

while True:
    # handling output
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_one_speed += 7
            if event.key == pygame.K_UP:
                player_one_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_one_speed -= 7
            if event.key == pygame.K_UP:
                player_one_speed += 7
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_two_speed += 7
            if event.key == pygame.K_UP:
                player_two_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_two_speed -= 7
            if event.key == pygame.K_UP:
                player_two_speed += 7


    # Game Logic
    ball_animation()
    player_one_animation()
    player_two_animation()

    # Visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen, player_one_color, player_one)
    pygame.draw.rect(screen, player_two_color, player_two)
    pygame.draw.ellipse(screen, ball_color, ball)
    pygame.draw.aaline(screen, vert_line_color, (screen_width/2, 0), (screen_width/2, screen_height))

    if score_time:
        ball_start()

    player_one_text = game_font.render(f"{player_one_score}", False, ball_color)
    screen.blit(player_one_text, (700, 450))

    player_two_text = game_font.render(f"{player_two_score}", False, ball_color)
    screen.blit(player_two_text, (560, 450))

    game_over_text = game_over_font.render(f"{game_over}", False, ball_color)
    screen.blit(player_two_text, (560, 450))

    # Updating the
    pygame.display.flip()
    clock.tick(60)



