import pygame

pygame.init()

screen = pygame.display.set_mode((900, 650))

pygame.display.set_caption("Basic Games")
icon = pygame.image.load('rockicon.png')
pygame.display.set_icon(icon)

#Pointer
pointer_image  = pygame.image.load('pointericon.png').convert_alpha()
pointer_image = pygame.transform.scale(pointer_image, (20, 20))
pointer_x = 450
pointer_y = 325
pointer_x_change = 0
pointer_y_change = 0

def pointer(x,y):
    screen.blit(pointer_image, (x,y))

# Game Loop, make sure window doesn't close. All events inside
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pointer_x_change = -0.5
            if event.key == pygame.K_RIGHT:
                pointer_x_change = 0.5
            if event.key == pygame.K_UP:
                pointer_y_change = -0.5
            if event.key == pygame.K_DOWN:
                pointer_y_change = 0.5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                pointer_x_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                pointer_y_change = 0
    screen.fill((150, 200, 45))
    pointer_x += pointer_x_change
    pointer_y += pointer_y_change
    pointer(pointer_x, pointer_y)
    pygame.display.update()