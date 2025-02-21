import pygame,sys
from functions import get_font
from classes import Button

pygame.init()
white = (255, 255, 255)
# Screen dimensions
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
BG1 = pygame.Surface((WIDTH,HEIGHT))
BG1.fill(white)

def winner_window(player1_score,player2_score,bullets_fired1,bullets_fired2):
    clock = pygame.time.Clock()
    pygame.display.set_caption("Winner Window")
    screen.blit(BG1,(0,0))

    #GAME OVER TEXT
    GAME_OVER_TEXT = get_font(80).render("GAME OVER", True, "#b68f40")
    GAME_OVER_RECT = GAME_OVER_TEXT.get_rect(center=(640, 100))
    screen.blit(GAME_OVER_TEXT, GAME_OVER_RECT)

    #PLAYER1 SCORE
    PLAYER1_SCORE_TEXT = get_font(40).render(f"Player 1 SCORE:{player1_score}", True, "#b68f40")
    PLAYER1_SCORE_RECT = PLAYER1_SCORE_TEXT.get_rect(center=(300, 250))
    screen.blit(PLAYER1_SCORE_TEXT,PLAYER1_SCORE_RECT)

    #PLAYER2 SCORE
    PLAYER2_SCORE_TEXT = get_font(40).render(f"Player 2 SCORE:{player2_score}", True, "#b68f40")
    PLAYER2_SCORE_RECT = PLAYER2_SCORE_TEXT.get_rect(center=(950, 250))
    screen.blit(PLAYER2_SCORE_TEXT,PLAYER2_SCORE_RECT)

    #PLAYER1 BULLETS FIRED
    PLAYER1_BULLETS_FIRED_TEXT = get_font(40).render(f"Player 1 BULLETS FIRED:{bullets_fired1}", True, "#b68f40")
    PLAYER1_BULLETS_FIRED_RECT = PLAYER1_BULLETS_FIRED_TEXT.get_rect(center=(300, 350))
    screen.blit(PLAYER1_BULLETS_FIRED_TEXT,PLAYER1_BULLETS_FIRED_RECT)

    #PLAYER2 BULLETS FIRED
    PLAYER2_BULLETS_FIRED_TEXT = get_font(40).render(f"Player 2 BULLETS FIRED:{bullets_fired2}", True, "#b68f40")
    PLAYER2_BULLETS_FIRED_RECT = PLAYER2_BULLETS_FIRED_TEXT.get_rect(center=(950, 350))
    screen.blit(PLAYER2_BULLETS_FIRED_TEXT,PLAYER2_BULLETS_FIRED_RECT)

    if player1_score > player2_score:
        Player = "Player 1"
    elif player1_score == player2_score:
        if bullets_fired1 < bullets_fired2:
            Player = "Player 1"
        else:
            Player = "Player 2"
    else:
        Player = "Player 2"

    #winner
    winner_TEXT = get_font(50).render(f"Winner is {Player}", True, "#b68f40")
    winner_RECT = winner_TEXT.get_rect(center=(640, 500))
    screen.blit(winner_TEXT,winner_RECT)

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
