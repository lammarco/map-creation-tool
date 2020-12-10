import pygame as pg
import json
from collections import namedtuple

Line = namedtuple('Line', ['pos_0', 'pos_1', 'color'])

#vars
lines = []
r = 8
d = 2*r
row = 51
col = 51

w = d * col
h = d * row
fps = 30

#colors
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,200,0)
sky_blue = (0,200,255)
blue = (0,0,255)
dark_red = (200,0,0)

grey = tuple(int(150*x/255) for x in white)
grey2 = tuple(int(100*x/255) for x in white)

#pg vars
screen = pg.display.set_mode([w, h])
clock = pg.time.Clock()

#defs
def DrawGrid():
    for x in range(r, w, d):
        pg.draw.line(screen, grey2, (x,0), (x, h))
    for y in range(r, w, d):
        pg.draw.line(screen, grey2, (0,y), (w, y))
    #draw center line
    pg.draw.line(screen,grey, (w/2,0), (w/2,h))
        
def DrawCursor(pos, color):
    pg.draw.circle(screen, color, pos, 5)

def DrawLines():
    for line in lines:
        pg.draw.line(screen, line[2], Matrix2Screen(line[0]), Matrix2Screen(line[1]),3)
        pg.draw.circle(screen, line[2], Matrix2Screen(line[0]), 3)
        pg.draw.circle(screen, line[2], Matrix2Screen(line[1]), 3)
                 
def SnapGrid(pos):
    return (round((pos[0]-r)/d)*d +r, round((pos[1]-r)/d)*d +r)

def SnapXYToGrid(x,y):
    return [round((x-r)/d)*d +r, round((y-r)/d)*d +r]

def Screen2Matrix(pos):
    return (int((pos[0]-w/2)/d), int(-pos[1]/d) + row - 1)

def Matrix2Screen(pos):
    return (pos[0]*d + w/2 ,(-pos[1] + row - 1)*d + r)

def Save(p:str = 'temp.txt'):
    if len(lines) <= 0:
        return
    try:
        with open(p,'w') as f:
            json.dump([l._asdict() for l in lines],f)
            print('Saved to', p)
    except Exception as e:
        print(type(e))

def Load(p:str = 'temp.txt'):
    try:
        Save()
        print(lines)
        with open(p,'r') as f:
            lines.clear()
            lines.extend([Line(tuple(l['pos_0']),tuple(l['pos_1']),tuple(l['color'])) for l in json.load(f)])
            #for line in lines:
                #if line[2] == (58, 94, 255):
                    #lines.append(Line(line[0],line[1],tuple(int(200*float(x/255) + 55) for x in blue)))
                    #lines.remove(line)
            print('Loaded', p)
        Refresh()
    except Exception as e:
        print(type(e), e)

def Refresh():
    screen.fill(black)
    DrawGrid()
    DrawLines()
