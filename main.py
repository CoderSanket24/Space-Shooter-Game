import pygame, sys
from functions import get_font,draw_gradient_background,Help
from classes import Button
from game import play1
from game2 import play2
from selectionScreen1 import selection_screen
from selectionScreen2 import selection_screen2

#initializes pygame module
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Black Color
BLACK = (0, 0, 0)

def main():
        running = True
        clock = pygame.time.Clock()

        while running:
                pygame.display.set_caption("Main Menu")
                clock.tick(60)
                screen.fill(BLACK)
                draw_gradient_background()

                Menu_Mouse_Pos = pygame.mouse.get_pos()
                
                MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
                MENU_RECT = MENU_TEXT.get_rect(center=(640, 80))

                MADE_BY_TEXT = get_font(30).render("Made By:", True, "#28b463")
                MADE_BY_RECT = MADE_BY_TEXT.get_rect(center=(1100, 400))
                screen.blit(MADE_BY_TEXT, MADE_BY_RECT)

                SANKET_TEXT = get_font(30).render("Sanket Botre (66)", True, "#b68f40")
                SANKET_RECT = SANKET_TEXT.get_rect(center=(1100, 450))
                screen.blit(SANKET_TEXT, SANKET_RECT)

                SANIKA_TEXT = get_font(30).render("Sanika Brahmankar (67)", True, "#b68f40")
                SANIKA_RECT = SANIKA_TEXT.get_rect(center=(1100, 500))
                screen.blit(SANIKA_TEXT, SANIKA_RECT)

                SUHANI_TEXT = get_font(30).render("Suhani Buche (68)", True, "#b68f40")
                SUHANI_RECT = SUHANI_TEXT.get_rect(center=(1100,550))
                screen.blit(SUHANI_TEXT,SUHANI_RECT)

                CHAITANYA_TEXT = get_font(30).render("Chaitanya Kulkarni 69)", True, "#b68f40")
                CHAITANYA_RECT = CHAITANYA_TEXT.get_rect(center=(1100,600))
                screen.blit(CHAITANYA_TEXT,CHAITANYA_RECT)

                KRUSHNA_TEXT = get_font(30).render("Krushnamegh Chakke (70)", True, "#b68f40")
                KRUSHNA_RECT = KRUSHNA_TEXT.get_rect(center=(1100,650))
                screen.blit(KRUSHNA_TEXT,KRUSHNA_RECT)
                
                
                SINGLEPLAYER_BUTTON = Button(image=pygame.image.load("assesories/options Rect.png"), pos=(640, 230), 
                                        text_input="SINGLEPLAYER", font=get_font(50), base_color="#d7fcd4", hovering_color="Yellow")
                MULTIPLAYER_BUTTON = Button(image=pygame.image.load("assesories/Options Rect.png"), pos=(640, 350), 
                                        text_input="MULTIPLAYER", font=get_font(50), base_color="#d7fcd4", hovering_color="Yellow")
                HELP_BUTTON = Button(image=pygame.image.load("assesories/Quit Rect.png"), pos=(640, 480), 
                                        text_input="HELP", font=get_font(50), base_color="#d7fcd4", hovering_color="Green")
                QUIT_BUTTON = Button(image=pygame.image.load("assesories/Quit Rect.png"), pos=(640, 610), 
                                        text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="Red")

                screen.blit(MENU_TEXT, MENU_RECT)
                
                for button in [SINGLEPLAYER_BUTTON, MULTIPLAYER_BUTTON, QUIT_BUTTON, HELP_BUTTON]:
                        button.changeColor(Menu_Mouse_Pos)
                        button.update(screen)

                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                running = False
                        elif event.type == pygame.MOUSEBUTTONDOWN: 
                                if SINGLEPLAYER_BUTTON.checkForInput(Menu_Mouse_Pos):
                                        Help()
                                        spaceship_image, asteroid_image = selection_screen()
                                        play1(spaceship_image, asteroid_image)
                                if MULTIPLAYER_BUTTON.checkForInput(Menu_Mouse_Pos):
                                        spaceship_image, spaceship2_image = selection_screen2()
                                        play2(spaceship_image, spaceship2_image)
                                if HELP_BUTTON.checkForInput(Menu_Mouse_Pos):
                                        Help()
                                if QUIT_BUTTON.checkForInput(Menu_Mouse_Pos):
                                        pygame.quit()
                                        sys.exit()
                
                pygame.display.update()
        pygame.quit()
        sys.exit()
if __name__ == "__main__":
    main()