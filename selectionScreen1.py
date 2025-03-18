import pygame,sys
from functions import get_font

pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

def selection_screen():
    pygame.display.set_caption("Selection Screen")
    running = True
    clock = pygame.time.Clock()

    # Load spaceship and asteroid images
    spaceship_images = [
        "assesories/spaceship.png",
        "assesories/spaceship1.png",
        "assesories/spaceship2.png",
        "assesories/spaceship3.png",
        "assesories/spaceship4.png",
    ]
    asteroid_images = [
        "assesories/asteroid.png",
        "assesories/asteroid1.png",
        "assesories/asteroid2.png",
        "assesories/asteroid3.png",
    ]

    selected_spaceship = 0
    selected_asteroid = 0

    while running:
        clock.tick(60)
        screen.fill(BLACK)
        
        title_text = get_font(100).render("SELECT YOUR SPACESHIP", True, "#b68f40")
        title_rect = title_text.get_rect(center=(640, 100))
        screen.blit(title_text, title_rect)

        # Render spaceship options
        for i, img_path in enumerate(spaceship_images):
            spaceship_img = pygame.image.load(img_path)
            x_pos = 250 + i * 200
            y_pos = 300
            spaceship_rect = spaceship_img.get_rect(center=(x_pos, y_pos))
            if i == selected_spaceship:
                pygame.draw.rect(screen, RED, spaceship_rect.inflate(20, 20), 5)  # Highlight selection
            screen.blit(spaceship_img, spaceship_rect)

        # Render asteroid options
        asteroid_text = get_font(50).render("CHOOSE ASTEROID", True, "#b68f40")
        asteroid_rect = asteroid_text.get_rect(center=(640, 500))
        screen.blit(asteroid_text, asteroid_rect)

        for i, img_path in enumerate(asteroid_images):
            asteroid_img = pygame.image.load(img_path)
            x_pos = 350 + i * 200
            y_pos = 600
            asteroid_rect = asteroid_img.get_rect(center=(x_pos, y_pos))
            if i == selected_asteroid:
                pygame.draw.rect(screen, RED, asteroid_rect.inflate(20, 20), 5)  # Highlight selection
            screen.blit(asteroid_img, asteroid_rect)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    selected_spaceship = (selected_spaceship + 1) % len(spaceship_images)
                elif event.key == pygame.K_LEFT:
                    selected_spaceship = (selected_spaceship - 1) % len(spaceship_images)
                elif event.key == pygame.K_DOWN:
                    selected_asteroid = (selected_asteroid + 1) % len(asteroid_images)
                elif event.key == pygame.K_UP:
                    selected_asteroid = (selected_asteroid - 1) % len(asteroid_images)
                elif event.key == pygame.K_RETURN:  # Press Enter to confirm selection
                    return spaceship_images[selected_spaceship], asteroid_images[selected_asteroid]

        pygame.display.flip()
