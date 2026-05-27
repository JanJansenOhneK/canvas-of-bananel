
import math

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

def draw_title():
    screen.fill((255,255,255))
    screen.blit(font("CANVAS",80),surf_cent(font("CANVAS",80),(math.sin(framecount/200)*3+350,math.sin(framecount/140)*1+50)))
    screen.blit(font("OF",80),surf_cent(font("OF",80),(math.sin(framecount/160)*1+350,math.sin(framecount/220)*3+150)))
    screen.blit(font("BANANEL",80),surf_cent(font("BANANEL",80),(math.cos(framecount/180)*3+350,math.cos(framecount/120)*4+250)))

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_title()
    pygame.display.flip()

    framecount += 1

pygame.quit()