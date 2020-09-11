# A simple python snake game
# Easy to code and learn
# Uses simple functions, variables and is fun to code

# importations
import tkinter as tk
import math
import random
import pygame
from tkinter import messagebox

from pygame import surface

# Class definition
class cube(object):
    rows = 0
    w = 0
    def _init_(self, start, dirnx = 1, dirny = 0, color = (255, 0, 0)):
        pass

    def move(self, dirnx, dirny):
        pass

    def draw(self, surface, eyes = False):
        pass

class snake(object):
    body = []
    turns = {}
    def __init__(self, color, pos):
        self.color = color
        self.head = cube(pos)
        self.body.append(self.head)
        self.dirnx = 0
        self.dirny = 1
    
    def move(self):
        pass

    def reset(self, pos):
        pass

    def addCube(self):
        pass

    def draw(self, surface):
        pass


def drawGrid(w, rows, surface):
    sizeBtwn = w // rows

    x = 0
    y = 0
    for l in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn

        pygame.draw. line(surface, (255,255, 255), (x, 0), (x, w))
        pygame.draw. line(surface, (255,255, 255), (0, y), (w, y))
    

def redrawWindow(surface):
    global rows, width
    surface.fill((0, 0, 0))
    drawGrid(width, rows, surface)
    pygame.display.update()

def randomSnack(rows, items):
    pass

def message_box(subject, content):
    pass

# The main loop of the game
def main():
    global width, rows
    width = 500
    rows = 20
    win = pygame.display.set_mode((width, width))
    s = snake((255, 0, 0), (10, 10))
    flag = True
    clock = pygame.time.Clock()

    # The while loop
    while flag:
        pygame.time.delay(50)
        clock.tick(10)

        redrawWindow(win)

    pass

main()