import pygame, sys
from functions import get_font
from classes import Button

pygame.init()
white = (255, 255, 255)
# Screen dimensions
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
BG1 = pygame.Surface((WIDTH,HEIGHT))
BG1.fill(white)

def score_window(player_score,high_score,bullets_fired=0):
    clock = pygame.time.Clock()
    pygame.display.set_caption("Score Window")
    screen.blit(BG1,(0,0))

    #GAME OVER TEXT
    GAME_OVER_TEXT = get_font(100).render("GAME OVER", True, "#b68f40")
    GAME_OVER_RECT = GAME_OVER_TEXT.get_rect(center=(640, 100))
    screen.blit(GAME_OVER_TEXT, GAME_OVER_RECT)

    #YOUR SCORE
    YOUR_SCORE_TEXT = get_font(50).render(f"YOUR SCORE:{player_score}", True, "#b68f40")
    YOUR_SCORE_RECT = YOUR_SCORE_TEXT.get_rect(center=(640, 400))
    screen.blit(YOUR_SCORE_TEXT,YOUR_SCORE_RECT)

    #HIGH SCORE
    HIGH_SCORE_TEXT = get_font(60).render(f"HIGH SCORE:{high_score}", True, "#b68f40")
    HIGH_SCORE_RECT = HIGH_SCORE_TEXT.get_rect(center=(640, 250))
    screen.blit(HIGH_SCORE_TEXT,HIGH_SCORE_RECT)

    bullet_text = get_font(50).render(f"BULLETS FIRED:{bullets_fired}", True, "#b68f40")
    bullet_rect = bullet_text.get_rect(center=(640, 500))
    screen.blit(bullet_text,bullet_rect)

    while True:
        Menu_Mouse_Pos = pygame.mouse.get_pos()
        
        #RESTART BUTTON
        RESTART_BUTTON = Button(image=pygame.image.load("assesories/Quit Rect.png"), pos=(425, 650), 
                                text_input="RESTART", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        RESTART_BUTTON.changeColor(Menu_Mouse_Pos)
        RESTART_BUTTON.update(screen)
        
        #Quit button
        QUIT_BUTTON = Button(image=pygame.image.load("assesories/Quit Rect.png"), pos=(855, 650), 
                                text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON.changeColor(Menu_Mouse_Pos)
        QUIT_BUTTON.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if RESTART_BUTTON.checkForInput(Menu_Mouse_Pos):
                    return True
                elif QUIT_BUTTON.checkForInput(Menu_Mouse_Pos):
                    return False
            
        pygame.display.flip()
        clock.tick(60)
