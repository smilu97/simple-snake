# author: smilu97

import pygame as pg
import sys
from .snake_player import SnakePlayer
from .core_serializer import serialize as serialize_state

red = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)

class SnakeAgentPlayer(SnakePlayer):

    def __init__(self,
        agent,
        renderable=False,
        sc_width=800,
        sc_height=800,
        block_sz=40,
        caption='Simple Snake Game',
        fps=60):
        super().__init__(sc_width, sc_height, block_sz, caption, fps)
        self.agent = agent
        self.renderable = renderable
    
    def run(self):
        '''
        SnakeGame.run
        '''

        if self.renderable:
            pg.init()
            pg.display.set_caption(self.caption)
            self.screen = pg.display.set_mode((self.sc_width, self.sc_height))
            self.clock = pg.time.Clock()

        while True:
            if self.renderable: self.clock.tick(self.fps)

            if not self.core.gameover:
                state = serialize_state(self.core)
                action = self.agent.process(state)
            
            if self.renderable:
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        sys.exit()
                    if event.type == pg.KEYDOWN:
                        if event.key == pg.K_r:
                            if self.core.gameover:
                                self.core.reset()
                        elif event.key == pg.K_q:
                            sys.exit()
            
            p_gameover = self.core.gameover
            self.core.next(action)
            if not p_gameover and self.core.gameover:
                print('GameOver, score:', self.core.level)
            if not self.renderable and self.core.gameover:
                return False
            
            if self.renderable:
                self.screen.fill(black)
                self.render()
                pg.display.update()

        return True
