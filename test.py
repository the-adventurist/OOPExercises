import pygame as pg
from pygame import Surface

pg.init()

running = True
while running:
    screen = pg.display.set_mode((500, 500))
    pg.display.flip()
    rectangle = pg.draw.rect(screen, (13, 90, 89), rect, width=50, border_radius=0, border_top_right_radius=10)

pg.quit()