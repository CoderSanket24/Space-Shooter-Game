import pygame, sys, time
from pygame import mixer
from classes import Spaceship,Spaceship2,Asteroid,Bullet
from functions import show_score1,show_score2,paused_fn,fade_out,countdown,show_bullets1,show_bullets2
from scoreGame2 import winner_window
# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

mixer.music.load("assesories/SkyFire.wav")

def play2(spaceship_image, spaceship2_image, asteroid_image="assesories/asteroid.png"):
    pygame.display.set_caption("Spaceship Game")
    
    # Preload backgrounds
    backgrounds = [
        pygame.image.load('assesories/bg.jpg'),
        pygame.image.load('assesories/bg2.jpg'),
        pygame.image.load('assesories/bg3.jpg'),
        pygame.image.load('assesories/bg4.jpg'),
    ]

    running = True

    while running:
        # Sound
        mixer.music.play(-1)

        # Initialize player and asteroid sprites
        player1 = Spaceship(spaceship_image)
        player2 = Spaceship2(spaceship2_image)
        all_sprites = pygame.sprite.Group()
        all_sprites.add(player1)
        all_sprites.add(player2)
        asteroids = pygame.sprite.Group()
        bullets = pygame.sprite.Group()
        bullets2 = pygame.sprite.Group()

        for _ in range(8):
            asteroid = Asteroid(asteroid_image)
            all_sprites.add(asteroid)
            asteroids.add(asteroid)

        #check for player collision with asteroid
        player1_collision = 'not collided'
        player2_collision = 'not collided'

        # Main game loop
        paused = False
        clock = pygame.time.Clock()
        player_score1 = 0
        player_score2 = 0
        bullet_score1 = 0
        bullet_score2 = 0
        game_active = True

        #Track elapsed time
        start_time = time.time()
        current_background = backgrounds[0]

        while game_active:
            clock.tick(30)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.KEYDOWN: 
                    if event.key == pygame.K_p: # Press 'P' to pause 
                        paused = not paused
                    if event.key == pygame.K_BACKSPACE: # Press BACKSPACE to fire bullet 
                        bullet = Bullet(player1.rect.centerx, player1.rect.top) 
                        all_sprites.add(bullet) 
                        bullets.add(bullet)
                        bullet_score1 += 1
                    if event.key == pygame.K_f: # Press F to fire bullet 
                        bullet = Bullet(player2.rect.centerx, player2.rect.top) 
                        all_sprites.add(bullet) 
                        bullets2.add(bullet)
                        bullet_score2 += 1
            
            if paused:
                if not paused_fn():
                    running = False
                    game_active = False
                paused = False
            
            else:
                # Calculate elapsed time and determine difficulty level
                elapsed_time = time.time() - start_time
                difficulty_level = int(elapsed_time // 30) + 1  # Increase difficulty every 30 seconds

                # Adjust game behavior based on difficulty
                current_background = update_background(difficulty_level, backgrounds)
                adjust_difficulty(difficulty_level, asteroids, all_sprites, asteroid_image)

                # Update sprites
                all_sprites.update()

                # Check for collisions
                if pygame.sprite.spritecollideany(player2, asteroids) and not pygame.sprite.spritecollideany(player1, asteroids):
                    player2.kill()
                    player2_collision = 'collided'
                if pygame.sprite.spritecollideany(player1, asteroids) and not pygame.sprite.spritecollideany(player2, asteroids):
                    player1.kill()
                    player1_collision = 'collided'
                if player1_collision == 'collided' and player2_collision == 'collided':
                    fade_out(screen)
                    restart = winner_window(player_score1,player_score2,bullet_score1,bullet_score2)
                    if restart:
                        countdown(screen)
                        pygame.display.set_caption("Spaceship Game")
                        # Break out of the game loop to restart
                        break
                    else:
                        # Exit both loops to return to the main menu
                        running = False
                        game_active = False

                # Check for player bullet-asteroid collisions 
                for bullet in bullets: 
                    hit_asteroids = pygame.sprite.spritecollide(bullet, asteroids, True) 
                    if hit_asteroids: 
                        bullet.kill() 
                        player_score1 += 1
                        for asteroid in hit_asteroids: 
                            # Optionally, add some score or explosion effects here 
                            new_asteroid = Asteroid(asteroid_image) 
                            all_sprites.add(new_asteroid) 
                            asteroids.add(new_asteroid)

                # Check for player2 bullet-asteroid collisions 
                for bullet in bullets2: 
                    hit_asteroids = pygame.sprite.spritecollide(bullet, asteroids, True) 
                    if hit_asteroids: 
                        bullet.kill() 
                        player_score2 += 1
                        for asteroid in hit_asteroids:
                            new_asteroid = Asteroid(asteroid_image) 
                            all_sprites.add(new_asteroid) 
                            asteroids.add(new_asteroid)
                # Draw
                screen.blit(current_background, (0, 0))
                all_sprites.draw(screen)
                show_score2(player_score2)
                show_score1(player_score1)
                show_bullets1(bullet_score1)
                show_bullets2(bullet_score2)
            pygame.display.flip()

        # If running is False, exit the game loop
        if not running:
            break    

def update_background(level, backgrounds):
    """
    Returns the background corresponding to the current difficulty level.
    """
    max_level = len(backgrounds)
    return backgrounds[min(level - 1, max_level - 1)]

def adjust_difficulty(level, asteroids, all_sprites, asteroid_image):
    # Increase the number of asteroids
    if len(asteroids) < level * 10:  # Max asteroids increases with level
        for _ in range(level * 2):  # Add more asteroids as difficulty increases
            new_asteroid = Asteroid(asteroid_image)
            asteroids.add(new_asteroid)
            all_sprites.add(new_asteroid)

    # Optionally, increase asteroid speed
    # for asteroid in asteroids:
    #     asteroid.speed_y += level * 0.1  # Increment speed based on difficulty level
