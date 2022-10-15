from Screen import fps,screen
import pygame
import math
class Cube:
    def __init__(self,width,height,position,color):
        self.width = width
        self.height = height
        self.position = position
        self.velocity = [0,0]
        self.acceleration = [0,9.8081]
        self.rectangle = pygame.Rect(self.position[0] - self.width/2,self.position[1] - self.height/2,self.width,self.height)
        self.color = color
        self.mouse_tracking = False
        self.mass = 1


    def update_position(self,delta):
            self.velocity[0] += self.acceleration[0] * delta/1000
            self.velocity[1] += self.acceleration[1]* delta/1000
            self.position[0] += self.velocity[0]* delta/1000
            self.position[1] += self.velocity[1]* delta/1000
            self.borders()
            self.rectangle = pygame.Rect(self.position[0] - self.width / 2, self.position[1] - self.height / 2, self.width, self.height)


    def update_position_mouse(self,delta,mouse_pos,prev_mouse_pos):
        self.position = list(pygame.mouse.get_pos())
        self.velocity[0] = mouse_pos[0] - prev_mouse_pos[0]
        self.velocity[1] =  prev_mouse_pos[1] - mouse_pos[1]
        self.borders()
        self.rectangle = pygame.Rect(self.position[0] - self.width / 2, self.position[1] - self.height / 2,self.width, self.height)


    def paste(self):
        pygame.draw.rect(screen, self.color,self.rectangle)

    def borders(self):
        if self.position[0] < 0 +self.width/2:
            self.position[0] = 0 +self.width/2
            self.velocity[0] = 0

        elif self.position[0] > 1920 -self.width/2:
            self.position[0] = 1920 -self.width/2
            self.velocity[0] = 0

        if self.position[1] < 0 +self.height/2:
            self.position[1] = 0 +self.height/2
            self.velocity[1] = 0

        elif self.position[1] > 1080 -self.height/2:
            self.position[1] = 1080 -self.height/2
            self.velocity[1] = 0

    def getKE(self):
        totVel = math.sqrt((self.velocity[0]**2) + (self.velocity[1]**2))
        return (.5) * (self.mass) * (totVel**2)
