import pygame as pg
from MapUtils import *

global cursor_color,line_pos0
cursor_color = white
line_pos0 = []

def OnClick(mousepos):
    if pg.key.get_mods() & pg.KMOD_SHIFT:
        #print(mousepos)
        for l in lines:
            if mousepos == l[0]:
                line_pos0.append(l[1])
                lines.remove(l)
                return
            if mousepos == l[1]:
                line_pos0.append(l[0])
                lines.remove(l)
                return
    if len(line_pos0) > 0 and mousepos not in line_pos0:
        for p in line_pos0:
            lines.append(Line(p,mousepos,tuple(int(230*float(x/255) + 25) for x in cursor_color)))
        line_pos0.clear()
        return
    
    line_pos0.append(mousepos)

pg.init()

# Run until the user asks to quit
running = True
while running:
    
    pos = SnapGrid(pg.mouse.get_pos())
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONUP:
            OnClick(Screen2Matrix(pos))
            
            #print("Mouse Click ", pos, Screen2Matrix(pos))
        if event.type == pg.KEYUP:
            if (event.key == pg.K_e and
                pg.key.get_mods() & pg.KMOD_SHIFT and
                pg.key.get_mods() & pg.KMOD_CTRL):
                print(lines)
                lines.clear()
            if event.key == pg.K_d:
                if pg.key.get_mods() & pg.KMOD_CTRL and len(lines) > 0:
                    print(lines.pop())
                if not pg.key.get_mods() & pg.KMOD_CTRL and len(line_pos0) > 0:
                    print(line_pos0)
                    line_pos0.clear()
            
            if len(line_pos0) > 0:
                if event.key == pg.K_1:
                    cursor_color = white
                if event.key == pg.K_2:
                    cursor_color = red
                if event.key == pg.K_3:
                    cursor_color = green
                if event.key == pg.K_4:
                    cursor_color = sky_blue
                if event.key == pg.K_5:
                    cursor_color = blue
                if event.key == pg.K_6:
                    cursor_color = dark_red
            else:
                if event.key == pg.K_s and pg.key.get_mods() & pg.KMOD_SHIFT:
                    Save()
                if event.key == pg.K_l and pg.key.get_mods() & pg.KMOD_SHIFT:
                    Load()
                if event.key == pg.K_1:
                    if pg.key.get_mods() & pg.KMOD_SHIFT:
                        Save('1.txt')
                    elif pg.key.get_mods() & pg.KMOD_CTRL:
                        Load('1.txt')
                    else:
                        cursor_color = white
                if event.key == pg.K_2:
                    if pg.key.get_mods() & pg.KMOD_SHIFT:
                        Save('2.txt')
                    elif pg.key.get_mods() & pg.KMOD_CTRL:
                        Load('2.txt')
                    else:
                        cursor_color = red
                if event.key == pg.K_3:
                    if pg.key.get_mods() & pg.KMOD_SHIFT:
                        Save('3.txt')
                    elif pg.key.get_mods() & pg.KMOD_CTRL:
                        Load('3.txt')
                    else:
                        cursor_color = green
                if event.key == pg.K_4:
                    if pg.key.get_mods() & pg.KMOD_SHIFT:
                        Save('4.txt')
                    elif pg.key.get_mods() & pg.KMOD_CTRL:
                        Load('4.txt')
                    else:
                        cursor_color = sky_blue
                if event.key == pg.K_5:
                    cursor_color = blue
                if event.key == pg.K_6:
                    cursor_color = dark_red
                
            
    Refresh()
    if len(line_pos0) > 0:
        for p in line_pos0:
            pg.draw.line(screen, cursor_color, Matrix2Screen(p), pos)
    DrawCursor(pos, cursor_color)
    #print(Screen2Matrix(pos),flush=True,end='\r')
    pg.display.set_caption(f'MiniMap Creator v1.0 {str(Screen2Matrix(pos))}')
    pg.display.update()
    clock.tick(fps)

pg.quit()
print(lines)
Save()
