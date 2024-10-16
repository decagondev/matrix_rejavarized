import pygame
import random

japanese_chars = "アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲンガギグゲゴザジズゼゾダヂヅデドバビブベボパピプペポ一二三四五六七八九十山川田木村花雨火水日月星空雲電風神"

class FallingText:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.font_size = random.randint(20, 30)
        self.font = pygame.font.SysFont('arial', self.font_size, True)
        self.opacity = random.randint(50, 255)  
        self.opacity_change = random.uniform(-2, 2)  
        self.char = random.choice(japanese_chars)  
        self.change_interval = random.randint(3, 10)  
        self.counter = 0  

    def update(self):
        self.y += self.speed
        if self.y > screen_height:
            self.y = random.randint(-100, -50)
            self.speed = random.uniform(5, 12)  

        self.opacity += self.opacity_change
        if self.opacity > 255:
            self.opacity = 255
            self.opacity_change = random.uniform(-2, -0.5)
        elif self.opacity < 50:
            self.opacity = 50
            self.opacity_change = random.uniform(0.5, 2)

        self.counter += 1
        if self.counter >= self.change_interval:
            self.char = random.choice(japanese_chars)
            self.counter = 0  

    def draw(self, screen):
        green_color = (0, 255, 0)
        text_surface = self.font.render(self.char, True, green_color)
        text_surface.set_alpha(self.opacity)  
        
        screen.blit(text_surface, (self.x, self.y))

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Matrix Code Screen Saver")

falling_texts = []
for i in range(300):  
    x_pos = random.randint(0, screen_width - 20)
    y_pos = random.randint(-500, -50)
    speed = random.uniform(5, 12)  
    falling_texts.append(FallingText(x_pos, y_pos, speed))

running = True
clock = pygame.time.Clock()

while running:
    screen.fill((0, 0, 0))  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for text_obj in falling_texts:
        text_obj.update()
        text_obj.draw(screen)

    pygame.display.flip()
    clock.tick(30)  

pygame.quit()

