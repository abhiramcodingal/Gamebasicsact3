import pygame

pygame.init()
screen = pygame.display.set_mode((300,400))

done = False
red = (255,0,0)
rectangle = pygame.Rect(150,150,100,50)

clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        rectangle.x -= 5
    if keys[pygame.K_RIGHT]:
        rectangle.x += 5
    if keys[pygame.K_UP]:
        rectangle.y -= 5
    if keys[pygame.K_DOWN]:
        rectangle.y += 5
    screen.fill((255,255,255))
    pygame.draw.rect(screen, red, rectangle)
    pygame.display.flip()
    clock.tick(30)

pygame.quit()