import pygame
import random

WIDTH, HEIGHT = 1280, 720

# Spaceship1 class
class Spaceship(pygame.sprite.Sprite):
    def __init__(self, image_path):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.center = (2*WIDTH // 3, HEIGHT - 50)
        self.speed_x = 0
        self.speed_Y = 0

    def update(self):
        self.speed_x = 0
        self.speed_Y = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.speed_x = -10
        if keys[pygame.K_RIGHT]:
            self.speed_x = 10
        if keys[pygame.K_UP]:
            self.speed_Y = -7
        if keys[pygame.K_DOWN]:
            self.speed_Y = 7
        self.rect.x += self.speed_x
        self.rect.y += self.speed_Y

        # Keep the spaceship within the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

# Spaceship2 class
class Spaceship2(pygame.sprite.Sprite):
    def __init__(self, image_path):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 3, HEIGHT - 50)
        self.speed_x = 0
        self.speed_Y = 0

    def update(self):
        self.speed_x = 0
        self.speed_Y = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.speed_x = -10
        if keys[pygame.K_d]:
            self.speed_x = 10
        if keys[pygame.K_w]:
            self.speed_Y = -7
        if keys[pygame.K_s]:
            self.speed_Y = 7
        self.rect.x += self.speed_x
        self.rect.y += self.speed_Y

        # Keep the spaceship within the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

# Asteroid class
class Asteroid(pygame.sprite.Sprite):
    def __init__(self,image_path,speed_factor=1.0):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speed_y = random.randrange(3, 8) * speed_factor

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.top > HEIGHT:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speed_y = random.randrange(1, 4)

    def increase_speed(self, speed_factor): 
        self.speed_y *= speed_factor

#Button class
class Button():
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color) 
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)
                  
#image button class
class ImageButton():
    def __init__(self, image, pos):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen):
        screen.blit(self.image, self.rect)

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

# Bullet class 
class Bullet(pygame.sprite.Sprite): 
    def __init__(self, x, y): 
        super().__init__() 
        self.image = pygame.image.load('assesories/bullet.png')
        self.rect = self.image.get_rect() 
        self.rect.centerx = x 
        self.rect.top = y 
        self.speed_y = -10 
    def update(self): 
         self.rect.y += self.speed_y 
         # Remove the bullet if it goes off screen 
         if self.rect.bottom < 0: 
              self.kill()