import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 500, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge the Boxes")

# Colors
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BG_COLOR = (30, 30, 30)

# Clock and timer
clock = pygame.time.Clock()
FPS = 60
GAME_DURATION = 60  # seconds
start_ticks = pygame.time.get_ticks()

# Fonts
font = pygame.font.SysFont("Arial", 30)

# Player setup
player_size = 40
player = pygame.Rect(WIDTH // 2 - player_size // 2, HEIGHT - 60, player_size, player_size)
player_speed = 7

# Enemy setup
enemy_size = 40
enemy_list = []

# Score
score = 0

def get_enemy_speed(score):
    if score <= 20:
        return 4
    elif score <= 30:
        return 5
    elif score <= 40:
        return 6
    elif score <= 50:
        return 7
    elif score <= 60:
        return 8
    elif score <= 80:
        return 9
    elif score <= 100:
        return 10
    elif score <= 120:  
        return 11
    elif score <= 140:  
        return 12
    elif score <= 160:  
        return 13
    elif score <= 180:  
        return 14
    elif score <= 200:  
        return 15

def drop_enemies():
    if len(enemy_list) < 10 and random.randint(0, 20) == 0:  # Random drop with probability
        x_pos = random.randint(0, WIDTH - enemy_size)
        new_enemy = pygame.Rect(x_pos, 0, enemy_size, enemy_size)
        enemy_list.append(new_enemy)

def move_enemies():
    speed = get_enemy_speed(score)
    for enemy in enemy_list:
        enemy.y += speed

def update_enemies_and_score():
    global score
    for enemy in enemy_list[:]:
        if enemy.y > HEIGHT:
            enemy_list.remove(enemy)
            score += 1

def detect_collision(player, enemies):
    for enemy in enemies:
        if player.colliderect(enemy):
            return True
    return False

def draw_player():
    pygame.draw.rect(screen, RED, player)

def draw_enemies():
    for enemy in enemy_list:
        pygame.draw.rect(screen, BLUE, enemy)

def draw_score():
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

def draw_timer(seconds_left):
    timer_text = font.render(f"Time: {seconds_left}", True, WHITE)
    screen.blit(timer_text, (WIDTH - 150, 10))

# Game loop
running = True
while running:
    clock.tick(FPS)
    screen.fill(BG_COLOR)

    # Time handling
    seconds_passed = (pygame.time.get_ticks() - start_ticks) / 1000
    seconds_left = max(0, int(GAME_DURATION - seconds_passed))

    if seconds_left == 0:
        print(f"Time's up! Final Score: {score}")
        running = False

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.right < WIDTH:
        player.x += player_speed

    # Enemy behavior
    drop_enemies()
    move_enemies()
    update_enemies_and_score()

    # Collision detection
    if detect_collision(player, enemy_list):
        print(f"Game Over! Final Score: {score}")
        running = False

    # Draw everything
    draw_player()
    draw_enemies()
    draw_score()
    draw_timer(seconds_left)
    pygame.display.flip()

pygame.quit()
sys.exit()
# End of the game
# This is a simple game where the player controls a red square and must avoid blue squares falling from the top of the screen.