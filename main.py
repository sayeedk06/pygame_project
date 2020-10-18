import pygame

pygame.init()

# create a display screen
screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Space game")

game_loop = True

while game_loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False

    screen.fill((255,255,255))
    pygame.display.update()