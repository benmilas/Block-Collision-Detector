import pygame

pygame.init()
WIDTH, HEIGHT = (1000, 500)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Collision Simulation")

# dimensions of box1
mass1 = 2
x1 = 600
y1 = 400
dx1 = -1
width1 = 100
height1 = 100


# dimensions of box2
mass2 = 1
x2 = 400
y2 = 400
dx2 = 0
width2 = 100
height2 = 100

# dimensions of wall
x3 = 0
y3 = 0
width3 = 20
height3 = 500

# collision counter
collisions = 0

FPS = 120
run = True
clock = pygame.time.Clock()

while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill((0, 0, 0))
    box1 = pygame.draw.rect(win, WHITE, (int(x1), y1, width1, height1))
    box2 = pygame.draw.rect(win, WHITE, (int(x2), y2, width2, height2))
    wall = pygame.draw.rect(win, WHITE, (x3, y3, width3, height3))
    pygame.font.init()
    header = pygame.font.SysFont(pygame.font.get_default_font(), 30)
    boxlabel = pygame.font.SysFont(pygame.font.get_default_font(), 20)
    collisionslabel = header.render('Collisions: ' + str(collisions), False, WHITE)
    box1label = boxlabel.render(str(mass1) + ' kg', False, BLACK)
    box2label = boxlabel.render(str(mass2) + ' kg', False, BLACK)
    win.blit(collisionslabel, (825, 10))
    win.blit(box1label, box1.center)
    win.blit(box2label, box2.center)

    # update position with direction
    x1 += dx1
    x2 += dx2

    # check bounds
    if x1 <= width3:
        collisions += 1
        dx1 = -dx1
    pygame.display.update()
    if x2 <= width3:
        collisions += 1
        dx2 = -dx2
    pygame.display.update()
    if x1 - x2 <= box2.width:
        collisions += 1
        temp = dx1
        dx1 = ((mass1 - mass2) / (mass1 + mass2)) * dx1 + ((2 * mass2) / (mass1 + mass2)) * dx2
        dx2 = ((2 * mass1) / (mass1 + mass2)) * temp + ((mass2 - mass1) / (mass1 + mass2)) * dx2
    pygame.display.update()







        

