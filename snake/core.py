# author: smilu97
# description: simple snake game

import random

class SnakeGame:

    def __init__(self,
        default_level=3,
        max_x=20,
        max_y=20):
        '''
        SnakeGame.__init__
        '''
        self.max_x = max_x
        self.max_y = max_y
        self.default_level = default_level

        self.reset()
    
    def reset(self):
        self.gameover = False
        self.x = random.randint(0, self.max_x)
        self.y = random.randint(0, self.max_y)
        self.level = self.default_level
        self.dx = 1
        self.dy = 0
        self.trails = []
        self.create_food()
    
    def create_food(self):
        while True:
            self.fx = random.randint(0, self.max_x)
            self.fy = random.randint(0, self.max_y)

            if not self.check_trail_coll(self.fx, self.fy) \
                and (self.fx != self.x or self.fy != self.y):
                break

    def check_trail_coll(self, x, y):
        for pos in self.trails:
            if pos[0] == x and pos[1] == y:
                return True
        return False
    
    def next(self, action):
        '''
        SnakeGame.run
        '''

        if action == 'left':
            if self.dx != 1:
                self.dx = -1
                self.dy = 0
        elif action == 'right':
            if self.dx != -1:
                self.dx = 1
                self.dy = 0
        elif action == 'up':
            if self.dy != 1:
                self.dx = 0
                self.dy = -1
        elif action == 'down':
            if self.dy != -1:
                self.dx = 0
                self.dy = 1
        
        px = self.x
        py = self.y
        if not self.gameover:
            self.x += self.dx
            self.y += self.dy
        stopped = False

        if self.check_trail_coll(self.x, self.y):
            stopped = True
            self.trails.append((px, py))

        if self.x == self.fx and self.y == self.fy:
            self.level += 1
            self.create_food()

        if self.x < 0:
            self.x = 0
            stopped = True
        elif self.x > self.max_x:
            self.x = self.max_x
            stopped = True
        if self.y < 0:
            self.y = 0
            stopped = True
        elif self.y > self.max_y:
            self.y = self.max_y
            stopped = True
        
        if stopped:
            self.gameover = True

        if not self.gameover:
            if not stopped:
                self.trails.append((px, py))
            del_len = len(self.trails) - self.level + 1
            if del_len > 0:
                self.trails = self.trails[del_len:]
