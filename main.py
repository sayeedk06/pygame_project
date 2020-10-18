import pygame

pygame.init()

# create a display screen
screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Space game")


player = pygame.image.load("image/player.png")

# player cordinates
x = 370
y = 480

pos_Xchange = 0

def playerPos(playerX=x, playerY=y):
    screen.blit(player,(playerX, playerY))

game_loop = True

# game loop stars here
while game_loop:

    # background color
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pos_Xchange = -0.1
            if event.key == pygame.K_RIGHT:
                pos_Xchange = 0.1
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                pos_Xchange = 0

    x = x + pos_Xchange
    x = x + pos_Xchange
    playerPos(x,y)
    pygame.display.update()

# game loop ends here