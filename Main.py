import pygame
pygame.init()
from Screen import *
import Cube
pygame.display.flip()
running = True
R1 = Cube.Cube(50,50,[800,600],(20,30,40))
clock = pygame.time.Clock()
screen.fill((2,255,255))
fonte = pygame.font.SysFont("arial",30)

font_color = (20, 30, 40)
has_pressed = False
mouse= pygame.mouse.get_pos()
while running:
    delta = clock.tick()
    prev_mouse = mouse
    mouse = pygame.mouse.get_pos()
    screen.fill((20, 25, 255))
    if R1.mouse_tracking:
        if pygame.mouse.get_pressed(3)[0]:
            R1.update_position_mouse(delta, mouse, prev_mouse)
            
        else:
            mouse_tracking = False
            R1.update_position(delta)
    elif  pygame.mouse.get_pressed(3)[0] and R1.rectangle.collidepoint(mouse[0],mouse[1]):
        R1.mouse_tracking = True

        R1.update_position_mouse(delta, mouse, mouse)
    else:
        mouse_tracking = False
        R1.update_position(delta)
    ax = fonte.render("Acceleration X " + str(R1.acceleration[0])+ " m/s^2",False,font_color)
    ay = fonte.render("Acceleration Y " + str(-1*R1.acceleration[1])+ " m/s^2", False, font_color)
    vx = fonte.render("Velocity X " + str(int(R1.velocity[0]))+ " m/s", False, font_color)
    vy = fonte.render("Velocity Y " + str(-1*int(R1.velocity[1]))+ " m/s", False, font_color)
    ke = fonte.render("Kinetic Energy " + str(int(R1.getKE())) + " J", False, font_color)
    screen.blit(ax,(20,20))
    screen.blit(ay, (20, 120))
    screen.blit(vx, (20, 220))
    screen.blit(vy, (20, 320))
    screen.blit(ke,(20,420))
    R1.paste()
    pygame.display.flip()

    # for loop through the event queue
    for event in pygame.event.get():

        # Check for QUIT event
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                running = False




