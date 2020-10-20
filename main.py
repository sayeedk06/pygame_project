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
pos_Ychange = 0

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
                pos_Xchange = -0.2
            if event.key == pygame.K_RIGHT:
                pos_Xchange = 0.2
            if event.key == pygame.K_UP:
                pos_Ychange = -0.2
            if event.key == pygame.K_DOWN:
                pos_Ychange = 0.2

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                pos_Xchange = 0
                pos_Ychange = 0

    x = x + pos_Xchange
    x = x + pos_Xchange
    y = y + pos_Ychange
    y = y + pos_Ychange

    if x <= 0:
        x = 0
    elif x >=736:
        x = 736
    elif y <= 0:
        y = 0
    elif y>= 536:
        y = 536
        
    playerPos(x,y)
    pygame.display.update()

# game loop ends here