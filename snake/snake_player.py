# author: smilu97
# description: simple snake game

import pygame as pg
import sys
from .core import SnakeGame

red = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)

class SnakePlayer:

    def __init__(self,
        sc_width=800,
        sc_height=800,
        block_sz=40,
        caption='Simple Snake Game',
        fps=10):
        self.sc_width = sc_width
        self.sc_height = sc_height
        self.block_sz = block_sz
        self.caption = caption
        self.fps = fps
        self.max_x = int(sc_width / block_sz - 1)
        self.max_y = int(sc_height / block_sz - 1)
        self.core = SnakeGame(max_x=self.max_x, max_y=self.max_y)
    
    def run(self):
        '''
        SnakeGame.run
        '''
        pg.init()
        pg.display.set_caption(self.caption)
        self.screen = pg.display.set_mode((self.sc_width, self.sc_height))
        self.clock = pg.time.Clock()

        while True:
            self.clock.tick(self.fps)

            action = ''
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_LEFT:
                        action = 'left'
                    elif event.key == pg.K_RIGHT:
                        action = 'right'
                    elif event.key == pg.K_UP:
                        action = 'up'
                    elif event.key == pg.K_DOWN:
                        action = 'down'
                    elif event.key == pg.K_r:
                        if self.core.gameover:
                            self.core.reset()
                    elif event.key == pg.K_q:
                        sys.exit()
            
            self.core.next(action)
            
            self.screen.fill(black)
            self.render()
            pg.display.update()
    
    def draw_rect(self, x, y, color=white):
        rct = (x * self.block_sz,
            y * self.block_sz,
            self.block_sz,
            self.block_sz)
        pg.draw.rect(self.screen, color, rct)
    
    def draw_grid(self):
        sz = self.block_sz
        gray = (125, 125, 125)
        for x in range(0, int(self.max_x * sz) + sz + 1, sz):
            pg.draw.line(self.screen, gray, (x, 0), (x, self.sc_height), 1)
        for y in range(0, int(self.max_y * sz) + sz + 1, sz):
            pg.draw.line(self.screen, gray, (0, y), (self.sc_width, y), 1)
    
    def render(self):
        self.draw_grid()
        for pos in self.core.trails:
            self.draw_rect(*pos)
        self.draw_rect(self.core.x, self.core.y)
        self.draw_rect(self.core.fx, self.core.fy, red)