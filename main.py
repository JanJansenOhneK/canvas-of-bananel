
import math
import random
import title_particle

import pygame
pygame.init()
screen = pygame.display.set_mode((700,700))
pygame.display.set_caption("Canvas of Bananel")
running = True
framecount = 0


def font(text:str,size:int) -> pygame.Surface:
    return pygame.font.SysFont("xanhmono",size).render(text,False,(0,0,0))
def surf_cent(surface:pygame.Surface,pos:tuple[int]) -> int:
    return (pos[0] - surface.get_width()/2,pos[1]) 

title_particles = []
def init_title():
    # create da particles
    for i in range(random.randint(50,70)):
        title_particles.append(title_particle.TitleParticle(
            [random.randint(0,700),random.randint(0,700)],
            [random.randint(-4,4)/100,random.randint(-4,4)/100],
            random.randint(60,80)/100,
            random.randint(5,10)
        ))


def draw_title():
    # make da white screen
    screen.fill((255,255,255))

    # render da particles
    for particle in title_particles:
        particle.frame()
        pygame.draw.circle(
            screen,
            (particle.alpha*255, particle.alpha*255, particle.alpha*255),
            particle.pos,
            particle.size/2
        )

    # make da text
    screen.blit(font("CANVAS",80),surf_cent(font("CANVAS",80),(math.sin(framecount/200)*6+350,math.sin(framecount/140)*2+50)))
    screen.blit(font("OF",80),surf_cent(font("OF",80),(math.sin(framecount/160)*2+350,math.sin(framecount/220)*6+150)))
    screen.blit(font("BANANEL",80),surf_cent(font("BANANEL",80),(math.cos(framecount/180)*6+350,math.cos(framecount/120)*8+250)))

init_title()

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(font("FC:",10),surf_cent(font("BANANEL",80)))

    draw_title()    
    pygame.display.flip()
    framecount += 1

pygame.quit()