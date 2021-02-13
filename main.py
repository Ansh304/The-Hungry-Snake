import pygame
import random
from pygame import mixer

pygame.init()  # initialize the pygame
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # screen set
pygame.display.set_caption("HUNGRY SNAKE")  # icon set

# player discription
player_colour = (0, 0, 255)
player_size_x = 30
player_size_y = 30
player_position_x = int((WIDTH / 2) - (player_size_x / 2))
player_position_y = int((HEIGHT / 2) - (player_size_y / 2))
player_x_change = 0
player_y_change = 0
player_list = []
player_lenght = 1

# enemy discription
enemy_colour = (255, 0, 0)
enemy_size = 15
enemy_position_x = random.randint(2 * enemy_size, WIDTH - 2 * enemy_size)
enemy_position_y = random.randint(2 * enemy_size, HEIGHT - 2 * enemy_size)

# for collision
collision = False
score = 0


def check_collision(p_x, p_y, e_x, e_y):
    global collision, score
    if (p_x >= e_x and p_x < (e_x + enemy_size + 7)) or (e_x >= p_x and e_x < (p_x + player_size_x + 7)):
        if (p_y >= e_y and p_y < (e_y + enemy_size + 7)) or (e_y >= p_y and e_y < (p_y + player_size_y + 7)):
            score += 1
            collision = True


def plot_snake(screen, player_colour, player_list, player_size_x, player_size_y):
    for x, y in player_list:
        pygame.draw.rect(screen, player_colour, (x, y, player_size_x,
                                                 player_size_y))  # making player(snake)


# for font
font = pygame.font.Font('newfont.ttf', 32)
text_X = 10
text_Y = 10


# for showing the score on screen
def show_score(x, y):
    global score
    score_value = font.render("score " + str(score), True, (0,0,0))
    screen.blit(score_value, (x, y))


speed = 4
clock = pygame.time.Clock()
# **********game loop**********

game_running = True
game_over = False

def welcome_window():                      # WELCOME WINDOW OF OUR GAME
    exit_welcom_window = False
    while not exit_welcom_window:
        global game_running
        screen.fill((0,0,0))
        font5 = pygame.font.Font('newfont.ttf', 64)
        welcome_note = 'WELCOME'

        welcome_text = font5.render(welcome_note, True, (255, 255, 255))
        screen.blit(welcome_text, (100, 100))
        welcome_text = font5.render("TO", True, (255, 255, 255))
        screen.blit(welcome_text, (300, 200))
        welcome_text = font5.render("GAMMING WORLD", True, (255, 255, 255))
        screen.blit(welcome_text, (250, 300))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # for quit the screen
                game_running = False
                exit_welcom_window = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    exit_welcom_window =True
        pygame.display.update()

welcome_window()

mixer.music.load('background.wav')
mixer.music.play(-1)


while game_running:
    screen.fill((255, 255, 204))  # filling the colour on the screen

    if game_over:

        screen.fill((255, 255, 255))
        font2 = pygame.font.Font('newfont.ttf', 64)
        over_text = font2.render("GAME OVER", True, (0, 0, 0))
        font3 = pygame.font.Font('newfont.ttf', 32)
        re_text = font3.render("press enter to re-start", True, (0, 0, 0))
        screen.blit(over_text, (100, 100))
        screen.blit(re_text, ((WIDTH // 2) - 100, (HEIGHT // 2) + 100))

        for event in pygame.event.get():

            if event.type == pygame.QUIT:  # for quit the screen
                game_running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game_over = False

                    player_position_x = int((WIDTH / 2) - (player_size_x / 2))
                    player_position_y = int((HEIGHT / 2) - (player_size_y / 2))
                    player_x_change = 0
                    player_y_change = 0
                    player_list = []
                    player_lenght = 1
                    score = 0


    else:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:  # for quit the screen
                game_running = False

            if event.type == pygame.KEYDOWN:  # for adding keyboard keys

                if event.key == pygame.K_RIGHT:
                    player_y_change = 0
                    player_x_change = speed
                if event.key == pygame.K_LEFT:
                    player_y_change = 0
                    player_x_change = -speed
                if event.key == pygame.K_DOWN:
                    player_x_change = 0
                    player_y_change = speed
                if event.key == pygame.K_UP:
                    player_x_change = 0
                    player_y_change = -speed
                if event.key == pygame.K_q: # cheat coad for incriment score
                    score += 5
        player_position_x += player_x_change
        player_position_y += player_y_change

        if (player_position_x <= 0) or (player_position_x + player_size_x >= WIDTH) or (player_position_y <= 0) or (
                player_position_y + player_size_y >= HEIGHT):  # fro restrict the boundries of snake
            game_over = True

        check_collision(player_position_x, player_position_y, enemy_position_x, enemy_position_y)  # calling collision

        if collision:  # conddii for collisio
            enemy_position_x = random.randint(enemy_size, WIDTH - enemy_size)
            enemy_position_y = random.randint(enemy_size, HEIGHT - enemy_size)
            player_lenght += 8       # increament the lenght of snake
            collision = False

        head = []  # for making head of snake
        head.append(player_position_x)
        head.append(player_position_y)
        player_list.append(head)

        if head in player_list[:len(player_list) - 2]:  # for collision from itself or its body so game ovver
            game_over = True

        if len(player_list) > player_lenght:  # for deleting the extra portion from snake
            del player_list[0]

        pygame.draw.circle(screen, enemy_colour, (enemy_position_x, enemy_position_y), enemy_size)  # making  enemy

        plot_snake(screen, player_colour, player_list, player_size_x, player_size_y)

        show_score(text_X, text_Y)

    clock.tick(100)
    pygame.display.update()

pygame.quit()
quit()
