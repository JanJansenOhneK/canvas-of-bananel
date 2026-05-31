
import math
import random
import etccode.title_particle as title_particle

import pygame
pygame.init()
screen = pygame.display.set_mode((700,700))
pygame.display.set_caption("Canvas of Bananel")
clock = pygame.time.Clock()
running = True
framecount = 0

save = open("saves/save0.cobl","w+")

def font(text:str,size:int) -> pygame.Surface:
    return pygame.font.SysFont("xanhmono",size).render(text,False,(0,0,0))
def surf_cent(surface:pygame.Surface,pos:tuple[int,int]) -> tuple[int,int]:
    return (pos[0] - surface.get_width()/2,pos[1]) 

title_particles = []
def init_title():
    # create da particles
    for i in range(random.randint(50,70)):
        title_particles.append(title_particle.TitleParticle(
            [random.randint(0,700),random.randint(0,700)],
            [random.randint(-40,40)/100,random.randint(-40,40)/100],
            random.randint(80,90)/100,
            random.randint(5,10)
        ))

class TitleButton:
    def __init__(self,text:str,selectable:bool = True):
        self.text = text
        self.selectable = selectable
class TitleMenu:
    def __init__(self,buttons:dict,logo:bool=False):
        self.buttons = buttons
        self.logo = logo

title_selbutton = 0
title_menu = 0
title_logo = True

def menu_change(menu:int):
    global title_selbutton, title_menu
    title_selbutton = 0
    title_menu = menu

def tb0_settings():
    print("settings opened")
    global title_menu
    menu_change(1)
def tb0_quit():
    print("quitted by title options")
    global running
    running = False
def tb1_back():
    print("backed to main menu")
    global title_menu
    menu_change(0)

title_menus = [
    TitleMenu(   # main menu
        {
            TitleButton("Settings"):tb0_settings,
            TitleButton("Quit"):tb0_quit
        },True
    ),TitleMenu( # settings
        {
            TitleButton("Back"):tb1_back
        }
    )
]

title_buttons = {}

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
    if title_logo:
        screen.blit(font("CANVAS",80),surf_cent(font("CANVAS",80),(math.sin(framecount/40)*6+350,math.sin(framecount/30)*2+50)))
        screen.blit(font("OF",80),surf_cent(font("OF",80),(math.sin(framecount/30)*2+350,math.sin(framecount/40)*6+150)))
        screen.blit(font("BANANEL",80),surf_cent(font("BANANEL",80),(math.cos(framecount/40)*6+350,math.cos(framecount/20)*8+250)))

    # make da buttons
    if title_logo:
        i = 0
        for button in title_buttons:
            if i == title_selbutton and button.selectable:
                screen.blit(
                    font(f">> {button.text} <<",40),
                    surf_cent(font(f">> {button.text} <<",40),(350,400+(i*50) ))
                )
            else:
                screen.blit(
                    font(f"{button.text}",40),
                    surf_cent(font(f"{button.text}",40),(350,400+(i*50) ))
                    
                )
            i += 1
    else:
        i = 0
        for button in title_buttons:
            if i == title_selbutton and button.selectable:
                screen.blit(
                    font(f">> {button.text} <<",40),
                    surf_cent(font(f">> {button.text} <<",40),(350,20+(i*50) ))
                )
            else:
                screen.blit(
                    font(f"{button.text}",40),
                    surf_cent(font(f"{button.text}",40),(350,20+(i*50) ))
                    
                )
            i += 1

init_title()

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("quitted by closing window")
            running = False

        elif event.type == pygame.MOUSEWHEEL:
            if event.y > 0:   # scroll up
                title_selbutton -= 1
                while not list(title_buttons.keys())[title_selbutton].selectable:
                    title_selbutton -= 1
            elif event.y < 0: # scroll down
                title_selbutton += 1
                while not list(title_buttons.keys())[title_selbutton].selectable:
                    title_selbutton += 1
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == pygame.BUTTON_LEFT:
                list(title_buttons.values())[title_selbutton]()

        elif event.type == pygame.KEYDOWN:
            pass

    title_buttons = title_menus[title_menu].buttons
    title_logo = title_menus[title_menu].logo

    title_selbutton = title_selbutton % len(title_buttons)

    draw_title()    
    screen.blit(font(f"FC: {framecount} FPS: {round(clock.get_fps()*100)/100}",10),(0,0))
    pygame.display.flip()

    framecount += 1
    clock.tick(60)

pygame.quit()