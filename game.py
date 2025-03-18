import pygame, sys
import random
from pygame import mixer
from classes import Spaceship,Asteroid,Bullet
from functions import show_score2,paused_fn,show_high_score,fade_out,countdown,pushpa_music,show_level,show_bullets_fired
from scoreGame1 import score_window
# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

#preload background music
mixer.music.load("assesories/SkyFire.wav")
Bullet_fire = mixer.Sound('assesories/laser.wav')

backgrounds = [
    pygame.image.load('assesories/bg.jpg'),
    pygame.image.load('assesories/bg2.jpg'),
    pygame.image.load('assesories/bg3.jpg'),
    pygame.image.load('assesories/bg4.jpg')
]

def play1(spaceship_image, asteroid_image):
    pygame.display.set_caption("Spaceship Game")
    running = True
    HIGH_SCORE = 0   #High score

    while running:
        bG = pygame.image.load('assesories/bg.jpg')
        mixer.music.play(-1)
        level = 1  # Start at Level 1
        
        # Initialize player and asteroid sprites
        player = Spaceship(spaceship_image)
        all_sprites = pygame.sprite.Group()
        all_sprites.add(player)
        asteroids = pygame.sprite.Group()
        bullets = pygame.sprite.Group()
        def spawn_asteroids(num):
            for _ in range(num):
                asteroid = Asteroid(asteroid_image)
                all_sprites.add(asteroid)
                asteroids.add(asteroid)

        spawn_asteroids(level + 4)  # More asteroids as levels increase

        paused = False
        clock = pygame.time.Clock()
        player_score = 0
        fired_bullets = 0
        game_active = True
        pushpa_played = False

        #game loop
        while game_active:
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN: 
                    if event.key == pygame.K_p: # Press 'P' to pause 
                        paused = not paused
                    elif event.key == pygame.K_SPACE: # Press SPACE to fire bullet 
                        bullet = Bullet(player.rect.centerx, player.rect.top) 
                        all_sprites.add(bullet) 
                        bullets.add(bullet)
                        Bullet_fire.play()
                        fired_bullets += 1
            
            if paused:
                if not paused_fn():
                    running = False
                    game_active = False
                paused = False
            
            else:
                # Update sprites
                all_sprites.update()

                if player_score == HIGH_SCORE and player_score != 0 and not pushpa_played:
                    pushpa_music()
                    pushpa_played = True 

                # Check for collisions
                if pygame.sprite.spritecollideany(player, asteroids): 
                    HIGH_SCORE = max(HIGH_SCORE, player_score)
                    fade_out(screen)
                    restart = score_window(player_score,HIGH_SCORE,fired_bullets)
                    if restart:
                        countdown(screen)
                        # Break out of the game loop to restart+
                        break
                    else:
                        # Exit both loops to return to the main menu
                        running = False
                        game_active = False

                # Check for bullet-asteroid collisions 
                for bullet in bullets: 
                    hit_asteroids = pygame.sprite.spritecollide(bullet, asteroids, True) 
                    if hit_asteroids: 
                        bullet.kill() 
                        player_score += 1
                        for _ in hit_asteroids:
                            # Optionally, add some score or explosion effects here 
                            new_asteroid = Asteroid(asteroid_image) 
                            all_sprites.add(new_asteroid) 
                            asteroids.add(new_asteroid)

                # Check for level progression
                if player_score == level *50: # Advance to the next level every 10 points
                    level += 1
                    spawn_asteroids(level + 7)

                # Draw
                screen.blit(backgrounds[min(level - 1, len(backgrounds) - 1)], (0, 0))
                all_sprites.draw(screen)
                show_level(level)
                show_score2(player_score)
                show_bullets_fired(fired_bullets)
                show_high_score(HIGH_SCORE)

            pygame.display.flip()

        # If running is False, exit the game loop
        if not running:
            break    
