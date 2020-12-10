import pygame as pg
from MapUtils import *

pg.init()
Load()
Refresh()
# Run until the user asks to quit
running = True
while running:
    pos = SnapGrid(pg.mouse.get_pos())
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYUP:
            if event.key == pg.K_0:
                pg.image.save(screen, "screenshot.png")
            if event.key == pg.K_l:
                Load()
            if event.key == pg.K_1:
                Load('1.txt')
            if event.key == pg.K_2:
                Load('2.txt')
            if event.key == pg.K_3:
                Load('3.txt')
            if event.key == pg.K_4:
                Load('4.txt')
         
    #pygame.display.flip()
    pg.display.update()
    clock.tick(fps)

pg.quit()
#print(lines)
