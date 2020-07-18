# Jimmy B. Pong tutorial from Youtuber: "Clear Code" 5-15-20
# 5-23-20 V2 Randomization of ball flight path after hitting player paddle,
# optional ball speed increase (in ball_animation()), and perfectly tracking opponent Ai (thanks to help from Ray B.)
# 5-25-20 V4 Do not apply bounce off either paddle for a for 1 second, to avoid the moments when the ball gets stuck on the paddles.
# added variable player_increment to quickly edit how many pixels per iteration of loop the player paddle can move.

import pygame, sys, random

def pause():
    global paused
    #pygame.mixer.music.pause()
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = False

        pause_text = game_font.render("Paused",False,red)
        pause_text_rect = pause_text.get_rect()
        pause_text_rect.center = ((screen_width / 2), (screen_height / 2) )
        screen.blit(pause_text, pause_text_rect)
        pygame.display.update()


def ball_restart():
    global ball_speed_y, ball_speed_x, score_time, old_x, old_y

    current_time = pygame.time.get_ticks()
    ball.center = (screen_width/2, screen_height/2) # Return ball back to center for new point

    if current_time - score_time < 700:
        number_three = game_font.render("3",False,light_grey)
        screen.blit(number_three,(screen_width/2 - 10, screen_height/2 + 20))

    if 700 < current_time - score_time < 1400:
        number_two = game_font.render("2",False,light_grey)
        screen.blit(number_two,(screen_width/2 - 10, screen_height/2 + 20))

    if 1400 < current_time - score_time < 2100:
        number_one = game_font.render("1",False,light_grey)
        screen.blit(number_one,(screen_width/2 - 10, screen_height/2 + 20))

    if current_time - score_time < 2100:
        ball_speed_x, ball_speed_y = 0,0
    else:
        ball_speed_x = old_x * random.choice((1,-1))
        ball_speed_y = old_y * random.choice((1,-1))
        score_time = None

def opponent_ai():
    # track ball
    opponent.centery += min(ball.centery - opponent.centery, opponent_speed)

    # Stop opponent paddle from going off screen.
    if opponent.top < 0:
        opponent.top = 0

    if opponent.bottom > screen_height:
        opponent.bottom = screen_height

def player_animation():
    player.y += player_speed
    if player.top < 0:
        player.top = 0

    if player.bottom > screen_height:
        player.bottom = screen_height

def ball_animation():
    global ball_speed_x, ball_speed_y, player_score, opponent_score, old_x, old_y, score_time, paddle_impact
    current_time = pygame.time.get_ticks()

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1

    # Player Wins
    if ball.left <= 0:
        score_time = pygame.time.get_ticks()
        player_score += 1
        old_x = ball_speed_x
        old_y = ball_speed_y

    # Opponent Wins
    if ball.right >= screen_width:
        score_time = pygame.time.get_ticks()
        opponent_score += 1
        old_x = ball_speed_x
        old_y = ball_speed_y

    # Ball hits either paddle.
    # Designed to stop ball from entering back of paddle, but still being inside paddle upon next inspection
    # ...(getting trapped in paddle).
    if (ball.colliderect(player) or ball.colliderect(opponent)) and (current_time - paddle_impact) > 700:
        ball_speed_x *= -1
        paddle_impact = pygame.time.get_ticks()

    # Make game get progressively harder with each player paddle hit.
    if ball.colliderect(player):
        # Speed limit
        if int(ball_speed_x) < 14:
            ball_speed_x *= 1.02
            ball_speed_y *= 1.02

        # randomize ball's flight path
        ball_speed_x += 0.1 * random.randint(-5,5)
        ball_speed_y += 0.1 * random.randint(-5,5)

# General Setup
pygame.init()
clock = pygame.time.Clock()   # clock method stored in the variable "clock"

# Setting up the main window
screen_width = 1280
screen_height = 830
screen = pygame.display.set_mode((screen_width, screen_height))  # returns a display-surface object
pygame.display.set_caption("Jimmy's Pong")

# Colors
light_grey = (200,200,200)
bg_color = pygame.Color("grey12")
red = (255, 0, 0)

# Game Rectangles
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30,30)
player = pygame.Rect(screen_width - 20, screen_height/2 - 70, 10,140)
opponent = pygame.Rect(10, screen_height / 2 - 70, 10,140)

# Game Variables
ball_speed_x = 7 * random.choice((1,-1))
ball_speed_y = 7 * random.choice((1,-1))
player_speed = 0
player_increment = 10  # how many pixels the player paddle can move per iteration of loop.
opponent_speed = 10
paused = False
old_x = 7
old_y = 7
paddle_impact = 1 # initialize variable, set to 1 milli-sec so first paddle bounce on serve has no chance of getting canceled.

# Text Variables:
player_score = 0
opponent_score = 0
game_font = pygame.font.Font("freesansbold.ttf",50)  # creates a font.
small_font = pygame.font.Font("freesansbold.ttf",20)  # creates a font.

#Score_Timer
score_time = 1

#Main
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_speed += -player_increment
            if event.key == pygame.K_DOWN:
                player_speed += player_increment
            if event.key == pygame.K_SPACE:
                paused = True
                pause()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_speed += player_increment
            if event.key == pygame.K_DOWN:
                player_speed += -player_increment


    # Game Logic
    ball_animation()
    player_animation()
    opponent_ai()


    # Visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen,light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width/2,0), (screen_width/2,screen_height))

    if score_time:
        ball_restart()

    player_text = game_font.render(f"{player_score}",False,light_grey)  # Creates a surface using our font, string and color.
    screen.blit(player_text,(685,470))  # adds the player_text surface to the display surface (called "screen" in our case).
    opponent_text = game_font.render(f"{opponent_score}",False,light_grey)  # Creates a surface using our font, string and color.
    screen.blit(opponent_text,(575,470))  # adds the player_text surface to the display surface (called "screen" in our case).
    ball_speed_indicator = small_font.render(f"Ball Speed: {abs(int(ball_speed_x))}",False,light_grey)
    screen.blit(ball_speed_indicator,(500, 20))

    pygame.display.update()
    clock.tick(60) # if we didn't set this speed of 60 cycles per second the computer might try and use all system resources to run as fast as possible.
