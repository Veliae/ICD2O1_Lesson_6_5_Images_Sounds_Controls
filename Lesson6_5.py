import pygame

# Initialize the game engine
pygame.init()

# ---------------------------
# Set window settings (size and name) 
WIDTH = 700
HEIGHT = 500
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Pygame Lesson 6.5")
# ---------------------------

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Make cursor insivible
pygame.mouse.set_visible(0)


# ---------------------------
# Initialize global variables

# --------- Colours ---------
white = (255, 255, 255)
black = (0, 0, 0)

# --------- Images ----------
# Background
background_img = pygame.image.load("tilemap-backgrounds_packed.png").convert()
background_img = pygame.transform.scale(background_img, (1400, 500)).convert()

# Platform
platform_img = pygame.image.load("tile_0022.png").convert()
platform_x = 0
platform_y = HEIGHT - platform_img.get_height()

# Players
player1_img = pygame.image.load("tile_0007.png").convert()
player2_img = pygame.image.load("tile_0001.png").convert()

player1_x = 10
player1_y = HEIGHT - platform_img.get_height() - player1_img.get_height()
player2_x = 600
player2_y = HEIGHT - platform_img.get_height() - player2_img.get_height()


# -------- Animation --------


# ---------------------------

# ---------------------------
# Functions


# ---------------------------

# --------------- Main program loop ---------------
running = True
while running:
    # ----- EVENT HANDLING -----
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

     # ----- USER INPUTS -----
    # Player 1 controlled by mouse 
    mouse = pygame.mouse.get_pos()
    player1_x = mouse[0]
    player1_y = mouse[1]

    # Player 2 controlled by wasd keys    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w] == True and player2_y > 0:
        player2_y -= 3
    if keys[pygame.K_s] == True and (player2_y < HEIGHT - player2_img.get_height()):
        player2_y += 3
    if keys[pygame.K_a] == True and player2_x > 0:
        player2_x -= 3
    if keys[pygame.K_d] == True and (player2_x < WIDTH - player2_img,get_width()):
        player2_x += 3






    # ----- GAME STATE UPDATES -----
    # All game math and comparisons happen here

     # ----- DRAWING -----
    # Blit background image to screen
    screen.blit(background_img, [0, 0])

    # Repeatedly draw the platform image across the bottom of the screen
    for i in range(0, WIDTH, platform_img.get_width()):
        screen.blit(platform_img, [i, platform_y])

   # Blit the players to screen
    screen.blit(player1_img, [player1_x, player1_y])
    screen.blit(player2_img, [player2_x, player2_y])

        # Must be the last two lines of the game loop
    pygame.display.flip()
    clock.tick(30)
    # ---------------------------
    # ---------------------------

pygame.quit()
