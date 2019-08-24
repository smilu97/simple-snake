# author: smilu97
# description: Randomly moving, snake agent

import random

# state_code = ['blank', 'tails', 'head', 'food']

class RandomAgent:

    def __init__(self):
        self.idx_to_action = ['left', 'right', 'up', 'down']

    def process(self, state):
        action = random.randint(0, 3)
        return self.idx_to_action[action]
