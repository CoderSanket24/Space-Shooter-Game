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

def selection_screen2():
    pygame.display.set_caption("Selection Screen")
    running = True
    clock = pygame.time.Clock()

    # Load spaceship and spaceship2 images
    spaceship_images = [
        "assesories/spaceship.png",
        "assesories/spaceship1.png",
        "assesories/spaceship2.png",
        "assesories/spaceship3.png",
        "assesories/spaceship4.png",
    ]
    spaceship2_images = [
        "assesories/spaceship5.png",
        "assesories/spaceship6.png",
        "assesories/spaceship7.png",
        "assesories/spaceship8.png",
        "assesories/spaceship9.png",
    ]

    selected_spaceship = 0
    selected_spaceship2 = 0

    while running:
        clock.tick(60)
        screen.fill(BLACK)
        
        title_text = get_font(80).render("SELECT PLAYER 1 SPACESHIP", True, "#b68f40")
        title_rect = title_text.get_rect(center=(640, 100))
        screen.blit(title_text, title_rect)

        # Render spaceship options
        for i, img_path in enumerate(spaceship_images):
            spaceship_img = pygame.image.load(img_path)
            x_pos = 250 + i * 200
            y_pos = 280
            spaceship_rect = spaceship_img.get_rect(center=(x_pos, y_pos))
            if i == selected_spaceship:
                pygame.draw.rect(screen, RED, spaceship_rect.inflate(20, 20), 5)  # Highlight selection
            screen.blit(spaceship_img, spaceship_rect)

        # Render spaceship2 options
        spaceship2_text = get_font(80).render("SELECT PLAYER 2 SPACESHIP", True, "#b68f40")
        spaceship2_rect = spaceship2_text.get_rect(center=(640, 450))
        screen.blit(spaceship2_text, spaceship2_rect)

        for i, img_path in enumerate(spaceship2_images):
            spaceship2_img = pygame.image.load(img_path)
            x_pos = 250 + i * 200
            y_pos = 600
            spaceship2_rect = spaceship2_img.get_rect(center=(x_pos, y_pos))
            if i == selected_spaceship2:
                pygame.draw.rect(screen, RED, spaceship2_rect.inflate(20, 20), 5)  # Highlight selection
            screen.blit(spaceship2_img, spaceship2_rect)

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
                    selected_spaceship2 = (selected_spaceship2 + 1) % len(spaceship2_images)
                elif event.key == pygame.K_UP:
                    selected_spaceship2 = (selected_spaceship2 - 1) % len(spaceship2_images)
                elif event.key == pygame.K_RETURN:  # Press Enter to confirm selection
                    return spaceship_images[selected_spaceship], spaceship2_images[selected_spaceship2]

        pygame.display.update()
