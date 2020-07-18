#Jimmy B. Snake Game, tutorial: Mr. Chatergoon
import pygame, random, sys

pygame.init()

#Colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
DARK_GREEN = (0,155,0)
BLUE = (0,0,255)
GREEN = (0,255,0)

#Game Settings:
WIDTH = 600
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jimmy's Snake Game")
clock = pygame.time.Clock()
FPS = 60

class Snake(pygame.sprite.Sprite):
    """Settings for the Snake"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20,20))  # snake
        self.image.fill(DARK_GREEN)
        self.rect = self.image.get_rect()  # fashion rectangle around image.
        self.rect.x = WIDTH/2
        self.rect.y = HEIGHT/2  # initial location of snake.
        self.snake_speed_x = 0 #set initial speed to 0
        self.snake_speed_y = 0
        self.snake_speed_universal = 5
        self.game_exit = False  # We will set True to exit.
        self.snake_list = []  # store snake coordinates
        self.snake_length = 1

    def update(self):
        self.snake_movement()
        self.snake_boundary()
        self.track_snake_coordinates()
        self.draw_snake()

    def snake_movement(self):
        """Keep track of the snake's movements."""
        keystate = pygame.key.get_pressed()  # list of keys pressed
        if keystate[pygame.K_RIGHT]:
            self.snake_speed_x = self.snake_speed_universal
            self.snake_speed_y = 0
        elif keystate[pygame.K_LEFT]:
            self.snake_speed_x = -self.snake_speed_universal
            self.snake_speed_y = 0
        elif keystate[pygame.K_UP]:
            self.snake_speed_y = -self.snake_speed_universal
            self.snake_speed_x = 0
        elif keystate[pygame.K_DOWN]:
            self.snake_speed_y = self.snake_speed_universal
            self.snake_speed_x = 0

        self.rect.x += self.snake_speed_x  # move snake right or left.
        self.rect.y += self.snake_speed_y  # move snake up or down.

    def snake_boundary(self):
        """If the snake goes off screen, end game."""
        if self.rect.right >= WIDTH or self.rect.left <= 0 or self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.game_exit = True

    def track_snake_coordinates(self):
        snake_coord = []
        snake_coord.append(self.rect.x)  # add the x coordinate
        snake_coord.append(self.rect.y)  # add the y coordinate
        self.snake_list.append(snake_coord)

        # Keep the list only as long as the snake.
        if len(self.snake_list) > self.snake_length:
            del self.snake_list[0]

    def draw_snake(self):
        print(self.snake_list)
        for i in self.snake_list[:-1]:
            pygame.draw.rect(screen, GREEN, (i[0], i[1], 20, 20))


class Apple(pygame.sprite.Sprite):
    """Apple settings"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20,20))
        self.image.fill(RED)
        self.rect = self.image.get_rect()  #get rectangle around apple.
        self.apple_size = 20
        # self.rect.x = round(random.randrange(0, WIDTH - self.apple_size)/10)*10
        # self.rect.y = round(random.randrange(0, HEIGHT - self.apple_size)/10)*10
        # Tutorial guy said the above code solves and issue, but I don't see it.
        self.rect.x = random.randrange(0, WIDTH - self.apple_size)
        self.rect.y = random.randrange(0, HEIGHT - self.apple_size)

    def draw_apple(self):
        self.rect.x = random.randrange(0, WIDTH - self.apple_size)
        self.rect.y = random.randrange(0, HEIGHT - self.apple_size)

    def update(self):
        pass

# Sprites
apple = Apple()
player = Snake()
all_sprites = pygame.sprite.Group() # group to contain all the sprites.
all_sprites.add(player)
all_sprites.add(apple)

# Game Functions:
def message_to_screen(text, color, font_size, y_position ):
    font = pygame.font.Font("freesansbold.ttf", font_size)
    message = font.render(text, True, color)
    message_rect = message.get_rect()  # gets a rectangle around the text
    message_rect.center = (WIDTH/2, y_position)
    screen.blit(message, message_rect)  # what to display and where.

# Main Game Loop
def gameLoop():
    game_exit = False
    game_over = False
    score = 0

    while not game_exit:
        clock.tick(FPS)
        # check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True

        # Check if snake is off screen:
        if player.game_exit:
            game_exit = True

        # Check if the snake eats the apple:
        if pygame.sprite.collide_rect(player, apple):
            apple.draw_apple()
            score += 1
            player.snake_length += 1

        # update
        screen.fill(WHITE)
        all_sprites.update()
        all_sprites.draw(screen)
        #message_to_screen(text, color, font_size, y_position
        message_to_screen(f"Score: {score}", BLACK, 20, 20)

        pygame.display.update()

    pygame.quit()

gameLoop()
