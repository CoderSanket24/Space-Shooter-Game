import pygame,sys
from pygame import mixer
from classes import ImageButton

pygame.init()

WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Score
font_score = pygame.font.Font(None, 32)

def get_font(size): 
    # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assesories/Cyberpunks Italic.ttf", size)

def help_font(size):
    return pygame.font.Font(None, size)

def paused_fn():
        clock = pygame.time.Clock()
        #background
        button_rect = pygame.Rect(490, 310, 300, 100)

        # Pause button
        Pause_button = ImageButton(image=pygame.image.load('assesories/play.png'),pos=(640,360))
        # quit button
        Quit_button = ImageButton(image=pygame.image.load('assesories/cross.png'),pos=(740,360))
        # help button
        Help_button = ImageButton(image=pygame.image.load('assesories/interrogation.png'),pos=(540,360))

        while True:
             Menu_Mouse_Pos = pygame.mouse.get_pos()
             
             screen.fill((255,255,255))
             pygame.draw.rect(screen, (255,255,255), button_rect)
             Pause_button.update(screen)
             Quit_button.update(screen)
             Help_button.update(screen)

             for event in pygame.event.get():
                 if event.type == pygame.QUIT:
                     pygame.quit()
                     sys.exit()

                 if event.type == pygame.KEYDOWN:
                     if event.key == pygame.K_p:
                         return True
                     
                 elif event.type == pygame.MOUSEBUTTONDOWN:
                     if Pause_button.checkForInput(Menu_Mouse_Pos):
                         return True
                     elif Quit_button.checkForInput(Menu_Mouse_Pos):
                        return False
                     elif Help_button.checkForInput(Menu_Mouse_Pos):
                        Help()
                     
             pygame.display.flip()
             clock.tick(60)

def Help():
    screen.fill((255,255,255))

    SCROLL_SPEED = 20  # Number of pixels per scroll
    content_height = 1100  # Total height of the content
    viewport_height = 720  # Height of the screen
    scroll_offset = 0  # Initial scroll offset

    Help_Manual = get_font(50).render("Help Manual", True, (0,0,0))
    Help_Manual_Rect = Help_Manual.get_rect(center=(640,50))

    instructions = [
        "Single Player Manual:",
        "1.To select spaceship press 'left' or 'right' arrow keys.",
        "2.To select asteroid press 'up' or 'down' arrow keys.",
        "3.Press 'Enter' to start the game.",
        "4.Use arrow keys to move and SPACE to shoot.",
        "5.Press 'P' to pause the game.",
        "6.Levels are based on score.",
        "7.Level increases at every 50 points.",
        "",
        "Multi Player Manual:",
        "1.To select spaceship press 'left' or 'right' arrow keys for player 1 and 'up' or 'Down' arrow keys for player 2.",
        "2.Press 'Enter' to start the game.",
        "3.For Player 1 Use 'WASD KEYS' to move and 'f' to shoot.",
        "4.For Player 2 Use 'ARROW KEYS' to move and 'Backspace' to shoot.",
        "5.Press 'P' to pause the game.",
        "6.Levels are based on time.",
        "7.Level increases at every 30 seconds.",
        "",
        "Enjoy the game!",
        "",
        "press Escape key to quit.",
    ]

    def draw_content(offset):
        """Draws the content of the help screen with the given scroll offset."""
        screen.fill((255, 255, 255))
        screen.blit(Help_Manual, (Help_Manual_Rect.x, Help_Manual_Rect.y - offset))

        for i, text in enumerate(instructions):
            line = help_font(30).render(text, True, (0, 0, 0))
            screen.blit(line, (100, 150 + i * 50 - offset))


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Press ESC to return
                    return
                elif event.key == pygame.K_DOWN:  # Scroll down
                    scroll_offset = min(scroll_offset + SCROLL_SPEED, content_height - viewport_height)
                elif event.key == pygame.K_UP:  # Scroll up
                    scroll_offset = max(scroll_offset - SCROLL_SPEED, 0)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:  # Mouse wheel up
                    scroll_offset = max(scroll_offset - SCROLL_SPEED, 0)
                elif event.button == 5:  # Mouse wheel down
                    scroll_offset = min(scroll_offset + SCROLL_SPEED, content_height - viewport_height)

        draw_content(scroll_offset)
        pygame.display.update()

def show_bullets_fired(fired_bullets):
    score = font_score.render("Bullets Fired : "+ str(fired_bullets),True,(255,255,255))
    screen.blit(score, (10, 40))

def show_bullets1(fired_bullets):
    score = font_score.render("Bullets Fired : "+ str(fired_bullets),True,(255,255,255))
    screen.blit(score, (1100, 40))

def show_bullets2(fired_bullets):
    score = font_score.render("Bullets Fired : "+ str(fired_bullets),True,(255,255,255))
    screen.blit(score, (10, 40))
            
def show_high_score(High_score):
     score = font_score.render("High Score : "+ str(High_score),True,(255,255,255))
     screen.blit(score, (1100,10))

def show_score2(score_value):
    score = font_score.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (10, 10))

def show_score1(score_value):
    score = font_score.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (1100, 10))

def show_level(level):
    score = font_score.render("Level : " + str(level), True, (255, 255, 255))
    screen.blit(score, (600, 10))


def draw_gradient_background():
    """Draw a dark gradient background."""
    for y in range(HEIGHT):
        gradient_color = (y * 255 // HEIGHT, 0, 128)
        pygame.draw.line(screen, gradient_color, (0, y), (WIDTH, y))

def fade_out(screen, color=(0, 0, 0), speed=5):
    fade_surface = pygame.Surface((WIDTH, HEIGHT))
    fade_surface.fill(color)
    for alpha in range(0, 255, speed):
        fade_surface.set_alpha(alpha)
        screen.blit(fade_surface, (0, 0))
        pygame.display.update()
        pygame.time.delay(10)  # Controls the fade speed

def countdown(screen, countdown_from=3):
    font = get_font(75)  # Use your font function
    for i in range(countdown_from, 0, -1):
        screen.fill((0, 0, 0))  # Clear the screen
        countdown_text = font.render(f"Restarting in {i}...", True, (255, 255, 255))
        countdown_rect = countdown_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(countdown_text, countdown_rect)
        pygame.display.update()
        pygame.time.wait(1000)  # Wait for 1 second

def pushpa_music():
    music = mixer.Sound("assesories/pushpa_jhukega_nahi.wav")
    music.play()
